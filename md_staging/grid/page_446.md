```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_446.jpeg
document_name: grid
page_number: 446
page_id: grid#page_446
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:16:58Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview
- Overview of features in the Essential Grid for Windows Forms.
- Instructions on customizing grid appearance, such as background color and grid lines.

## Content

### Grid with Background Color Set to Beige

![Grid with Background Color set to Beige](#figure-171)
**Figure 171: Grid with Background Color set to Beige**

- **ResizingCellsLinesColor**: Specifies the color for the grid lines (for example, active border). Default value is set to `GrayText`.

#### Setting `ResizingCellsLinesColor` Property

The following code examples can be used to set this property:

1. **Using C#**
    ```csharp
    [C#]
    // Specify the color for the grid line marker while resizing rows and columns.
    this.gridControl1.Properties.ResizingCellsLinesColor = Color.PaleVioletRed;
    ```
2. **Using VB.NET**
    ```vb
    [VB.NET]
    ' Specify the color for the grid line marker while resizing rows and columns.
    Me.gridControl1.Properties.ResizingCellsLinesColor = Color.PaleVioletRed
    ```

### Borders

Specifies settings for Top, Left, Bottom, and Right borders.

#### Setting `Borders` Property

The following code examples can be used to set this property:

1. **Using C#**
    ```csharp
    [C#]
    ```

---

<!-- tags: [syncfusion, winforms, grid, controlling, customizing, resizing, lines, borders, background, color] keywords: [grid, essential grid, windows forms, background color, resizing, cells lines color, borders, c#, vb.net, customization, appearance] -->
```