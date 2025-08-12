```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_510.jpeg
document_name: grid
page_number: 510
page_id: grid#page_510
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:21:14Z
fidelity: lossless
-->


## Overview

- Demonstrates the usage of VB.NET to apply styling to cells in a grid.
- Explains the Merge Cells feature, which combines adjacent cells with the same value into a single cell for enhanced display and functionality.
- Describes various settings for the Merge Cells mode and behavior.

## Content

### Using VB.NET

```vb
[VB.NET]

Dim style As GridStyleInfo
style = grid(4, 3)
grid.BanneredRanges.Add(GridRangeInfo.FromTlhw(4, 3, 8, 3))
style.BackgroundImage = 
GetImage("common\Images\Grid\BannerCells\back1.jpg")
style.Text = "back1.jpg"
style.TextColor = Color.Red
style.BackgroundImageMode = GridBackgroundImageMode.StretchImage
```

### 4.1.4.26 Merge Cells Feature

The Merge Cells feature merges two or more adjacent cells with the same value into one cell and displays the content in the merged cell. A single cell is created by combining two or more selected cells.

**Note**: The data in the merged cells will be displayed on the first cell of the merged range.

To use merge cells, you need to set `Model.Options.MergeCellsMode` and `MergeCell` properties of the cells to select the required merge behavior for cells.

1. **The `GridMergeCellsMode` enumeration specifies behavior of the merged cells in a grid. Following is the list of options under this enumeration:**

   - **None**
     - Merge cells behavior is disabled.
   - **OnDemandCalculation**
     - The number of cells to be merged are calculated before the merged cells are displayed and the results are saved. Floating cells will only be recalculated if the width or content of the cells change.
   - **BeforeDisplayCalculation**
     - The number of cells to be merged are always calculated before cells are displayed.

<!-- tags: [product, module, control, api, version?] keywords: [merge cells, grid, vb.net, style, background image, bannered range, gridmergecellsmode, ondemandcalculation, beforedisplaycalculation, syncfusion, winforms, 11.4.0.26] -->
```