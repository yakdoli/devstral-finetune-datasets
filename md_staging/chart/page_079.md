```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_079.jpeg
document_name: chart
page_number: 079
page_id: chart#page_079
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:20:02Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates how to create a chart with Step Line series.
- Explains the details and properties of Step Line series.
- Provides code examples to add Step Line series to a chart.

## Content

### Chart Details

The image shows a 3D bar chart labeled "Daily Server Load," with two series: "Server 1" and "Server 2," represented by orange and blue bars, respectively. The legend is shown at the top, and the chart axis labels are as follows:
- Y-axis: "Server Load (MB)" ranging from 0 to 500.
- X-axis: Values ranging from 0 to 80.

#### Figure 45: Chart displaying Step Line Series

The chart details are summarized in the following table:

| Details                   |                                                                 |
|---------------------------|-----------------------------------------------------------------|
| Number of Y values per point | 1                                                             |
| Number of Series           | One or More                                                   |
| Cannot be Combined with    | Pie, Bar, Stacked Bar, Polar, Radar.                         |

### Step Line Series

Step Line series can be added to the chart using the following code:

```csharp
// Create chart series and add data points into it.
ChartSeries series = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.StepLine);
series.Points.Add(0, 1);
series.Points.Add(1, 3);
series.Points.Add(2, 2);
series.Points.Add(3, 2);

// Add the series to the chart series collection.
```

This code snippet demonstrates how to create a new series of type `StepLine`, add data points, and then add the series to the chart's collection.

## API Reference (if applicable)
- Namespace: Not directly shown in the image, refer to Syncfusion documentation for complete namespace information.
- Members: `ChartSeries`, `Points`, `NewSeries`, `Model`.
- Parameters include `Series Name` and `ChartSeriesType`, indicating the type of series being added.

## Code Examples (multi-language supported)
The provided code example is in C#. It shows the creation and configuration of a Step Line series, adding data points, and integrating the series into a chart object.

```csharp
// Example: Adding a Step Line series to a chart.
ChartSeries series = this.chartControl1.Model.NewSeries("StepLineSeries", ChartSeriesType.StepLine);
series.Points.Add(0, 1);  // Example data point
series.Points.Add(1, 3);
series.Points.Add(2, 2);
series.Points.Add(3, 2);
```

### Cross References
- See also: Documentation for `ChartSeries`, `Points`, and `Model` classes in the Syncfusion documentation for additional properties and methods related to chart construction and customization.

## RAG Annotations
<!-- tags: [Syncfusion, WinForms, Chart, StepLineSeries, DailyServerLoad] keywords: [chart, series, StepLine, load, server, data points, API] -->
```