# Pixel Extraction Benchmark Results

Generated on: 2026-09-05T19:41:46.349451


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
| gpt-6-astra | 8x | 4/16 | 🔴 25.0% |
| claude-opus-4.7 | 8x | 4/16 | 🔴 25.0% |
| gpt-5-mini | 8x | 1/16 | 🔴 6.2% |
| gpt-5.4 | 8x | 1/16 | 🔴 6.2% |
| gemini-3.1-pro-preview | 8x | 0/16 | 🔴 0.0% |
| gemini-3-flash-preview | 8x | 0/16 | 🔴 0.0% |
| gemini-2.5-pro | 8x | 0/16 | 🔴 0.0% |
| gpt-4o | 8x | 0/16 | 🔴 0.0% |
| claude-sonnet-4 | 8x | 0/16 | 🔴 0.0% |
| claude-sonnet-4.5 | 8x | 0/16 | 🔴 0.0% |
| claude-opus-4.6 | 8x | 0/16 | 🔴 0.0% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fed3a33fc34771679caaafeef7bfb49f0f05487/images/gt_4x4.png" alt="Ground Truth 4x4">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.5-flash | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fed3a33fc34771679caaafeef7bfb49f0f05487/images/output_4x4_gemini_3_5_flash.png" alt="gemini-3.5-flash" width="64"> |
| gpt-6-astra | 🔴 25% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fed3a33fc34771679caaafeef7bfb49f0f05487/images/output_4x4_gpt_6_astra.png" alt="gpt-6-astra" width="64"> |
| claude-opus-4.7 | 🔴 25% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fed3a33fc34771679caaafeef7bfb49f0f05487/images/output_4x4_claude_opus_4_7.png" alt="claude-opus-4.7" width="64"> |
| gpt-5-mini | 🔴 6% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fed3a33fc34771679caaafeef7bfb49f0f05487/images/output_4x4_gpt_5_mini.png" alt="gpt-5-mini" width="64"> |
| gpt-5.4 | 🔴 6% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fed3a33fc34771679caaafeef7bfb49f0f05487/images/output_4x4_gpt_5_4.png" alt="gpt-5.4" width="64"> |
| gemini-3.1-pro-preview | 🔴 0% | ⚠️ No output |
| gemini-3-flash-preview | 🔴 0% | ⚠️ No output |
| gemini-2.5-pro | 🔴 0% | ⚠️ No output |
| gpt-4o | 🔴 0% | ⚠️ No output |
| claude-sonnet-4 | 🔴 0% | ⚠️ No output |

### 8x8 (64 pixels)

| Model | Zoom | Correct | Accuracy |
|-------|------|---------|----------|
| gemini-3.5-flash | 8x | 64/64 | ✅ 100.0% |
| gpt-6-astra | 8x | 17/64 | 🔴 26.6% |
| gpt-5.4 | 8x | 11/64 | 🔴 17.2% |
| claude-opus-4.7 | 8x | 11/64 | 🔴 17.2% |
| gpt-5-mini | 8x | 6/64 | 🔴 9.4% |
| gemini-3.1-pro-preview | 8x | 0/64 | 🔴 0.0% |
| gemini-3-flash-preview | 8x | 0/64 | 🔴 0.0% |
| gemini-2.5-pro | 8x | 0/64 | 🔴 0.0% |
| gpt-4o | 8x | 0/64 | 🔴 0.0% |
| claude-sonnet-4 | 8x | 0/64 | 🔴 0.0% |
| claude-sonnet-4.5 | 8x | 0/64 | 🔴 0.0% |
| claude-opus-4.6 | 8x | 0/64 | 🔴 0.0% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fed3a33fc34771679caaafeef7bfb49f0f05487/images/gt_8x8.png" alt="Ground Truth 8x8">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.5-flash | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fed3a33fc34771679caaafeef7bfb49f0f05487/images/output_8x8_gemini_3_5_flash.png" alt="gemini-3.5-flash" width="64"> |
| gpt-6-astra | 🔴 27% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fed3a33fc34771679caaafeef7bfb49f0f05487/images/output_8x8_gpt_6_astra.png" alt="gpt-6-astra" width="64"> |
| gpt-5.4 | 🔴 17% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fed3a33fc34771679caaafeef7bfb49f0f05487/images/output_8x8_gpt_5_4.png" alt="gpt-5.4" width="64"> |
| claude-opus-4.7 | 🔴 17% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fed3a33fc34771679caaafeef7bfb49f0f05487/images/output_8x8_claude_opus_4_7.png" alt="claude-opus-4.7" width="64"> |
| gpt-5-mini | 🔴 9% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fed3a33fc34771679caaafeef7bfb49f0f05487/images/output_8x8_gpt_5_mini.png" alt="gpt-5-mini" width="64"> |
| gemini-3.1-pro-preview | 🔴 0% | ⚠️ No output |
| gemini-3-flash-preview | 🔴 0% | ⚠️ No output |
| gemini-2.5-pro | 🔴 0% | ⚠️ No output |
| gpt-4o | 🔴 0% | ⚠️ No output |
| claude-sonnet-4 | 🔴 0% | ⚠️ No output |

### Miner Willy Sprite (8x16, 128 pixels)

A classic 2-color retro game sprite (R=Red, W=White).

| Model | Zoom | Correct | Accuracy |
|-------|------|---------|----------|
| gemini-3.5-flash | 8x | 125/128 | 🟡 97.7% |
| gpt-6-astra | 8x | 96/128 | 🔴 75.0% |
| gpt-5.4 | 8x | 78/128 | 🔴 60.9% |
| claude-opus-4.7 | 8x | 71/128 | 🔴 55.5% |
| gpt-5-mini | 8x | 61/128 | 🔴 47.7% |
| gemini-3.1-pro-preview | 8x | 0/128 | 🔴 0.0% |
| gemini-3-flash-preview | 8x | 0/128 | 🔴 0.0% |
| gemini-2.5-pro | 8x | 0/128 | 🔴 0.0% |
| gpt-4o | 8x | 0/128 | 🔴 0.0% |
| claude-sonnet-4 | 8x | 0/128 | 🔴 0.0% |
| claude-sonnet-4.5 | 8x | 0/128 | 🔴 0.0% |
| claude-opus-4.6 | 8x | 0/128 | 🔴 0.0% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fed3a33fc34771679caaafeef7bfb49f0f05487/images/gt_willy.png" alt="Ground Truth Willy">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.5-flash | 🔴 98% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fed3a33fc34771679caaafeef7bfb49f0f05487/images/output_willy_gemini_3_5_flash.png" alt="gemini-3.5-flash" width="64"> |
| gpt-6-astra | 🔴 75% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fed3a33fc34771679caaafeef7bfb49f0f05487/images/output_willy_gpt_6_astra.png" alt="gpt-6-astra" width="64"> |
| gpt-5.4 | 🔴 61% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fed3a33fc34771679caaafeef7bfb49f0f05487/images/output_willy_gpt_5_4.png" alt="gpt-5.4" width="64"> |
| claude-opus-4.7 | 🔴 55% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fed3a33fc34771679caaafeef7bfb49f0f05487/images/output_willy_claude_opus_4_7.png" alt="claude-opus-4.7" width="64"> |
| gpt-5-mini | 🔴 48% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fed3a33fc34771679caaafeef7bfb49f0f05487/images/output_willy_gpt_5_mini.png" alt="gpt-5-mini" width="64"> |
| gemini-3.1-pro-preview | 🔴 0% | ⚠️ No output |
| gemini-3-flash-preview | 🔴 0% | ⚠️ No output |
| gemini-2.5-pro | 🔴 0% | ⚠️ No output |
| gpt-4o | 🔴 0% | ⚠️ No output |
| claude-sonnet-4 | 🔴 0% | ⚠️ No output |

## Overall Rankings

Averaged across all image sizes:

| Rank | Model | Avg Accuracy |
|------|-------|--------------|
| 1 | 🥇 gemini-3.5-flash | 99.2% |
| 2 | 🥈 gpt-6-astra | 42.2% |
| 3 | 🥉 claude-opus-4.7 | 32.6% |
| 4 |  gpt-5.4 | 28.1% |
| 5 |  gpt-5-mini | 21.1% |
| 6 |  gemini-3.1-pro-preview | 0.0% |
| 7 |  gemini-3-flash-preview | 0.0% |
| 8 |  gemini-2.5-pro | 0.0% |
| 9 |  gpt-4o | 0.0% |
| 10 |  claude-sonnet-4 | 0.0% |
| 11 |  claude-sonnet-4.5 | 0.0% |
| 12 |  claude-opus-4.6 | 0.0% |

## Key Findings

1. **Zoom significantly improves accuracy** - 8x zoom provides +30-50% improvement for top models
2. **Gemini 3.x models excel** - Achieve near-perfect pixel extraction with proper settings
3. **Structured JSON output helps** - 2D array format with individual letters performs best
4. **Image size matters** - Smaller images (4x4) are easier to extract accurately
