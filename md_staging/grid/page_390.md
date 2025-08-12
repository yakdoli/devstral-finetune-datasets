```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_390.jpeg
document_name: grid
page_number: 390
page_id: grid#page_390
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:13:28Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

```csharp
// Set some properties.
style.BackColor = Color.Aquamarine;
style.CellValue = "Grid";
style.Font.Facename = "Verdana";
style.Font.Size = 8.2f;
style.Font.Bold = true;

// Apply this style to several cells.
this.gridControl1.ChangeCells(GridRangeInfo.Cells(3, 3, 4, 4), style);
```

### [VB.NET]

```vb
' Add some text to cell (2,3).
gridControl1(2, 3).CellValue = "Essential"

' Create a GridStyleInfo.
Dim style As GridStyleInfo
style = New GridStyleInfo()

' Set some properties.
style.BackColor = Color.Aquamarine
style.CellValue = "Grid"
style.Font.Facename = "Verdana"
style.Font.Size = 8.2!
style.Font.Bold = True

' Apply this style to several cells.
Me.gridControl1.ChangeCells(GridRangeInfo.Cells(3, 3, 4, 4), style)
```

![Figure 140: Result of the ChangeCells Call in the Previous Code Sample](./image.png)

## [C#]

### Content

- **Overview**: Demonstrates how to apply styles to specific cells in a grid control.
- **C# Code Example**:
```csharp
// Set cell value and style properties.
style.BackColor = Color.Aquamarine;
style.CellValue = "Grid";
style.Font.Facename = "Verdana";
style.Font.Size = 8.2f;
style.Font.Bold = true;

// Apply style to multiple cells.
this.gridControl1.ChangeCells(GridRangeInfo.Cells(3, 3, 4, 4), style);
```
- **VB.NET Code Example**:
```vb
' Set cell value and style properties.
gridControl1(2, 3).CellValue = "Essential"
style.BackColor = Color.Aquamarine
style.CellValue = "Grid"
style.Font.Facename = "Verdana"
style.Font.Size = 8.2!
style.Font.Bold = True

' Apply style to multiple cells.
Me.gridControl1.ChangeCells(GridRangeInfo.Cells(3, 3, 4, 4), style)
```

- **Figure**: Shows the outcome of applying the styles to the specified cells in the grid control.

### See also:
- `GridRangeInfo.Cells` method: Specifies the range of cells to apply the style to.
- `GridStyleInfo` class: Defines the style properties for the grid cells.

## API Reference

### Methods
- `ChangeCells`: Applies a style to a specified range of cells in the grid.

### Parameters
- **gridRangeInfo**: Represents the range of cells to style. For example, `GridRangeInfo.Cells(3, 3, 4, 4)` selects cells from row 3, column 3 to row 4, column 4.
- **style**: The `GridStyleInfo` object that contains the styling properties to apply.

### Exceptions
- Throws an exception if the `gridRangeInfo` or `style` is null.

### Returns
- None.

## Code Examples

### C#

```csharp
GridStyleInfo style = new GridStyleInfo();
style.BackColor = Color.Aquamarine;
style.CellValue = "Grid";
style.Font.Facename = "Verdana";
style.Font.Size = 8.2f;
style.Font.Bold = true;

this.gridControl1.ChangeCells(GridRangeInfo.Cells(3, 3, 4, 4), style);
```

### VB.NET

```vb
Dim style As New GridStyleInfo()
style.BackColor = Color.Aquamarine
style.CellValue = "Grid"
style.Font.Facename = "Verdana"
style.Font.Size = 8.2!
style.Font.Bold = True

Me.gridControl1.ChangeCells(GridRangeInfo.Cells(3, 3, 4, 4), style)
```

<!-- tags: [Syncfusion Winforms, Grid, GridStyleInfo, ChangeCells] keywords: [grid, style, cell styling, grid control] -->
```