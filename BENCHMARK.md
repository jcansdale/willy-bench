# Pixel Extraction Benchmark

A benchmark suite for testing vision models' ability to extract pixel-level color data from small images.

## Overview

This benchmark tests how accurately various AI vision models can identify individual pixel colors in small images (4x4, 8x8, 8x16). It uses the GitHub Copilot API to test multiple models including:

- **Gemini models** (gemini-3.5-flash, gemini-3.6-flash, gemini-3.7-flash, gemini-3.8-flash)
- **GPT models** (gpt-4o-2024-05-13, gpt-5.4, gpt-5.5, gpt-5.6-terra, gpt-5.6-sol, gpt-6-astra)
- **Claude models** (claude-haiku-4.5, claude-sonnet-5, claude-opus-5)
- **Grok models** (grok-4.6)

GPT-5.4 and newer GPT models, plus Grok 4.6, use the Responses API.

## Key Findings

Based on extensive testing:

| Model | API | Latest Average Accuracy | Notes |
|-------|-----|-------------------------|-------|
| gemini-3.5-flash | Chat | **99.2%** | Near-perfect across the latest benchmark |
| gemini-3.6-flash | Chat | TBD | Gemini version comparison |
| gemini-3.7-flash | Chat | TBD | Gemini version comparison |
| gemini-3.8-flash | Chat | TBD | Current Gemini comparison |
| gpt-5.4 | Responses | 37.0% | Requires Responses API |
| gpt-5.5 | Responses | TBD | Intermediate GPT generation |
| gpt-5.6-terra | Responses | TBD | General-purpose GPT-5.6 tier |
| gpt-5.6-sol | Responses | TBD | Powerful GPT-5.6 tier |
| gpt-6-astra | Responses | TBD | Frontier GPT model |
| gpt-4o-2024-05-13 | Chat | 46.9% | Pinned because newer GPT-4o snapshots reject vision input |
| claude-haiku-4.5 | Chat | TBD | Lightweight Claude baseline |
| claude-sonnet-5 | Chat | TBD | Balanced Claude model |
| claude-opus-5 | Chat | TBD | Frontier Claude model |
| grok-4.6 | Responses | TBD | Current xAI comparison |

### Critical Settings for Best Results

1. **Use contiguous 32px logical cells** for a model-independent visual resolution
2. **Use low reasoning effort where supported** to reduce provider-default compute differences
3. **Use 2D JSON array format** (each pixel as separate element)
4. **Smaller images are easier** (4x4 > 8x8 > 16x16)

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
python benchmark.py --models "gemini-3.8-flash,gpt-6-astra,claude-sonnet-5" \
                    --sizes "4x4,8x8" \
                    --zoom 32 \
                    --reasoning-effort low \
                    --willy

# Regenerate report with image URLs (for CI)
python benchmark.py --regenerate --image-base-url "https://example.com/images"
```

### Miner Willy Sprite Test

The benchmark includes an 8x16 classic retro game sprite challenge:

```bash
python benchmark.py --willy --zoom 32
```

This tests models on a 2-color (Red/White) Miner Willy sprite — a more complex pixel extraction task. The `--zoom` value is the rendered size of each original sprite pixel; cells remain contiguous with no added grid lines.

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
   - Configure models, sizes, cell size, reasoning effort, and seed

3. **View results**:
   - Job summary shows emoji visual comparison
   - Download artifacts for PNG images with error highlighting

## Output

Results are saved to `benchmark_results/`:

- `RESULTS.md` - Markdown report with tables, visual comparison, and collapsible reasoning summaries when available
- `results.json` - Detailed JSON data for analysis, including model-provided `reasoning_text` when available
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
| Chat Completions | `/chat/completions` | Most models (Gemini, Claude, gpt-4o-2024-05-13) |
| Responses | `/responses` | GPT-5.4+, GPT-6 Astra, Grok 4.6, GPT Codex models |

The `cop` CLI auto-detects which API to use based on model name.

## How It Works

1. **Image Generation**: Creates random colored images using 8 distinct colors (R, G, B, Y, M, C, O, P)
2. **Prompt Engineering**: Asks models to output a JSON 2D array of color letters
3. **Metrics**: Reports raw pixel accuracy and Cohen's kappa, where 1 is perfect agreement, 0 is chance-level agreement, and negative values are worse than chance
4. **Reasoning**: Uses low reasoning effort where supported and captures optional reasoning summaries without mixing them into the scored output
5. **Cell size**: Renders every logical pixel as a contiguous 32x32 block using nearest-neighbor scaling
6. **Visual Output**: Generates PNG images showing errors

## License

MIT
