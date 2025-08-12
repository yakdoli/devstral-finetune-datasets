```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_500.jpeg
document_name: grid
page_number: 500
page_id: grid#page_500
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:20:30Z
fidelity: lossless
-->

## Overview

- Demonstrates the `PrintToFit` functionality in the Essential Grid for Windows Forms.
- Explains how multiple grids can be printed across various pages using the `MultipleGridPrintDocument` helper class.
- Lists printing options and their corresponding behaviors.

## Content

### 4.1.4.21 Multiple Grid Printing

**Summary:**
Multiple grids can be printed across various pages using the `MultipleGridPrintDocument` helper class. This functionality is achieved by drawing the full-size grid to a large bitmap and then scaling this bitmap to fit the output page.

#### PrintToFit Functionality

This functionality can also be achieved by clicking the `PrintToFit` button on the UI. Refer to **Figure 193: Print To Fit** for a visual representation.

**Figure 193: Print To Fit**

The functionality allows grids to be printed "to fit," ensuring that the contents of the grid are scaled appropriately to fit within the printed output.

#### Multiple Grid Printing Options

- **MultiGridPrinting:** Customizes the way printing support is provided for grids. It enables multiple grids to be printed in a single print.
- **PrintGridInNewPage:** Multiple grids can be printed continuously, but each grid's starting page will begin on a new page.
- **DefaultGridPrint:** Multiple grids will be printed without considering column breaks.
- **ScaleColumnsToFit:** Multiple grid columns will be scaled to fit the printed page.

#### Properties

**Table 8: Properties Table**

| Property               | Description                                                                                        | Type               | Data Type | Reference links       |
|------------------------|----------------------------------------------------------------------------------------------------|--------------------|-----------|-----------------------|
| MultiGridPrinting      | Customizes the way printing support is provided for grids. It enables multiple grids to be printed in a single print. |       |             |                   |
| PrintGridInNewPage     | Multiple grids can be printed continuously. However, the consecutive grid's starting page will begin on a new page. |       |             |                   |
| DefaultGridPrint       | Multiple grids will be printed without considering the column breaks. |       |             |                   |
| ScaleColumnsToFit      | Multiple grid columns will be scaled to fit the printed page. |       |             |                   |

---

<!-- tags: [printtofit, multiplesgridprintdocument, multigridprinting, printgridinnewpage, defaultgridprint, scalecolumntostfit, essentialgrid, windowsforms] keywords: [print, multiple grid printing, grid printing, scaling, output page, print options] -->
```