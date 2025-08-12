```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_080.jpeg
document_name: chart
page_number: 080
page_id: chart#page_080
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:20:42Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
this.chartControl1.Series.Add(series);
```

### [VB.NET]
```vb.net
' Create chart series and add data points into it.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.StepLine)
series.Points.Add(0, 1)
series.Points.Add(1, 3)
series.Points.Add(2, 2)
series.Points.Add(3, 2)

' Add the series to the chart series collection.
Me.chartControl1.Series.Add(series)
```

### Customization Options
- DisplayShadow
- DisplayText
- DrawSeriesNameDepth
- ElementBorders
- HighlightInterior
- HitTestRadius
- ImageIndex
- Images
- Rotate
- Spacing Between Series
- ShadowInterior
- ShadowOffset
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

## 4.4.2 Bar Charts

Bar Charts are the simplest and most versatile of statistical diagrams. Displayed in horizontal bars, these charts are used to compare values across categories, for showing the variations in the value of an item over time.

A very similar, more common, chart type is the Column Charts where the bars are rendered vertically.

Essential Chart supports these different types of Bar Charts:

### 4.4.2.1 Bar Chart
