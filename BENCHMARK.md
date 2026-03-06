# Pixel Extraction Benchmark

A benchmark suite for testing vision models' ability to extract pixel-level color data from small images.

## Overview

This benchmark tests how accurately various AI vision models can identify individual pixel colors in small images (4x4, 8x8, 8x16). It uses the GitHub Copilot API to test multiple models including:

- **Gemini 3.x** (gemini-3.1-pro-preview, gemini-3-pro-preview) — Best performers
- **Gemini 2.5** (gemini-2.5-pro)
- **GPT models** (gpt-4o, gpt-5.4) — gpt-5.4 requires Responses API
- **Claude models** (claude-sonnet-4, claude-opus-4.6)

## Key Findings

Based on extensive testing:

| Model | API | Best Accuracy | Notes |
|-------|-----|---------------|-------|
| gemini-3.1-pro-preview | Chat | **100%** | Perfect on 4x4, 8x8 with 8x zoom |
| gemini-3-pro-preview | Chat | **100%** | Perfect on 4x4, 8x8 with 8x zoom |
| gemini-2.5-pro | Chat | ~78% | Good but not perfect |
| claude-sonnet-4 | Chat | ~66% | Improved with proper prompting |
| claude-opus-4.6 | Chat | ~66% | Similar to sonnet |
| gpt-5.4 | Responses | ~63% | Requires Responses API |
| gpt-4o | Chat | ~62% | Better on smaller images |

### Critical Settings for Best Results

1. **Use 8x zoom** (+30-50% improvement)
2. **Use 2D JSON array format** (each pixel as separate element)
3. **Smaller images are easier** (4x4 > 8x8 > 16x16)

## Installation

```bash
# Clone the repository
git clone https://github.com/jcansdale/willy-bench.git
cd willy-bench

# Install dependencies
pip install -e .
pip install Pillow
```

## Usage

### Local Testing

```bash
# Quick test (3 top models, 4x4 only)
python benchmark.py --quick

# Full benchmark with Willy sprite
python benchmark.py --models "gemini-3.1-pro-preview,gpt-4o,claude-sonnet-4" \
                    --sizes "4x4,8x8" \
                    --zoom 8 \
                    --willy

# Regenerate report with image URLs (for CI)
python benchmark.py --regenerate --image-base-url "https://example.com/images"
```

### Miner Willy Sprite Test

The benchmark includes an 8x16 classic retro game sprite challenge:

```bash
python benchmark.py --willy --zoom 8
```

This tests models on a 2-color (Red/White) Miner Willy sprite — a more complex pixel extraction task.

### Authentication

The benchmark requires GitHub Copilot access. Authentication options:

1. **Interactive (local)**: Run `cop login` first
2. **Environment variable (CI/CD)**: Set `COPILOT_GITHUB_TOKEN`

### GitHub Actions

The benchmark runs as a GitHub Actions workflow:

1. **Set up secrets**:
   - Go to Settings → Secrets → Actions
   - Add `COPILOT_GITHUB_TOKEN` with your Copilot credentials

2. **Run manually**:
   - Go to Actions → Pixel Extraction Benchmark
   - Click "Run workflow"
   - Configure models, sizes, zoom, seed

3. **View results**:
   - Job summary shows emoji visual comparison
   - Download artifacts for PNG images with error highlighting

## Output

Results are saved to `benchmark_results/`:

- `RESULTS.md` - Markdown report with tables and visual comparison
- `results.json` - Detailed JSON data for analysis
- `images/` - PNG images showing ground truth vs model output
  - Red X marks on incorrect pixels
  - Ground truth images for reference

### Visual Comparison

The benchmark generates visual comparisons showing:
- **Ground truth** — The actual pixel colors
- **Model output** — What each model extracted
- **Error highlighting** — Red X on incorrect pixels

## APIs

The benchmark supports two Copilot APIs:

| API | Endpoint | Models |
|-----|----------|--------|
| Chat Completions | `/chat/completions` | Most models (Gemini, Claude, gpt-4o) |
| Responses | `/responses` | gpt-5.4, gpt-5.x-codex models |

The `cop` CLI auto-detects which API to use based on model name.

## How It Works

1. **Image Generation**: Creates random colored images using 8 distinct colors (R, G, B, Y, M, C, O, P)
2. **Prompt Engineering**: Asks models to output a JSON 2D array of color letters
3. **Accuracy Measurement**: Compares model output against ground truth pixel-by-pixel
4. **Zoom**: Scales images up (8x) before sending to improve model accuracy
5. **Visual Output**: Generates PNG images showing errors

## License

MIT
