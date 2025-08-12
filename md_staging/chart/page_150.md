```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_150.jpeg
document_name: chart
page_number: 150
page_id: chart#page_150
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:24:05Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Polar series can be added to the chart using code examples in C# and VB.NET.
- Number of Y values per point is 1.
- Only one series is allowed in the chart.
- Cannot be combined with any other chart types.

## Content

### Polar Series Details

| Data Point Details         | Value                   |
|----------------------------|--------------------------|
| Number of Y values per point | 1.                      |
| Number of Series            | One.                    |
| Cannot be Combined with     | Any other chart types. |

### Adding Polar Series to the Chart

#### C#

```csharp
// Create chart series and add data points into it.
ChartSeries series = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Polar);
series.Points.Add(0, 1);
series.Points.Add(1, 3);
series.Points.Add(2, 4);

// Add the series to the chart series collection.
this.chartControl1.Series.Add(series);
```

#### VB.NET

```vb
' Create chart series and add data points into it.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Polar)
series.Points.Add(0, 1)
series.Points.Add(1, 3)
series.Points.Add(2, 4)

' Add the series to the chart series collection.
Me.chartControl1.Series.Add(series)
```

### Customization Options

- Border
- DisplayText
- DrawSeriesNameInDepth
- ElementBorders
- ImageIndex
- Images
- LightAngle
- LightColor
- Radar Type
- Rotate
- ShadingMode
- ShadowInterior
- ShadowOffset
- FancyToolTip
- Font
- Interior
- LegendItem
- Name
- PointsToolTipFormat
- SmartLabels
- Summary
- Text
- TextColor
- TextFormat
- TextOffset
- TextOrientation
- Visible

### Page-level Metadata

- Copyright: © 2013 Syncfusion. All rights reserved.
- Page: 150

<!-- tags: [chart, Polar series, Windows Forms, C#, VB.NET, customization options, Syncfusion Winforms, 11.4.0.26] keywords: [chart series, data points, Polar chart, series addition, customization, light angle, light color, font settings, text formatting, text orientation] -->
```