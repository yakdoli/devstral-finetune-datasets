<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_107.jpeg
document_name: chart
page_number: 107
page_id: chart#page_107
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:21:35Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates how to create and customize chart series using Syncfusion WinForms controls.
- Includes code examples in C# and VB.NET for adding data points and series to a chart.

## Content

### Chart Series Example

#### C#
```csharp
// Create chart series and add data points into it.
ChartSeries series = this.chartControl1.Model.NewSeries("Series
Name", ChartSeriesType.StackingArea);
series.Points.Add(0, 1);
series.Points.Add(1, 3);
series.Points.Add(2, 4);

ChartSeries series2 = this.chartControl1.Model.NewSeries("Series
Name", ChartSeriesType.StackingArea);
series2.Points.Add(0, 2);
series2.Points.Add(1, 1);
series2.Points.Add(2, 1);

// Add the series to the chart series collection.
this.chartControl1.Series.Add(series);
this.chartControl1.Series.Add(series2);
```

#### VB.NET
```vb.net
' Create chart series and add data points into it.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Series
Name", ChartSeriesType.StackingArea)
series.Points.Add(0, 1)
series.Points.Add(1, 3)
series.Points.Add(2, 4)

Dim series2 As ChartSeries = Me.chartControl1.Model.NewSeries("Series
Name", ChartSeriesType.StackingArea)
series2.Points.Add(0, 2)
series2.Points.Add(1, 1)
series2.Points.Add(2, 1)

' Add the series to the chart series collection.
Me.chartControl1.Series.Add(series)
Me.chartControl1.Series.Add(series2)
```

### Customization Options
- Border
- DisplayText
- DrawSeriesNameInDepth
- ElementBorders
- HighlightInterior
- ImageIndex
- Rotate
- SeriesToolTipFormat
- Spacing Between Series
- ZOrder
- FancyToolTip
- Font
- Interior
- LegendItem
- Name
- PointsToolTipFormat
- SmartLabels

## Page-level Navigation/TOC (if applicable)
- None

## Cross References
- None

<!-- tags: [chart, windows forms, series, data points, customization, C#, VB.NET] keywords: [chart series, data points, chartControl, NewSeries, StackingArea, customization options] -->