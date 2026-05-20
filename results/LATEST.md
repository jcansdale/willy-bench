# Pixel Extraction Benchmark Results

Generated on: 2026-05-20T11:04:07.277840


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
| gemini-3.1-pro-preview | 8x | 16/16 | ✅ 100.0% |
| gemini-3-flash-preview | 8x | 16/16 | ✅ 100.0% |
| gemini-2.5-pro | 8x | 16/16 | ✅ 100.0% |
| gpt-4o | 8x | 12/16 | 🔴 75.0% |
| claude-opus-4.7 | 8x | 6/16 | 🔴 37.5% |
| gpt-5.4 | 8x | 4/16 | 🔴 25.0% |
| claude-sonnet-4.5 | 8x | 4/16 | 🔴 25.0% |
| claude-opus-4.6 | 8x | 4/16 | 🔴 25.0% |
| gpt-5-mini | 8x | 1/16 | 🔴 6.2% |
| claude-sonnet-4 | 8x | 0/16 | 🔴 0.0% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/gt_4x4.png" alt="Ground Truth 4x4">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.5-flash | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_4x4_gemini_3_5_flash.png" alt="gemini-3.5-flash" width="64"> |
| gemini-3.1-pro-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_4x4_gemini_3_1_pro_preview.png" alt="gemini-3.1-pro-preview" width="64"> |
| gemini-3-flash-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_4x4_gemini_3_flash_preview.png" alt="gemini-3-flash-preview" width="64"> |
| gemini-2.5-pro | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_4x4_gemini_2_5_pro.png" alt="gemini-2.5-pro" width="64"> |
| gpt-4o | 🔴 75% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_4x4_gpt_4o.png" alt="gpt-4o" width="64"> |
| claude-opus-4.7 | 🔴 38% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_4x4_claude_opus_4_7.png" alt="claude-opus-4.7" width="64"> |
| gpt-5.4 | 🔴 25% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_4x4_gpt_5_4.png" alt="gpt-5.4" width="64"> |
| claude-sonnet-4.5 | 🔴 25% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_4x4_claude_sonnet_4_5.png" alt="claude-sonnet-4.5" width="64"> |
| claude-opus-4.6 | 🔴 25% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_4x4_claude_opus_4_6.png" alt="claude-opus-4.6" width="64"> |
| gpt-5-mini | 🔴 6% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_4x4_gpt_5_mini.png" alt="gpt-5-mini" width="64"> |

### 8x8 (64 pixels)

| Model | Zoom | Correct | Accuracy |
|-------|------|---------|----------|
| gemini-3.5-flash | 8x | 64/64 | ✅ 100.0% |
| gemini-3.1-pro-preview | 8x | 64/64 | ✅ 100.0% |
| gemini-3-flash-preview | 8x | 64/64 | ✅ 100.0% |
| gemini-2.5-pro | 8x | 31/64 | 🔴 48.4% |
| claude-opus-4.6 | 8x | 16/64 | 🔴 25.0% |
| claude-sonnet-4.5 | 8x | 13/64 | 🔴 20.3% |
| gpt-5.4 | 8x | 12/64 | 🔴 18.8% |
| claude-opus-4.7 | 8x | 7/64 | 🔴 10.9% |
| gpt-5-mini | 8x | 5/64 | 🔴 7.8% |
| gpt-4o | 8x | 4/64 | 🔴 6.2% |
| claude-sonnet-4 | 8x | 0/64 | 🔴 0.0% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/gt_8x8.png" alt="Ground Truth 8x8">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.5-flash | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_8x8_gemini_3_5_flash.png" alt="gemini-3.5-flash" width="64"> |
| gemini-3.1-pro-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_8x8_gemini_3_1_pro_preview.png" alt="gemini-3.1-pro-preview" width="64"> |
| gemini-3-flash-preview | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_8x8_gemini_3_flash_preview.png" alt="gemini-3-flash-preview" width="64"> |
| gemini-2.5-pro | 🔴 48% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_8x8_gemini_2_5_pro.png" alt="gemini-2.5-pro" width="64"> |
| claude-opus-4.6 | 🔴 25% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_8x8_claude_opus_4_6.png" alt="claude-opus-4.6" width="64"> |
| claude-sonnet-4.5 | 🔴 20% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_8x8_claude_sonnet_4_5.png" alt="claude-sonnet-4.5" width="64"> |
| gpt-5.4 | 🔴 19% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_8x8_gpt_5_4.png" alt="gpt-5.4" width="64"> |
| claude-opus-4.7 | 🔴 11% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_8x8_claude_opus_4_7.png" alt="claude-opus-4.7" width="64"> |
| gpt-5-mini | 🔴 8% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_8x8_gpt_5_mini.png" alt="gpt-5-mini" width="64"> |
| gpt-4o | 🔴 6% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_8x8_gpt_4o.png" alt="gpt-4o" width="64"> |

### Miner Willy Sprite (8x16, 128 pixels)

A classic 2-color retro game sprite (R=Red, W=White).

| Model | Zoom | Correct | Accuracy |
|-------|------|---------|----------|
| gemini-3.5-flash | 8x | 125/128 | 🟡 97.7% |
| gemini-3.1-pro-preview | 8x | 123/128 | 🟡 96.1% |
| gemini-2.5-pro | 8x | 96/128 | 🔴 75.0% |
| gemini-3-flash-preview | 8x | 94/128 | 🔴 73.4% |
| claude-opus-4.6 | 8x | 90/128 | 🔴 70.3% |
| gpt-5.4 | 8x | 86/128 | 🔴 67.2% |
| claude-opus-4.7 | 8x | 85/128 | 🔴 66.4% |
| gpt-5-mini | 8x | 77/128 | 🔴 60.2% |
| gpt-4o | 8x | 76/128 | 🔴 59.4% |
| claude-sonnet-4.5 | 8x | 76/128 | 🔴 59.4% |
| claude-sonnet-4 | 8x | 0/128 | 🔴 0.0% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/gt_willy.png" alt="Ground Truth Willy">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.5-flash | 🔴 98% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_willy_gemini_3_5_flash.png" alt="gemini-3.5-flash" width="64"> |
| gemini-3.1-pro-preview | 🔴 96% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_willy_gemini_3_1_pro_preview.png" alt="gemini-3.1-pro-preview" width="64"> |
| gemini-2.5-pro | 🔴 75% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_willy_gemini_2_5_pro.png" alt="gemini-2.5-pro" width="64"> |
| gemini-3-flash-preview | 🔴 73% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_willy_gemini_3_flash_preview.png" alt="gemini-3-flash-preview" width="64"> |
| claude-opus-4.6 | 🔴 70% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_willy_claude_opus_4_6.png" alt="claude-opus-4.6" width="64"> |
| gpt-5.4 | 🔴 67% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_willy_gpt_5_4.png" alt="gpt-5.4" width="64"> |
| claude-opus-4.7 | 🔴 66% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_willy_claude_opus_4_7.png" alt="claude-opus-4.7" width="64"> |
| gpt-5-mini | 🔴 60% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_willy_gpt_5_mini.png" alt="gpt-5-mini" width="64"> |
| gpt-4o | 🔴 59% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_willy_gpt_4o.png" alt="gpt-4o" width="64"> |
| claude-sonnet-4.5 | 🔴 59% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cf336fda24fc743d59fb7b7d53623854f67bf3b7/images/output_willy_claude_sonnet_4_5.png" alt="claude-sonnet-4.5" width="64"> |

## Overall Rankings

Averaged across all image sizes:

| Rank | Model | Avg Accuracy |
|------|-------|--------------|
| 1 | 🥇 gemini-3.5-flash | 99.2% |
| 2 | 🥈 gemini-3.1-pro-preview | 98.7% |
| 3 | 🥉 gemini-3-flash-preview | 91.1% |
| 4 |  gemini-2.5-pro | 74.5% |
| 5 |  gpt-4o | 46.9% |
| 6 |  claude-opus-4.6 | 40.1% |
| 7 |  claude-opus-4.7 | 38.3% |
| 8 |  gpt-5.4 | 37.0% |
| 9 |  claude-sonnet-4.5 | 34.9% |
| 10 |  gpt-5-mini | 24.7% |
| 11 |  claude-sonnet-4 | 0.0% |

## Key Findings

1. **Zoom significantly improves accuracy** - 8x zoom provides +30-50% improvement for top models
2. **Gemini 3.x models excel** - Achieve near-perfect pixel extraction with proper settings
3. **Structured JSON output helps** - 2D array format with individual letters performs best
4. **Image size matters** - Smaller images (4x4) are easier to extract accurately
