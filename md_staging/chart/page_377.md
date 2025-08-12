<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_377.jpeg
document_name: chart
page_number: 377
page_id: chart#page_377
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:37:55Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Content

### Chart with Empty Points

#### Showing Empty Point without any gap between Data Points

It is possible to set some data point as empty point and still show the chart without any gap between the points. You need to set `AllowGapForEmptyPoints` property to `false` to enable this feature. By default, it is set to `true`.

![](https://via.placeholder.com/150x75?text=Figure-243:-Chart-with-Point1-as-Empty-Point)

Note: You need to set `ChartControl.Indexed` property to `true` for the above setting to be effective.

```csharp
this.chartControl1.Series[0].Points[3].IsEmpty = true;
this.chartControl1.Series[0].Points[4].IsEmpty = true;
this.chartControl1.Series[0].Points[5].IsEmpty = true;
```

```vb.net
Me.chartControl1.Series(0).Points(3).IsEmpty = True
Me.chartControl1.Series(0).Points(4).IsEmpty = True
Me.chartControl1.Series(0).Points(5).IsEmpty = True
```

## API Reference

### Properties

- `AllowGapForEmptyPoints`: Determines whether to show a gap for empty points. Default is `true`.

## Code Examples

The examples demonstrate how to configure empty points in a chart without gaps.

### C#

```csharp
using Syncfusion.Windows.Forms.Chart;

// Configure the chart
ChartControl chartControl1 = new ChartControl();
chartControl1.Series.Add(new ChartSeries());
chartControl1.Series[0].Points.Add(new ChartDataPoint(1992.5, 400));
chartControl1.Series[0].Points.Add(new ChartDataPoint(1995, 450));
chartControl1.Series[0].Points.Add(new ChartDataPoint(1997.5, 500));
chartControl1.Series[0].Points[3].IsEmpty = true;
chartControl1.Series[0].Points[4].IsEmpty = true;
chartControl1.Series[0].Points[5].IsEmpty = true;
chartControl1.AllowGapForEmptyPoints = false;
```

### VB.NET

```vb.net
Imports Syncfusion.Windows.Forms.Chart

' Configure the chart
Dim chartControl1 As New ChartControl()
chartControl1.Series.Add(New ChartSeries())
chartControl1.Series(0).Points.Add(New ChartDataPoint(1992.5, 400))
chartControl1.Series(0).Points.Add(New ChartDataPoint(1995, 450))
chartControl1.Series(0).Points.Add(New ChartDataPoint(1997.5, 500))
chartControl1.Series(0).Points(3).IsEmpty = True
chartControl1.Series(0).Points(4).IsEmpty = True
chartControl1.Series(0).Points(5).IsEmpty = True
chartControl1.AllowGapForEmptyPoints = False
```

## Cross References

See also: [Chart Series Properties](#chart-series-properties), [Data Point Customization](#data-point-customization)

<!-- tags: [syncfusion, winforms, chart, empty points, data points, api reference] keywords: [essential chart, windows forms, empty points, gaps, indexed property, allowgapforemptypoints, csharp, vb.net] -->