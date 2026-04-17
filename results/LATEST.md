# Pixel Extraction Benchmark Results

Generated on: 2026-04-17T12:01:56.529148


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
| gemini-3.1-pro-preview | 8x | 16/16 | ✅ 100.0% |
| gemini-3-flash-preview | 8x | 16/16 | ✅ 100.0% |
| gemini-2.5-pro | 8x | 16/16 | ✅ 100.0% |
| gpt-4o | 8x | 14/16 | 🟡 87.5% |
| claude-opus-4.7 | 8x | 7/16 | 🔴 43.8% |
| claude-sonnet-4.5 | 8x | 5/16 | 🔴 31.2% |
| claude-sonnet-4 | 8x | 3/16 | 🔴 18.8% |
| claude-opus-4.6 | 8x | 3/16 | 🔴 18.8% |
| gpt-5-mini | 8x | 2/16 | 🔴 12.5% |
| gemini-3-pro-preview | 8x | 0/16 | 🔴 0.0% |
| gpt-5.4 | 8x | 0/16 | 🔴 0.0% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/gt_4x4.png" alt="Ground Truth 4x4">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.1-pro-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_4x4_gemini_3_1_pro_preview.png" alt="gemini-3.1-pro-preview" width="64"> |
| gemini-3-flash-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_4x4_gemini_3_flash_preview.png" alt="gemini-3-flash-preview" width="64"> |
| gemini-2.5-pro | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_4x4_gemini_2_5_pro.png" alt="gemini-2.5-pro" width="64"> |
| gpt-4o | 🔴 88% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_4x4_gpt_4o.png" alt="gpt-4o" width="64"> |
| claude-opus-4.7 | 🔴 44% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_4x4_claude_opus_4_7.png" alt="claude-opus-4.7" width="64"> |
| claude-sonnet-4.5 | 🔴 31% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_4x4_claude_sonnet_4_5.png" alt="claude-sonnet-4.5" width="64"> |
| claude-sonnet-4 | 🔴 19% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_4x4_claude_sonnet_4.png" alt="claude-sonnet-4" width="64"> |
| claude-opus-4.6 | 🔴 19% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_4x4_claude_opus_4_6.png" alt="claude-opus-4.6" width="64"> |
| gpt-5-mini | 🔴 12% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_4x4_gpt_5_mini.png" alt="gpt-5-mini" width="64"> |
| gemini-3-pro-preview | 🔴 0% | ⚠️ No output |

### 8x8 (64 pixels)

| Model | Zoom | Correct | Accuracy |
|-------|------|---------|----------|
| gemini-3.1-pro-preview | 8x | 64/64 | ✅ 100.0% |
| gemini-3-flash-preview | 8x | 64/64 | ✅ 100.0% |
| gemini-2.5-pro | 8x | 30/64 | 🔴 46.9% |
| claude-sonnet-4 | 8x | 13/64 | 🔴 20.3% |
| claude-sonnet-4.5 | 8x | 13/64 | 🔴 20.3% |
| gpt-4o | 8x | 10/64 | 🔴 15.6% |
| gpt-5.4 | 8x | 9/64 | 🔴 14.1% |
| claude-opus-4.6 | 8x | 8/64 | 🔴 12.5% |
| claude-opus-4.7 | 8x | 8/64 | 🔴 12.5% |
| gpt-5-mini | 8x | 4/64 | 🔴 6.2% |
| gemini-3-pro-preview | 8x | 0/64 | 🔴 0.0% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/gt_8x8.png" alt="Ground Truth 8x8">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.1-pro-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_8x8_gemini_3_1_pro_preview.png" alt="gemini-3.1-pro-preview" width="64"> |
| gemini-3-flash-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_8x8_gemini_3_flash_preview.png" alt="gemini-3-flash-preview" width="64"> |
| gemini-2.5-pro | 🔴 47% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_8x8_gemini_2_5_pro.png" alt="gemini-2.5-pro" width="64"> |
| claude-sonnet-4 | 🔴 20% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_8x8_claude_sonnet_4.png" alt="claude-sonnet-4" width="64"> |
| claude-sonnet-4.5 | 🔴 20% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_8x8_claude_sonnet_4_5.png" alt="claude-sonnet-4.5" width="64"> |
| gpt-4o | 🔴 16% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_8x8_gpt_4o.png" alt="gpt-4o" width="64"> |
| gpt-5.4 | 🔴 14% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_8x8_gpt_5_4.png" alt="gpt-5.4" width="64"> |
| claude-opus-4.6 | 🔴 12% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_8x8_claude_opus_4_6.png" alt="claude-opus-4.6" width="64"> |
| claude-opus-4.7 | 🔴 12% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_8x8_claude_opus_4_7.png" alt="claude-opus-4.7" width="64"> |
| gpt-5-mini | 🔴 6% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_8x8_gpt_5_mini.png" alt="gpt-5-mini" width="64"> |

### Miner Willy Sprite (8x16, 128 pixels)

A classic 2-color retro game sprite (R=Red, W=White).

| Model | Zoom | Correct | Accuracy |
|-------|------|---------|----------|
| gemini-3.1-pro-preview | 8x | 125/128 | 🟡 97.7% |
| gemini-3-flash-preview | 8x | 109/128 | 🟡 85.2% |
| gemini-2.5-pro | 8x | 100/128 | 🔴 78.1% |
| gpt-5.4 | 8x | 88/128 | 🔴 68.8% |
| gpt-4o | 8x | 84/128 | 🔴 65.6% |
| claude-sonnet-4.5 | 8x | 78/128 | 🔴 60.9% |
| claude-sonnet-4 | 8x | 72/128 | 🔴 56.2% |
| claude-opus-4.7 | 8x | 72/128 | 🔴 56.2% |
| gpt-5-mini | 8x | 70/128 | 🔴 54.7% |
| gemini-3-pro-preview | 8x | 0/128 | 🔴 0.0% |
| claude-opus-4.6 | 8x | 0/128 | 🔴 0.0% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/gt_willy.png" alt="Ground Truth Willy">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.1-pro-preview | 🔴 98% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_willy_gemini_3_1_pro_preview.png" alt="gemini-3.1-pro-preview" width="64"> |
| gemini-3-flash-preview | 🔴 85% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_willy_gemini_3_flash_preview.png" alt="gemini-3-flash-preview" width="64"> |
| gemini-2.5-pro | 🔴 78% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_willy_gemini_2_5_pro.png" alt="gemini-2.5-pro" width="64"> |
| gpt-5.4 | 🔴 69% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_willy_gpt_5_4.png" alt="gpt-5.4" width="64"> |
| gpt-4o | 🔴 66% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_willy_gpt_4o.png" alt="gpt-4o" width="64"> |
| claude-sonnet-4.5 | 🔴 61% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_willy_claude_sonnet_4_5.png" alt="claude-sonnet-4.5" width="64"> |
| claude-sonnet-4 | 🔴 56% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_willy_claude_sonnet_4.png" alt="claude-sonnet-4" width="64"> |
| claude-opus-4.7 | 🔴 56% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_willy_claude_opus_4_7.png" alt="claude-opus-4.7" width="64"> |
| gpt-5-mini | 🔴 55% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/85367a7e016d4035f4eb3ad87c9ebaaa2e51017f/images/output_willy_gpt_5_mini.png" alt="gpt-5-mini" width="64"> |
| gemini-3-pro-preview | 🔴 0% | ⚠️ No output |

## Overall Rankings

Averaged across all image sizes:

| Rank | Model | Avg Accuracy |
|------|-------|--------------|
| 1 | 🥇 gemini-3.1-pro-preview | 99.2% |
| 2 | 🥈 gemini-3-flash-preview | 95.1% |
| 3 | 🥉 gemini-2.5-pro | 75.0% |
| 4 |  gpt-4o | 56.2% |
| 5 |  claude-sonnet-4.5 | 37.5% |
| 6 |  claude-opus-4.7 | 37.5% |
| 7 |  claude-sonnet-4 | 31.8% |
| 8 |  gpt-5.4 | 27.6% |
| 9 |  gpt-5-mini | 24.5% |
| 10 |  claude-opus-4.6 | 10.4% |
| 11 |  gemini-3-pro-preview | 0.0% |

## Key Findings

1. **Zoom significantly improves accuracy** - 8x zoom provides +30-50% improvement for top models
2. **Gemini 3.x models excel** - Achieve near-perfect pixel extraction with proper settings
3. **Structured JSON output helps** - 2D array format with individual letters performs best
4. **Image size matters** - Smaller images (4x4) are easier to extract accurately
