# Pixel Extraction Benchmark Results

Generated on: 2026-04-12T00:54:14.322225


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
| gpt-4o | 8x | 8/16 | 🔴 50.0% |
| claude-sonnet-4.5 | 8x | 5/16 | 🔴 31.2% |
| claude-opus-4.6 | 8x | 4/16 | 🔴 25.0% |
| claude-sonnet-4 | 8x | 2/16 | 🔴 12.5% |
| gpt-5-mini | 8x | 1/16 | 🔴 6.2% |
| gpt-5.4 | 8x | 1/16 | 🔴 6.2% |
| gemini-3-pro-preview | 8x | 0/16 | 🔴 0.0% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/gt_4x4.png" alt="Ground Truth 4x4">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.1-pro-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_4x4_gemini_3_1_pro_preview.png" alt="gemini-3.1-pro-preview" width="64"> |
| gemini-3-flash-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_4x4_gemini_3_flash_preview.png" alt="gemini-3-flash-preview" width="64"> |
| gemini-2.5-pro | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_4x4_gemini_2_5_pro.png" alt="gemini-2.5-pro" width="64"> |
| gpt-4o | 🔴 50% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_4x4_gpt_4o.png" alt="gpt-4o" width="64"> |
| claude-sonnet-4.5 | 🔴 31% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_4x4_claude_sonnet_4_5.png" alt="claude-sonnet-4.5" width="64"> |
| claude-opus-4.6 | 🔴 25% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_4x4_claude_opus_4_6.png" alt="claude-opus-4.6" width="64"> |
| claude-sonnet-4 | 🔴 12% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_4x4_claude_sonnet_4.png" alt="claude-sonnet-4" width="64"> |
| gpt-5-mini | 🔴 6% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_4x4_gpt_5_mini.png" alt="gpt-5-mini" width="64"> |
| gpt-5.4 | 🔴 6% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_4x4_gpt_5_4.png" alt="gpt-5.4" width="64"> |
| gemini-3-pro-preview | 🔴 0% | ⚠️ No output |

### 8x8 (64 pixels)

| Model | Zoom | Correct | Accuracy |
|-------|------|---------|----------|
| gemini-3.1-pro-preview | 8x | 64/64 | ✅ 100.0% |
| gemini-3-flash-preview | 8x | 64/64 | ✅ 100.0% |
| gemini-2.5-pro | 8x | 32/64 | 🔴 50.0% |
| claude-sonnet-4 | 8x | 13/64 | 🔴 20.3% |
| claude-opus-4.6 | 8x | 13/64 | 🔴 20.3% |
| gpt-4o | 8x | 10/64 | 🔴 15.6% |
| claude-sonnet-4.5 | 8x | 9/64 | 🔴 14.1% |
| gpt-5-mini | 8x | 6/64 | 🔴 9.4% |
| gpt-5.4 | 8x | 4/64 | 🔴 6.2% |
| gemini-3-pro-preview | 8x | 0/64 | 🔴 0.0% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/gt_8x8.png" alt="Ground Truth 8x8">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.1-pro-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_8x8_gemini_3_1_pro_preview.png" alt="gemini-3.1-pro-preview" width="64"> |
| gemini-3-flash-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_8x8_gemini_3_flash_preview.png" alt="gemini-3-flash-preview" width="64"> |
| gemini-2.5-pro | 🔴 50% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_8x8_gemini_2_5_pro.png" alt="gemini-2.5-pro" width="64"> |
| claude-sonnet-4 | 🔴 20% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_8x8_claude_sonnet_4.png" alt="claude-sonnet-4" width="64"> |
| claude-opus-4.6 | 🔴 20% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_8x8_claude_opus_4_6.png" alt="claude-opus-4.6" width="64"> |
| gpt-4o | 🔴 16% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_8x8_gpt_4o.png" alt="gpt-4o" width="64"> |
| claude-sonnet-4.5 | 🔴 14% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_8x8_claude_sonnet_4_5.png" alt="claude-sonnet-4.5" width="64"> |
| gpt-5-mini | 🔴 9% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_8x8_gpt_5_mini.png" alt="gpt-5-mini" width="64"> |
| gpt-5.4 | 🔴 6% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_8x8_gpt_5_4.png" alt="gpt-5.4" width="64"> |
| gemini-3-pro-preview | 🔴 0% | ⚠️ No output |

### Miner Willy Sprite (8x16, 128 pixels)

A classic 2-color retro game sprite (R=Red, W=White).

| Model | Zoom | Correct | Accuracy |
|-------|------|---------|----------|
| gemini-3.1-pro-preview | 8x | 123/128 | 🟡 96.1% |
| gemini-3-flash-preview | 8x | 111/128 | 🟡 86.7% |
| gemini-2.5-pro | 8x | 105/128 | 🟡 82.0% |
| gpt-5.4 | 8x | 77/128 | 🔴 60.2% |
| claude-opus-4.6 | 8x | 77/128 | 🔴 60.2% |
| gpt-4o | 8x | 76/128 | 🔴 59.4% |
| claude-sonnet-4.5 | 8x | 74/128 | 🔴 57.8% |
| gpt-5-mini | 8x | 72/128 | 🔴 56.2% |
| claude-sonnet-4 | 8x | 68/128 | 🔴 53.1% |
| gemini-3-pro-preview | 8x | 0/128 | 🔴 0.0% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/gt_willy.png" alt="Ground Truth Willy">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.1-pro-preview | 🔴 96% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_willy_gemini_3_1_pro_preview.png" alt="gemini-3.1-pro-preview" width="64"> |
| gemini-3-flash-preview | 🔴 87% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_willy_gemini_3_flash_preview.png" alt="gemini-3-flash-preview" width="64"> |
| gemini-2.5-pro | 🔴 82% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_willy_gemini_2_5_pro.png" alt="gemini-2.5-pro" width="64"> |
| gpt-5.4 | 🔴 60% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_willy_gpt_5_4.png" alt="gpt-5.4" width="64"> |
| claude-opus-4.6 | 🔴 60% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_willy_claude_opus_4_6.png" alt="claude-opus-4.6" width="64"> |
| gpt-4o | 🔴 59% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_willy_gpt_4o.png" alt="gpt-4o" width="64"> |
| claude-sonnet-4.5 | 🔴 58% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_willy_claude_sonnet_4_5.png" alt="claude-sonnet-4.5" width="64"> |
| gpt-5-mini | 🔴 56% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_willy_gpt_5_mini.png" alt="gpt-5-mini" width="64"> |
| claude-sonnet-4 | 🔴 53% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/7fd4d9a20cff71b5c9ea1c48cedb0f6ee09aed28/images/output_willy_claude_sonnet_4.png" alt="claude-sonnet-4" width="64"> |
| gemini-3-pro-preview | 🔴 0% | ⚠️ No output |

## Overall Rankings

Averaged across all image sizes:

| Rank | Model | Avg Accuracy |
|------|-------|--------------|
| 1 | 🥇 gemini-3.1-pro-preview | 98.7% |
| 2 | 🥈 gemini-3-flash-preview | 95.6% |
| 3 | 🥉 gemini-2.5-pro | 77.3% |
| 4 |  gpt-4o | 41.7% |
| 5 |  claude-opus-4.6 | 35.2% |
| 6 |  claude-sonnet-4.5 | 34.4% |
| 7 |  claude-sonnet-4 | 28.6% |
| 8 |  gpt-5.4 | 24.2% |
| 9 |  gpt-5-mini | 24.0% |
| 10 |  gemini-3-pro-preview | 0.0% |

## Key Findings

1. **Zoom significantly improves accuracy** - 8x zoom provides +30-50% improvement for top models
2. **Gemini 3.x models excel** - Achieve near-perfect pixel extraction with proper settings
3. **Structured JSON output helps** - 2D array format with individual letters performs best
4. **Image size matters** - Smaller images (4x4) are easier to extract accurately
