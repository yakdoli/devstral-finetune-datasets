```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_222.jpeg
document_name: XlsIO
page_number: 222
page_id: XlsIO#page_222
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:02:14Z
fidelity: lossless
-->

## XlsIO

### Overview
- Opening an existing worksheet from a workbook.
- Accessing and editing an existing chart.
- Modifying series names, chart title, axis titles, and legend position.
- Setting format properties for chart title text.
- Adjusting minimum and maximum values for the value axis.
- Setting dimensions for the chart (height and width).
- Saving the workbook to disk and closing it.

### Content

```csharp
[C#]

// Opening the Existing Worksheet from a Workbook.
IWorkbook workbook = 
application.Workbooks.Open(@"..\..\\..\\..\\Data\\EditChartsTemplate.xls");

// The first worksheet object in the worksheets collection is accessed.
IWorksheet sheet = workbook.Worksheets[0];

// Editing the Existing Chart.
IChart chart = sheet.Charts[0];
chart.ChartTitle = "Texas Books Unit Sales";
chart.PrimaryCategoryAxis.Title = "City";
chart.PrimaryValueAxis.Title = "Sales (in Dollars)";
chart.Legend.Position = ExcelLegendPosition.Top;

// Setting the Series Names in a Legend.
IChartSerie serieOne = chart.Series[0];
serieOne.Name = "Jan";
IChartSerie seriethree = chart.Series[1];
seriethree.Name = "Feb";
IChartSerie seriethree = chart.Series[2];
seriethree.Name = "March";

// Setting the Title Area text.
IChartTextArea Area = chart.ChartTitleArea;
Area.Bold = true;
Area.Underline = ExcelUnderline.Single;

// Setting the Minimum and Maximum Value for Value Axis.
chart.PrimaryValueAxis.MinimumValue = 10;
chart.PrimaryValueAxis.MaximumValue = 100;

// Setting the Height of the chart.
chart.Height = 1/10;

// Setting the Width of the chart.
chart.Width = 1/72;

// Saving the workbook to disk.
workbook.SaveAs("Sample.xls");

// Closing the workbook.
workbook.Close();
```

## API Reference
- **Namespace**: The namespace used in the code is not explicitly mentioned, but it refers to the `XlsIO` library.
- **Class**: `IWorkbook`, `IWorksheet`, `IChart`, `IChartSerie`, `IChartTextArea`.
- **Properties**:
  - `Workbook.Worksheets`
  - `Worksheet.Charts`
  - `Chart.ChartTitle`
  - `Chart.PrimaryCategoryAxis`
  - `Chart.PrimaryValueAxis`
  - `Chart.Legend`
  - `Chart.Series`
  - `Chart.ChartTitleArea`
  - `Chart.PrimaryValueAxis.MinimumValue`
  - `Chart.PrimaryValueAxis.MaximumValue`
  - `Chart.Height`
  - `Chart.Width`
  - `Workbook.SaveAs`
  - `Workbook.Close`

## Code Examples

The provided C# code demonstrates how to:
1. Open an existing workbook using the `Workbooks.Open` method.
2. Access the first worksheet in the workbook.
3. Modify the chart properties, such as title, axis titles, legend position, and series names.
4. Set formatting for the chart title text.
5. Adjust the axis minimum and maximum values.
6. Set the dimensions of the chart.
7. Save the workbook and close it.

## Page-level Navigation/TOC
- **Opening an Existing Workbook**.
- **Accessing Worksheets**.
- **Editing Charts**.
- **Setting Series Names**.
- **Formatting Chart Titles**.
- **Adjusting Axis Values**.
- **Setting Chart Dimensions**.
- **Saving and Closing Workbooks**.

## Cross References
- Related functionalities can be found in the XlsIO documentation, particularly in sections dealing with chart manipulation and workbook operations.

<!-- tags: [product, module, control, api, version?] keywords: [XlsIO, workbook, worksheet, chart, legend, axis, series, title, save, close] -->
```