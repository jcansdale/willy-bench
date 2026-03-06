#!/usr/bin/env python3
"""
cop — GitHub Copilot CLI

Usage:
  cop chat [PROMPT]          Send a prompt (reads stdin if omitted)
  cop models                 List available models
  cop login                  Force re-authentication
  cop logout                 Clear stored credentials
"""

import argparse
import base64
import json
import mimetypes
import os
import sys
import time
from pathlib import Path

import requests

# ---------------------------------------------------------------------------
# Constants (mirror packages/ai/src/utils/oauth/github-copilot.ts)
# ---------------------------------------------------------------------------

_CLIENT_ID = base64.b64decode("SXYxLmI1MDdhMDhjODdlY2ZlOTg=").decode()

COPILOT_HEADERS = {
    "User-Agent": "GitHubCopilotChat/0.35.0",
    "Editor-Version": "vscode/1.107.0",
    "Editor-Plugin-Version": "copilot-chat/0.35.0",
    "Copilot-Integration-Id": "vscode-chat",
}

DEVICE_CODE_URL = "https://github.com/login/device/code"
ACCESS_TOKEN_URL = "https://github.com/login/oauth/access_token"
COPILOT_TOKEN_URL = "https://api.github.com/copilot_internal/v2/token"
DEFAULT_BASE_URL = "https://api.individual.githubcopilot.com"

CREDENTIALS_FILE = Path.home() / ".copilot_chat_creds.json"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _parse_proxy_ep(copilot_token: str) -> str:
    """
    Copilot token format: tid=...;exp=...;proxy-ep=proxy.individual.githubcopilot.com;...
    Convert proxy-ep → https://api.individual.githubcopilot.com
    """
    for part in copilot_token.split(";"):
        if part.startswith("proxy-ep="):
            host = part[len("proxy-ep="):]
            host = host.replace("proxy.", "api.", 1)
            return f"https://{host}"
    return DEFAULT_BASE_URL


def _load_credentials() -> dict | None:
    if CREDENTIALS_FILE.exists():
        try:
            return json.loads(CREDENTIALS_FILE.read_text())
        except Exception:
            pass
    return None


def _save_credentials(creds: dict) -> None:
    CREDENTIALS_FILE.write_text(json.dumps(creds, indent=2))
    CREDENTIALS_FILE.chmod(0o600)


# ---------------------------------------------------------------------------
# Step 1 – GitHub device flow → GitHub OAuth access token
# ---------------------------------------------------------------------------


def _start_device_flow() -> dict:
    """Request a device code from GitHub."""
    resp = requests.post(
        DEVICE_CODE_URL,
        headers={"Accept": "application/json", **COPILOT_HEADERS},
        json={"client_id": _CLIENT_ID, "scope": "read:user"},
        timeout=15,
    )
    resp.raise_for_status()
    data = resp.json()
    required = {"device_code", "user_code", "verification_uri", "interval", "expires_in"}
    missing = required - data.keys()
    if missing:
        raise RuntimeError(f"Device code response missing fields: {missing}\n{data}")
    return data


def _poll_for_github_token(device: dict) -> str:
    """Poll GitHub until the user completes the browser auth step."""
    deadline = time.time() + device["expires_in"]
    interval = max(5, device["interval"])

    while time.time() < deadline:
        time.sleep(interval)
        resp = requests.post(
            ACCESS_TOKEN_URL,
            headers={"Accept": "application/json", **COPILOT_HEADERS},
            json={
                "client_id": _CLIENT_ID,
                "device_code": device["device_code"],
                "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
            },
            timeout=15,
        )
        resp.raise_for_status()
        data = resp.json()

        if "access_token" in data:
            return data["access_token"]

        error = data.get("error", "")
        if error == "authorization_pending":
            continue
        if error == "slow_down":
            interval += 5
            continue
        raise RuntimeError(f"Device flow failed: {error} — {data.get('error_description', '')}")

    raise RuntimeError("Device flow timed out.")


def github_device_login() -> str:
    """Full GitHub device-flow login; returns the GitHub OAuth access token."""
    device = _start_device_flow()

    print("\n─── GitHub Device Login ──────────────────────────────────────")
    print(f"  Open:  {device['verification_uri']}")
    print(f"  Enter: {device['user_code']}")
    print("──────────────────────────────────────────────────────────────")
    print("Waiting for you to complete the login in your browser…\n")

    return _poll_for_github_token(device)


# ---------------------------------------------------------------------------
# Step 2 – Exchange GitHub token → short-lived Copilot session token
# ---------------------------------------------------------------------------


def get_copilot_token(github_token: str) -> dict:
    """
    Exchange a GitHub OAuth token for a Copilot session token.
    Returns {"access": <copilot_token>, "expires": <unix_ms>, "base_url": ...}
    """
    resp = requests.get(
        COPILOT_TOKEN_URL,
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {github_token}",
            **COPILOT_HEADERS,
        },
        timeout=15,
    )
    resp.raise_for_status()
    data = resp.json()

    token = data.get("token")
    expires_at = data.get("expires_at")
    if not token or not isinstance(expires_at, (int, float)):
        raise RuntimeError(f"Unexpected Copilot token response: {data}")

    return {
        "github_token": github_token,
        "access": token,
        # expires_at is UNIX seconds from GitHub; store as ms with a 5-min buffer
        "expires": int(expires_at) * 1000 - 5 * 60 * 1000,
        "base_url": _parse_proxy_ep(token),
    }


# ---------------------------------------------------------------------------
# Credential management
# ---------------------------------------------------------------------------


def _is_expired(creds: dict) -> bool:
    return creds.get("expires", 0) < time.time() * 1000


def load_or_login() -> dict:
    """Return fresh Copilot credentials, re-logging in or refreshing as needed."""
    # Check for environment variable token (for CI/CD)
    env_token = os.environ.get("COPILOT_GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    if env_token:
        print("Using GitHub token from environment variable…", file=sys.stderr)
        # In CI, fail fast if the token doesn't work
        creds = get_copilot_token(env_token)
        return creds

    creds = _load_credentials()

    if creds and not _is_expired(creds):
        print("Using cached Copilot credentials.", file=sys.stderr)
        return creds

    if creds and _is_expired(creds):
        print("Copilot session expired — refreshing via stored GitHub token…", file=sys.stderr)
        try:
            creds = get_copilot_token(creds["github_token"])
            _save_credentials(creds)
            return creds
        except Exception as exc:
            print(f"Refresh failed ({exc}); starting fresh login.", file=sys.stderr)

    # Full device-flow login (only works interactively)
    if not sys.stdin.isatty():
        raise RuntimeError(
            "No valid credentials and running non-interactively. "
            "Set COPILOT_GITHUB_TOKEN environment variable."
        )
    github_token = github_device_login()
    creds = get_copilot_token(github_token)
    _save_credentials(creds)
    return creds


# ---------------------------------------------------------------------------
# Step 3 – Chat completion via Copilot's OpenAI-compatible API
# ---------------------------------------------------------------------------


# A small curated palette for human-readable colour names
_NAMED_COLOURS: list[tuple[tuple[int, int, int], str]] = [
    ((0,   0,   0),   "black"),
    ((255, 255, 255), "white"),
    ((189, 189, 189), "silver/light grey"),
    ((128, 128, 128), "grey"),
    ((255,   0,   0), "red"),
    ((189,   0,   0), "dark red"),
    ((128,   0,   0), "maroon"),
    ((0,   255,   0), "lime"),
    ((0,   128,   0), "green"),
    ((0,     0, 255), "blue"),
    ((0,     0, 128), "navy"),
    ((0,   255, 255), "cyan"),
    ((0,   189, 189), "dark cyan"),
    ((255, 255,   0), "yellow"),
    ((189, 189,   0), "dark yellow/olive"),
    ((255,   0, 255), "magenta"),
    ((189,   0, 189), "dark magenta"),
    ((255, 165,   0), "orange"),
    ((255, 192, 203), "pink"),
    ((165,  42,  42), "brown"),
]


def _nearest_colour_name(rgb: tuple[int, int, int]) -> str:
    """Return the closest human-readable colour name for an RGB tuple."""
    r, g, b = rgb
    best_name, best_dist = "unknown", float("inf")
    for (cr, cg, cb), name in _NAMED_COLOURS:
        d = (r - cr) ** 2 + (g - cg) ** 2 + (b - cb) ** 2
        if d < best_dist:
            best_dist, best_name = d, name
    return best_name


def _image_to_text_grid(source: str, zoom: int = 1) -> str:
    """Convert an image to a palette + single-char grid text representation."""
    import io
    from PIL import Image

    if source.startswith("http://") or source.startswith("https://"):
        resp = requests.get(source, timeout=30)
        resp.raise_for_status()
        img = Image.open(io.BytesIO(resp.content)).convert("RGB")
    else:
        path = Path(source)
        if not path.exists():
            raise FileNotFoundError(f"Image not found: {source}")
        img = Image.open(path).convert("RGB")

    if zoom > 1:
        img = img.resize((img.width * zoom, img.height * zoom), Image.NEAREST)

    # Collect unique colours in scan order
    unique: list[tuple[int, int, int]] = []
    seen: set[tuple[int, int, int]] = set()
    for y in range(img.height):
        for x in range(img.width):
            px = img.getpixel((x, y))
            if px not in seen:
                seen.add(px)
                unique.append(px)

    # Assign single uppercase letters A, B, C, … (up to 26)
    labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    colour_to_char = {px: labels[i] for i, px in enumerate(unique[:26])}

    # Build palette legend
    lines = [f"Image: {img.width}×{img.height} pixels", "Palette:"]
    for px, char in colour_to_char.items():
        hex_col = "#{:02X}{:02X}{:02X}".format(*px)
        name = _nearest_colour_name(px)
        lines.append(f"  {char} = {hex_col} ({name})")

    lines.append(f"Grid ({img.width}×{img.height}, left-to-right top-to-bottom):")
    for y in range(img.height):
        row = "".join(colour_to_char.get(img.getpixel((x, y)), "?") for x in range(img.width))
        lines.append(row)

    return "\n".join(lines)


def _image_to_data_url(source: str, zoom: int = 1) -> str:
    """Return a base64 data URI for a local file or remote URL, optionally zoomed."""
    import io
    from PIL import Image

    if source.startswith("http://") or source.startswith("https://"):
        resp = requests.get(source, timeout=30)
        resp.raise_for_status()
        img = Image.open(io.BytesIO(resp.content))
    else:
        path = Path(source)
        if not path.exists():
            raise FileNotFoundError(f"Image not found: {source}")
        img = Image.open(path)

    if zoom > 1:
        img = img.resize((img.width * zoom, img.height * zoom), Image.NEAREST)

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    data = base64.b64encode(buf.getvalue()).decode()
    return f"data:image/png;base64,{data}"


def copilot_chat(
    creds: dict,
    prompt: str,
    model: str = "gpt-4o",
    images: list[str] | None = None,
    zoom: int = 1,
    grid: bool = False,
) -> str:
    """Send a prompt (with optional images) and return the assistant's reply."""
    base_url = creds.get("base_url", DEFAULT_BASE_URL)
    url = f"{base_url}/chat/completions"

    # Build content
    if images and grid:
        # Text-grid mode: convert each image to palette+grid text, no attachment
        grid_blocks = []
        for img_src in images:
            grid_blocks.append(_image_to_text_grid(img_src, zoom=zoom))
        grid_text = "\n\n".join(grid_blocks)
        content: str | list = f"{grid_text}\n\n{prompt}"
    elif images:
        content = [{"type": "text", "text": prompt}]
        for img in images:
            content.append({
                "type": "image_url",
                "image_url": {"url": _image_to_data_url(img, zoom=zoom)},
            })
    else:
        content = prompt

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": content}],
        "stream": False,
    }

    resp = requests.post(
        url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {creds['access']}",
            **COPILOT_HEADERS,
        },
        json=payload,
        timeout=60,
    )

    if not resp.ok:
        raise RuntimeError(f"Copilot API error {resp.status_code}: {resp.text}")

    data = resp.json()
    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError) as exc:
        raise RuntimeError(f"Unexpected response shape: {data}") from exc


def copilot_responses(
    creds: dict,
    prompt: str,
    model: str = "gpt-4o",
    images: list[str] | None = None,
    zoom: int = 1,
    instructions: str | None = None,
) -> str:
    """Send a prompt using the Responses API and return the assistant's reply.
    
    The Responses API is OpenAI's newer API format that supports:
    - Native tool use
    - Structured outputs
    - Multi-turn conversations
    - Some models only available here (e.g., gpt-5.4)
    """
    base_url = creds.get("base_url", DEFAULT_BASE_URL)
    url = f"{base_url}/responses"

    # Build input content - Responses API uses different format
    if images:
        # Multi-part input with images using message format
        content = [{"type": "input_text", "text": prompt}]
        for img in images:
            content.append({
                "type": "input_image",
                "image_url": _image_to_data_url(img, zoom=zoom),
            })
        # Wrap in message structure
        input_content = [{
            "type": "message",
            "role": "user",
            "content": content,
        }]
    else:
        # Simple text input - just a string
        input_content = prompt

    payload = {
        "model": model,
        "input": input_content,
    }
    
    if instructions:
        payload["instructions"] = instructions

    resp = requests.post(
        url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {creds['access']}",
            **COPILOT_HEADERS,
        },
        json=payload,
        timeout=120,  # Responses API may take longer
    )

    if not resp.ok:
        raise RuntimeError(f"Copilot Responses API error {resp.status_code}: {resp.text}")

    data = resp.json()
    try:
        # Responses API returns output array with content blocks
        output = data.get("output", [])
        for item in output:
            if item.get("type") == "message":
                content = item.get("content", [])
                for block in content:
                    if block.get("type") == "output_text":
                        return block.get("text", "")
        # Fallback: try to find any text
        raise RuntimeError(f"No text output found in response: {data}")
    except (KeyError, IndexError) as exc:
        raise RuntimeError(f"Unexpected response shape: {data}") from exc


# ---------------------------------------------------------------------------
# Extra commands
# ---------------------------------------------------------------------------


def list_models(creds: dict) -> None:
    """Print all models available to this account."""
    base = creds.get("base_url", DEFAULT_BASE_URL)
    resp = requests.get(
        f"{base}/models",
        headers={"Authorization": f"Bearer {creds['access']}", **COPILOT_HEADERS},
        timeout=15,
    )
    resp.raise_for_status()
    models = resp.json().get("data", [])

    # Group by rough family
    families: dict[str, list[str]] = {}
    for m in models:
        mid = m.get("id", "")
        if mid.startswith("text-embedding"):
            continue  # skip embedding models
        family = mid.split("-")[0]  # gpt / claude / gemini / …
        families.setdefault(family, []).append(mid)

    for family, ids in sorted(families.items()):
        print(f"\n{family.upper()}")
        for mid in sorted(ids):
            print(f"  {mid}")
    print()


def do_logout() -> None:
    if CREDENTIALS_FILE.exists():
        CREDENTIALS_FILE.unlink()
        print("Credentials removed.")
    else:
        print("No stored credentials found.")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cop",
        description="GitHub Copilot CLI — chat with any Copilot model from your terminal.",
    )
    sub = parser.add_subparsers(dest="command")

    # chat
    chat_p = sub.add_parser("chat", help="Send a prompt to Copilot")
    chat_p.add_argument(
        "prompt",
        nargs="*",
        help="Prompt text (omit to read from stdin)",
    )
    chat_p.add_argument(
        "-m", "--model",
        action="append",
        dest="models",
        metavar="MODEL",
        help="Model to use; repeat for multiple (default: gpt-4o or $COPILOT_MODEL)",
    )
    chat_p.add_argument(
        "-i", "--image",
        action="append",
        dest="images",
        metavar="FILE_OR_URL",
        help="Image to include (local file or https:// URL); can be repeated",
    )
    chat_p.add_argument(
        "-z", "--zoom",
        type=int,
        default=1,
        metavar="N",
        help="Upscale images by N× (nearest-neighbour) before sending (default: 1)",
    )
    chat_p.add_argument(
        "-g", "--grid",
        action="store_true",
        default=False,
        help="Send image(s) as palette+grid text instead of an image attachment",
    )
    chat_p.add_argument(
        "-o", "--output",
        metavar="FILE",
        help="Write reply to FILE instead of (or in addition to) stdout. "
             "With multiple -m models the stem gets _{model} appended.",
    )
    chat_p.add_argument(
        "--api",
        choices=["chat", "responses", "auto"],
        default="auto",
        help="API to use: 'chat' (completions), 'responses', or 'auto' (default: auto)",
    )

    # models
    sub.add_parser("models", help="List available models")

    # login
    sub.add_parser("login", help="Authenticate with GitHub (device flow)")

    # logout
    sub.add_parser("logout", help="Remove stored credentials")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    # Default to 'chat' when no subcommand given
    if args.command is None:
        parser.print_help()
        sys.exit(0)

    # ── logout (no network needed)
    if args.command == "logout":
        do_logout()
        return

    # ── login (force fresh login)
    if args.command == "login":
        if CREDENTIALS_FILE.exists():
            CREDENTIALS_FILE.unlink()
        load_or_login()
        print("Login successful. Credentials saved.")
        return

    # All other commands need credentials
    creds = load_or_login()

    # ── models
    if args.command == "models":
        list_models(creds)
        return

    # ── chat
    prompt_parts = args.prompt if args.prompt else []
    prompt = " ".join(prompt_parts).strip()
    if not prompt:
        if not sys.stdin.isatty():
            prompt = sys.stdin.read().strip()
        else:
            prompt = input("Prompt: ").strip()
    if not prompt:
        print("No prompt provided.", file=sys.stderr)
        sys.exit(1)

    models = args.models or [os.environ.get("COPILOT_MODEL", "gpt-4o")]
    images = getattr(args, "images", None)
    zoom = getattr(args, "zoom", 1)
    grid = getattr(args, "grid", False)
    output = getattr(args, "output", None)
    api_choice = getattr(args, "api", "auto")
    
    # Models that require Responses API
    RESPONSES_ONLY_MODELS = {"gpt-5.4", "gpt-5.3-codex", "gpt-5.2-codex", "gpt-5.1-codex", "gpt-5.1-codex-max", "gpt-5.1-codex-mini", "goldeneye"}
    
    if grid and images:
        print("(grid text mode)")
    elif zoom > 1 and images:
        print(f"(zoom ×{zoom})")
    multi = len(models) > 1
    sep = "─" * 62
    for model in models:
        if multi:
            print(f"\n{sep}\n[{model}]\n{sep}")
        
        # Determine which API to use
        if api_choice == "auto":
            use_responses = model in RESPONSES_ONLY_MODELS
        else:
            use_responses = (api_choice == "responses")
        
        if use_responses and grid:
            print("Warning: --grid not supported with Responses API, ignoring", file=sys.stderr)
        
        try:
            if use_responses:
                if multi or api_choice == "auto":
                    print(f"(using Responses API)", file=sys.stderr)
                reply = copilot_responses(creds, prompt, model=model, images=images, zoom=zoom)
            else:
                reply = copilot_chat(creds, prompt, model=model, images=images, zoom=zoom, grid=grid)
            print(reply)
            if output:
                if multi:
                    p = Path(output)
                    out_path = p.with_stem(f"{p.stem}_{model}") if hasattr(p, 'with_stem') else p.parent / f"{p.stem}_{model}{p.suffix}"
                else:
                    out_path = Path(output)
                out_path.write_text(reply)
                print(f"(written to {out_path})", file=sys.stderr)
        except Exception as exc:
            print(f"ERROR: {exc}", file=sys.stderr)


if __name__ == "__main__":
    main()
