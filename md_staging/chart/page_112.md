```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_112.jpeg
document_name: chart
page_number: 112
page_id: chart#page_112
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:22:46Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Content

### Customization Options
- Border
- DisplayText
- DrawSeriesNameInDepth
- ElementBorders
- ImageIndex
- Rotate
- SeriesToolTipFormat
- Spacing Between Series
- Stepltem.Inverted
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

### 4.4.4.6 Range Area Chart

RangeArea chart is similar to the Area charts; the only difference is, we need to give two y values (Start & End). RangeArea chart will be rendered from the start value of the x axis (Lower bounds) to the end value of the y axis (upper bounds) above, on the corresponding x axis values.

This chart type gives a clear look and it may be used in cases where we have to display a range of values, per single x point. For example: if we have to display the range of temperature per day in a chart, RangeArea Chart will be the most convenient type of chart.

## API Reference

### Code Examples

```csharp
this.chartControl1.Series.Add(series);
```

```vb
' Create chart series and add data points into it.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.StepArea)
series.Points.Add(0, 1)
series.Points.Add(1, 3)
series.Points.Add(2, 4)
series.Points.Add(3, 2)
series.Points.Add(4, 3)

' Add the series to the chart series collection.
Me.chartControl1.Series.Add(series)
```

```markdown
## References
- [Document Link](#chart#page_112)
```

<!-- tags: [syncfusion-sdk, windows-forms, charts, range-area-chart, customization-options] keywords: [Render from start value, end value, x axis, y axis, temperature per day, clear look, convenient chart type] -->
```