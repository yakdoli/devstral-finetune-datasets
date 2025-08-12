```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_230.jpeg
document_name: XlsIO
page_number: 230
page_id: XlsIO#page_230
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:02:53Z
fidelity: lossless
-->

## Content

```csharp
ExcelEngine excelEngine = new ExcelEngine();

// Create a new workbook (similar to creating a new workbook in Excel)
// Open a workbook including data
IWorkbook workbook =
excelEngine.Excel.Workbooks.Open(@"EmbeddedChart.xlsx");

// The first worksheet object in the worksheet collection is accessed.
IWorksheet sheet = workbook.Worksheets[0];
sheet.Name = "Sample";

// Add a new chart to the existing worksheet
IChartShape chart = workbook.Worksheets[0].Charts[0];

// Set chart series
IChartSerie serieOne = chart.Series[0];
IChartSerie serieTwo = chart.Series[1];

// Set fill type of chart back wall
chart.BackWall.Fill.FillType = ExcelFillType.Gradient;

// Set fill options for the back wall
chart.BackWall.Fill.GradientColorType =
ExcelGradientColor.TwoColor;
chart.BackWall.Fill.GradientStyle =
ExcelGradientStyle.Diagonal_Down;

// Set the foreground and background color of the back wall
chart.BackWall.Fill.ForeColor =
System.Drawing.Color.WhiteSmoke;
chart.BackWall.Fill.BackColor =
System.Drawing.Color.LightBlue;

// Set the border line color of the back wall
```
