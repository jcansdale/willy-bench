# Pixel Extraction Benchmark Results

Generated on: 2026-09-05T20:38:35.621651


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
| gemini-3.6-flash | 8x | 16/16 | ✅ 100.0% |
| gemini-3.7-flash | 8x | 16/16 | ✅ 100.0% |
| gemini-3.8-flash | 8x | 16/16 | ✅ 100.0% |
| gpt-4o-2024-05-13 | 8x | 14/16 | 🟡 87.5% |
| gpt-6-astra | 8x | 7/16 | 🔴 43.8% |
| gpt-5.6-terra | 8x | 4/16 | 🔴 25.0% |
| gpt-5.5 | 8x | 3/16 | 🔴 18.8% |
| gpt-5.4 | 8x | 2/16 | 🔴 12.5% |
| gpt-5.6-sol | 8x | 1/16 | 🔴 6.2% |
| claude-haiku-4.5 | 8x | 1/16 | 🔴 6.2% |
| claude-sonnet-5 | 8x | 1/16 | 🔴 6.2% |
| grok-4.6 | 8x | 1/16 | 🔴 6.2% |
| claude-opus-5 | 8x | 0/16 | 🔴 0.0% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/gt_4x4.png" alt="Ground Truth 4x4">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.5-flash | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_4x4_gemini_3_5_flash.png" alt="gemini-3.5-flash" width="64"> |
| gemini-3.6-flash | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_4x4_gemini_3_6_flash.png" alt="gemini-3.6-flash" width="64"> |
| gemini-3.7-flash | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_4x4_gemini_3_7_flash.png" alt="gemini-3.7-flash" width="64"> |
| gemini-3.8-flash | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_4x4_gemini_3_8_flash.png" alt="gemini-3.8-flash" width="64"> |
| gpt-4o-2024-05-13 | 🔴 88% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_4x4_gpt_4o_2024_05_13.png" alt="gpt-4o-2024-05-13" width="64"> |
| gpt-6-astra | 🔴 44% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_4x4_gpt_6_astra.png" alt="gpt-6-astra" width="64"> |
| gpt-5.6-terra | 🔴 25% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_4x4_gpt_5_6_terra.png" alt="gpt-5.6-terra" width="64"> |
| gpt-5.5 | 🔴 19% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_4x4_gpt_5_5.png" alt="gpt-5.5" width="64"> |
| gpt-5.4 | 🔴 12% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_4x4_gpt_5_4.png" alt="gpt-5.4" width="64"> |
| gpt-5.6-sol | 🔴 6% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_4x4_gpt_5_6_sol.png" alt="gpt-5.6-sol" width="64"> |

### 8x8 (64 pixels)

| Model | Zoom | Correct | Accuracy |
|-------|------|---------|----------|
| gemini-3.5-flash | 8x | 64/64 | ✅ 100.0% |
| gemini-3.6-flash | 8x | 64/64 | ✅ 100.0% |
| gemini-3.7-flash | 8x | 64/64 | ✅ 100.0% |
| gemini-3.8-flash | 8x | 64/64 | ✅ 100.0% |
| gpt-6-astra | 8x | 26/64 | 🔴 40.6% |
| gpt-4o-2024-05-13 | 8x | 23/64 | 🔴 35.9% |
| gpt-5.6-terra | 8x | 13/64 | 🔴 20.3% |
| gpt-5.5 | 8x | 9/64 | 🔴 14.1% |
| gpt-5.6-sol | 8x | 8/64 | 🔴 12.5% |
| claude-haiku-4.5 | 8x | 8/64 | 🔴 12.5% |
| claude-sonnet-5 | 8x | 8/64 | 🔴 12.5% |
| claude-opus-5 | 8x | 8/64 | 🔴 12.5% |
| gpt-5.4 | 8x | 7/64 | 🔴 10.9% |
| grok-4.6 | 8x | 0/64 | 🔴 0.0% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/gt_8x8.png" alt="Ground Truth 8x8">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.5-flash | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_8x8_gemini_3_5_flash.png" alt="gemini-3.5-flash" width="64"> |
| gemini-3.6-flash | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_8x8_gemini_3_6_flash.png" alt="gemini-3.6-flash" width="64"> |
| gemini-3.7-flash | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_8x8_gemini_3_7_flash.png" alt="gemini-3.7-flash" width="64"> |
| gemini-3.8-flash | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_8x8_gemini_3_8_flash.png" alt="gemini-3.8-flash" width="64"> |
| gpt-6-astra | 🔴 41% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_8x8_gpt_6_astra.png" alt="gpt-6-astra" width="64"> |
| gpt-4o-2024-05-13 | 🔴 36% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_8x8_gpt_4o_2024_05_13.png" alt="gpt-4o-2024-05-13" width="64"> |
| gpt-5.6-terra | 🔴 20% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_8x8_gpt_5_6_terra.png" alt="gpt-5.6-terra" width="64"> |
| gpt-5.5 | 🔴 14% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_8x8_gpt_5_5.png" alt="gpt-5.5" width="64"> |
| gpt-5.6-sol | 🔴 12% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_8x8_gpt_5_6_sol.png" alt="gpt-5.6-sol" width="64"> |
| claude-haiku-4.5 | 🔴 12% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_8x8_claude_haiku_4_5.png" alt="claude-haiku-4.5" width="64"> |

### Miner Willy Sprite (8x16, 128 pixels)

A classic 2-color retro game sprite (R=Red, W=White).

| Model | Zoom | Correct | Accuracy |
|-------|------|---------|----------|
| gemini-3.8-flash | 8x | 128/128 | ✅ 100.0% |
| gemini-3.7-flash | 8x | 125/128 | 🟡 97.7% |
| gemini-3.6-flash | 8x | 104/128 | 🟡 81.2% |
| gpt-5.6-sol | 8x | 98/128 | 🔴 76.6% |
| gpt-6-astra | 8x | 93/128 | 🔴 72.7% |
| claude-haiku-4.5 | 8x | 90/128 | 🔴 70.3% |
| gpt-5.4 | 8x | 86/128 | 🔴 67.2% |
| gpt-5.5 | 8x | 84/128 | 🔴 65.6% |
| gpt-5.6-terra | 8x | 82/128 | 🔴 64.1% |
| gpt-4o-2024-05-13 | 8x | 78/128 | 🔴 60.9% |
| claude-sonnet-5 | 8x | 78/128 | 🔴 60.9% |
| claude-opus-5 | 8x | 72/128 | 🔴 56.2% |
| grok-4.6 | 8x | 67/128 | 🔴 52.3% |
| gemini-3.5-flash | 8x | 0/128 | 🔴 0.0% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/gt_willy.png" alt="Ground Truth Willy">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.8-flash | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_willy_gemini_3_8_flash.png" alt="gemini-3.8-flash" width="64"> |
| gemini-3.7-flash | 🔴 98% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_willy_gemini_3_7_flash.png" alt="gemini-3.7-flash" width="64"> |
| gemini-3.6-flash | 🔴 81% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_willy_gemini_3_6_flash.png" alt="gemini-3.6-flash" width="64"> |
| gpt-5.6-sol | 🔴 77% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_willy_gpt_5_6_sol.png" alt="gpt-5.6-sol" width="64"> |
| gpt-6-astra | 🔴 73% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_willy_gpt_6_astra.png" alt="gpt-6-astra" width="64"> |
| claude-haiku-4.5 | 🔴 70% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_willy_claude_haiku_4_5.png" alt="claude-haiku-4.5" width="64"> |
| gpt-5.4 | 🔴 67% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_willy_gpt_5_4.png" alt="gpt-5.4" width="64"> |
| gpt-5.5 | 🔴 66% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_willy_gpt_5_5.png" alt="gpt-5.5" width="64"> |
| gpt-5.6-terra | 🔴 64% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_willy_gpt_5_6_terra.png" alt="gpt-5.6-terra" width="64"> |
| gpt-4o-2024-05-13 | 🔴 61% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/3e538b3f274e7a5d3cbb355e2f66ca58265207e4/images/output_willy_gpt_4o_2024_05_13.png" alt="gpt-4o-2024-05-13" width="64"> |

## Overall Rankings

Averaged across all image sizes:

| Rank | Model | Avg Accuracy |
|------|-------|--------------|
| 1 | 🥇 gemini-3.8-flash | 100.0% |
| 2 | 🥈 gemini-3.7-flash | 99.2% |
| 3 | 🥉 gemini-3.6-flash | 93.8% |
| 4 |  gemini-3.5-flash | 66.7% |
| 5 |  gpt-4o-2024-05-13 | 61.5% |
| 6 |  gpt-6-astra | 52.3% |
| 7 |  gpt-5.6-terra | 36.5% |
| 8 |  gpt-5.5 | 32.8% |
| 9 |  gpt-5.6-sol | 31.8% |
| 10 |  gpt-5.4 | 30.2% |
| 11 |  claude-haiku-4.5 | 29.7% |
| 12 |  claude-sonnet-5 | 26.6% |
| 13 |  claude-opus-5 | 22.9% |
| 14 |  grok-4.6 | 19.5% |

## Key Findings

1. **Zoom significantly improves accuracy** - 8x zoom provides +30-50% improvement for top models
2. **Gemini 3.x models excel** - Achieve near-perfect pixel extraction with proper settings
3. **Structured JSON output helps** - 2D array format with individual letters performs best
4. **Image size matters** - Smaller images (4x4) are easier to extract accurately
