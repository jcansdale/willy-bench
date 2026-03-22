# Pixel Extraction Benchmark Results

Generated on: 2026-03-22T00:43:33.066070


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
| gemini-3-pro-preview | 8x | 16/16 | ✅ 100.0% |
| gemini-3-flash-preview | 8x | 16/16 | ✅ 100.0% |
| gemini-2.5-pro | 8x | 16/16 | ✅ 100.0% |
| gpt-4o | 8x | 15/16 | 🟡 93.8% |
| claude-sonnet-4.5 | 8x | 4/16 | 🔴 25.0% |
| claude-opus-4.6 | 8x | 4/16 | 🔴 25.0% |
| gpt-5-mini | 8x | 2/16 | 🔴 12.5% |
| claude-sonnet-4 | 8x | 2/16 | 🔴 12.5% |
| gpt-5.4 | 8x | 1/16 | 🔴 6.2% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/gt_4x4.png" alt="Ground Truth 4x4">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.1-pro-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_4x4_gemini_3_1_pro_preview.png" alt="gemini-3.1-pro-preview" width="64"> |
| gemini-3-pro-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_4x4_gemini_3_pro_preview.png" alt="gemini-3-pro-preview" width="64"> |
| gemini-3-flash-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_4x4_gemini_3_flash_preview.png" alt="gemini-3-flash-preview" width="64"> |
| gemini-2.5-pro | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_4x4_gemini_2_5_pro.png" alt="gemini-2.5-pro" width="64"> |
| gpt-4o | 🔴 94% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_4x4_gpt_4o.png" alt="gpt-4o" width="64"> |
| claude-sonnet-4.5 | 🔴 25% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_4x4_claude_sonnet_4_5.png" alt="claude-sonnet-4.5" width="64"> |
| claude-opus-4.6 | 🔴 25% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_4x4_claude_opus_4_6.png" alt="claude-opus-4.6" width="64"> |
| gpt-5-mini | 🔴 12% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_4x4_gpt_5_mini.png" alt="gpt-5-mini" width="64"> |
| claude-sonnet-4 | 🔴 12% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_4x4_claude_sonnet_4.png" alt="claude-sonnet-4" width="64"> |
| gpt-5.4 | 🔴 6% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_4x4_gpt_5_4.png" alt="gpt-5.4" width="64"> |

### 8x8 (64 pixels)

| Model | Zoom | Correct | Accuracy |
|-------|------|---------|----------|
| gemini-3.1-pro-preview | 8x | 64/64 | ✅ 100.0% |
| gemini-3-pro-preview | 8x | 64/64 | ✅ 100.0% |
| gemini-3-flash-preview | 8x | 64/64 | ✅ 100.0% |
| gemini-2.5-pro | 8x | 27/64 | 🔴 42.2% |
| claude-opus-4.6 | 8x | 13/64 | 🔴 20.3% |
| gpt-5.4 | 8x | 11/64 | 🔴 17.2% |
| gpt-4o | 8x | 8/64 | 🔴 12.5% |
| gpt-5-mini | 8x | 8/64 | 🔴 12.5% |
| claude-sonnet-4.5 | 8x | 7/64 | 🔴 10.9% |
| claude-sonnet-4 | 8x | 6/64 | 🔴 9.4% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/gt_8x8.png" alt="Ground Truth 8x8">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.1-pro-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_8x8_gemini_3_1_pro_preview.png" alt="gemini-3.1-pro-preview" width="64"> |
| gemini-3-pro-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_8x8_gemini_3_pro_preview.png" alt="gemini-3-pro-preview" width="64"> |
| gemini-3-flash-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_8x8_gemini_3_flash_preview.png" alt="gemini-3-flash-preview" width="64"> |
| gemini-2.5-pro | 🔴 42% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_8x8_gemini_2_5_pro.png" alt="gemini-2.5-pro" width="64"> |
| claude-opus-4.6 | 🔴 20% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_8x8_claude_opus_4_6.png" alt="claude-opus-4.6" width="64"> |
| gpt-5.4 | 🔴 17% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_8x8_gpt_5_4.png" alt="gpt-5.4" width="64"> |
| gpt-4o | 🔴 12% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_8x8_gpt_4o.png" alt="gpt-4o" width="64"> |
| gpt-5-mini | 🔴 12% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_8x8_gpt_5_mini.png" alt="gpt-5-mini" width="64"> |
| claude-sonnet-4.5 | 🔴 11% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_8x8_claude_sonnet_4_5.png" alt="claude-sonnet-4.5" width="64"> |
| claude-sonnet-4 | 🔴 9% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_8x8_claude_sonnet_4.png" alt="claude-sonnet-4" width="64"> |

### Miner Willy Sprite (8x16, 128 pixels)

A classic 2-color retro game sprite (R=Red, W=White).

| Model | Zoom | Correct | Accuracy |
|-------|------|---------|----------|
| gemini-3-flash-preview | 8x | 128/128 | ✅ 100.0% |
| gemini-3.1-pro-preview | 8x | 124/128 | 🟡 96.9% |
| gemini-3-pro-preview | 8x | 118/128 | 🟡 92.2% |
| gemini-2.5-pro | 8x | 93/128 | 🔴 72.7% |
| gpt-5.4 | 8x | 93/128 | 🔴 72.7% |
| claude-sonnet-4.5 | 8x | 84/128 | 🔴 65.6% |
| claude-opus-4.6 | 8x | 81/128 | 🔴 63.3% |
| gpt-4o | 8x | 78/128 | 🔴 60.9% |
| gpt-5-mini | 8x | 73/128 | 🔴 57.0% |
| claude-sonnet-4 | 8x | 68/128 | 🔴 53.1% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/gt_willy.png" alt="Ground Truth Willy">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3-flash-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_willy_gemini_3_flash_preview.png" alt="gemini-3-flash-preview" width="64"> |
| gemini-3.1-pro-preview | 🔴 97% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_willy_gemini_3_1_pro_preview.png" alt="gemini-3.1-pro-preview" width="64"> |
| gemini-3-pro-preview | 🔴 92% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_willy_gemini_3_pro_preview.png" alt="gemini-3-pro-preview" width="64"> |
| gemini-2.5-pro | 🔴 73% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_willy_gemini_2_5_pro.png" alt="gemini-2.5-pro" width="64"> |
| gpt-5.4 | 🔴 73% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_willy_gpt_5_4.png" alt="gpt-5.4" width="64"> |
| claude-sonnet-4.5 | 🔴 66% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_willy_claude_sonnet_4_5.png" alt="claude-sonnet-4.5" width="64"> |
| claude-opus-4.6 | 🔴 63% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_willy_claude_opus_4_6.png" alt="claude-opus-4.6" width="64"> |
| gpt-4o | 🔴 61% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_willy_gpt_4o.png" alt="gpt-4o" width="64"> |
| gpt-5-mini | 🔴 57% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_willy_gpt_5_mini.png" alt="gpt-5-mini" width="64"> |
| claude-sonnet-4 | 🔴 53% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/0cba8b3031dd5f6be41ebac7256df84a50c43cb1/images/output_willy_claude_sonnet_4.png" alt="claude-sonnet-4" width="64"> |

## Overall Rankings

Averaged across all image sizes:

| Rank | Model | Avg Accuracy |
|------|-------|--------------|
| 1 | 🥇 gemini-3-flash-preview | 100.0% |
| 2 | 🥈 gemini-3.1-pro-preview | 99.0% |
| 3 | 🥉 gemini-3-pro-preview | 97.4% |
| 4 |  gemini-2.5-pro | 71.6% |
| 5 |  gpt-4o | 55.7% |
| 6 |  claude-opus-4.6 | 36.2% |
| 7 |  claude-sonnet-4.5 | 33.9% |
| 8 |  gpt-5.4 | 32.0% |
| 9 |  gpt-5-mini | 27.3% |
| 10 |  claude-sonnet-4 | 25.0% |

## Key Findings

1. **Zoom significantly improves accuracy** - 8x zoom provides +30-50% improvement for top models
2. **Gemini 3.x models excel** - Achieve near-perfect pixel extraction with proper settings
3. **Structured JSON output helps** - 2D array format with individual letters performs best
4. **Image size matters** - Smaller images (4x4) are easier to extract accurately
