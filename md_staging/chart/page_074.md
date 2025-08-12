```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_074.jpeg
document_name: chart
page_number: 074
page_id: chart#page_074
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:19:44Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
series.Points.Add(3, new double[] { 10, 8, 8 });
series.Points.Add(4, new double[] { 40, 10, 10 });

// Add the series to the chart series collection.
this.chartControl1.Series.Add(series);
```

```vb
' Create chart series and add data points into it.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Line)
series.Points.Add(1, new double[] { 20, 8, 8 })
series.Points.Add(2, new double[] { 70, 5, 5 })
series.Points.Add(3, new double[] { 10, 8, 8 })
series.Points.Add(4, new double[] { 40, 10, 10 })

' Add the series to the chart series collection.
Me.chartControl1.Series.Add(series)
```

### 4.4.1.2 Spline Chart

Spline Chart is similar to a Line Chart except that it connects the different data points using splines instead of straight lines.

When rendered in 3D, the plot looks like a ribbon and hence such types are also referred to as Ribbon or Strip Charts.

The appearance of the lines and the points can be configured with options such as the colors used, thickness of the lines and the symbols displayed.

The appearance of the lines and the points can be configured with options such as the colors used, thickness of the lines and the symbols displayed.


<!-- tags: [product, Windows Forms, Spline Chart, Ribbon Chart, Strip Chart, Syncfusion] keywords: [spline, chart, line chart, 3d, ribbon, strip, configuration, colors, thickness, symbols, points, data points, straight lines, splines, Windows Forms, Syncfusion] -->
```