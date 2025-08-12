```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_219.jpeg
document_name: XlsIO
page_number: 219
page_id: XlsIO#page_219
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:02:36Z
fidelity: lossless
-->

# The IChart Interface in XlsIO

## Overview
- The `IChart` interface represents the in-memory representation of the Chart Worksheet in an Excel workbook.
- Formatting is similar to the one discussed in the `Embedded Chart` section.
- Demonstrates how to enter data for a chart, add a chart to an existing worksheet, and set series names in a legend.

## Content

### Chart Data Entry and Formatting

#### Code Example: Entering Data and Formatting for a Chart
```csharp
[C#]

// Entering the Data for the chart.
sheet.Range["A1"].Text = "Texas books Unit sales";
sheet.Range["A1:D1"].Merge();
sheet.Range["A1"].CellStyle.Font.Bold = true;

sheet.Range["B2"].Text = "Jan";
sheet.Range["C2"].Text = "Feb";
sheet.Range["D2"].Text = "Mar";

sheet.Range["A3"].Text = "Austin";
sheet.Range["A4"].Text = "Dallas";
sheet.Range["A5"].Text = "Houston";
sheet.Range["A6"].Text = "San Antonio";

sheet.Range["B3"].Number = 53.75;
sheet.Range["B4"].Number = 52.85;
sheet.Range["B5"].Number = 59.77;
sheet.Range["B6"].Number = 96.15;

sheet.Range["C3"].Number = 79.79;
sheet.Range["C4"].Number = 59.22;
sheet.Range["C5"].Number = 10.09;
sheet.Range["C6"].Number = 73.02;

sheet.Range["D3"].Number = 26.72;
sheet.Range["D4"].Number = 33.71;
sheet.Range["D5"].Number = 45.81;
sheet.Range["D6"].Number = 12.17;

// Adding a New chart to the Existing Worksheet.
IChart chart = workbook.Charts.Add();
chart.DataRange = sheet.Range["B3:D6"];
chart.Name = "ChartWorksheet";
chart.PrimaryCategoryAxis.Title = "City";
chart.PrimaryValueAxis.Title = "Sales (in Dollars)";
chart.ChartTitle = "Texas Books Unit Sales";

// Setting the Series Names in a Legend.
IChartSerie serieOne = chart.Series[0];
serieOne.Name = "Jan";
```

### Explanation
- **Data Entry**: The data for the chart is entered into specific cells of the worksheet, including city names and sales figures for January, February, and March.
- **Formatting**: The title of the chart is merged across columns and formatted as bold.
- **Chart Creation**: A new chart is added to the worksheet, and its data range is set to the cells containing the sales data.
- **Axis Titles**: Primary category and value axes are labeled appropriately for clarity.
- **Legend Series**: The series name for the first data series is set to "Jan".

## API Reference

### Namespaces and Classes
- **`IChart`**: Represents the in-memory representation of the Chart Worksheet.
- **`IChartSerie`**: Represents a series in the chart.

### Methods and Properties
- **`IChart.Add()`**: Adds a new chart to the workbook.
- **`IChart.DataRange`**: Sets the range of cells containing the data for the chart.
- **`IChart.Name`**: Sets the name of the chart.
- **`IChart.PrimaryCategoryAxis.Title`**: Sets the title of the primary category axis.
- **`IChart.PrimaryValueAxis.Title`**: Sets the title of the primary value axis.
- **`IChart.ChartTitle`**: Sets the title of the chart.
- **`IChartSeries.Name`**: Sets the name of a series in the legend.

## Code Examples

The provided code example demonstrates how to:
1. Enter data into the worksheet.
2. Add a chart to the worksheet.
3. Format the chart by setting titles and data ranges.
4. Set series names in the legend.

<!-- tags: [XlsIO, IChart, Chart, Worksheet, DataEntry, ChartFormatting, SeriesNames] keywords: [Excel, Workbook, Worksheet, Chart, DataRange, AxisTitle, Legend] -->
```