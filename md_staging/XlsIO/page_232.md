```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_232.jpeg
document_name: XlsIO
page_number: 232
page_id: XlsIO#page_232
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:04:56Z
fidelity: lossless
-->

### Sample Code

```csharp
// Set embedded chart positions
chart.TopRow = 2;
chart.BottomRow = 30;
chart.LeftColumn = 5;
chart.RightColumn = 18;
serieTwo.Name = "Temperature,deg.F";

// Set chart legends
chart.Legend.Position = ExcelLegendPosition.Right;
chart.Legend.IsVerticalLegend = false;

// Save the workbook
workbook.SaveAs("Sample.xlsx");
```

### VB.NET Sample Code

```vb
' Instantiate the spreadsheet creation engine
Dim excelEngine As New ExcelEngine()

' Create a new workbook (similar to creating a new workbook in Excel)
' Open a workbook including data
Dim workbook As IWorkbook = excelEngine.Excel.Workbooks.Open("EmbeddedChart.xlsx")

' The first worksheet object in the worksheet collection is accessed.
Dim sheet As IWorksheet = workbook.Worksheets(0)
sheet.Name = "Sample"
```

<!-- tags: [XlsIO, workbook, chart, embedded chart, VB.NET, saved as, sample code, document_name, embedded chart, document creation, chart legends, vertical legend, workbook open, worksheet name, worksheet object] keywords: [workbook, chart, embedded chart, VB.NET, SaveAs, sample code, document_name, embedded chart, document creation, chart legends, vertical legend, workbook open, worksheet name, worksheet object] -->
```