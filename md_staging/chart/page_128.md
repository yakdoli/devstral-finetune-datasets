```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_128.jpeg
document_name: chart
page_number: 128
page_id: chart#page_128
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:23:38Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Details on how to add Candle series to a chart using both C# and VB.NET.
- Highlighted customization options available for Candle series.

## Content

### Chart Series Table
| Number of Series | Cannot be Combined with |
|-------------------|--------------------------|
| One or More.     | Pie, Bar, Stacked Bar charts, Polar, Radar. |

### Adding Candle Series

Candle series can be added to the chart using the following code.

#### [C#]
```csharp
// Create chart series and add data point into it.
ChartSeries series = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Candle);
// Arguments: X value, High, Low, Open, Close
series.Points.Add(0, 5, 1, 3, 4);
series.Points.Add(1, 8, 7, 4, 7);
series.Points.Add(2, 8, 4, 5, 6);

// Add the series to the chart series collection.
this.chartControl1.Series.Add(series);
```

#### [VB.NET]
```vb.net
' Create chart series and add data point into it.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Candle)
' Arguments: X value, High, Low, Open, Close
series.Points.Add(0, 5, 1, 3, 4)
series.Points.Add(1, 8, 7, 4, 7)
series.Points.Add(2, 8, 4, 5, 6)

' Add the series to the chart series collection.
Me.chartControl1.Series.Add(series)
```

### Customization Options
- Border, DisplayShadow, DisplayText, DrawSeriesNameInDepth, ImageIndex, Images,
- PhongAlpha, Rotate, Spacing Between Series
- ShadingMode, ShadowInterior, ShadowOffset, FancyToolTip, Font, Interior, LegendItem, Name,
- PointsToolTipFormat, SmartLabels,
- Summary, Text, TextColor, TextFormat, TextOffset, TextOrientation, Visible

## Page-level Navigation/TOC (if applicable)
None

## Cross References
None

<!-- tags: [product, module, control, api, version?] keywords: [chart, windows forms, candle series, customization options, essential chart, Syncfusion] -->
```