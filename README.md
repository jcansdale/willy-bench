# Willy Bench — Pixel Extraction Benchmark

A benchmark suite for testing vision models' ability to extract pixel-level color data from small images, using the GitHub Copilot API.

## Features

- **Pixel extraction benchmark** — Tests how accurately AI models can identify individual pixel colors
- **Visual comparison** — PNG images showing ground truth vs model output with error highlighting
- **Miner Willy sprite test** — Classic 8x16 retro game sprite challenge
- **Multiple APIs** — Supports both Chat Completions and Responses API
- **GitHub Actions** — Automated benchmarking with results in job summary

## Quick Start

```bash
# Install
pip install -e .
pip install Pillow

# Run quick benchmark
python benchmark.py --quick

# Run full benchmark with Willy sprite
python benchmark.py --willy --zoom 32 --reasoning-effort low
```

## cop CLI

A command-line interface for GitHub Copilot with vision model support.

```bash
# Chat with default model
cop chat "What is the capital of France?"

# Use a specific model
cop chat -m gemini-4-argon "Explain quantum computing"

# Send an image for analysis
cop chat -i image.png "Describe this image"

# Use zoom for pixel-level extraction  
cop chat -i sprite.png -z 8 "Extract pixel colors as JSON"

# Force Responses API (for gpt-6.1-sol etc.)
cop chat -m gpt-6.1-sol --api responses "Hello"

# List available models
cop models
```

## Supported Models

The default suite contains 17 vision models, checked against the Copilot catalog on 2026-10-21:

| Model | API |
|-------|-----|
| gemini-3.8-flash | Chat Completions |
| gemini-4-argon | Chat Completions |
| gpt-4o-2024-05-13 | Chat Completions |
| gpt-5.6-terra | Responses |
| gpt-5.6-sol | Responses |
| gpt-6-astra | Responses |
| gpt-6-luna | Responses |
| gpt-6-sol | Responses |
| gpt-6.1-sol | Responses |
| claude-haiku-4.5 | Chat Completions |
| claude-haiku-5.5 | Chat Completions |
| claude-sonnet-5 | Chat Completions |
| claude-sonnet-5.5 | Chat Completions |
| claude-opus-5 | Chat Completions |
| claude-opus-5.5 | Chat Completions |
| grok-4.6 | Responses |
| grok-4.7 | Responses |

The quick suite uses `gemini-4-argon`, `gpt-6.1-sol`, and `claude-sonnet-5.5`.
Low reasoning effort is requested for all default models except `gpt-4o-2024-05-13`
and `claude-haiku-4.5`, which do not advertise that option.

Gemini 3.5/3.6/3.7 Flash and GPT-5.4/5.5 are no longer in the active suite
because they are absent from the catalog. Their historical results are preserved.

## Benchmark Results

See latest results: [GitHub Actions](../../actions/workflows/pixel-benchmark.yml)
and [recorded results](results/LATEST.md). Full benchmark results for new additions
have not yet been recorded.

The benchmark generates:
- **Visual comparison** with emoji grids in job summary
- **PNG images** with error highlighting (red X on wrong pixels)
- **JSON results** for further analysis

### Example Output

```
Testing gemini-3.8-flash... ✅ 16/16 (100%)
Testing gpt-6-astra... 🔴 3/16 (19%)
Testing claude-sonnet-5... ✅ 16/16 (100%)
```

## Authentication

### Interactive (local)
```bash
cop login
```

### CI/CD
Set `COPILOT_GITHUB_TOKEN` environment variable with a GitHub token that has Copilot access.

## Tests

Run configuration and API-routing regression tests without API calls:

```bash
python -m unittest discover -s tests -v
```

## License

MIT
