```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_206.jpeg
document_name: chart
page_number: 206
page_id: chart#page_206
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:27:39Z
fidelity: lossless
-->

## Error Bars

### DrawErrorBars

**Error Bars** are used to indicate a degree of uncertainty in the plotted data through a bar indicating an "error range".

The 2nd y value is used to indicate the error range. For example, a value of 5 indicates an error range of -5 to +5 from the specified y value.

| **Details**          |                                                                                     |
|----------------------|-------------------------------------------------------------------------------------|
| **Possible Values**  | True or False                                                                      |
| **Default Value**    | False                                                                              |
| **2D / 3D Limitations** | No                                                                               |
| **Applies to Chart Element** | All series                                                                 |
| **Applies to Chart Types** | Column Chart, Line Chart and HiLo Chart                                         |

Here is some sample code.

```csharp
// Generating Series
ChartSeries series = this.chartControl1.Model.NewSeries("Sales", ChartSeriesType.Column);
// 2nd Y value indicates the error range
series.Points.Add(1, new double[] { 20, 5 });
series.Points.Add(2, new double[] { 70, 6 });
series.Points.Add(3, new double[] { 10, 3 });
series.Points.Add(4, new double[] { 40, 6 });
series.Text = series.Name;
// Adding Series to the Chart
this.chartControl1.Series.Add(series);
// Specifies the Error Bar in Column chart.
this.chartControl1.Series[0].DrawErrorBars = true;
```

```vb.net
' Generating Series
series As ChartSeries = Me.chartControl1.Model.NewSeries("Sales", ChartSeriesType.Column)
' 2nd Y value indicates the error range
```

<!-- tags: [Syncfusion, Winforms, Error Bars, Chart, Column Chart, Line Chart, HiLo Chart] keywords: [DrawErrorBars, error range, chart, data uncertainty, 2nd Y value, sample code] -->
```