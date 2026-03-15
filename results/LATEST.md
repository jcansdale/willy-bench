# Pixel Extraction Benchmark Results

Generated on: 2026-03-15T00:46:51.231055


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
| gpt-4o | 8x | 11/16 | 🔴 68.8% |
| claude-sonnet-4.5 | 8x | 5/16 | 🔴 31.2% |
| claude-sonnet-4 | 8x | 3/16 | 🔴 18.8% |
| claude-opus-4.6 | 8x | 3/16 | 🔴 18.8% |
| gpt-5.4 | 8x | 2/16 | 🔴 12.5% |
| gpt-5-mini | 8x | 1/16 | 🔴 6.2% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/gt_4x4.png" alt="Ground Truth 4x4">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.1-pro-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_4x4_gemini_3_1_pro_preview.png" alt="gemini-3.1-pro-preview" width="64"> |
| gemini-3-pro-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_4x4_gemini_3_pro_preview.png" alt="gemini-3-pro-preview" width="64"> |
| gemini-3-flash-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_4x4_gemini_3_flash_preview.png" alt="gemini-3-flash-preview" width="64"> |
| gemini-2.5-pro | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_4x4_gemini_2_5_pro.png" alt="gemini-2.5-pro" width="64"> |
| gpt-4o | 🔴 69% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_4x4_gpt_4o.png" alt="gpt-4o" width="64"> |
| claude-sonnet-4.5 | 🔴 31% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_4x4_claude_sonnet_4_5.png" alt="claude-sonnet-4.5" width="64"> |
| claude-sonnet-4 | 🔴 19% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_4x4_claude_sonnet_4.png" alt="claude-sonnet-4" width="64"> |
| claude-opus-4.6 | 🔴 19% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_4x4_claude_opus_4_6.png" alt="claude-opus-4.6" width="64"> |
| gpt-5.4 | 🔴 12% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_4x4_gpt_5_4.png" alt="gpt-5.4" width="64"> |
| gpt-5-mini | 🔴 6% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_4x4_gpt_5_mini.png" alt="gpt-5-mini" width="64"> |

### 8x8 (64 pixels)

| Model | Zoom | Correct | Accuracy |
|-------|------|---------|----------|
| gemini-3.1-pro-preview | 8x | 64/64 | ✅ 100.0% |
| gemini-3-pro-preview | 8x | 64/64 | ✅ 100.0% |
| gemini-3-flash-preview | 8x | 64/64 | ✅ 100.0% |
| gemini-2.5-pro | 8x | 16/64 | 🔴 25.0% |
| claude-opus-4.6 | 8x | 15/64 | 🔴 23.4% |
| gpt-4o | 8x | 14/64 | 🔴 21.9% |
| claude-sonnet-4 | 8x | 14/64 | 🔴 21.9% |
| claude-sonnet-4.5 | 8x | 10/64 | 🔴 15.6% |
| gpt-5.4 | 8x | 8/64 | 🔴 12.5% |
| gpt-5-mini | 8x | 6/64 | 🔴 9.4% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/gt_8x8.png" alt="Ground Truth 8x8">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.1-pro-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_8x8_gemini_3_1_pro_preview.png" alt="gemini-3.1-pro-preview" width="64"> |
| gemini-3-pro-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_8x8_gemini_3_pro_preview.png" alt="gemini-3-pro-preview" width="64"> |
| gemini-3-flash-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_8x8_gemini_3_flash_preview.png" alt="gemini-3-flash-preview" width="64"> |
| gemini-2.5-pro | 🔴 25% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_8x8_gemini_2_5_pro.png" alt="gemini-2.5-pro" width="64"> |
| claude-opus-4.6 | 🔴 23% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_8x8_claude_opus_4_6.png" alt="claude-opus-4.6" width="64"> |
| gpt-4o | 🔴 22% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_8x8_gpt_4o.png" alt="gpt-4o" width="64"> |
| claude-sonnet-4 | 🔴 22% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_8x8_claude_sonnet_4.png" alt="claude-sonnet-4" width="64"> |
| claude-sonnet-4.5 | 🔴 16% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_8x8_claude_sonnet_4_5.png" alt="claude-sonnet-4.5" width="64"> |
| gpt-5.4 | 🔴 12% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_8x8_gpt_5_4.png" alt="gpt-5.4" width="64"> |
| gpt-5-mini | 🔴 9% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_8x8_gpt_5_mini.png" alt="gpt-5-mini" width="64"> |

### Miner Willy Sprite (8x16, 128 pixels)

A classic 2-color retro game sprite (R=Red, W=White).

| Model | Zoom | Correct | Accuracy |
|-------|------|---------|----------|
| gemini-3-flash-preview | 8x | 128/128 | ✅ 100.0% |
| gemini-3-pro-preview | 8x | 125/128 | 🟡 97.7% |
| gemini-3.1-pro-preview | 8x | 124/128 | 🟡 96.9% |
| gemini-2.5-pro | 8x | 97/128 | 🔴 75.8% |
| gpt-5.4 | 8x | 82/128 | 🔴 64.1% |
| claude-opus-4.6 | 8x | 82/128 | 🔴 64.1% |
| gpt-4o | 8x | 80/128 | 🔴 62.5% |
| claude-sonnet-4.5 | 8x | 73/128 | 🔴 57.0% |
| claude-sonnet-4 | 8x | 68/128 | 🔴 53.1% |
| gpt-5-mini | 8x | 66/128 | 🔴 51.6% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/gt_willy.png" alt="Ground Truth Willy">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3-flash-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_willy_gemini_3_flash_preview.png" alt="gemini-3-flash-preview" width="64"> |
| gemini-3-pro-preview | 🔴 98% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_willy_gemini_3_pro_preview.png" alt="gemini-3-pro-preview" width="64"> |
| gemini-3.1-pro-preview | 🔴 97% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_willy_gemini_3_1_pro_preview.png" alt="gemini-3.1-pro-preview" width="64"> |
| gemini-2.5-pro | 🔴 76% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_willy_gemini_2_5_pro.png" alt="gemini-2.5-pro" width="64"> |
| gpt-5.4 | 🔴 64% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_willy_gpt_5_4.png" alt="gpt-5.4" width="64"> |
| claude-opus-4.6 | 🔴 64% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_willy_claude_opus_4_6.png" alt="claude-opus-4.6" width="64"> |
| gpt-4o | 🔴 62% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_willy_gpt_4o.png" alt="gpt-4o" width="64"> |
| claude-sonnet-4.5 | 🔴 57% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_willy_claude_sonnet_4_5.png" alt="claude-sonnet-4.5" width="64"> |
| claude-sonnet-4 | 🔴 53% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_willy_claude_sonnet_4.png" alt="claude-sonnet-4" width="64"> |
| gpt-5-mini | 🔴 52% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/60cc83f13c1387437ef16ae5baa42e15ae5f6ffc/images/output_willy_gpt_5_mini.png" alt="gpt-5-mini" width="64"> |

## Overall Rankings

Averaged across all image sizes:

| Rank | Model | Avg Accuracy |
|------|-------|--------------|
| 1 | 🥇 gemini-3-flash-preview | 100.0% |
| 2 | 🥈 gemini-3-pro-preview | 99.2% |
| 3 | 🥉 gemini-3.1-pro-preview | 99.0% |
| 4 |  gemini-2.5-pro | 66.9% |
| 5 |  gpt-4o | 51.0% |
| 6 |  claude-opus-4.6 | 35.4% |
| 7 |  claude-sonnet-4.5 | 34.6% |
| 8 |  claude-sonnet-4 | 31.2% |
| 9 |  gpt-5.4 | 29.7% |
| 10 |  gpt-5-mini | 22.4% |

## Key Findings

1. **Zoom significantly improves accuracy** - 8x zoom provides +30-50% improvement for top models
2. **Gemini 3.x models excel** - Achieve near-perfect pixel extraction with proper settings
3. **Structured JSON output helps** - 2D array format with individual letters performs best
4. **Image size matters** - Smaller images (4x4) are easier to extract accurately
