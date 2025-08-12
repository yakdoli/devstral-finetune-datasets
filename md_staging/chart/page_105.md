```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_105.jpeg
document_name: chart
page_number: 105
page_id: chart#page_105
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:21:59Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Adding Spline Area Series to the Chart

Spline area series can be added to the chart using the following code.

#### C#
```csharp
// Create a chart series and add data points into it.
ChartSeries series = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.SplineArea);
ChartSeries series = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Area);
series.Points.Add(0, 4.5);
series.Points.Add(1, 3);
series.Points.Add(2, 4);
series.Points.Add(3, 3);

// Add the series to the chart series collection.
this.chartControl1.Series.Add(series);
```

#### VB.NET
```vb
' Create a chart series and add data points into it.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.SplineArea)
ChartSeries series = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Area)
series.Points.Add(0, 4.5)
series.Points.Add(1, 3)
series.Points.Add(2, 4)
series.Points.Add(3, 3)

' Add the series to the chart series collection.
Me.chartControl1.Series.Add(series)
```

### Customization Options

The following customization options are available for the chart series:

- Border
- DisplayText
- DrawSeriesNameInDepth
- ElementBorders
- ImageIndex
- Rotate
- SeriesToolTipFormat
- Spacing Between Series
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

## Page-level Navigation/TOC (if applicable)

<!-- tags: [Syncfusion, WinForms, Chart, Spline Area Series, Customization Options, Series Properties] keywords: [chart series, spline area, data points, customization, chart control, series options, charting, Windows Forms] -->
```