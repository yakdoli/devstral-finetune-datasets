```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_092.jpeg
document_name: chart
page_number: 092
page_id: chart#page_092
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:21:35Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

```csharp
ChartSeriesType.Tornado);

series.Points.Add(1, 0, 48);
series.Points.Add(2, 0, 42);
series.Points.Add(3, 0, 27);
series.Points.Add(4, 0, 20);
series.Points.Add(5, 0, 9);

// Add the series to the chart series collection.
this.chartControl1.Series.Add(series);

ChartSeries series2 = this.chartControl1.Model.NewSeries("Series 1",
ChartSeriesType.Tornado);

series2.Points.Add(1, 0, -45);
series2.Points.Add(2, 0, -39);
series2.Points.Add(3, 0, -31);
series2.Points.Add(4, 0, -20);
series2.Points.Add(5, 0, -11);

this.chartControl1.Series.Add(series2);
```

### [VB.NET]

```vb
' Create chart series and add data points into it.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Series 0", ChartSeriesType.Tornado)

series.Points.Add(1, 0, 48)
series.Points.Add(2, 0, 42)
series.Points.Add(3, 0, 27)
series.Points.Add(4, 0, 20)
series.Points.Add(5, 0, 9)

' Add the series to the chart series collection.
Me.chartControl1.Series.Add(series)

' Create chart series and add data points into it.
Dim series2 As ChartSeries = Me.chartControl1.Model.NewSeries("Series 0", ChartSeriesType.Tornado)

series2.Points.Add(1, 0, -45)
series2.Points.Add(2, 0, -39)
series2.Points.Add(3, 0, -31)
series2.Points.Add(4, 0, -20)
series2.Points.Add(5, 0, -11)
```

## Page-level Navigation/TOC (if applicable)

<!-- tags: [chart, tornado chart, windows forms, syncfusion winforms, data visualization] keywords: [tornado chart, windows forms chart, essential chart, chart control, chart series, series type, data points, series collection, chart model, chart points, series1, series2, vb.net, csharp] -->
```