```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_085.jpeg
document_name: XlsIO
page_number: 085
page_id: XlsIO#page_085
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:54:16Z
fidelity: lossless
-->

# Essential XlsIO

```csharp
// Open an existing Excel 2007 file. Note that you should select the ExcelOpenType when opening .xlsx files
IWorkbook workbook = excelEngine.Excel.Workbooks.Open("Excel2007.xlsx", ExcelOpenType.Automatic);

// The first worksheet object in the worksheets collection is accessed.
IWorksheet sheet = workbook.Worksheets[0];

// Write data
sheet.Range["C3:O28"].Text = "Hello world";

// Select the version to be saved
workbook.Version = ExcelVersion.Excel2007; // or
// workbook.Version = ExcelVersion.Excel2010;

// Save it as "Excel2007" format.
workbook.SaveAs("Sample.xlsx");
```

### [VB.NET]

```vb.net
' Open an existing Excel 2007 file. Note that you should select the ExcelOpenType when opening .xlsx files
Dim workbook As IWorkbook = excelEngine.Excel.Workbooks.Open("Excel2007.xlsx", ExcelOpenType.Automatic)

' Select the version to be saved.
workbook.Version = ExcelVersion.Excel2007 ' or
' workbook.Version = ExcelVersion.Excel2010

' The first worksheet object in the worksheets collection is accessed.
Dim sheet As IWorksheet = workbook.Worksheets(0)

' Write data
sheet.Range("C3:O28").Text = "Hello world"

' Save it as "Excel 2007" format.
workbook.SaveAs("Sample.xlsx")
```

**Note:** You can use the very same API to work with the xlsx file or any other older format.

You can also set the **default version** of the workbook when you want to work with the same format.

<!-- tags: [XlsIO, Excel, Workbook, Worksheet, Save, Format, Version] keywords: [Excel 2007, .xlsx, IWorkbook, IWorksheet, SaveAs, ExcelVersion, Workbook.Version, Worksheet.Range, xlsx] -->
```