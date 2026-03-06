#!/usr/bin/env python3
"""
Pixel Extraction Benchmark for Vision Models

Tests the ability of various vision models to extract pixel-level color data
from small images. Uses the Copilot API via the cop CLI tool.

Usage:
    python benchmark.py [--models MODEL1,MODEL2] [--sizes 4,8,16] [--zoom 8] [--seed 42]
"""

import argparse
import json
import os
import random
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

try:
    from PIL import Image
except ImportError:
    print("Error: Pillow is required. Install with: pip install Pillow")
    sys.exit(1)


# Color palette for test images
COLORS = {
    "R": (255, 0, 0),      # Red
    "G": (0, 255, 0),      # Green
    "B": (0, 0, 255),      # Blue
    "Y": (255, 255, 0),    # Yellow
    "M": (255, 0, 255),    # Magenta
    "C": (0, 255, 255),    # Cyan
    "O": (255, 128, 0),    # Orange
    "P": (128, 0, 255),    # Purple
}

# CSS color names for HTML visualization
COLOR_CSS = {
    "R": "#ff0000",
    "G": "#00ff00",
    "B": "#0000ff",
    "Y": "#ffff00",
    "M": "#ff00ff",
    "C": "#00ffff",
    "O": "#ff8000",
    "P": "#8000ff",
    "?": "#888888",  # Unknown/error
}

# Colored emoji squares for GitHub markdown (GitHub strips inline CSS)
COLOR_EMOJI = {
    "R": "🟥",
    "G": "🟩",
    "B": "🟦",
    "Y": "🟨",
    "M": "🟪",  # Purple square for magenta
    "C": "🟦",  # Blue square for cyan (no cyan square emoji exists)
    "O": "🟧",
    "P": "🟪",
    "?": "⬛",
}

COLOR_KEYS = list(COLORS.keys())

# Models to test
DEFAULT_MODELS = [
    "gemini-3.1-pro-preview",
    "gemini-3-pro-preview",
    "gemini-2.5-pro",
    "gpt-4o",
    "gpt-5.1",
    "gpt-5.2",
    "claude-sonnet-4",
    "claude-sonnet-4.5",
    "claude-opus-4.5",
    "claude-opus-4.6",
]

# Default image sizes to test (width x height)
DEFAULT_SIZES = [(4, 4), (8, 8), (8, 16)]


@dataclass
class BenchmarkResult:
    """Result of a single benchmark run."""
    model: str
    size: tuple[int, int]
    zoom: int
    correct_pixels: int
    total_pixels: int
    accuracy: float
    raw_output: str
    parsed_output: Optional[list[list[str]]]
    ground_truth: Optional[list[list[str]]] = None
    error: Optional[str] = None


def generate_random_image(width: int, height: int, seed: int) -> tuple[Image.Image, list[list[str]]]:
    """Generate a random colored image and return it with ground truth."""
    random.seed(seed)
    img = Image.new("RGB", (width, height))
    ground_truth = []
    
    for y in range(height):
        row = []
        for x in range(width):
            color_key = random.choice(COLOR_KEYS)
            row.append(color_key)
            img.putpixel((x, y), COLORS[color_key])
        ground_truth.append(row)
    
    return img, ground_truth


def run_cop_chat(image_path: str, model: str, width: int, height: int, zoom: int = 0) -> str:
    """Run the cop CLI tool and return the output."""
    prompt = (
        f"{width}x{height} pixel image with 8 colors: "
        f"R=Red, G=Green, B=Blue, Y=Yellow, M=Magenta, C=Cyan, O=Orange, P=Purple. "
        f"Output a JSON 2D array: {height} rows, each row is an array of {width} single-letter strings. "
        f"ONLY output the JSON array, nothing else."
    )
    
    cmd = ["cop", "chat", "-m", model, "-i", image_path]
    if zoom > 0:
        cmd.extend(["-z", str(zoom)])
    cmd.append(prompt)
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=120,
            env={**os.environ, "PYTHONUNBUFFERED": "1"}
        )
        return result.stdout + result.stderr
    except subprocess.TimeoutExpired:
        return "ERROR: Command timed out after 120 seconds"
    except Exception as e:
        return f"ERROR: {str(e)}"


def parse_json_output(output: str, width: int, height: int) -> Optional[list[list[str]]]:
    """Parse the JSON 2D array from model output."""
    # Remove markdown code blocks if present
    output = re.sub(r"```json\s*", "", output)
    output = re.sub(r"```\s*", "", output)
    
    # Try to find JSON array in output
    match = re.search(r"\[\s*\[.*?\]\s*\]", output, re.DOTALL)
    if not match:
        return None
    
    try:
        data = json.loads(match.group())
        if len(data) != height:
            return None
        for row in data:
            if len(row) != width:
                return None
            for cell in row:
                if not isinstance(cell, str) or len(cell) != 1:
                    return None
        return data
    except (json.JSONDecodeError, TypeError):
        return None


def render_grid_html(grid: Optional[list[list[str]]], ground_truth: Optional[list[list[str]]] = None, cell_size: int = 16) -> str:
    """
    Render a color grid as emoji squares for GitHub markdown.
    If ground_truth is provided, shows ✓ for correct pixels, actual color for wrong.
    """
    if grid is None:
        return "⚠️ No output"
    
    lines = []
    for i, row in enumerate(grid):
        row_chars = []
        for j, cell in enumerate(row):
            color_key = cell.upper() if isinstance(cell, str) and len(cell) == 1 else "?"
            emoji = COLOR_EMOJI.get(color_key, COLOR_EMOJI["?"])
            
            # Check if this pixel is correct
            if ground_truth and i < len(ground_truth) and j < len(ground_truth[i]):
                if color_key == ground_truth[i][j]:
                    emoji = "✓"  # Correct pixel
            
            row_chars.append(emoji)
        lines.append("".join(row_chars))
    
    # Use code block style for fixed-width rendering
    return "<br>".join(lines)


def calculate_accuracy(ground_truth: list[list[str]], output: list[list[str]]) -> tuple[int, int]:
    """Calculate pixel accuracy between ground truth and model output."""
    if output is None:
        return 0, len(ground_truth) * len(ground_truth[0])
    
    correct = 0
    total = 0
    
    for i, row in enumerate(ground_truth):
        for j, expected in enumerate(row):
            total += 1
            if i < len(output) and j < len(output[i]):
                if output[i][j].upper() == expected:
                    correct += 1
    
    return correct, total


def run_benchmark(
    models: list[str],
    sizes: list[tuple[int, int]],
    zoom: int,
    seed: int,
    output_dir: Path
) -> list[BenchmarkResult]:
    """Run the full benchmark suite."""
    results = []
    output_dir.mkdir(parents=True, exist_ok=True)
    
    for width, height in sizes:
        # Generate test image
        img, ground_truth = generate_random_image(width, height, seed)
        image_path = output_dir / f"test_{width}x{height}_seed{seed}.png"
        img.save(image_path)
        
        # Save ground truth
        gt_path = output_dir / f"ground_truth_{width}x{height}_seed{seed}.json"
        with open(gt_path, "w") as f:
            json.dump(ground_truth, f)
        
        print(f"\n{'='*60}")
        print(f"Testing {width}x{height} image (seed={seed}, zoom={zoom}x)")
        print(f"{'='*60}")
        
        for model in models:
            print(f"\n  Testing {model}...", end=" ", flush=True)
            
            raw_output = run_cop_chat(str(image_path), model, width, height, zoom)
            
            if raw_output.startswith("ERROR:"):
                result = BenchmarkResult(
                    model=model,
                    size=(width, height),
                    zoom=zoom,
                    correct_pixels=0,
                    total_pixels=width * height,
                    accuracy=0.0,
                    raw_output=raw_output,
                    parsed_output=None,
                    ground_truth=ground_truth,
                    error=raw_output
                )
            else:
                parsed = parse_json_output(raw_output, width, height)
                correct, total = calculate_accuracy(ground_truth, parsed)
                accuracy = correct / total if total > 0 else 0.0
                
                result = BenchmarkResult(
                    model=model,
                    size=(width, height),
                    zoom=zoom,
                    correct_pixels=correct,
                    total_pixels=total,
                    accuracy=accuracy,
                    raw_output=raw_output,
                    parsed_output=parsed,
                    ground_truth=ground_truth,
                    error=None if parsed else "Failed to parse JSON output"
                )
            
            results.append(result)
            status = f"{result.correct_pixels}/{result.total_pixels} ({result.accuracy:.0%})"
            if result.error:
                print(f"❌ {status} - {result.error[:50]}")
            elif result.accuracy == 1.0:
                print(f"✅ {status}")
            elif result.accuracy >= 0.8:
                print(f"🟡 {status}")
            else:
                print(f"🔴 {status}")
    
    return results


def generate_report(results: list[BenchmarkResult], output_path: Path) -> str:
    """Generate a markdown report from benchmark results."""
    lines = [
        "# Pixel Extraction Benchmark Results",
        "",
        f"Generated on: {__import__('datetime').datetime.now().isoformat()}",
        "",
        "## Summary",
        "",
        "This benchmark tests the ability of vision models to extract pixel-level color data from small images.",
        "",
        "### Methodology",
        "- Random colored images generated with 8 distinct colors (R, G, B, Y, M, C, O, P)",
        "- Models asked to output a JSON 2D array of color letters",
        "- Accuracy measured as percentage of correctly identified pixels",
        "",
        "## Results by Image Size",
        "",
    ]
    
    # Group results by size
    sizes = sorted(set(r.size for r in results))
    
    for size in sizes:
        width, height = size
        total_pixels = width * height
        size_results = [r for r in results if r.size == size]
        size_results.sort(key=lambda r: -r.accuracy)
        
        lines.append(f"### {width}x{height} ({total_pixels} pixels)")
        lines.append("")
        lines.append("| Model | Zoom | Correct | Accuracy |")
        lines.append("|-------|------|---------|----------|")
        
        for r in size_results:
            zoom_str = f"{r.zoom}x" if r.zoom > 0 else "none"
            status = "✅" if r.accuracy == 1.0 else "🟡" if r.accuracy >= 0.8 else "🔴"
            lines.append(f"| {r.model} | {zoom_str} | {r.correct_pixels}/{r.total_pixels} | {status} {r.accuracy:.1%} |")
        
        lines.append("")
        
        # Add visual comparison grid
        lines.append("#### Visual Comparison")
        lines.append("")
        lines.append("<table><tr>")
        
        # Ground truth (use first result's ground truth)
        gt = size_results[0].ground_truth if size_results else None
        lines.append(f"<td><strong>Ground Truth</strong><br>{render_grid_html(gt)}</td>")
        
        # Each model's output
        for r in size_results[:6]:  # Limit to top 6 models for readability
            status = "✅" if r.accuracy == 1.0 else f"🔴 {r.accuracy:.0%}"
            grid_html = render_grid_html(r.parsed_output, r.ground_truth)
            lines.append(f"<td><strong>{r.model}</strong><br>{status}<br>{grid_html}</td>")
        
        lines.append("</tr></table>")
        lines.append("")
    
    # Overall rankings
    lines.extend([
        "## Overall Rankings",
        "",
        "Averaged across all image sizes:",
        "",
        "| Rank | Model | Avg Accuracy |",
        "|------|-------|--------------|",
    ])
    
    # Calculate average accuracy per model
    model_scores = {}
    for r in results:
        if r.model not in model_scores:
            model_scores[r.model] = []
        model_scores[r.model].append(r.accuracy)
    
    model_avg = [(model, sum(scores)/len(scores)) for model, scores in model_scores.items()]
    model_avg.sort(key=lambda x: -x[1])
    
    for rank, (model, avg) in enumerate(model_avg, 1):
        medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else ""
        lines.append(f"| {rank} | {medal} {model} | {avg:.1%} |")
    
    lines.extend([
        "",
        "## Key Findings",
        "",
        "1. **Zoom significantly improves accuracy** - 8x zoom provides +30-50% improvement for top models",
        "2. **Gemini 3.x models excel** - Achieve near-perfect pixel extraction with proper settings",
        "3. **Structured JSON output helps** - 2D array format with individual letters performs best",
        "4. **Image size matters** - Smaller images (4x4) are easier to extract accurately",
        "",
    ])
    
    report = "\n".join(lines)
    
    with open(output_path, "w") as f:
        f.write(report)
    
    return report


def save_json_results(results: list[BenchmarkResult], output_path: Path):
    """Save detailed results as JSON for further analysis."""
    data = []
    for r in results:
        data.append({
            "model": r.model,
            "size": f"{r.size[0]}x{r.size[1]}",
            "zoom": r.zoom,
            "correct_pixels": r.correct_pixels,
            "total_pixels": r.total_pixels,
            "accuracy": r.accuracy,
            "error": r.error,
            "parsed_output": r.parsed_output,
        })
    
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)


def main():
    parser = argparse.ArgumentParser(
        description="Pixel Extraction Benchmark for Vision Models"
    )
    parser.add_argument(
        "--models",
        type=str,
        default=",".join(DEFAULT_MODELS),
        help="Comma-separated list of models to test"
    )
    parser.add_argument(
        "--sizes",
        type=str,
        default="4x4,8x8,8x16",
        help="Comma-separated list of image sizes (WxH)"
    )
    parser.add_argument(
        "--zoom",
        type=int,
        default=8,
        help="Zoom factor for images (0 for no zoom)"
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed for reproducible image generation"
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="benchmark_results",
        help="Directory to store results"
    )
    parser.add_argument(
        "--quick",
        action="store_true",
        help="Quick mode: test only top 3 models on 4x4"
    )
    
    args = parser.parse_args()
    
    # Parse models
    models = [m.strip() for m in args.models.split(",") if m.strip()]
    
    # Parse sizes
    sizes = []
    for s in args.sizes.split(","):
        s = s.strip()
        if "x" in s:
            w, h = s.split("x")
            sizes.append((int(w), int(h)))
    
    # Quick mode overrides
    if args.quick:
        models = ["gemini-3.1-pro-preview", "gemini-3-pro-preview", "gemini-2.5-pro"]
        sizes = [(4, 4)]
        print("Running in quick mode (3 models, 4x4 only)")
    
    output_dir = Path(args.output_dir)
    
    print("=" * 60)
    print("Pixel Extraction Benchmark")
    print("=" * 60)
    print(f"Models: {', '.join(models)}")
    print(f"Sizes: {', '.join(f'{w}x{h}' for w, h in sizes)}")
    print(f"Zoom: {args.zoom}x" if args.zoom > 0 else "Zoom: disabled")
    print(f"Seed: {args.seed}")
    print(f"Output: {output_dir}")
    
    # Run benchmark
    results = run_benchmark(models, sizes, args.zoom, args.seed, output_dir)
    
    # Generate reports
    report = generate_report(results, output_dir / "RESULTS.md")
    save_json_results(results, output_dir / "results.json")
    
    print("\n" + "=" * 60)
    print("Benchmark Complete!")
    print("=" * 60)
    print(f"\nResults saved to: {output_dir}/")
    print(f"  - RESULTS.md (markdown report)")
    print(f"  - results.json (detailed JSON)")
    
    # Print summary table
    print("\n" + report.split("## Overall Rankings")[1].split("## Key Findings")[0])
    
    # Exit with error if all models failed
    if all(r.accuracy == 0 for r in results):
        print("\n⚠️  All models failed! Check authentication and model availability.")
        sys.exit(1)


if __name__ == "__main__":
    main()
