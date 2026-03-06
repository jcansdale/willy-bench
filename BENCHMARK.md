# Pixel Extraction Benchmark

A benchmark suite for testing vision models' ability to extract pixel-level color data from small images.

## Overview

This benchmark tests how accurately various AI vision models can identify individual pixel colors in small images (4x4, 8x8, 8x16, 16x16). It uses the GitHub Copilot API to test multiple models including:

- Gemini 3.x (gemini-3.1-pro-preview, gemini-3-pro-preview)
- Gemini 2.5 (gemini-2.5-pro)
- GPT models (gpt-4o, gpt-5.1, gpt-5.2)
- Claude models (claude-sonnet-4, claude-opus-4.5, etc.)

## Key Findings

Based on extensive testing:

| Model | Best Accuracy | Notes |
|-------|---------------|-------|
| gemini-3.1-pro-preview | **100%** | Perfect on 4x4, 8x8 with 8x zoom |
| gemini-3-pro-preview | **100%** | Perfect on 4x4, 8x8 with 8x zoom |
| gemini-2.5-pro | 68-87% | Good but not perfect |
| gpt-5.1 | 26-87% | Varies by image size |
| gpt-4o | 21-81% | Better on smaller images |
| Claude models | 10-31% | Generate patterns, not actual pixels |

### Critical Settings for Best Results

1. **Use 8x zoom** (+30-50% improvement)
2. **Use 2D JSON array format** (each pixel as separate element)
3. **Smaller images are easier** (4x4 > 8x8 > 16x16)

## Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/codespaces-blank.git
cd codespaces-blank

# Install dependencies
pip install -e .
pip install Pillow
```

## Usage

### Local Testing

```bash
# Quick test (3 top models, 4x4 only)
python benchmark.py --quick

# Full benchmark
python benchmark.py --models "gemini-3.1-pro-preview,gemini-3-pro-preview,gpt-4o" \
                    --sizes "4x4,8x8,8x16" \
                    --zoom 8 \
                    --seed 42

# Test without zoom
python benchmark.py --zoom 0
```

### Authentication

The benchmark requires GitHub Copilot access. Authentication options:

1. **Interactive (local)**: Run `cop login` first
2. **Environment variable (CI/CD)**: Set `COPILOT_GITHUB_TOKEN` or `GH_TOKEN`

### GitHub Actions

The benchmark can run as a GitHub Actions workflow:

1. **Set up secrets**:
   - Go to Settings → Secrets → Actions
   - Add `COPILOT_GITHUB_TOKEN` with a GitHub PAT that has Copilot access

2. **Run manually**:
   - Go to Actions → Pixel Extraction Benchmark
   - Click "Run workflow"
   - Configure models, sizes, zoom, seed

3. **Automated runs**:
   - Runs weekly on Sunday at midnight UTC
   - Runs on push to main (quick mode)

## Output

Results are saved to `benchmark_results/`:

- `RESULTS.md` - Markdown report with tables and rankings
- `results.json` - Detailed JSON data for analysis
- `test_*.png` - Generated test images
- `ground_truth_*.json` - Ground truth pixel data

## Example Results

```
Model                   | 8x Zoom | No Zoom | Δ
------------------------|---------|---------|----
gemini-3.1-pro-preview  | 64/64 100% | 34/64 53% | +30
gemini-3-pro-preview    | 64/64 100% | 35/64 54% | +29
gemini-2.5-pro          | 44/64 68% | 20/64 31% | +24
gpt-4o                  | 14/64 21% | 12/64 18% | +2
claude-sonnet-4         | 10/64 15% |  7/64 10% | +3
```

## How It Works

1. **Image Generation**: Creates random colored images using 8 distinct colors (R, G, B, Y, M, C, O, P)
2. **Prompt Engineering**: Asks models to output a JSON 2D array of color letters
3. **Accuracy Measurement**: Compares model output against ground truth pixel-by-pixel
4. **Zoom**: Optionally scales images up (8x) before sending to improve model accuracy

## License

MIT
