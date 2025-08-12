```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_103.jpeg
document_name: chart
page_number: 103
page_id: chart#page_103
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:21:22Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Chart Series Creation

#### C#

```csharp
// Create a chart series and add data points into it.
ChartSeries series = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Area);
series.Points.Add(0, 4.5);
series.Points.Add(1, 3);
series.Points.Add(2, 4);
series.Points.Add(3, 3);

// Add the series to the chart series collection.
this.chartControl1.Series.Add(series);
```

#### VB.NET

```vb.net
' Create a chart series and add data points into it.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Area)
ChartSeries series = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Area)
series.Points.Add(0, 4.5)
series.Points.Add(1, 3)
series.Points.Add(2, 4)
series.Points.Add(3, 3)

' Add the series to the chart series collection.
Me.chartControl1.Series.Add(series)
```

### Customization Options

- Border, DisplayShadow, DisplayText, DrawSeriesNameInDepth, ElementBorders,
- HighlightInterior, ImageIndex, Rotate, SeriesToolTipFormat
- SpacingBetweenSeries, FancyToolTip, Font, Interior, LegendItem, Name, PointsToolTipFormat,
- SmartLabels,
- Summary, Text, TextColor, TextFormat, TextOffset, TextOrientation, Visible

### Spline Area Chart

**4.4.4.2 Spline Area Chart**

Spline Area Chart is similar to an Area Chart with the only difference being the way in which the points of a series are connected. It connects each series of points by a smooth spline curve. The area enclosed by the chart is filled with specified interior brush.
```