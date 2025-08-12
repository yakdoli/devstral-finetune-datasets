```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_509.jpeg
document_name: grid
page_number: 509
page_id: grid#page_509
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:21:08Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Demonstrates the functionality of Banner Cells in the Essential Grid.
- Explains how to combine the background of neighboring cells using Banner Cells.
- Provides code examples in C# for displaying images using Banner Cells.

## Content

Figure 196: Banner Cells

![Banner Cells](banner-cells.png)

### Displaying Image using Banner Cells

The following code examples illustrate how to display images by using banner cells:

#### Using C#

```csharp
GridStyleInfo style;
style = grid[4, 3];
grid.BANNEREDRanges.Add(GridRangeInfo.FromTlhw(4, 3, 8, 3));
style.BackgroundImage = getImage(@"common\Images\Grid\BannerCells\back1.jpg");
style.Text = "back1.jpg";
```

## API Reference (if applicable)
This section would typically contain references to the API used in the code examples, such as `GridStyleInfo`, `GridRangeInfo`, and methods like `getImage`.

## Code Examples
- The provided C# example demonstrates how to set up Banner Cells and apply an image to them.

## Page-level Navigation/TOC (if applicable)
- This page focuses on Banner Cells and their usage in the Essential Grid.

## Cross References
- Refer to other sections or pages that discuss related topics, such as Grid styling, or other features of the Essential Grid.

<!-- tags: [product, module, control, api, version?] keywords: [Banner Cells, Essential Grid, Windows Forms, GridStyleInfo, GridRangeInfo, getImage] -->
```