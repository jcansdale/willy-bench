# Pixel Extraction Benchmark Results

Generated on: 2026-03-08T00:41:26.102971


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
| gpt-4o | 8x | 13/16 | 🟡 81.2% |
| claude-opus-4.6 | 8x | 4/16 | 🔴 25.0% |
| claude-sonnet-4 | 8x | 3/16 | 🔴 18.8% |
| gpt-5.4 | 8x | 2/16 | 🔴 12.5% |
| claude-sonnet-4.5 | 8x | 2/16 | 🔴 12.5% |
| gpt-5-mini | 8x | 1/16 | 🔴 6.2% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/gt_4x4.png" alt="Ground Truth 4x4">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.1-pro-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_4x4_gemini_3_1_pro_preview.png" alt="gemini-3.1-pro-preview" width="64"> |
| gemini-3-pro-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_4x4_gemini_3_pro_preview.png" alt="gemini-3-pro-preview" width="64"> |
| gemini-3-flash-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_4x4_gemini_3_flash_preview.png" alt="gemini-3-flash-preview" width="64"> |
| gemini-2.5-pro | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_4x4_gemini_2_5_pro.png" alt="gemini-2.5-pro" width="64"> |
| gpt-4o | 🔴 81% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_4x4_gpt_4o.png" alt="gpt-4o" width="64"> |
| claude-opus-4.6 | 🔴 25% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_4x4_claude_opus_4_6.png" alt="claude-opus-4.6" width="64"> |
| claude-sonnet-4 | 🔴 19% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_4x4_claude_sonnet_4.png" alt="claude-sonnet-4" width="64"> |
| gpt-5.4 | 🔴 12% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_4x4_gpt_5_4.png" alt="gpt-5.4" width="64"> |
| claude-sonnet-4.5 | 🔴 12% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_4x4_claude_sonnet_4_5.png" alt="claude-sonnet-4.5" width="64"> |
| gpt-5-mini | 🔴 6% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_4x4_gpt_5_mini.png" alt="gpt-5-mini" width="64"> |

### 8x8 (64 pixels)

| Model | Zoom | Correct | Accuracy |
|-------|------|---------|----------|
| gemini-3.1-pro-preview | 8x | 64/64 | ✅ 100.0% |
| gemini-3-pro-preview | 8x | 64/64 | ✅ 100.0% |
| gemini-3-flash-preview | 8x | 64/64 | ✅ 100.0% |
| gemini-2.5-pro | 8x | 23/64 | 🔴 35.9% |
| claude-sonnet-4 | 8x | 13/64 | 🔴 20.3% |
| claude-opus-4.6 | 8x | 11/64 | 🔴 17.2% |
| gpt-5-mini | 8x | 10/64 | 🔴 15.6% |
| gpt-4o | 8x | 9/64 | 🔴 14.1% |
| claude-sonnet-4.5 | 8x | 9/64 | 🔴 14.1% |
| gpt-5.4 | 8x | 7/64 | 🔴 10.9% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/gt_8x8.png" alt="Ground Truth 8x8">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.1-pro-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_8x8_gemini_3_1_pro_preview.png" alt="gemini-3.1-pro-preview" width="64"> |
| gemini-3-pro-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_8x8_gemini_3_pro_preview.png" alt="gemini-3-pro-preview" width="64"> |
| gemini-3-flash-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_8x8_gemini_3_flash_preview.png" alt="gemini-3-flash-preview" width="64"> |
| gemini-2.5-pro | 🔴 36% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_8x8_gemini_2_5_pro.png" alt="gemini-2.5-pro" width="64"> |
| claude-sonnet-4 | 🔴 20% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_8x8_claude_sonnet_4.png" alt="claude-sonnet-4" width="64"> |
| claude-opus-4.6 | 🔴 17% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_8x8_claude_opus_4_6.png" alt="claude-opus-4.6" width="64"> |
| gpt-5-mini | 🔴 16% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_8x8_gpt_5_mini.png" alt="gpt-5-mini" width="64"> |
| gpt-4o | 🔴 14% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_8x8_gpt_4o.png" alt="gpt-4o" width="64"> |
| claude-sonnet-4.5 | 🔴 14% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_8x8_claude_sonnet_4_5.png" alt="claude-sonnet-4.5" width="64"> |
| gpt-5.4 | 🔴 11% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_8x8_gpt_5_4.png" alt="gpt-5.4" width="64"> |

### Miner Willy Sprite (8x16, 128 pixels)

A classic 2-color retro game sprite (R=Red, W=White).

| Model | Zoom | Correct | Accuracy |
|-------|------|---------|----------|
| gemini-3.1-pro-preview | 8x | 124/128 | 🟡 96.9% |
| gemini-3-pro-preview | 8x | 123/128 | 🟡 96.1% |
| gemini-3-flash-preview | 8x | 108/128 | 🟡 84.4% |
| gemini-2.5-pro | 8x | 105/128 | 🟡 82.0% |
| gpt-5.4 | 8x | 87/128 | 🔴 68.0% |
| gpt-4o | 8x | 80/128 | 🔴 62.5% |
| claude-sonnet-4.5 | 8x | 76/128 | 🔴 59.4% |
| claude-opus-4.6 | 8x | 75/128 | 🔴 58.6% |
| gpt-5-mini | 8x | 69/128 | 🔴 53.9% |
| claude-sonnet-4 | 8x | 66/128 | 🔴 51.6% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/gt_willy.png" alt="Ground Truth Willy">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.1-pro-preview | 🔴 97% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_willy_gemini_3_1_pro_preview.png" alt="gemini-3.1-pro-preview" width="64"> |
| gemini-3-pro-preview | 🔴 96% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_willy_gemini_3_pro_preview.png" alt="gemini-3-pro-preview" width="64"> |
| gemini-3-flash-preview | 🔴 84% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_willy_gemini_3_flash_preview.png" alt="gemini-3-flash-preview" width="64"> |
| gemini-2.5-pro | 🔴 82% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_willy_gemini_2_5_pro.png" alt="gemini-2.5-pro" width="64"> |
| gpt-5.4 | 🔴 68% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_willy_gpt_5_4.png" alt="gpt-5.4" width="64"> |
| gpt-4o | 🔴 62% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_willy_gpt_4o.png" alt="gpt-4o" width="64"> |
| claude-sonnet-4.5 | 🔴 59% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_willy_claude_sonnet_4_5.png" alt="claude-sonnet-4.5" width="64"> |
| claude-opus-4.6 | 🔴 59% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_willy_claude_opus_4_6.png" alt="claude-opus-4.6" width="64"> |
| gpt-5-mini | 🔴 54% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_willy_gpt_5_mini.png" alt="gpt-5-mini" width="64"> |
| claude-sonnet-4 | 🔴 52% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/a83306dc2b9a201b91c1f4c0a2859e9292862ae0/images/output_willy_claude_sonnet_4.png" alt="claude-sonnet-4" width="64"> |

## Overall Rankings

Averaged across all image sizes:

| Rank | Model | Avg Accuracy |
|------|-------|--------------|
| 1 | 🥇 gemini-3.1-pro-preview | 99.0% |
| 2 | 🥈 gemini-3-pro-preview | 98.7% |
| 3 | 🥉 gemini-3-flash-preview | 94.8% |
| 4 |  gemini-2.5-pro | 72.7% |
| 5 |  gpt-4o | 52.6% |
| 6 |  claude-opus-4.6 | 33.6% |
| 7 |  gpt-5.4 | 30.5% |
| 8 |  claude-sonnet-4 | 30.2% |
| 9 |  claude-sonnet-4.5 | 28.6% |
| 10 |  gpt-5-mini | 25.3% |

## Key Findings

1. **Zoom significantly improves accuracy** - 8x zoom provides +30-50% improvement for top models
2. **Gemini 3.x models excel** - Achieve near-perfect pixel extraction with proper settings
3. **Structured JSON output helps** - 2D array format with individual letters performs best
4. **Image size matters** - Smaller images (4x4) are easier to extract accurately
