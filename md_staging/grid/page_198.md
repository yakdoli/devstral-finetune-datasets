```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_198.jpeg
document_name: grid
page_number: 198
page_id: grid#page_198
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:00:38Z
fidelity: lossless
-->

## Overview

- Explanation of how to set `CellTipText` in a Grid for different levels: table, cell, row, and column.
- Code examples in C# and VB.NET for setting `CellTipText`.
- Introduction to Excel-like Cell Comment Tips, including how to implement and manage them.

## Content

### Tip Text for Table

```csharp
// Tip Text for table.
this.gridControl1.TableStyle.CellTipText = "TipText for table";
```

### Using VB.NET

```vb
[VB.NET]

' Tip Text for cell (2,3).
Me.gridControl1(2, 3).CellTipText = "TipText for cell 2,3"

' Tip Text for row 3.
Me.gridControl1.RowStyle(3).CellTipText = "TipText for row 3"

' Tip Text for column 4.
Me.gridControl1.ColStyle(4).CellTipText = "TipText for column 4"

' Tip Text for table.
Me.gridControl1.TableStyle.CellTipText = "TipText for table"
```

**Figure 105: Cell Tips**  
![](attachment:grid#page_198-cell-tips.png)

#### 4.1.4.2.10.5 Cell Comment Tips

- Excel-like Cell Comment Tips can be included in a Grid by deriving the mouse controller class.
- The comment text is a custom style property added to cells that hold comments.
- To change, add or delete a comment, right-click the cell or left-click the red corner.

## API Reference

### Properties

- **CellTipText**: Specifies the text to be displayed as a tooltip for a cell, row, column, or table.

### Methods/Events

- **MouseController**: Derive this class to implement Excel-like Cell Comment Tips.

## Code Examples

### C#

```csharp
// Example of setting cell tip text for a specific cell.
gridControl1[2, 3].CellTipText = "TipText for cell 2,3";

// Example of setting cell tip text for a row.
gridControl1.RowStyle(3).CellTipText = "TipText for row 3";

// Example of setting cell tip text for a column.
gridControl1.ColStyle(4).CellTipText = "TipText for column 4";

// Example of setting cell tip text for the entire table.
gridControl1.TableStyle.CellTipText = "TipText for table";
```

### VB.NET

```vb
' Example of setting cell tip text for a specific cell.
Me.gridControl1(2, 3).CellTipText = "TipText for cell 2,3"

' Example of setting cell tip text for a row.
Me.gridControl1.RowStyle(3).CellTipText = "TipText for row 3"

' Example of setting cell tip text for a column.
Me.gridControl1.ColStyle(4).CellTipText = "TipText for column 4"

' Example of setting cell tip text for the entire table.
Me.gridControl1.TableStyle.CellTipText = "TipText for table"
```

### Implementing Cell Comment Tips

```csharp
// Derive MouseController to implement cell comment tips.
public class CustomMouseController : GridMouseController
{
    // Additional methods to handle custom button click for comment management.
}
```

## Page-level Navigation/TOC

- [Tip Text for Table](grid#page_198#tip-text-for-table)
- [Using VB.NET](grid#page_198#using-vb-net)
- [Cell Comment Tips](grid#page_198#cell-comment-tips)

## Cross References

- See also:  
  - [Mouse Controller Derivation](grid#mouse-controller-derivation)
  - [Custom Style Properties](grid#custom-style-properties)

<!-- tags: [Syncfusion Winforms, Grid Control, Cell Comment Tips, Mouse Controller, CellTipText] keywords: [CellTipText, Excel-like Comment Tips, Grid, MouseController, cell, row, column, table] -->
```