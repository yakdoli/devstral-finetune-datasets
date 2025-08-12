```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_211.jpeg
document_name: XlsIO
page_number: 211
page_id: XlsIO#page_211
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:01:58Z
fidelity: lossless
-->

# Essential XlsIO

## Overview
- APIs for creating an embedded chart in Essential XlsIO.
- Supports formatting and modifying chart areas, plot areas, and chart title areas using gradient, texture, patterns, and pictures.
- Utilizes `IChartShape` and `IChartSeries` interfaces for chart customization.
- Enables/disables Legends and Data Tables through `HasLegend` and `HasDataTable` properties.
- Allows resizing and positioning of embedded charts in a worksheet.

## Content

### Chart Creation
Charts in XlsIO can be created either:
- Through the Data Range of the chart.
- By adding series one by one.

#### Example: Creating a Chart Through Data Range in C#

```csharp
[C#]

// Clustered Column Chart.
IChartShape chart = sheet.Charts.Add();

// Set Chart Type.
chart.ChartType = ExcelChartType.Column_Clustered

// Set Data Range.
chart.DataRange = sheet.Range["A1:E5"];

// Specify Series
chart.IsSeriesInRows = false;

// Chart Title
chart.ChartTitle = "Sales comparison";

// X-axis title
chart.PrimaryCategoryAxis.Title = "Fruit Types";

// Y-axis title
chart.PrimaryValueAxis.Title = "Months";

// Show Data Table.
chart.HasDataTable = true;

// Format Chart Area.
IChartFrameFormat chartArea = chart.ChartArea;

// Border
```

### Chart Formatting and Customization
- Use `IChartShape` to represent the in-memory chart and modify its attributes.
- `IChartFrameFormat` is utilized to adjust the chart's overall format.
- `IChartSeries` helps in formatting the individual chart series.
- Provides options to enable or disable Legends (`HasLegend`) and Data Tables (`HasDataTable`).
- Allows resizing and repositioning of the embedded chart on a worksheet.

## API Reference

### Interfaces
- **IChartShape**
  - Represents the in-memory embedded chart.
  - Used for formatting and modifying chart settings such as chart area, plot area, and chart title area.

- **IChartFrameFormat**
  - Used to change the format of the chart.

- **IChartSeries**
  - Used to format series within the chart.

### Properties
- `HasLegend`: Enables/disables legends in the chart.
- `HasDataTable`: Enables/disables data tables in the chart.

### Methods
- `Add()`: Adds a new chart to the worksheet.
- `Set ChartType`: Sets the type of the chart (e.g., Clustered Column).
- `Set DataRange`: Sets the data range for the chart.

## Cross References
- For more information on using `IChartShape`, refer to the XlsIO API documentation.

<!-- tags: [syncfusion, xlsio, chart, customization, data range, formatting, api] keywords: [chart, embedded chart, IChartShape, IChartSeries, IChartFrameFormat, chart formatting, data range, series, legend, data table, worksheet] -->
```