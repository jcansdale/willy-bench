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
cop chat -m gemini-3.5-flash "Explain quantum computing"

# Send an image for analysis
cop chat -i image.png "Describe this image"

# Use zoom for pixel-level extraction  
cop chat -i sprite.png -z 8 "Extract pixel colors as JSON"

# Force Responses API (for gpt-5.4 etc.)
cop chat -m gpt-5.4 --api responses "Hello"

# List available models
cop models
```

## Supported Models

| Model | API | Latest Average Accuracy |
|-------|-----|-------------------------|
| gemini-3.5-flash | Chat Completions | **99.2%** |
| gemini-3.6-flash | Chat Completions | TBD |
| gemini-3.7-flash | Chat Completions | TBD |
| gemini-3.8-flash | Chat Completions | TBD |
| gpt-4o-2024-05-13 | Chat Completions | 46.9% |
| gpt-5.4 | Responses | 37.0% |
| gpt-5.5 | Responses | TBD |
| gpt-5.6-terra | Responses | TBD |
| gpt-5.6-sol | Responses | TBD |
| gpt-6-astra | Responses | TBD |
| claude-haiku-4.5 | Chat Completions | TBD |
| claude-sonnet-5 | Chat Completions | TBD |
| claude-opus-5 | Chat Completions | TBD |
| grok-4.6 | Responses | TBD |

## Benchmark Results

See latest results: [GitHub Actions](../../actions/workflows/pixel-benchmark.yml)

The benchmark generates:
- **Visual comparison** with emoji grids in job summary
- **PNG images** with error highlighting (red X on wrong pixels)
- **JSON results** for further analysis

### Example Output

```
Testing gemini-3.8-flash... ✅ 16/16 (100%)
Testing gpt-6-astra... 🔴 4/16 (25%)
Testing claude-sonnet-5... 🔴 2/16 (12%)
```

## Authentication

### Interactive (local)
```bash
cop login
```

### CI/CD
Set `COPILOT_GITHUB_TOKEN` environment variable with a GitHub token that has Copilot access.

## License

MIT
