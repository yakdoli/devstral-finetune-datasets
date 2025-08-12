```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_256.jpeg
document_name: XlsIO
page_number: 256
page_id: XlsIO#page_256
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:06:43Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
sheet.PageSetup.DifferentOddAndEvenPagesHF = False
sheet.PageSetup.DifferentFirstPageHF = False
sheet.PageSetup.HFScaleWithDoc = True
sheet.PageSetup.AlignHFWithPageMargins = True
```

## 4.2.5 Tables

In Excel, Tables can be inserted by selecting Table option from the Insert menu.

### Table Creation By Using XlsIO

XlsIO provides support to read and write tables in a spreadsheet. The table is added as an `IListObject` to the worksheet. The input data to the table must be a range of data existing in the worksheet. `IListObject` returns the collection of tables in the worksheet.

[C#]

```csharp
// Create Table
IListObject table1 = sheet.ListObjects.Create("Table1", sheet["A1:C8"]);
```

[VB.NET]

```vb
' Create Table
Dim table1 As IListObject = sheet.ListObjects.Create("Table1", sheet("A1:C8"))
```

### Total Row

You can add the "Total Row" to any table by accessing the `Table Columns`. Columns in the tables are accessed by using the index. It is possible to set "Totals Calculation" to the Total Row cells by using the `ExcelTotalsCalculation` enumerator. These cells will be updated once they are calculated.

[C#]

```csharp
// Total Row
table1.Columns[0].TotalsRowLabel = "Total";
table1.Columns[1].TotalsCalculation = ExcelTotalsCalculation.Sum;
table1.Columns[2].TotalsCalculation = ExcelTotalsCalculation.Sum;
```
```html
<!-- tags: [xlsio, essential xlsio, tables, table creation, total row, winforms, syncfusion] keywords: [essentialxlsio, table, totalscalculation, listobject, excel, tables, total row, xlsio api, winforms controls] -->
```