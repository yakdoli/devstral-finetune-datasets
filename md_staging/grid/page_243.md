```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_243.jpeg
document_name: grid
page_number: 243
page_id: grid#page_243
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:05:01Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

To view samples from the dashboard:

- Open Syncfusion Dashboard.
- Select UI > Windows Forms.
- Click Run Samples.
- Navigate to Grid > MS Excel-Style Features > Mark Header Demo

## 4.1.4.6 Formula Support

Setting the cell type of a cell to `FormulaCell` will allow you to enter algebraic expressions using formulas and cell references. Cell references are entries such as A11 for column A row 11 or BA3 for column BA row 3. A formula is a defined calculation from the Formula Library which is included with Essential Grid. This Formula Library is extensible and lets you to add additional formulas.

This section discusses the following topics:

### 4.1.4.6.1 Defining a FormulaCell

You can use Formula Cells for every cell in a grid or for just a few cells. Even if you set the `CellType` property to `FormulaCell` to every cell in a grid, the default behavior is to treat such cells as text box cells, unless you start the cell entry with an equal sign. If the cell value starts with an equal sign, then the cell is considered as a formula cell and its contents are treated as such.

To make all cells present in a grid as potential formula cells, you will have to set the cell type of the standard `BaseStyle` to `FormulaCell` by using the following code.

### C#

```csharp
// Set up a Formula Cell.
this.gridControl1.BaseStylesMap["Standard"].StyleInfo.CellType = "FormulaCell";
```

### VB.NET

```vb
' Set up a Formula Cell.
Me.gridControl1.BaseStylesMap("Standard").StyleInfo.CellType = "FormulaCell"
```

<!-- tags: [Essential Grid, Windows Forms, Formula Support, FormulaCell, CellType, BaseStyle, Formula Library, Syncfusion Winforms] keywords: [Essential Grid, Windows Forms, Formula Support, FormulaCell, CellType, BaseStyle, Formula Library, Syncfusion Winforms] -->
```