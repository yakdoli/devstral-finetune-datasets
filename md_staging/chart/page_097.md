```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_097.jpeg
document_name: chart
page_number: 097
page_id: chart#page_097
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:21:31Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Code Example

```vb
Dim series As ChartSeries = Me.ChartControl1.Model.NewSeries("Series 0", ChartSeriesType.ColumnRange)
series.Points.Add(0, 100, 400)
series.Points.Add(2, 300, 600)
series.Points.Add(4, 200, 700)
series.Text = series.Name

' Add the series to the chart series collection.
Me.ChartControl1.Series.Add(series)
```

### Customization Options
- Border
- ColumnDrawMode
- ColumnWidthMode
- ColumnFixedWidth
- DisplayText
- DrawSeriesNameInDepth
- ElementBorders
- ImageIndex
- Images
- LightAngle
- LightColor
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

### 4.4.3.3 Stacking Column Chart

Stacking Column Charts are similar to regular column charts except that the y values stack on top of each other in the specified series order. This helps visualize the relationship of parts to the whole.

The following image shows a sample Stacking Column Chart.

<!-- tags: [Syncfusion Winforms, Chart, Stacking Column Chart, Customization Options, Series, ChartSeriesType] keywords: [Chart, Stacking Column Chart, Customization Options, ChartSeries, Series, Stacking, Column] -->
```