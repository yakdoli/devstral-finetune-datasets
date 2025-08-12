```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_137.jpeg
document_name: chart
page_number: 137
page_id: chart#page_137
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:23:56Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

```csharp
series.Points.Add (2, 4, 8);
series.ReversalAmount = 1.0;

// Add the series to the chart series collection.
this.chartControl1.Series.Add (series);
```

```vb
' Create chart series and add data points into it.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries ("Series Name", ChartSeriesType.PointAndFigure)
' Arguments: X value, low value, high value
series.Points.Add (0, 1, 5)
series.Points.Add (1, 3, 7)
series.Points.Add (2, 4, 8)
series.ReversalAmount = 1.0

' Add the series to the chart series collection.
Me.chartControl1.Series.Add (series)
```

### Customization Options

- DisplayShadow
- DisplayText
- DrawSeriesNameInDepth
- HeightBox
- PriceDownColor
- PriceUpColor
- ReversalAmount
- Spacing Between Series
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

### 4.4.7.6 Renko Chart

Renko charting method is thought to have acquired its name from "renga" which is the Japanese word for bricks. Renko Charts were introduced by Steve Nison. Renko (Bricks) are drawn equal in size for a determined amount. A brick is drawn in the direction of the prior move only if prices move by a minimum amount. If prices change by the determined amount or more, a new brick is drawn. If prices change by less than the determined amount (specified by **ReversalAmount**), the new price is ignored. The default value of **ReversalAmount** is 1.

If the new closing price penetrates the previous bricks closing price in the opposite direction, a trend reversal highlighted by the change in color of the bricks happens. Use the **PriceUpColor** to indicate bullish trend and **PriceDownColor** to indicate bearish trend.

---

<!-- tags: [Syncfusion Winforms, Essential Chart, Windows Forms, Renko Chart, Chart Series, Customization Options] keywords: [chart(points, add), chart(seriescollection, add), Renko, ReversalAmount, PriceUpColor, PriceDownColor, chartControl1] -->
```