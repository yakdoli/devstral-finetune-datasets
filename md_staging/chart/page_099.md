```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_099.jpeg
document_name: chart
page_number: 099
page_id: chart#page_099
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:21:09Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
series2.Points.Add(2, 1);

// Add the series to the chart series collection.
this.chartControl1.Series.Add(series);
this.chartControl1.Series.Add(series2);
```

### [VB.NET]
```vb
' Create chart series and add data points into it.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.StackingColumn)
series.Points.Add(0, 1)
series.Points.Add(1, 3)
series.Points.Add(2, 4)

Dim series2 As ChartSeries = Me.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.StackingColumn)
series2.Points.Add(0, 2)
series2.Points.Add(1, 1)
series2.Points.Add(2, 1)

' Add the series to the chart series collection.
Me.chartControl1.Series.Add(series)
Me.chartControl1.Series.Add(series2)
```

## Customization Options

- Border, ColumnWidthMode, ColumnFixedWidth, DisplayShadow, DisplayText, DrawSeriesNameInDepth, ElementBorders, ImageIndex, Images, LightAngle, LightColor, Rotate, Spacing, Spacing Between Series, ShadingMode, ShadowInterior, ShadowOffset, ZOrder, FancyToolTip, Font, Interior, LegendItem, Name, PointsToolTipFormat, SmartLabels, Summary, Text, TextColor, TextFormat, TextOffset, TextOrientation, Visible

## See Also

- Stacking Area Chart, Stacking Bar Chart

### 4.4.3.4 Stacked Column100 Chart

This chart type displays multiple series of data as stacked Columns ensuring that the cumulative proportion of each stacked element always totals 100 percent. The y-axis will hence always be rendered with the range 0 - 100.
```