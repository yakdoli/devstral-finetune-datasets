```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_154.jpeg
document_name: chart
page_number: 154
page_id: chart#page_154
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:24:20Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- This page provides details on creating a chart that displays both a line chart and a column chart using the Syncfusion Windows Forms Chart control.
- It includes a breakdown of the chart details and code samples for both C# and VB.NET to demonstrate how to add combination series.

## Content

### Chart Details

The following table describes the key details about the chart configuration:

| Details                | Description                                   |
|-------------------------|-----------------------------------------------|
| **Number of Series**   | One or more.                                  |
| **Cannot be Combined with** | Pie, Bar, Polar, Radar.                    |

#### Addition of Combination Series

Combination series can be added to the chart using the following code snippets:

##### C#

```csharp
ChartSeries series = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Line);
series.Points.Add(0, 2);
series.Points.Add(1, 1);
series.Points.Add(2, 1);

// Create chart series and add data points into it.
ChartSeries series2 = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Column);
series2.Points.Add(0, 1);
series2.Points.Add(1, 3);
series2.Points.Add(2, 4);

// Add the series to the chart series collection.
this.chartControl1.Series.Add(series);
this.chartControl1.Series.Add(series2);
```

##### VB.NET

```vb
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Line)
series.Points.Add(0, 2)
series.Points.Add(1, 1)
series.Points.Add(2, 1)

' Create chart series and add data points into it.
Dim series2 As ChartSeries = Me.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Column)
series2.Points.Add(0, 1)
series2.Points.Add(1, 3)
```

## API Reference

The following methods and properties are used to create and configure the chart:
- `ChartControl.Model.NewSeries(name As String, chartType As ChartSeriesType)`
- `ChartSeries.Points.Add(x As Double, y As Double)`
- `ChartControl.Series.Add(series As ChartSeries)`

## Code Examples

The above code examples demonstrate how to:
1. Create two chart series: one for a line chart and one for a column chart.
2. Add data points to each series.
3. Add the series to the chart's collection.

## Cross References
See also:
- Chart Series in Syncfusion Windows Forms Documentation
- Chart Controls in Syncfusion Windows Forms

<!-- tags: [syncfusion, windowsforms, chart] keywords: [combination series, line chart, column chart, code samples, C#, VB.NET] -->
```