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
python benchmark.py --willy --zoom 8
```

## cop CLI

A command-line interface for GitHub Copilot with vision model support.

```bash
# Chat with default model
cop chat "What is the capital of France?"

# Use a specific model
cop chat -m gemini-3.1-pro-preview "Explain quantum computing"

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

| Model | API | Best Pixel Accuracy |
|-------|-----|---------------------|
| gemini-3.1-pro-preview | Chat Completions | **100%** |
| gemini-3-pro-preview | Chat Completions | **100%** |
| gemini-2.5-pro | Chat Completions | ~78% |
| gpt-4o | Chat Completions | ~62% |
| gpt-5.4 | Responses | ~63% |
| claude-sonnet-4 | Chat Completions | ~66% |
| claude-opus-4.6 | Chat Completions | ~66% |
| claude-opus-4.7 | Chat Completions | TBD |

## Benchmark Results

See latest results: [GitHub Actions](../../actions/workflows/pixel-benchmark.yml)

The benchmark generates:
- **Visual comparison** with emoji grids in job summary
- **PNG images** with error highlighting (red X on wrong pixels)
- **JSON results** for further analysis

### Example Output

```
Testing gemini-3.1-pro-preview... ✅ 16/16 (100%)
Testing gpt-4o... 🔴 12/16 (75%)
Testing claude-sonnet-4... 🔴 10/16 (62%)
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
