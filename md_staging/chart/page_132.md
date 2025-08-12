```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_132.jpeg
document_name: chart
page_number: 132
page_id: chart#page_132
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:23:52Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
// Add the series to the chart series collection.
this.chartControl1.Series.Add(series);
```

```vbnet
[VB.NET]

' Create chart series and add data point into it.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.HiLoOpenClose)
' Arguments: X value, High, Low, Open, Close
series.Points.Add(0, 5, 1, 3, 4)
series.Points.Add(1, 8, 7, 4, 7)
series.Points.Add(2, 8, 4, 5, 6)

' Add the series to the chart series collection.
Me.chartControl1.Series.Add(series)
```

### Customization Options

| DisplayText | DrawSeriesNameInDepth | OpenCloseDrawMode | PhongAlpha | Rotate |
|-------------|-----------------------|-------------------|------------|--------|
| SpacingBetweenSeries | ShadingMode | FancyToolTip | Font | Interior |
| LegendItem | Name | PointsToolTipFormat | SmartLabels | Summary |
| Text | TextColor | TextFormat | TextOffset | TextOrientation |
| Visible |  |  |  |  |

### 4.4.7.4 Kagi Chart

Kagi Charts are a Japanese invention and date since the late 1870's, but were popularized in the western world by Steven Nison. They contain a series of connecting vertical lines where the thickness and direction of those lines depend on price. If closing prices continue to move in the direction of the prior vertical Kagi line, then that line is extended. However, if the closing price reverses by a pre-determined "reversal" amount, a new Kagi line is drawn in the next column in the opposite direction.

---

<!-- tags: [syncfusion, winforms, chart, kagi chart, version:11.4.0.26] keywords: [Essential Chart for Windows Forms, chart customization, HiLoOpenClose, Kagi Chart] -->
```