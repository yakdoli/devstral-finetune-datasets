```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_130.jpeg
document_name: chart
page_number: 130
page_id: chart#page_130
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:22:57Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

| Cannot be Combined with                                      |
|--------------------------------------------------------------|
| Pie, Bar, Stacked Bar charts, Polar, Radar                   |

Hi Lo series can be added to the chart using the following code.

## Content

```csharp
[C#]

// Create chart series and add data points into it.
ChartSeries series = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.HiLo);
series.Points.Add(0, 1, 3);
series.Points.Add(1, 3, 4);
series.Points.Add(2, 4, 8);

// Add the series to the chart series collection.
this.chartControl1.Series.Add(series);
```

```vbnet
[VB.NET]

' Create chart series and add data points into it.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.HiLo)
series.Points.Add(0, 1, 3)
series.Points.Add(1, 3, 4)
series.Points.Add(2, 4, 8)

' Add the series to the chart series collection.
Me.chartControl1.Series.Add(series)
```

### Customization Options

- DisplayText
- DrawErrorBars
- DrawSeriesNameInDepth
- ErrorBarsSymbolShape
- PhongAlpha
- Rotate
- Spacing Between Series
- ShadingMode
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

## 4.4.7.3 Hi Lo Open Close Chart

Hi Lo Open Close Chart is a special kind of chart that is normally used in stock analysis. This chart type expects four y values for every point in the series. Those values should represent the High, Low, Open and Close values of the stock, in that order, for that period.

<!-- tags: [Essential Chart, Windows Forms, Chart Series, Hi Lo, Hi Lo Open Close Chart, C#, VB.NET, Syncfusion] keywords: [Essential Chart, Windows Forms, Chart Series, Hi Lo, Hi Lo Open Close Chart] -->
```