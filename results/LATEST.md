# Pixel Extraction Benchmark Results

Generated on: 2026-09-05T20:11:35.357606


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
| gemini-3.8-flash | 8x | 16/16 | ✅ 100.0% |
| gpt-4o-2024-05-13 | 8x | 14/16 | 🟡 87.5% |
| gpt-6-astra | 8x | 7/16 | 🔴 43.8% |
| claude-opus-5 | 8x | 6/16 | 🔴 37.5% |
| grok-4.6 | 8x | 4/16 | 🔴 25.0% |
| gpt-5.4 | 8x | 3/16 | 🔴 18.8% |
| gpt-5.6-terra | 8x | 3/16 | 🔴 18.8% |
| gpt-5.6-sol | 8x | 3/16 | 🔴 18.8% |
| claude-sonnet-5 | 8x | 2/16 | 🔴 12.5% |
| gpt-5.5 | 8x | 1/16 | 🔴 6.2% |
| claude-haiku-4.5 | 8x | 1/16 | 🔴 6.2% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/gt_4x4.png" alt="Ground Truth 4x4">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.5-flash | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_4x4_gemini_3_5_flash.png" alt="gemini-3.5-flash" width="64"> |
| gemini-3.8-flash | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_4x4_gemini_3_8_flash.png" alt="gemini-3.8-flash" width="64"> |
| gpt-4o-2024-05-13 | 🔴 88% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_4x4_gpt_4o_2024_05_13.png" alt="gpt-4o-2024-05-13" width="64"> |
| gpt-6-astra | 🔴 44% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_4x4_gpt_6_astra.png" alt="gpt-6-astra" width="64"> |
| claude-opus-5 | 🔴 38% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_4x4_claude_opus_5.png" alt="claude-opus-5" width="64"> |
| grok-4.6 | 🔴 25% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_4x4_grok_4_6.png" alt="grok-4.6" width="64"> |
| gpt-5.4 | 🔴 19% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_4x4_gpt_5_4.png" alt="gpt-5.4" width="64"> |
| gpt-5.6-terra | 🔴 19% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_4x4_gpt_5_6_terra.png" alt="gpt-5.6-terra" width="64"> |
| gpt-5.6-sol | 🔴 19% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_4x4_gpt_5_6_sol.png" alt="gpt-5.6-sol" width="64"> |
| claude-sonnet-5 | 🔴 12% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_4x4_claude_sonnet_5.png" alt="claude-sonnet-5" width="64"> |

### 8x8 (64 pixels)

| Model | Zoom | Correct | Accuracy |
|-------|------|---------|----------|
| gemini-3.5-flash | 8x | 64/64 | ✅ 100.0% |
| gemini-3.8-flash | 8x | 64/64 | ✅ 100.0% |
| gpt-6-astra | 8x | 20/64 | 🔴 31.2% |
| gpt-4o-2024-05-13 | 8x | 18/64 | 🔴 28.1% |
| gpt-5.6-terra | 8x | 14/64 | 🔴 21.9% |
| gpt-5.4 | 8x | 11/64 | 🔴 17.2% |
| claude-opus-5 | 8x | 8/64 | 🔴 12.5% |
| claude-haiku-4.5 | 8x | 7/64 | 🔴 10.9% |
| claude-sonnet-5 | 8x | 7/64 | 🔴 10.9% |
| gpt-5.5 | 8x | 6/64 | 🔴 9.4% |
| gpt-5.6-sol | 8x | 6/64 | 🔴 9.4% |
| grok-4.6 | 8x | 0/64 | 🔴 0.0% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/gt_8x8.png" alt="Ground Truth 8x8">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.5-flash | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_8x8_gemini_3_5_flash.png" alt="gemini-3.5-flash" width="64"> |
| gemini-3.8-flash | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_8x8_gemini_3_8_flash.png" alt="gemini-3.8-flash" width="64"> |
| gpt-6-astra | 🔴 31% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_8x8_gpt_6_astra.png" alt="gpt-6-astra" width="64"> |
| gpt-4o-2024-05-13 | 🔴 28% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_8x8_gpt_4o_2024_05_13.png" alt="gpt-4o-2024-05-13" width="64"> |
| gpt-5.6-terra | 🔴 22% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_8x8_gpt_5_6_terra.png" alt="gpt-5.6-terra" width="64"> |
| gpt-5.4 | 🔴 17% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_8x8_gpt_5_4.png" alt="gpt-5.4" width="64"> |
| claude-opus-5 | 🔴 12% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_8x8_claude_opus_5.png" alt="claude-opus-5" width="64"> |
| claude-haiku-4.5 | 🔴 11% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_8x8_claude_haiku_4_5.png" alt="claude-haiku-4.5" width="64"> |
| claude-sonnet-5 | 🔴 11% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_8x8_claude_sonnet_5.png" alt="claude-sonnet-5" width="64"> |
| gpt-5.5 | 🔴 9% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_8x8_gpt_5_5.png" alt="gpt-5.5" width="64"> |

### Miner Willy Sprite (8x16, 128 pixels)

A classic 2-color retro game sprite (R=Red, W=White).

| Model | Zoom | Correct | Accuracy |
|-------|------|---------|----------|
| gemini-3.8-flash | 8x | 128/128 | ✅ 100.0% |
| gpt-5.6-sol | 8x | 100/128 | 🔴 78.1% |
| gpt-6-astra | 8x | 98/128 | 🔴 76.6% |
| gpt-5.6-terra | 8x | 90/128 | 🔴 70.3% |
| claude-haiku-4.5 | 8x | 90/128 | 🔴 70.3% |
| grok-4.6 | 8x | 85/128 | 🔴 66.4% |
| gpt-4o-2024-05-13 | 8x | 84/128 | 🔴 65.6% |
| claude-opus-5 | 8x | 80/128 | 🔴 62.5% |
| claude-sonnet-5 | 8x | 77/128 | 🔴 60.2% |
| gpt-5.4 | 8x | 68/128 | 🔴 53.1% |
| gpt-5.5 | 8x | 67/128 | 🔴 52.3% |
| gemini-3.5-flash | 8x | 0/128 | 🔴 0.0% |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/gt_willy.png" alt="Ground Truth Willy">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.8-flash | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_willy_gemini_3_8_flash.png" alt="gemini-3.8-flash" width="64"> |
| gpt-5.6-sol | 🔴 78% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_willy_gpt_5_6_sol.png" alt="gpt-5.6-sol" width="64"> |
| gpt-6-astra | 🔴 77% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_willy_gpt_6_astra.png" alt="gpt-6-astra" width="64"> |
| gpt-5.6-terra | 🔴 70% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_willy_gpt_5_6_terra.png" alt="gpt-5.6-terra" width="64"> |
| claude-haiku-4.5 | 🔴 70% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_willy_claude_haiku_4_5.png" alt="claude-haiku-4.5" width="64"> |
| grok-4.6 | 🔴 66% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_willy_grok_4_6.png" alt="grok-4.6" width="64"> |
| gpt-4o-2024-05-13 | 🔴 66% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_willy_gpt_4o_2024_05_13.png" alt="gpt-4o-2024-05-13" width="64"> |
| claude-opus-5 | 🔴 62% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_willy_claude_opus_5.png" alt="claude-opus-5" width="64"> |
| claude-sonnet-5 | 🔴 60% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_willy_claude_sonnet_5.png" alt="claude-sonnet-5" width="64"> |
| gpt-5.4 | 🔴 53% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/636300cd40c53cb960f8554c5bc94a49750b8ae0/images/output_willy_gpt_5_4.png" alt="gpt-5.4" width="64"> |

## Overall Rankings

Averaged across all image sizes:

| Rank | Model | Avg Accuracy |
|------|-------|--------------|
| 1 | 🥇 gemini-3.8-flash | 100.0% |
| 2 | 🥈 gemini-3.5-flash | 66.7% |
| 3 | 🥉 gpt-4o-2024-05-13 | 60.4% |
| 4 |  gpt-6-astra | 50.5% |
| 5 |  claude-opus-5 | 37.5% |
| 6 |  gpt-5.6-terra | 37.0% |
| 7 |  gpt-5.6-sol | 35.4% |
| 8 |  grok-4.6 | 30.5% |
| 9 |  gpt-5.4 | 29.7% |
| 10 |  claude-haiku-4.5 | 29.2% |
| 11 |  claude-sonnet-5 | 27.9% |
| 12 |  gpt-5.5 | 22.7% |

## Key Findings

1. **Zoom significantly improves accuracy** - 8x zoom provides +30-50% improvement for top models
2. **Gemini 3.x models excel** - Achieve near-perfect pixel extraction with proper settings
3. **Structured JSON output helps** - 2D array format with individual letters performs best
4. **Image size matters** - Smaller images (4x4) are easier to extract accurately
