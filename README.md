# cop — GitHub Copilot CLI

A command-line interface for GitHub Copilot with vision model support.

## Features

- **Chat with Copilot models** — Access GPT, Claude, and Gemini models
- **Image support** — Send images with prompts for vision analysis
- **Zoom mode** — Automatically scale images for better pixel-level extraction
- **Multiple models** — Switch between models with `-m` flag

## Installation

```bash
pip install -e .
```

## Usage

```bash
# Chat with default model
cop chat "What is the capital of France?"

# Use a specific model
cop chat -m gemini-3.1-pro-preview "Explain quantum computing"

# Send an image for analysis
cop chat -i image.png "Describe this image"

# Use zoom for pixel-level extraction
cop chat -i sprite.png -z 8 "Extract pixel colors as JSON"

# List available models
cop models

# Login (if needed)
cop login
```

## Available Models

- `gpt-4o`, `gpt-5.1`, `gpt-5.2`
- `claude-sonnet-4`, `claude-sonnet-4.5`, `claude-opus-4.5`, `claude-opus-4.6`
- `gemini-2.5-pro`, `gemini-3-pro-preview`, `gemini-3.1-pro-preview`

## Pixel Extraction Benchmark

This repo includes a benchmark for testing vision models' ability to extract pixel-level data. See [BENCHMARK.md](BENCHMARK.md) for details.

```bash
# Run quick benchmark
python benchmark.py --quick

# Run full benchmark
python benchmark.py --models "gemini-3.1-pro-preview,gpt-4o" --sizes "4x4,8x8"
```

## Authentication

The CLI uses GitHub's device flow for authentication:

1. Run `cop login`
2. Open the URL and enter the code shown
3. Credentials are cached in `~/.copilot_chat_creds.json`

For CI/CD, set `COPILOT_GITHUB_TOKEN` or `GH_TOKEN` environment variable.

## License

MIT
