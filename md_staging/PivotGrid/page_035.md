```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_035.jpeg
document_name: PivotGrid
page_number: 035
page_id: PivotGrid#page_035
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:54:56Z
fidelity: lossless
-->

## Essential PivotGrid Windows Forms

### Code Examples

```csharp
this.pivotGridControl1.ShowSubTotals = false;
```

```vb
Me.pivotGridControl1.ShowSubTotals = False
```

### 4.9 Exporting Pivot Grid to Excel, Word, and PDF

The PivotGrid is exported into different formats and the formatting styles are applied as per the visual style of PivotGrid.

There are three options to export PivotGrid:

1.  Export to Excel
2.  Export to Word
3.  Export to PDF

#### Export to Excel:

Exporting data to an Excel spreadsheet is one of the most commonly preferred features in the .NET world. Essential Grid control has an in-built support to export an Excel spreadsheet. The class **ExcelExport** provides support for exporting data from the PivotGrid control to an Excel spreadsheet for verification and/or computation.

This class automatically copies a grid's styles and formats to an Excel spreadsheet. This enables you to export PivotGrid to an Excel document.

The following code illustrates exporting PivotGrid to an Excel:

```csharp
ExcelExport excelExport = new ExcelExport(pivotGridControl1,
Syncfusion.XlsIO.ExcelVersion.Excel2010);

excelExport.ExportMode = (ExportAsPivotTable) ? ExportModes.PivotTable
: ExportModes.Cell;

excelExport.Export(FileName);
```

#### Export to Excel provides two options:

1.  Cell-by-Cell Export
2.  Pivot Table Export
```