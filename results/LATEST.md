# Pixel Extraction Benchmark Results

Generated on: 2026-09-05T19:48:25.948394


## Summary

This benchmark tests the ability of vision models to extract pixel-level color data from small images.

### Methodology
- Random colored images generated with 8 distinct colors (R, G, B, Y, M, C, O, P)
- Models asked to output a JSON 2D array of color letters
- Accuracy measured as percentage of correctly identified pixels

## Results by Image Size

### 4x4 (16 pixels)

| Model | Zoom | Correct | Accuracy |
|-------|------|---------|----------|
| gemini-3.5-flash | 8x | 16/16 | ✅ 100.0% |
| gpt-6-astra | 8x | 7/16 | 🔴 43.8% |
| gpt-5.4 | 8x | 3/16 | 🔴 18.8% |
| claude-opus-4.7 | 8x | 3/16 | 🔴 18.8% |
| gpt-5-mini | 8x | 2/16 | 🔴 12.5% |
| gpt-4o | 8x | 0/16 | 🔴 0.0% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/193750018f6af7c9b0cf027fecc70e22cd5eb2f4/images/gt_4x4.png" alt="Ground Truth 4x4">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.5-flash | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/193750018f6af7c9b0cf027fecc70e22cd5eb2f4/images/output_4x4_gemini_3_5_flash.png" alt="gemini-3.5-flash" width="64"> |
| gpt-6-astra | 🔴 44% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/193750018f6af7c9b0cf027fecc70e22cd5eb2f4/images/output_4x4_gpt_6_astra.png" alt="gpt-6-astra" width="64"> |
| gpt-5.4 | 🔴 19% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/193750018f6af7c9b0cf027fecc70e22cd5eb2f4/images/output_4x4_gpt_5_4.png" alt="gpt-5.4" width="64"> |
| claude-opus-4.7 | 🔴 19% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/193750018f6af7c9b0cf027fecc70e22cd5eb2f4/images/output_4x4_claude_opus_4_7.png" alt="claude-opus-4.7" width="64"> |
| gpt-5-mini | 🔴 12% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/193750018f6af7c9b0cf027fecc70e22cd5eb2f4/images/output_4x4_gpt_5_mini.png" alt="gpt-5-mini" width="64"> |
| gpt-4o | 🔴 0% | ⚠️ No output |

### 8x8 (64 pixels)

| Model | Zoom | Correct | Accuracy |
|-------|------|---------|----------|
| gemini-3.5-flash | 8x | 64/64 | ✅ 100.0% |
| gpt-6-astra | 8x | 13/64 | 🔴 20.3% |
| gpt-5-mini | 8x | 10/64 | 🔴 15.6% |
| claude-opus-4.7 | 8x | 9/64 | 🔴 14.1% |
| gpt-5.4 | 8x | 7/64 | 🔴 10.9% |
| gpt-4o | 8x | 0/64 | 🔴 0.0% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/193750018f6af7c9b0cf027fecc70e22cd5eb2f4/images/gt_8x8.png" alt="Ground Truth 8x8">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.5-flash | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/193750018f6af7c9b0cf027fecc70e22cd5eb2f4/images/output_8x8_gemini_3_5_flash.png" alt="gemini-3.5-flash" width="64"> |
| gpt-6-astra | 🔴 20% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/193750018f6af7c9b0cf027fecc70e22cd5eb2f4/images/output_8x8_gpt_6_astra.png" alt="gpt-6-astra" width="64"> |
| gpt-5-mini | 🔴 16% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/193750018f6af7c9b0cf027fecc70e22cd5eb2f4/images/output_8x8_gpt_5_mini.png" alt="gpt-5-mini" width="64"> |
| claude-opus-4.7 | 🔴 14% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/193750018f6af7c9b0cf027fecc70e22cd5eb2f4/images/output_8x8_claude_opus_4_7.png" alt="claude-opus-4.7" width="64"> |
| gpt-5.4 | 🔴 11% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/193750018f6af7c9b0cf027fecc70e22cd5eb2f4/images/output_8x8_gpt_5_4.png" alt="gpt-5.4" width="64"> |
| gpt-4o | 🔴 0% | ⚠️ No output |

### Miner Willy Sprite (8x16, 128 pixels)

A classic 2-color retro game sprite (R=Red, W=White).

| Model | Zoom | Correct | Accuracy |
|-------|------|---------|----------|
| gemini-3.5-flash | 8x | 127/128 | 🟡 99.2% |
| gpt-6-astra | 8x | 97/128 | 🔴 75.8% |
| gpt-5.4 | 8x | 82/128 | 🔴 64.1% |
| gpt-5-mini | 8x | 68/128 | 🔴 53.1% |
| claude-opus-4.7 | 8x | 65/128 | 🔴 50.8% |
| gpt-4o | 8x | 0/128 | 🔴 0.0% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/193750018f6af7c9b0cf027fecc70e22cd5eb2f4/images/gt_willy.png" alt="Ground Truth Willy">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.5-flash | 🔴 99% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/193750018f6af7c9b0cf027fecc70e22cd5eb2f4/images/output_willy_gemini_3_5_flash.png" alt="gemini-3.5-flash" width="64"> |
| gpt-6-astra | 🔴 76% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/193750018f6af7c9b0cf027fecc70e22cd5eb2f4/images/output_willy_gpt_6_astra.png" alt="gpt-6-astra" width="64"> |
| gpt-5.4 | 🔴 64% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/193750018f6af7c9b0cf027fecc70e22cd5eb2f4/images/output_willy_gpt_5_4.png" alt="gpt-5.4" width="64"> |
| gpt-5-mini | 🔴 53% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/193750018f6af7c9b0cf027fecc70e22cd5eb2f4/images/output_willy_gpt_5_mini.png" alt="gpt-5-mini" width="64"> |
| claude-opus-4.7 | 🔴 51% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/193750018f6af7c9b0cf027fecc70e22cd5eb2f4/images/output_willy_claude_opus_4_7.png" alt="claude-opus-4.7" width="64"> |
| gpt-4o | 🔴 0% | ⚠️ No output |

## Overall Rankings

Averaged across all image sizes:

| Rank | Model | Avg Accuracy |
|------|-------|--------------|
| 1 | 🥇 gemini-3.5-flash | 99.7% |
| 2 | 🥈 gpt-6-astra | 46.6% |
| 3 | 🥉 gpt-5.4 | 31.2% |
| 4 |  claude-opus-4.7 | 27.9% |
| 5 |  gpt-5-mini | 27.1% |
| 6 |  gpt-4o | 0.0% |

## Key Findings

1. **Zoom significantly improves accuracy** - 8x zoom provides +30-50% improvement for top models
2. **Gemini 3.x models excel** - Achieve near-perfect pixel extraction with proper settings
3. **Structured JSON output helps** - 2D array format with individual letters performs best
4. **Image size matters** - Smaller images (4x4) are easier to extract accurately
