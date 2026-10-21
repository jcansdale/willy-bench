# Pixel Extraction Benchmark Results

Generated on: 2026-10-21T11:16:19.542383


## Summary

This benchmark tests the ability of vision models to extract pixel-level color data from small images.

### Methodology
- Random colored images generated with 8 distinct colors (R, G, B, Y, M, C, O, P)
- Each logical pixel is rendered as a contiguous 32x32 pixel cell using nearest-neighbor scaling
- Reasoning effort is low where the model supports it; otherwise the provider default is used
- Models asked to output a JSON 2D array of color letters
- Accuracy measured as percentage of correctly identified pixels
- Cohen's kappa adjusts accuracy for agreement expected by chance: 1 is perfect, 0 is chance-level, and negative values are worse than chance

## Results by Image Size

### 4x4 (16 pixels)

| Model | Cell Size | Reasoning | Correct | Accuracy | Kappa |
|-------|-----------|-----------|---------|----------|-------|
| gemini-3.8-flash | 32x | low | 16/16 | ✅ 100.0% | 1.000 |
| gemini-4-argon | 32x | low | 16/16 | ✅ 100.0% | 1.000 |
| claude-haiku-4.5 | 32x | provider-default | 16/16 | ✅ 100.0% | 1.000 |
| claude-sonnet-5 | 32x | low | 16/16 | ✅ 100.0% | 1.000 |
| claude-sonnet-5.5 | 32x | low | 16/16 | ✅ 100.0% | 1.000 |
| claude-opus-5 | 32x | low | 16/16 | ✅ 100.0% | 1.000 |
| claude-opus-5.5 | 32x | low | 16/16 | ✅ 100.0% | 1.000 |
| gpt-4o-2024-05-13 | 32x | provider-default | 15/16 | 🟡 93.8% | 0.918 |
| grok-4.7 | 32x | low | 7/16 | 🔴 43.8% | 0.308 |
| gpt-5.6-terra | 32x | low | 6/16 | 🔴 37.5% | 0.231 |
| gpt-6-astra | 32x | low | 5/16 | 🔴 31.2% | 0.154 |
| gpt-6.1-sol | 32x | low | 5/16 | 🔴 31.2% | 0.120 |
| gpt-6-sol | 32x | low | 3/16 | 🔴 18.8% | 0.071 |
| grok-4.6 | 32x | low | 3/16 | 🔴 18.8% | 0.019 |
| gpt-5.6-sol | 32x | low | 5/16 | 🔴 31.2% | 0.000 |
| gpt-6-luna | 32x | low | 5/16 | 🔴 31.2% | 0.000 |
| claude-haiku-5.5 | 32x | low | 0/16 | 🔴 0.0% | N/A |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/gt_4x4.png" alt="Ground Truth 4x4">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.8-flash | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_4x4_gemini_3_8_flash.png" alt="gemini-3.8-flash" width="64"> |
| gemini-4-argon | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_4x4_gemini_4_argon.png" alt="gemini-4-argon" width="64"> |
| claude-haiku-4.5 | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_4x4_claude_haiku_4_5.png" alt="claude-haiku-4.5" width="64"> |
| claude-sonnet-5 | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_4x4_claude_sonnet_5.png" alt="claude-sonnet-5" width="64"> |
| claude-sonnet-5.5 | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_4x4_claude_sonnet_5_5.png" alt="claude-sonnet-5.5" width="64"> |
| claude-opus-5 | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_4x4_claude_opus_5.png" alt="claude-opus-5" width="64"> |
| claude-opus-5.5 | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_4x4_claude_opus_5_5.png" alt="claude-opus-5.5" width="64"> |
| gpt-4o-2024-05-13 | 🔴 94% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_4x4_gpt_4o_2024_05_13.png" alt="gpt-4o-2024-05-13" width="64"> |
| grok-4.7 | 🔴 44% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_4x4_grok_4_7.png" alt="grok-4.7" width="64"> |
| gpt-5.6-terra | 🔴 38% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_4x4_gpt_5_6_terra.png" alt="gpt-5.6-terra" width="64"> |

#### Reasoning Summaries

> These model-provided summaries may not faithfully represent the model's internal computation.

<details>
<summary>gemini-3.8-flash (16/16, 100.0%)</summary>

<p>**My Internal Monologue on Image Data Analysis**</p>

<p>Alright, let&#x27;s break down this image data. The first thing I&#x27;m processing is its fundamental dimensionality – it&#x27;s a compact 4x4 pixel grid. This is a very manageable size, allowing for a direct, pixel-by-pixel examination.</p>

<p>Now, I&#x27;m moving through the rows, systematically taking in the color information for each pixel.</p>

<p>In Row 0, I see:<br>
*   At coordinate (0,0), the color is Green [G].<br>
*   Moving right to (0,1), it&#x27;s Red [R].<br>
*   Then, at (0,2), I register Magenta [M].<br>
*   And finally, at (0,3), it&#x27;s Yellow [Y].</p>

<p>Shifting my focus to Row 1:<br>
*   Starting at (1,0), the color is Yellow [Y].<br>
*   Next, at (1,1), I note Blue [B].<br>
*   Moving to (1,2), it&#x27;s Green [G].<br>
*   And the last pixel in this row, at (1,3), is also Green [G].</p>

<p>Proceeding to Row 2:<br>
*   At (2,0), the color is Orange [O].<br>
*   Then, at (2,1), I see Red [R].<br>
*   Consecutively, at (2,2), it&#x27;s also Red [R].<br>
*   And concluding Row 2 at (2,3), it&#x27;s Green [G].</p>

<p>Finally, I&#x27;m examining Row 3:<br>
*   At (3,0), the color is Yellow [Y].<br>
*   Moving along, at (3,1), it&#x27;s also Yellow [Y].<br>
*   Then, at (3,2), I encounter Red [R].<br>
*   And the very last pixel of the image, at (3,3), is Yellow [Y].</p>

<p>So, in essence, my thought process involves this granular, sequential intake of color information for each pixel, structured by rows and their corresponding X-coordinates. It&#x27;s a direct, unambiguous data parse.</p>

<p></p>

</details>

<details>
<summary>claude-opus-5 (16/16, 100.0%)</summary>

<p>I&#x27;m reading off the pixel grid row by row, noting each cell&#x27;s color to map out the 4x4 image.</p>

<p></p>

</details>

<details>
<summary>grok-4.7 (7/16, 43.8%)</summary>

<p>I need to generate a 4x4 JSON array of single-letter color codes.</p>

<p>I&#x27;m analyzing the image to identify the colors in each of the four rows.</p>

<p>I&#x27;ve mapped every pixel in the 4x4 grid. The first two rows are yellow, magenta, blue, green. The last two rows are orange, red, red, lime green.</p>

</details>

<details>
<summary>gpt-5.6-terra (6/16, 37.5%)</summary>

<p>**Identifying color quadrants**</p>

<p>I’m focusing on defining the quadrants for an image labeled as 128. The top left will be green, the top right will be blue, the bottom left will be yellow, and the bottom right will be red. It seems like I need to put this information into JSON format. Let’s ensure I get this structured properly for whoever needs to use this. This is a clear task, so I’ll get right on it!</p>

</details>

<details>
<summary>gpt-6-astra (5/16, 31.2%)</summary>

<p>**Inspecting quadrants in image**</p>

<p>I need to inspect the quadrants of an image. The top-left section appears to be a green area at coordinates x0-31 and y0-63, which is part of an image that is likely 128 in size. I want to identify the cell colors in row 1 as green, red, magenta, and yellow, and do the same for row 2. For the visual breakdown: green is from 0-31, red from 32-63, magenta from 64-95, and yellow from 96-127 in the top part, while the bottom contains orange and blue sections too!</p>

</details>

<details>
<summary>gpt-6.1-sol (5/16, 31.2%)</summary>

<p>**Inspecting image quadrants**</p>

<p>I need to inspect the quadrants of image 128. So, for the top left red section, is it x0-31? It seems like the top shows red from 0-31 in the first row. I should mentally visualize that the red left quarter is there, with magenta occupying the middle half and green in the right quarter. For the second row, the red section on the left is probably the same. I should specify the outputs: R M M G and then Y Y G G.</p>

</details>

<details>
<summary>gpt-6-sol (3/16, 18.8%)</summary>

<p>**Inspecting Image Blocks**</p>

<p>I&#x27;m checking an image that&#x27;s 128 squares in size and divided into 4x4 blocks. In the top-left block, I see colors: red (R), green (G), blue (B), and yellow (Y). The second row has magenta (M), cyan (C), orange (O), and purple (P). The third row shows blue (B), yellow (Y), red (R), and green (G), while the fourth has orange (O), purple (P), magenta (M), and cyan (C). I want to ensure I accurately inspect these colors and their positioning!</p>

</details>

<details>
<summary>grok-4.6 (3/16, 18.8%)</summary>

<p>I need to produce a 4x4 JSON 2D array using the eight specified single-letter color codes.</p>

<p>The image appears to be a 2x2 grid rather than 4x4. I need to determine how to map those four colors into the required 4x4 array.</p>

<p>Perhaps each of the four visible quadrants is a 2x2 pixel block. That would still only yield four colors, not eight.</p>

<p>The image contains only four colors: magenta, yellow, orange, and green. Each color occupies a 2x2 block in the 4x4 grid. The resulting JSON array is:</p>

<p>[&quot;M&quot;,&quot;M&quot;,&quot;Y&quot;,&quot;Y&quot;],<br>
[&quot;M&quot;,&quot;M&quot;,&quot;Y&quot;,&quot;Y&quot;],<br>
[&quot;O&quot;,&quot;O&quot;,&quot;G&quot;,&quot;G&quot;],<br>
[&quot;O&quot;,&quot;O&quot;,&quot;G&quot;,&quot;G&quot;]</p>

</details>

<details>
<summary>gpt-5.6-sol (5/16, 31.2%)</summary>

<p>**Inspecting the image**</p>

<p>I need to take a closer look at the image. It seems like it&#x27;s a solid yellow 4x4, which likely signifies something like four points of yellow. I think I should focus on gathering the necessary information and presenting it in JSON format only. Keeping it streamlined and straightforward is my goal, ensuring that everything is clear and concise. That should help in understanding the content better!</p>

</details>

<details>
<summary>gpt-6-luna (5/16, 31.2%)</summary>

<p>**Creating a yellow image array**</p>

<p>I&#x27;m focusing on creating a 4x4 array that displays solid yellow. I&#x27;ll need to ensure that the values are all set to represent yellow. Then, it must be in JSON format as well. This should be straightforward, but I want to double-check that I&#x27;m structuring the data correctly so it meets the requirements. I find it crucial to keep everything organized for clarity and proper functionality. Let&#x27;s get started on that!</p>

</details>

### 8x8 (64 pixels)

| Model | Cell Size | Reasoning | Correct | Accuracy | Kappa |
|-------|-----------|-----------|---------|----------|-------|
| gemini-3.8-flash | 32x | low | 64/64 | ✅ 100.0% | 1.000 |
| gemini-4-argon | 32x | low | 64/64 | ✅ 100.0% | 1.000 |
| claude-haiku-5.5 | 32x | low | 64/64 | ✅ 100.0% | 1.000 |
| claude-sonnet-5.5 | 32x | low | 64/64 | ✅ 100.0% | 1.000 |
| claude-opus-5 | 32x | low | 64/64 | ✅ 100.0% | 1.000 |
| claude-opus-5.5 | 32x | low | 64/64 | ✅ 100.0% | 1.000 |
| gpt-6-astra | 32x | low | 48/64 | 🔴 75.0% | 0.711 |
| claude-sonnet-5 | 32x | low | 40/64 | 🔴 62.5% | 0.562 |
| claude-haiku-4.5 | 32x | provider-default | 33/64 | 🔴 51.6% | 0.434 |
| gpt-6.1-sol | 32x | low | 25/64 | 🔴 39.1% | 0.286 |
| gpt-5.6-terra | 32x | low | 20/64 | 🔴 31.2% | 0.215 |
| gpt-4o-2024-05-13 | 32x | provider-default | 19/64 | 🔴 29.7% | 0.196 |
| grok-4.7 | 32x | low | 19/64 | 🔴 29.7% | 0.185 |
| grok-4.6 | 32x | low | 16/64 | 🔴 25.0% | 0.112 |
| gpt-5.6-sol | 32x | low | 12/64 | 🔴 18.8% | 0.092 |
| gpt-6-sol | 32x | low | 13/64 | 🔴 20.3% | 0.064 |
| gpt-6-luna | 32x | low | 4/64 | 🔴 6.2% | 0.000 |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/gt_8x8.png" alt="Ground Truth 8x8">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.8-flash | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_8x8_gemini_3_8_flash.png" alt="gemini-3.8-flash" width="64"> |
| gemini-4-argon | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_8x8_gemini_4_argon.png" alt="gemini-4-argon" width="64"> |
| claude-haiku-5.5 | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_8x8_claude_haiku_5_5.png" alt="claude-haiku-5.5" width="64"> |
| claude-sonnet-5.5 | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_8x8_claude_sonnet_5_5.png" alt="claude-sonnet-5.5" width="64"> |
| claude-opus-5 | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_8x8_claude_opus_5.png" alt="claude-opus-5" width="64"> |
| claude-opus-5.5 | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_8x8_claude_opus_5_5.png" alt="claude-opus-5.5" width="64"> |
| gpt-6-astra | 🔴 75% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_8x8_gpt_6_astra.png" alt="gpt-6-astra" width="64"> |
| claude-sonnet-5 | 🔴 62% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_8x8_claude_sonnet_5.png" alt="claude-sonnet-5" width="64"> |
| claude-haiku-4.5 | 🔴 52% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_8x8_claude_haiku_4_5.png" alt="claude-haiku-4.5" width="64"> |
| gpt-6.1-sol | 🔴 39% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_8x8_gpt_6_1_sol.png" alt="gpt-6.1-sol" width="64"> |

#### Reasoning Summaries

> These model-provided summaries may not faithfully represent the model's internal computation.

<details>
<summary>gemini-3.8-flash (64/64, 100.0%)</summary>

<p>**My Thought Process for Generating the Color Array Representation**</p>

<p>Alright, the objective here is to produce an 8x8 JSON array that visually represents the dominant colors within an image, using a specific shorthand for each color: R for Red, G for Green, B for Blue, Y for Yellow, M for Magenta, C for Cyan, O for Orange, and P for Purple. My approach will be to systematically scan the image, row by row, and at each coordinate, identify the primary color that best fits the visual information, assigning the corresponding letter. This is a direct, albeit simplified, form of image quantization or color mapping.</p>

<p>I&#x27;ll start with the topmost row, Row 0, and proceed downwards to Row 7. Within each row, I&#x27;ll move from the leftmost column (column 0) to the rightmost (column 7).</p>

<p>So, for Row 0:<br>
*   At coordinate (0,0), I see a distinct **Green (G)**.<br>
*   Moving right to (0,1), that&#x27;s clearly **Red (R)**.<br>
*   Next at (0,2), it appears to be **Magenta (M)**.<br>
*   (0,3) is a vibrant **Yellow (Y)**.<br>
*   (0,4) also looks like **Yellow (Y)**.<br>
*   Then at (0,5), I perceive **Blue (B)**.<br>
*   (0,6) is back to **Green (G)**.<br>
*   And finally, (0,7) is also **Green (G)**.</p>

<p>Now, let&#x27;s tackle Row 1:<br>
*   At (1,0), this shade suggests **Orange (O)**.<br>
*   (1,1) is **Red (R)**.<br>
*   (1,2) is another **Red (R)**.<br>
*   (1,3) is **Green (G)**.<br>
*   (1,4) is **Yellow (Y)**.<br>
*   (1,5) continues as **Yellow (Y)**.<br>
*   (1,6) is **Red (R)**.<br>
*   And (1,7) is **Yellow (Y)**.</p>

<p>Moving to Row 2:<br>
*   (2,0) has that warm hue of **Orange (O)**.<br>
*   (2,1) is **Yellow (Y)**.<br>
*   (2,2) presents a clear **Purple (P)**.<br>
*   (2,3) is **Magenta (M)**.<br>
*   (2,4) is **Red (R)**.<br>
*   (2,5) is a pure **Blue (B)**.<br>
*   (2,6) transitions back to **Orange (O)**.<br>
*   And (2,7) is **Cyan (C)**.</p>

<p>Onto Row 3:<br>
*   (3,0) is **Magenta (M)**.<br>
*   (3,1) is **Blue (B)**.<br>
*   (3,2) is **Yellow (Y)**.<br>
*   (3,3) is **Cyan (C)**.<br>
*   (3,4) is **Green (G)**.<br>
*   (3,5) is also **Green (G)**.<br>
*   (3,6) is **Orange (O)**.<br>
*   And (3,7) is **Green (G)**.</p>

<p>For Row 4:<br>
*   (4,0) starts with **Cyan (C)**.<br>
*   (4,1) is also **Cyan (C)**.<br>
*   (4,2) is **Magenta (M)**.<br>
*   (4,3) is **Red (R)**.<br>
*   (4,4) is **Purple (P)**.<br>
*   (4,5) is **Green (G)**.<br>
*   (4,6) is **Orange (O)**.<br>
*   And (4,7) is **Green (G)**.</p>

<p>Row 5 is next:<br>
*   (5,0) is **Magenta (M)**.<br>
*   (5,1) is **Cyan (C)**.<br>
*   (5,2) is **Yellow (Y)**.<br>
*   (5,3) is **Green (G)**.<br>
*   (5,4) is **Red (R)**.<br>
*   (5,5) is **Yellow (Y)**.<br>
*   (5,6) is **Magenta (M)**.<br>
*   And (5,7) is **Green (G)**.</p>

<p>Now for Row 6:<br>
*   (6,0) is **Yellow (Y)**.<br>
*   (6,1) is **Green (G)**.<br>
*   (6,2) is **Orange (O)**.<br>
*   (6,3) is **Magenta (M)**.<br>
*   (6,4) is **Purple (P)**.<br>
*   (6,5) is **Cyan (C)**.<br>
*   (6,6) is **Blue (B)**.<br>
*   And (6,7) is **Cyan (C)**.</p>

<p>Finally, Row 7:<br>
*   (7,0) is **Cyan (C)**.<br>
*   (7,1) is **Yellow (Y)**.<br>
*   (7,2) is **Magenta (M)**.<br>
*   (7,3) is **Green (G)**.<br>
*   (7,4) is **Blue (B)**.<br>
*   (7,5) is **Yellow (Y)**.<br>
*   (7,6) is **Blue (B)**.<br>
*   And (7,7) is **Purple (P)**.</p>

<p>I&#x27;m performing a quick double-check on the purples and blues. Looking at Row 2, coordinate (2,2) is indeed a distinct purple, and (2,3) is magenta, which aligns with the mapping. I also see purples at (4,4), (6,4), and (7,7), all fitting the P designation. For blues, I&#x27;ve marked (0,5), (2,5), (3,1), (6,6), (7,4), and (7,6) as B, and they all appear to be pure blues in the visual representation. This confirms my initial readings. The systematic row-by-row, column-by-column approach ensures I don&#x27;t miss any positions, and the visual confirmation of specific color clusters helps validate the mapping. The output will be a clean, structured JSON array as requested.</p>

<p></p>

</details>

<details>
<summary>gpt-6-astra (48/64, 75.0%)</summary>

<p>**Considering pixel mapping**</p>

<p>I need to focus on determining the pixel centers for the specified rows in the 256-cell image divided into 32 segments. For instance, row 1 contains red, magenta, yellow, and blue, while row 2 starts with orange, red, yellow, and others. I’ll inspect the image in my mind to visualize these boundaries effectively. That way, I can grasp how the colors align within the specified structure. This should help me map everything accurately!</p>

<p>**Verifying pixel coordinates**</p>

<p>I need to carefully establish the coordinates for each row in the image. For instance, row 1 has coordinates y16 with colors red, magenta, and so on. Row 2 holds orange and includes a rightmost cyan area. I should look closely to confirm the cyan extends from y64 to y96. By verifying the rows, such as checking row 4&#x27;s rightmost green at y96 and row 7&#x27;s cyan, I&#x27;ll ensure everything aligns and is accurate!</p>

</details>

<details>
<summary>gpt-5.6-terra (20/64, 31.2%)</summary>

<p>**Mapping color grids**</p>

<p>I need to create an 8x8 block map for an image grid that seems to have colors organized by rows. The dimensions are 256 pixels per side, and each cell is 32 pixels wide. From observations, I see that the top row is blue, green, yellow, and possibly cyan. The vertical transitions in color need to be considered as gradients while inspecting the colors closely. I&#x27;ll model the grid with these observations, aiming for an 8-color cyclic structure.</p>

<p>**Analyzing color fields**</p>

<p>I&#x27;m examining the image colors organized in fields of 64 pixels wide. The color distribution seems to have horizontal boundaries every 32 pixels, and I suspect the rectangles might be aligned by rows. For the first segment (y0-31), I see blue, green, yellow, and cyan. The next segments continue with red, green, yellow, and cyan. As I inspect further, it looks like the colors are consistent within each 32-cell region, differing only at the boundaries.</p>

</details>

<details>
<summary>grok-4.7 (19/64, 29.7%)</summary>

<p>I need to generate an 8x8 JSON array of single-letter color codes.</p>

<p>Examining the image pixel by pixel to identify each color.</p>

<p>Row 1: M, R, R, Y, G, G, B, B<br>
Row 2: O, O, P, R, G, G, G, G<br>
Row 3: O, B, P, R, G, G, G, G<br>
Row 4: C, C, Y, R, G, G, G, G<br>
Row 5: C, C, Y, R, M, M, B, B<br>
Row 6: C, C, M, M, M, M, B, B<br>
Row 7: Y, Y, M, M, R, B, B, B</p>

<p>Row 8: Y, Y, M, M, R, B, B, B</p>

<p>Reconsidering the dark purple cell in row 2 column 3. It may actually be dark blue rather than purple. Verifying that all eight colors appear in the final grid.</p>

<p>The dark cell in row 2 column 3 is dark blue. The purple cell is in row 3 column 3.</p>

<p>The dark square in row 2 column 3 has a purplish tint, so it is likely purple rather than blue. The bright blue remains separate.</p>

<p>The two dark shades are distinct palette colors, so the darker one cannot be blue. It must be purple.</p>

<p>The cell in row 2 column 3 is dark blue rather than purple. It is significantly darker than the bright blue and lacks red, so it maps to B.</p>

<p>The dark cell in row 2 column 3 is purple. The dark cell in row 3 column 2 is blue. The purple cell in row 3 column 3 remains purple.</p>

<p>Reconsidering the two dark cells. If bright blue is B, the deep blue may actually be B as well, and the perceived difference could just be image compression. Only the purple cell in row 3 column 3 would remain P.</p>

<p>The image is a clean pixel grid, so each cell has an exact color. The darkest cell in row 2 column 3 is navy purple and maps to P. The cell below it in row 3 column 2 is a saturated blue and maps to B.</p>

<p>Standard web color values are being checked against the image. Bright blue matches #0000FF, purple matches #800080, and the dark navy cell does not align with a standard pure color.</p>

<p>Standard blue is #0000FF, so the dark cell in row 3 column 2 cannot be bright blue. It must also be purple. That would make three consecutive cells purple: row 2 column 3, row 3 column 2, and row 3 column 3.</p>

<p>The darker cell in row 3 column 2 is bright blue. Its perceived darkness is due to simultaneous contrast with adjacent colors. The dark cell in row 2 column 3 is purple.</p>

<p>The two purple cells may actually be different shades. The darker navy one could be blue, while the violet one is purple.</p>

<p>The darker navy cell in row 2 column 3 is blue. The clearer blue cell in row 3 column 2 is also blue. The purple cell in row 3 column 3 remains purple.</p>

</details>

<details>
<summary>grok-4.6 (16/64, 25.0%)</summary>

<p>I need to generate an 8x8 JSON array of single-letter color codes.</p>

<p>I&#x27;m examining the image pixel by pixel to identify each color.</p>

<p>Mapping the first three rows: top row appears to be red, red, yellow, green; second row is orange, orange, orange, yellow, green; third row is cyan, cyan, cyan, red, green.</p>

<p>Revising the second row to orange, orange, yellow, green. The third row is cyan, cyan, red, green. Now identifying the fourth row.</p>

<p>Reconsidering the first row as red, red, yellow, green. The image appears to be divided into vertical color bands: reds on the left, yellows in the center, greens on the right top, then oranges below, followed by cyans, magentas, and blues at the bottom.</p>

<p>The fourth row appears to be cyan, cyan, magenta, green. The image shows a red square in the center with pink directly below it. I am now trying to map the fifth row.</p>

<p>The fourth row is cyan, cyan, magenta, green. The fifth row appears to be cyan, magenta, yellow, green. I am now identifying the sixth row.</p>

<p>The seventh row appears to be cyan, cyan, magenta, blue. The eighth row likely mirrors the bottom pattern. I am now pixelating the full grid to finalize the exact color sequence.</p>

<p>The fifth row is cyan, magenta, yellow, green. The sixth row appears to be cyan, magenta, purple, yellow, green.</p>

<p>Reconsidering the sixth row. The image shows a darker purple below the pink, so the sequence may be cyan, magenta, purple, yellow, green rather than cyan, magenta, magenta, yellow, green.</p>

<p>I am now mapping the grid column by column. The first column is red, orange, cyan, cyan, cyan, cyan, cyan, cyan. The second column appears to be red, orange, cyan, cyan, magenta, magenta, magenta, magenta. I am still determining the exact colors for the third column.</p>

<p>The third column appears to be yellow, yellow, red, magenta, magenta, purple, purple, blue. The fourth column is green, green, green, green, yellow, yellow, blue, blue. The rightmost columns are mostly green above and blue below.</p>

<p>The fifth row is cyan, magenta, yellow, green. The sixth row appears to be cyan, magenta, purple, yellow, green. The seventh row is cyan, magenta, purple, blue, blue, blue, blue, blue. The eighth row is cyan, magenta, blue, blue, blue, blue, blue, blue.</p>

</details>

<details>
<summary>gpt-5.6-sol (12/64, 18.8%)</summary>

<p>**Inferring grid colors**</p>

<p>I&#x27;m trying to infer grid colors for an image that&#x27;s potentially 256 pixels in total, structured in 4x4 quadrants, or even possibly 8x8 pixels, with each color block. The visible quadrants include top-left in red, top-right in orange, bottom-left in cyan, and bottom-right in blue. The prompt mentions 8 colors, but the visual only shows 4. I&#x27;ll produce an 8x8 based sampling with labels like R for red and O for orange, formatted in JSON only.</p>

</details>

<details>
<summary>gpt-6-sol (13/64, 20.3%)</summary>

<p>**Creating a map of bands**</p>

<p>I need to create bands that are 32 pixels each for an image that&#x27;s 256x256 in size. There will be 8 horizontal bands with the first being green from y0-31 and y32-63, then orange for y64-95, magenta for y96-127, cyan for y128-159, magenta again for y160-191, yellow for y192-223, and cyan again for y224-255. I see that the top part of the image is indeed green from y0-63. Alright, I need to output this!</p>

</details>

<details>
<summary>gpt-6-luna (4/64, 6.2%)</summary>

<p>**Analyzing pixel colors**</p>

<p>I&#x27;m trying to infer the color from an 8x8 pixel image. It seems to display uniformly, likely a solid color like purple or magenta. The upper part looks vivid and could be RGB #a000ff, suggesting it’s pixel art. I need to explore the color palette and realize the whole square appears as deep purple-blue without a visible grid. I’m concluding that it could be solid purple, so I&#x27;ll go with that choice.</p>

</details>

### Miner Willy Sprite (8x16, 128 pixels)

A classic 2-color retro game sprite (R=Red, W=White).

| Model | Cell Size | Reasoning | Correct | Accuracy | Kappa |
|-------|-----------|-----------|---------|----------|-------|
| gemini-3.8-flash | 32x | low | 128/128 | ✅ 100.0% | 1.000 |
| gemini-4-argon | 32x | low | 128/128 | ✅ 100.0% | 1.000 |
| claude-sonnet-5.5 | 32x | low | 128/128 | ✅ 100.0% | 1.000 |
| claude-opus-5.5 | 32x | low | 128/128 | ✅ 100.0% | 1.000 |
| claude-haiku-5.5 | 32x | low | 127/128 | 🟡 99.2% | 0.984 |
| claude-opus-5 | 32x | low | 125/128 | 🟡 97.7% | 0.952 |
| gpt-6-astra | 32x | low | 107/128 | 🟡 83.6% | 0.663 |
| gpt-6.1-sol | 32x | low | 95/128 | 🔴 74.2% | 0.480 |
| claude-sonnet-5 | 32x | low | 93/128 | 🔴 72.7% | 0.431 |
| grok-4.6 | 32x | low | 83/128 | 🔴 64.8% | 0.311 |
| claude-haiku-4.5 | 32x | provider-default | 84/128 | 🔴 65.6% | 0.300 |
| gpt-5.6-terra | 32x | low | 64/128 | 🔴 50.0% | 0.123 |
| gpt-6-sol | 32x | low | 64/128 | 🔴 50.0% | 0.123 |
| gpt-4o-2024-05-13 | 32x | provider-default | 69/128 | 🔴 53.9% | 0.005 |
| gpt-6-luna | 32x | low | 76/128 | 🔴 59.4% | 0.000 |
| gpt-5.6-sol | 32x | low | 57/128 | 🔴 44.5% | -0.069 |
| grok-4.7 | 32x | low | 0/128 | 🔴 0.0% | N/A |

#### Visual Comparison

**Ground Truth:**

<img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/gt_willy.png" alt="Ground Truth Willy">

| Model | Result | Output |
|-------|--------|--------|
| gemini-3.8-flash | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_willy_gemini_3_8_flash.png" alt="gemini-3.8-flash" width="64"> |
| gemini-4-argon | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_willy_gemini_4_argon.png" alt="gemini-4-argon" width="64"> |
| claude-sonnet-5.5 | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_willy_claude_sonnet_5_5.png" alt="claude-sonnet-5.5" width="64"> |
| claude-opus-5.5 | ✅ 100% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_willy_claude_opus_5_5.png" alt="claude-opus-5.5" width="64"> |
| claude-haiku-5.5 | 🔴 99% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_willy_claude_haiku_5_5.png" alt="claude-haiku-5.5" width="64"> |
| claude-opus-5 | 🔴 98% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_willy_claude_opus_5.png" alt="claude-opus-5" width="64"> |
| gpt-6-astra | 🔴 84% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_willy_gpt_6_astra.png" alt="gpt-6-astra" width="64"> |
| gpt-6.1-sol | 🔴 74% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_willy_gpt_6_1_sol.png" alt="gpt-6.1-sol" width="64"> |
| claude-sonnet-5 | 🔴 73% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_willy_claude_sonnet_5.png" alt="claude-sonnet-5" width="64"> |
| grok-4.6 | 🔴 65% | <img src="https://raw.githubusercontent.com/jcansdale/willy-bench/cb4ce88424d416207968132afde4a34c8f369221/images/output_willy_grok_4_6.png" alt="grok-4.6" width="64"> |

#### Reasoning Summaries

> These model-provided summaries may not faithfully represent the model's internal computation.

<details>
<summary>gemini-3.8-flash (128/128, 100.0%)</summary>

<p>**Deconstructing the Sprite: My Thought Process**</p>

<p>Alright, let&#x27;s break down this 8x16 sprite. My immediate goal is to understand its structure by meticulously examining each row, pixel by pixel, and visualizing the shape as it emerges.</p>

<p>I&#x27;ll start from the top, row 0, and move downwards, tracking the Red (R) and White (W) pixels. The width is a fixed 8 columns, so I need to be precise with my counting.</p>

<p>**Row 0:** I see a solid block of Red at the beginning – 5 pixels (columns 0-4). Then, there are 2 White pixels (columns 5-6), and finally, a single Red pixel at column 7. So, [R, R, R, R, R, W, W, R].</p>

<p>**Row 1:** This row has Red on the outer edges (columns 0-1 and column 7), with a wider band of White in the middle (columns 2-6). That&#x27;s [R, R, W, W, W, W, W, R].</p>

<p>**Row 2:** Now, things start to change. I see a single Red pixel at column 0, then a White pixel at column 1. The middle is White again (columns 2-5), and the row ends with 2 Red pixels (columns 6-7). So, [R, W, W, W, W, W, R, R]. The White pixel at column 1 here is interesting – it suggests something might be protruding or rounded on the left side.</p>

<p>**Row 3:** Back to 2 Red pixels on the left (columns 0-1). Then, 2 White pixels (columns 2-3). A single Red pixel at column 4 – this looks like a key feature, possibly an eye. Another White pixel at column 5, and finally, 2 Red pixels on the right (columns 6-7). Thus, [R, R, W, W, R, W, R, R].</p>

<p>**Row 4:** This is where the beak detail becomes clearer. I have 2 Red pixels on the left (columns 0-1). Then, the White pixels start, extending significantly across columns 2-6. This 5-pixel-wide White section is the beak&#x27;s body. Critically, there&#x27;s a Red pixel at column 7 – meaning the beak doesn&#x27;t quite touch the right edge, leaving a thin Red outline. So, [R, R, W, W, W, W, W, R]. My initial thought about column 7 being White here was incorrect; careful column counting reveals it&#x27;s Red.</p>

<p>**Row 5:** Here, the structure shifts again. 2 Red pixels on the left (columns 0-1). The White section narrows to 4 pixels (columns 2-5), suggesting the neck or head shape. Then, 2 Red pixels on the right (columns 6-7). [R, R, W, W, W, W, R, R].</p>

<p>**Row 6:** This row defines the neck. It has 3 Red pixels on the left (columns 0-2), then 2 White pixels in the center (columns 3-4). The right side has 3 Red pixels (columns 5-7). This 3-2-3 Red-White-Red pattern is a clear indicator of a constricted neck area. So, [R, R, R, W, W, R, R, R]. This confirms my understanding of the neck&#x27;s width.</p>

<p>**Row 7:** The body starts to widen again. 2 Red pixels on the left (columns 0-1), 4 White pixels in the middle (columns 2-5), and 2 Red pixels on the right (columns 6-7). This mirrors Row 5: [R, R, W, W, W, W, R, R].</p>

<p>**Row 8:** The body widens further, with Red pixels only on the extreme edges. 1 Red on the left (column 0), a wide 6-pixel White section in the middle (columns 1-6), and 1 Red on the right (column 7). [R, W, W, W, W, W, W, R].</p>

<p>**Row 9:** This row is identical to Row 8: [R, W, W, W, W, W, W, R].</p>

<p>**Row 10:** Now, a significant change. The Red on the left edge disappears, and the White starts from column 0 (columns 0-3). A single Red pixel appears at column 4. The rest are White (columns 5-7). [W, W, W, W, R, W, W, W]. This looks like the underside of the body or a new feature.</p>

<p>**Row 11:** The pattern continues to shift. 5 White pixels at the start (columns 0-4). A single Red pixel at column 5. Then 2 White pixels on the right (columns 6-7). [W, W, W, W, W, R, W, W].</p>

<p>**Row 12:** The Red on the left returns. 2 Red pixels (columns 0-1), 4 White pixels in the middle (columns 2-5), and 2 Red pixels on the right (columns 6-7). This pattern [R, R, W, W, W, W, R, R] is reminiscent of earlier rows, suggesting symmetry or a recurring shape.</p>

<p>**Row 13:** Red on the edges again, but narrower. 1 Red on the left (column 0), 3 White pixels (columns 1-3), 1 Red pixel in the middle (column 4 – possibly another eye or detail), 2 White pixels (columns 5-6), and 1 Red on the right (column 7). [R, W, W, W, R, W, W, R].</p>

<p>**Row 14:** Similar to row 13 but with slightly different White/Red distribution. 1 Red on the left (column 0), 2 White (columns 1-2), 1 Red (column 3), 3 White (columns 4-6), and 1 Red on the right (column 7). [R, W, W, R, W, W, W, R].</p>

<p>**Row 15:** The final row. 1 Red on the left (column 0), 3 White (columns 1-3), 1 Red in the middle (column 4), and 3 White on the right (columns 5-7). [R, W, W, W, R, W, W, W].</p>

<p>By systematically going through each row and column, I&#x27;ve pieced together the sprite. I can now visualize the overall shape: a head with a beak, a narrower neck, and a wider body. The details like the eye and the specific pixel arrangements suggest it might be a bird or a similar creature. The Red and White pixel data now feels complete and interpretable.</p>

<p></p>

</details>

<details>
<summary>claude-haiku-5.5 (127/128, 99.2%)</summary>

<p>I&#x27;m mapping out the grid of the image, 8 columns by 16 rows at 32px each, and sampling pixel colors row by row to reconstruct the pattern—starting with red and gray segments in the first couple rows.</p>

<p>Continuing down through rows 2 through 7, I&#x27;m tracking where the red blocks shift position relative to the gray columns, noting the red segments move slightly inward in rows 2-3 before shifting outward again toward the edges in rows 4-7, with row 6 showing a wider red spread on both sides.</p>

<p></p>

</details>

<details>
<summary>claude-opus-5 (125/128, 97.7%)</summary>

<p>I&#x27;m analyzing the pixel grid structure, mapping out which cells in each row are red versus gray based on the image dimensions and column positions.</p>

<p>Continuing through rows 6 through 11, mapping out each row&#x27;s red and gray column pattern based on where the color transitions occur in the image, building up the full grid row by row.</p>

<p></p>

</details>

<details>
<summary>claude-sonnet-5 (93/128, 72.7%)</summary>

<p>I&#x27;m mapping out the grid pattern cell by cell, tracking which positions are red versus white across each row to reconstruct the image&#x27;s structure.</p>

<p></p>

</details>

<details>
<summary>grok-4.6 (83/128, 64.8%)</summary>

<p>Converting the 8x16 pixel sprite into a JSON 2D array.</p>

<p>Mapping the 8x16 pixel image into an array of 16 rows and 8 columns. Red pixels will be encoded as &quot;R&quot; and gray pixels as &quot;W&quot;.</p>

<p>Drafting the JSON array row by row, starting with the top rows and continuing down.</p>

<p>The previous row guesses were inaccurate. I am re-examining the image to determine the correct pixel layout before finalizing the JSON array.</p>

</details>

<details>
<summary>gpt-5.6-terra (64/128, 50.0%)</summary>

<p>**Interpreting image coordinates**</p>

<p>I need to infer the dimensions of an image that’s 8x16, where each pixel is 32, and the width is 256. The background is red, and there&#x27;s a gray rectangle at the lower left. It looks like the rectangle spans from coordinates x0 to x127, and y256 to y383. Each grid row is 32. I need to confirm the pixel positions of the gray rectangle, which covers coordinates from (0, 256) to (128, 384). This gives me a 4x4 layout.</p>

</details>

<details>
<summary>gpt-6-sol (64/128, 50.0%)</summary>

<p>**Creating a map image**</p>

<p>I&#x27;m planning to create a map image that’s 256x512 pixels, divided into 32 segments. The first 10 rows will be red, while for the rows from 320 to 383, I’m thinking of using gray for rows 10 and 11. I’ll color the rest in red. I&#x27;ll make sure to get the dimensions right, so everything lines up nicely in the final design. Let&#x27;s get started on this!</p>

</details>

<details>
<summary>gpt-6-luna (76/128, 59.4%)</summary>

<p>**Classifying image colors**</p>

<p>I’m trying to infer if the image is a blank gray. The sprite of 8x16 appears to show a uniform gray field, likely labeled as W. I need to classify the colors, and the image dimensions are 256x512 with a gray background (#b8b8b8) and no visible red. Given that I’m mapping W to white/gray, every pixel should be W. I’ll output 16 rows of 8.</p>

</details>

<details>
<summary>gpt-5.6-sol (57/128, 44.5%)</summary>

<p>**Mapping image pixels**</p>

<p>I&#x27;m working on inferring image pixels in an 8x16 format from a 256x512 image. Each pixel block seems to be 32x32. I&#x27;ll map red against gray: the background is gray, while the left side is red with a stepped boundary. I need to inspect the rows for specific boundaries. </p>

<p>It seems like: rows 1-3 have a boundary at x128, rows 4 at x160, and others might extend from there. It&#x27;s essential to systematically identify these transitions.</p>

<p>**Analyzing image boundaries**</p>

<p>I&#x27;m examining the image boundaries to understand how the visible sections are mapped. It seems there’s a top vertical boundary at x128 until y95, with several steps right and left at various y-coordinates. </p>

<p>When I reach y448, it appears the bottom section is fully red. I’m curious if the transition looks plausible, especially with the triangular gray region and diagonal boundaries. I’ll need to inspect the coordinates more accurately to understand the dimensions and overall scale of the 256x512 image displayed.</p>

<p>**Analyzing red boundary shape**</p>

<p>I&#x27;m looking at the red shape and noticing that at y=416, it extends only around x96. Upon inspecting the screenshot, I see this red shape has an inward notch. The boundary moves from the point (x160,y352) diagonally to (x128,y384), then diagonally left to (x96,y416) before it angles right toward (256,512). It seems that at approximately (97,415), the red boundary descends diagonally toward the bottom right, filling under that diagonal.</p>

</details>

## Overall Rankings

Averaged across all successful image tests and ranked by Cohen's kappa:

| Rank | Model | Avg Accuracy | Avg Kappa |
|------|-------|--------------|-----------|
| 1 | 🥇 gemini-3.8-flash | 100.0% | 1.000 |
| 2 | 🥈 gemini-4-argon | 100.0% | 1.000 |
| 3 | 🥉 claude-sonnet-5.5 | 100.0% | 1.000 |
| 4 |  claude-opus-5.5 | 100.0% | 1.000 |
| 5 |  claude-haiku-5.5 | 99.6% | 0.992 |
| 6 |  claude-opus-5 | 99.2% | 0.984 |
| 7 |  claude-sonnet-5 | 78.4% | 0.664 |
| 8 |  claude-haiku-4.5 | 72.4% | 0.578 |
| 9 |  gpt-6-astra | 63.3% | 0.509 |
| 10 |  gpt-4o-2024-05-13 | 59.1% | 0.373 |
| 11 |  gpt-6.1-sol | 48.2% | 0.295 |
| 12 |  grok-4.7 | 36.7% | 0.246 |
| 13 |  gpt-5.6-terra | 39.6% | 0.190 |
| 14 |  grok-4.6 | 36.2% | 0.147 |
| 15 |  gpt-6-sol | 29.7% | 0.086 |
| 16 |  gpt-5.6-sol | 31.5% | 0.008 |
| 17 |  gpt-6-luna | 32.3% | 0.000 |

## Key Findings

1. **Fixed cell sizing standardizes visual resolution** - Every model receives the same contiguous nearest-neighbor rendering
2. **Gemini 3.x models excel** - Achieve near-perfect pixel extraction with proper settings
3. **Structured JSON output helps** - 2D array format with individual letters performs best
4. **Image size matters** - Smaller images (4x4) are easier to extract accurately
