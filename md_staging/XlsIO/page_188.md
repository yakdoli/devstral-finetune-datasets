```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_188.jpeg
document_name: XlsIO
page_number: 188
page_id: XlsIO#page_188
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:01:29Z
fidelity: lossless
-->

## XlsIO

### Overview
- XlsIO provides functionality to autofit row and column sizes based on the content within a specified range of cells.
- Demonstrates how to apply Autofit features within a specific range of cells in a worksheet.

### Content

#### Overview of Autofit Features
XlsIO also allows to autofit a row/column based on the content in a range of cells within the cells.

```csharp
// AutoFit columns within a Range.
IWorksheet.Range[int startRow, int startColumn, int lastRow, int lastColumn].AutoFitColumns()

// AutoFit rows within a Range.
IWorksheet.Range[int startRow, int startColumn, int lastRow, int lastColumn].AutoFitRows();
```

#### Example Code: Autofitting within a Range of Cells
Following code example illustrates autofitting within a range of cells.

**[C#]**
```csharp
// Entering text inside the Cells.
sheet.Range["B2:I20"].Text = "Autofit";
sheet.Range[1, 2].Value = "A very long text, This should be ignored by mySheet.Range[5, 2, 19, 2].AutoFitColumns()";
sheet.Rows[4].RowHeight = 90;
sheet.Rows[15].RowHeight = 90;

// AutoFit columns applied within a Range.
mySheet.Range[5, 2, 19, 2].AutoFitColumns();

// AutoFit rows applied within a Range.
mySheet.Range[5, 2, 13, 4].AutoFitRows();
```

**[VB.NET]**
```vb
' Entering text inside the Cells.
sheet.Range["B2:I20"].Text = "Autofit"
sheet.Range[1, 2].Value = "A very long text, This should be ignored by mySheet.Range[5, 2, 19, 2].AutoFitColumns()"
sheet.Rows[4].RowHeight = 90
sheet.Rows[15].RowHeight = 90

' AutoFit columns applied within a Range.
mySheet.Range[5, 2, 19, 2].AutoFitColumns()

' AutoFit rows applied within a Range.
mySheet.Range[5, 2, 13, 4].AutoFitRows()
```

<!-- tags: [XlsIO, autofit, row, column, range, C#, VB.NET] keywords: [xlsio, autofit columns, autofit rows, worksheet, range, c#, vb.net] -->
```