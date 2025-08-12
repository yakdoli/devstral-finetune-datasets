```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_082.jpeg
document_name: chart
page_number: 082
page_id: chart#page_082
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:20:09Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

Bar series can be added to the chart using the following code.

## Adding Bar Series to the Chart

```csharp
// Create chart series and add data points into it.
ChartSeries series = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Bar);
series.Points.Add(0, 1);
series.Points.Add(1, 3);
series.Points.Add(2, 4);

// Add the series to the chart series collection.
this.chartControl1.Series.Add(series);
```

```vb.net
' Create chart series and add data point into it.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Bar)
series.Points.Add(0, 1)
series.Points.Add(1, 3)
series.Points.Add(2, 4)

' Add the series to the chart series collection.
Me.chartControl1.Series.Add(series)
```

## Customization Options

- Border
- ColumnDrawMode
- DisplayShadow
- DisplayText
- DrawSeriesNameInDepth
- ElementBorders
- HighlightInterior
- ImageIndex
- Images
- LightAngle
- LightColor
- PhongAlpha
- Rotate
- Spacing
- Spacing Between Series
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

## See Also

- Column Chart

---

<!-- tags: [chart, bar series, customization options, essential chart for windows forms, syncfusion winforms] keywords: [create chart series, add data points, add series to collection, column draw mode, display shadow, display text, element borders, highlight interior, image index, light angle, light color, phong alpha, rotate, shading mode, shadow interior, shadow offset, tooltip, smart labels, summary, text color, text format, text offset, text orientation, visibility] -->
```