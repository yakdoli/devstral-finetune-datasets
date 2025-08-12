```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_090.jpeg
document_name: chart
page_number: 090
page_id: chart#page_090
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:20:40Z
fidelity: lossless
-->

---

### Essential Chart for Windows Forms

```csharp
[C#]

// Create chart series and add data points into it.
ChartSeries series = this.chartControl1.Model.NewSeries("System 1", ChartSeriesType.Histogram);
series.Text = series.Name;

series.Points.Add(3, 1020);
series.Points.Add(45, 440);
series.Points.Add(23, 605);

// Add the series to the chart series collection.
this.chartControl1.Series.Add(series);
```

```vbnet
[VB.NET]

' Create chart series and add data points into it.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("System 1", ChartSeriesType.Histogram)
series.Text = series.Name

series.Points.Add(3, 1000)
series.Points.Add(45, 1000)
series.Points.Add(23, 1000)

' Add the series to the chart series collection.
Me.chartControl1.Series.Add(series)
```

### Customization Options

- Border
- DisplayShadow
- DisplayText
- DrawHistogramNormalDistribution
- LightAngle
- LightColor
- NumberOfHistogramIntervals
- PhongAlpha
- Rotate
- Spacing Between Series
- ShadingMode
- ShadowInterior
- ShadowOffset
- ShowHistogramDataPoints
- FancyToolTip
- Font
- Interior
- LegendItem
- Name

---

<!-- tags: [Syncfusion Winforms, chart, Customization Options, Histogram, Series] keywords: [chart series, Histogram Normal Distribution, data points, ChartSeries, NumberOfHistogramIntervals, ShadingMode, DisplayText, ShadowInterior, ShadowOffset] -->
```