```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_156.jpeg
document_name: grid
page_number: 156
page_id: grid#page_156
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:58:15Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Overview

- Demonstrates how to set the cell type to "Control" in a grid.
- Explains the Currency Edit cell type for editing monetary values.
- Provides code examples in both C# and VB.NET for setting cell types.

## Content

### Setting the Cell Type to Control

The following code example illustrates how to set the cell type to Control.

```csharp
// Set up a Control Cell.
this.radioButton1.Checked = true;
this.gridControl1.CoveredRanges.Add(GridRangeInfo.Cells(2, 2, 8, 2));
this.gridControl1.ColWidths[2] = 200;
this.gridControl1[2, 2].CellType = "Control";

// Set the control object.
this.gridControl1[2, 2].Control = this.dataPanel;
```

```vb
' Set up a Control Cell.
Me.radioButton1.Checked = True
Me.gridControl1.CoveredRanges.Add(GridRangeInfo.Cells(2, 2, 8, 2))
Me.gridControl1.ColWidths(2) = 200
Me.gridControl1(2, 2).CellType = "Control"

' Set the control object.
Me.gridControl1(2, 2).Control = Me.dataPanel
```

The following screenshot shows a panel holding two radio buttons and a push button in the cell.

![Figure 79: Control Cells](attachment:Control_Cells.png)

### Currency Edit

The Currency Edit cell type lets you edit monetary values and display them using different currency formats. To achieve this, you must set the `CellType` property to `Currency`. You can also configure additional properties such as the decimal and group separators for the cell value.

#### Setting the Cell Type to CurrencyEdit

The following code example illustrates how to set the cell type to CurrencyEdit.

```csharp
// Set up a Currency Edit Cell.
this.gridControl1[2, 2].CellType = "CurrencyEdit";

// Optionally, configure additional properties.
this.gridControl1[2, 2].DecimalSeparator = ".";
this.gridControl1[2, 2].GroupSeparator = ",";
```

```vb
' Set up a Currency Edit Cell.
Me.gridControl1(2, 2).CellType = "CurrencyEdit"

' Optionally, configure additional properties.
Me.gridControl1(2, 2).DecimalSeparator = "."
Me.gridControl1(2, 2).GroupSeparator = ","
```

## API Reference

- **Properties**
  - `CellType`: Specifies the type of the cell.
  - `DecimalSeparator`: Specifies the separator used for decimal values.
  - `GroupSeparator`: Specifies the separator used for grouping numeric values.

## Code Examples

### C#

```csharp
// Example to set the cell type to Control.
this.gridControl1[2, 2].CellType = "Control";
this.gridControl1[2, 2].Control = this.dataPanel;
```

### VB.NET

```vb
' Example to set the cell type to Control.
Me.gridControl1(2, 2).CellType = "Control"
Me.gridControl1(2, 2).Control = Me.dataPanel
```

## Cross References

- Refer to the Grid Control documentation for more information on cell types and properties.
- Additional details on currency formatting can be found in the related API documentation.

<!-- tags: [syncfusion, grid, windows forms, celltype, currencyedit, control] keywords: [celltype, currencyedit, control, grid control, windows forms] -->
```