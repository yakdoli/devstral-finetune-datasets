```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_213.jpeg
document_name: XlsIO
page_number: 213
page_id: XlsIO#page_213
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:02:46Z
fidelity: lossless
-->

# Essential XlsIO

## Content

### Formatting Data Series

```csharp
// Format Data Series.
IChartSerie chartAppleSerie = chart.Series["Apples"];

// Color of first serie.
chartAppleSerie.SerieFormat.AreaProperties.ForeColor = Color.Red;
chartAppleSerie = chart.Series["Oranges"];

// Color of second serie.
chartAppleSerie.SerieFormat.AreaProperties.ForeColor = Color.Orange;
chartAppleSerie = chart.Series["Grapes"];

// Color of third serie.
chartAppleSerie.SerieFormat.AreaProperties.ForeColor = Color.Purple;
chartAppleSerie = chart.Series["Banana"];

// Color of fourth serie.
chartAppleSerie.SerieFormat.AreaProperties.ForeColor = Color.Yellow;

// Embedded chart position.
chart.TopRow = 10;
chart.BottomRow = 40;
chart.LeftColumn = 5;
chart.RightColumn = 15;
```

### Creating a Clustered Column Chart in VB.NET

```vb
' Clustered Column Chart.
Dim chart As IChartShape = sheet.Charts.Add()

' Set Chart Type.
chart.ChartType = ExcelChartType.Column_Clustered

' Set Data Range.
chart.DataRange = sheet.Range("A1:E5")

' Specify Series.
chart.IsSeriesInRows = False

' Chart Title
chart.ChartTitle = "Sales comparison"

' X-axis title
chart.PrimaryCategoryAxis.Title = "Fruit Types"

' Y-axis title
```

## API Reference

### Methods/Properties
- `chart.Series[string seriesName]`: Accesses a specific data series by name.
- `SerieFormat.AreaProperties.ForeColor`: Sets the foreground color of the data series.
- `chart.TopRow`, `chart.BottomRow`, `chart.LeftColumn`, `chart.RightColumn`: Set the position and size of the embedded chart.
- `chart.ChartType`: Sets the type of the chart (e.g., Column_Clustered).
- `chart.DataRange`: Specifies the range of cells containing the data for the chart.
- `chart.IsSeriesInRows`: Determines whether the series are in rows or columns.
- `chart.ChartTitle`: Sets the title of the chart.
- `chart.PrimaryCategoryAxis.Title`: Sets the title of the primary axis.

## Code Examples

### C#

```csharp
// Sample code to format a chart and set its properties.
using System;
using System.Drawing;
using Syncfusion.XlsIO;

// Create a new Excel engine.
var excelEngine = new ExcelEngine();
IApplication application = excelEngine.Excel;
application.DefaultVersion = ExcelVersion.Xls2010;

// Add a new workbook and select the first worksheet.
IWorkbook workbook = application.Workbooks.Create(1);
IWorksheet worksheet = workbook.Worksheets[0];

// Add some sample data.
worksheet["A1"] = "Fruits";
worksheet["A2"] = "Apples";
worksheet["A3"] = "Oranges";
worksheet["A4"] = "Grapes";
worksheet["A5"] = "Banana";

worksheet["B1"] = "Sales";
worksheet["B2"] = 100;
worksheet["B3"] = 150;
worksheet["B4"] = 200;
worksheet["B5"] = 130;

// Insert a chart.
IChartShape chart = worksheet.Charts.Add(@7, @3, @20, @15);
chart.ChartType = ExcelChartType.Column_Clustered;
chart.DataRange = worksheet.Range["A1", "B5"];

// Format the chart.
chart.Series["Apples"].SerieFormat.AreaProperties.ForeColor = Color.Red;
chart.Series["Oranges"].SerieFormat.AreaProperties.ForeColor = Color.Orange;
chart.Series["Grapes"].SerieFormat.AreaProperties.ForeColor = Color.Purple;
chart.Series["Banana"].SerieFormat.AreaProperties.ForeColor = Color.Yellow;

chart.ChartTitle = "Sales comparison";
chart.PrimaryCategoryAxis.Title = "Fruit Types";

// Save the workbook and close the application.
workbook.SaveAs("ClusteredColumnChart.xlsx");
excelEngine.Dispose();
```

## Cross References

See also: [Getting Started with XlsIO](#getting-started), [Working with Charts](#charts)

<!-- tags: [xlsio, clustered column chart, chart formatting, winforms, syncfusion] keywords: [ChartShape, ExcelChartType, SerieFormat, AreaProperties] -->
```