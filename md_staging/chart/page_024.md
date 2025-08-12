```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_024.jpeg
document_name: chart
page_number: 024
page_id: chart#page_024
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:17:05Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Creates a new ChartSeries and adds data points to it in both C# and VB.NET.
- Demonstrates setting the series type to a column chart.
- Explains how to add the series to the Chart control.

## Content

### Adding Data Points and Configuring the Chart in C#

```csharp
// Add points to the series.
// format (x, y)
series.Points.Add(1, 400);
series.Points.Add(2, 385);
series.Points.Add(3, 412);
series.Points.Add(4, 467);
series.Points.Add(5, 478);
series.Points.Add(6, 397);
series.Points.Add(7, 355);
series.Points.Add(8, 456);
series.Points.Add(9, 409);

// Set the type of Chart.
series.Type = ChartSeriesType.Column;

// Add the series to the Chart.
this.chartControl1.Series.Add(series);
```

### Adding Data Points and Configuring the Chart in VB.NET

```vb
Imports Syncfusion.Windows
Imports Syncfusion.Windows.Forms.Chart

' Create a new ChartSeries. The string specified is the name of the series.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Series")

' Set the Text property of the series. This will be used by the legend.
series.Text = series.Name

' Add points to the series.
series.Points.Add(1, 400)
series.Points.Add(2, 385)
series.Points.Add(3, 412)
series.Points.Add(4, 467)
series.Points.Add(5, 478)
series.Points.Add(6, 397)
series.Points.Add(7, 355)
series.Points.Add(8, 456)
series.Points.Add(9, 409)

' Set the type of Chart.
series.Type = ChartSeriesType.Column

' Add the series to the Chart.
Me.chartControl1.Series.Add(series)
```

## API Reference
- **ChartSeries**:
  - **Points**: Collection of data points used to plot the series.
  - **Type**: Specifies the type of chart to render (e.g., Column).
- **ChartControl**: Main control object that holds the chart.
  - **Series**: Collection to which ChartSeries objects are added.

<!-- tags: [Syncfusion, Essential Chart, WinForms, ChartSeries, ChartControl, Data Points, Column Chart] keywords: [adding series, configuring chart, WinForms integration, data visualization] -->
```