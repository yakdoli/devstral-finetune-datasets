```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_487.jpeg
document_name: grid
page_number: 487
page_id: grid#page_487
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:19:54Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Demonstrates how to customize grid appearance using `gridControl1` properties.
- Explains衍生GridPrintDocument的过程及其在打印控制方面的应用。

## Content

### Customizing Grid Appearance

To achieve a specific visual effect for cells in the grid, the following code snippet can be applied:

```csharp
Me.gridControl1(2, 2).Font.Bold = True

' Cover (6,2) through (7,4) so it is treated as a large fancy label.
Me.gridControl1.Model.CoveredRanges.Add(GridRangeInfo.Cells(6, 2, 7, 4))
Me.gridControl1(6, 2).CellType = "Static"
Me.gridControl1(6, 2).Text = "Big Label"
Me.gridControl1(6, 2).HorizontalAlignment = GridHorizontalAlignment.Center
Me.gridControl1(6, 2).VerticalAlignment = GridVerticalAlignment.Middle
Me.gridControl1(6, 2).Font.Size = 12
Me.gridControl1(6, 2).Font.Bold = True
Me.GridControl1(6, 2).Interior = New BrushInfo(GradientStyle.PathRectangle, _Color.FromArgb(0xED, 0xF0, 0xF6), _Color.FromArgb(0x2A, 0x43, 0x7E))
Me.GridControl1(6, 2).TextColor = Color.FromArgb(0x66, 0x6E, 0x98)
```

#### Section 4.1.4.16 Deriving GridPrintDocument

The `GridPrintDocument` has events like `BeginPrint`, `PrintPage`, and `EndPrint`, which are inherited from `PrintDocument`. This allows you to access the printing flow at specific points. To gain more control, you can derive the `GridPrintDocument` and override members like `OnPrint`. This enables accessing grid members such as `ViewLayout` and `TopRowIndex` to obtain information about the page being printed. The code snippet below shows how to print the top and bottom row of the page:

---

#### Example: Custom Print Document for a Grid

```csharp
[C#]

public class MyPrintDocument : GridPrintDocument
{
    GridControlBase _grid;

    public MyPrintDocument(GridControlBase grid, bool printPreview):base(grid, printPreview)
    {
        _grid = grid;
    }

    protected override void OnPrintPage(System.Drawing.Printing.PrintPageEventArgs ev)
    {
        base.OnPrintPage(ev);
    }
}
```

### Summary

This section illustrates how to customize the appearance of specific cells within a grid and how to derive a custom print document (`GridPrintDocument`) to gain additional control over printing grid content.

---
<!-- tags: [Syncfusion Winforms, Grid, PrintDocument, Customization] keywords: [GridPrintDocument, covered ranges, customization, printing, C#] -->
```