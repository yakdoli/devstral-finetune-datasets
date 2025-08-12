```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_098.jpeg
document_name: XlsIO
page_number: 098
page_id: XlsIO#page_098
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:54:04Z
fidelity: lossless
-->

## Code Examples

#### Using C#

```csharp
// Open an existing spreadsheet which will be used as a template for
// generating the new spreadsheet.
// After opening the spreadsheet, the workbook object represents the
// complete in-memory object model of the template spreadsheet.
IWorkbook workbook = application.Workbooks.Open("SpreadsheetFromTemplate.xls");

// The first worksheet object in the worksheets collection is accessed.
IWorksheet sheet = workbook.Worksheets[0];

// Inserting some additional data.
sheet.Range["A1"].Text = "New text that was not present in the template";

// Saving the workbook to disk. This spreadsheet is the result of opening
// an existing spreadsheet and then saving the result to a new workbook.
workbook.SaveAs("Sample.xls");

// Close the workbook.
Workbook.Close();

// Dispose the Excel engine
excelEngine.Dispose();
```

#### Using VB.NET

```vb
' New instance of XlsIO is created.[Equivalent to launching MS Excel with no
' workbooks open].
' The instantiation process consists of two steps.

' Step 1: Instantiate the spreadsheet creation engine.
Dim excelEngine As ExcelEngine = New ExcelEngine()

' Step 2: Instantiate the excel application object.
Dim application As IApplication = excelEngine.Excel

' Open an existing spreadsheet which, will be used as a template for
' generating the new spreadsheet.
' After opening the spreadsheet, the workbook object represents the complete
' in-memory object model of the template spreadsheet.
Dim workbook As IWorkbook = application.Workbooks.Open(".....\Data\SpreadsheetFromTemplate.xls")

' The first worksheet object in the worksheets collection is accessed.
Dim sheet As IWorksheet = workbook.Worksheets(0)
```

## RAG Annotations

<!-- tags: Syncfusion, WinForms, XlsIO, Spreadsheet Manipulation, Multiple Language Support keywords: open spreadsheet, modify spreadsheet, Excel engine disposal, workbook saving, VB.NET, C# -->
```