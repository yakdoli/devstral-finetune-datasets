```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_158.jpeg
document_name: grid
page_number: 158
page_id: grid#page_158
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:57:52Z
fidelity: lossless
-->

## Essential Grid for Windows Forms

### Currency Cells

<figure>
  <img src="Currency_Cells" alt="Currency Cells" />
  <figcaption>Figure 80: Currency Cells</figcaption>
</figure>

#### Formula Cell

The `FormulaCell` cell type allows you to add algebraic formulas to a cell that depends on other cells. The cell value should be a well-formed formula starting with an `'='` and the `CellType` property set to `FormulaCell`. If a Formula Cell does not begin with an `'='`, the cell is treated as a text box cell. For details, see [Formula Support](#).

##### Example: Setting a Cell Type to `FormulaCell`

The following code example illustrates how to set the cell type to `FormulaCell`.

#### C#

```csharp
// Set Cell Type as Formula Cell.
gridControl1[rowIndex, colIndex].CellType = "FormulaCell";

// Assign a Formula.
gridControl1[rowIndex, colIndex].CellValue = "= (A1+A2) / 2";
```

#### VB.NET

```vb
' Set Cell Type as Formula Cell.
gridControl1(rowIndex, colIndex).CellType = "FormulaCell"

' Assign a Formula.
gridControl1(rowIndex, colIndex).CellValue = "= (A1+A2) / 2"
```

### API Reference

#### Properties
- `CellType`: Specifies the type of the cell.
- `CellValue`: Gets or sets the value of the cell.

#### Methods
- `SupportsFormula`: Indicates whether the cell supports formulas.

### Code Examples

#### Example: Creating a FormulaCell

```csharp
// Example of creating a FormulaCell
gridControl1[3, 3].CellType = "FormulaCell";
gridControl1[3, 3].CellValue = "= (A1+A2) / 2";
```

```vb
' Example of creating a FormulaCell
gridControl1(3, 3).CellType = "FormulaCell"
gridControl1(3, 3).CellValue = "= (A1+A2) / 2"
```

### Cross References

See also:
- [Formula Support](#)

<!-- tags: [syncfusion-sdk, essential-grid, windows-forms, formula-cell, cell-type, algebraic-formulas] keywords: [currency-cells, cell-type, formula-support, algebraic-formulas, text-box-cell, well-formed-formula] -->
```