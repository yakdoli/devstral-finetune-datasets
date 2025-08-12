```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_169.jpeg
document_name: chart
page_number: 169
page_id: chart#page_169
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:25:55Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

```csharp
// 2) Another way to create a series
// This will automatically add the series to the chart
ChartSeries series = chartControl1.Model.NewSeries("Sales Performance", ChartSeriesType.Bar);
series.Points.Add(0, 200);
series.Points.Add(1, 300);
```

### [VB.NET]

```vb
' 1) One way to create a series:
Dim series1 As New ChartSeries("Sales Performance", ChartSeriesType.Bar)
series.Points.Add(0, 200)
series.Points.Add(1, 300)
' Remember to add the series to the chart.
Me.chartControl1.Series.Add(series)

' 2) Another way to create a series
' This will automatically add the series to the chart
ChartSeries series = Me.chartControl1.Model.NewSeries("Sales Performance", ChartSeriesType.Bar)
series.Points.Add(0, 200)
series.Points.Add(1, 300)
```

**Note:** Same ChartSeries object being added to more than one chart is not supported. It binds the series to the default primary axis always.

## Chart Points

The ChartPoint class holds value information about a single point in a series (x and y values). The following table describes the kind of x and y values you can specify via a chart point.

| Axis | Number of Values | Value Types |
|------|-------------------|-------------|
| X    | 1                | double or DateTime |
| Y    | 1 or more         | double or DateTime |

Here is some sample code that shows adding data points to the Points collection. You could also optionally create a ChartPoint instance first and then add it to the Points collection.
```