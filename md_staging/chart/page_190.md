```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_190.jpeg
document_name: chart
page_number: 190
page_id: chart#page_190
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:26:49Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Content

The following code snippet demonstrates how to create a column chart with `RelativeWidthMode`. Here, the width of the bars is calculated relative to a uniform column width, specified as `Interval * 0.75`.

```vb
series.Points.Add(1, New Double() { 24, Interval * 0.75 })
series.Points.Add(2, New Double() { 36, Interval * 0.75 })
series.Points.Add(3, New Double() { 48, Interval * 0.75 })
Me.chartControl1.Series.Add(series)

Me.chartControl1.ColumnWidthMode = ChartColumnWidthMode.RelativeWidthMode
```

#### Example: Column Chart with RelativeWidthMode

Below is the column chart generated in the code snippet above. This example shows a bar chart titled "Daily Performance," illustrating the task completion percentages for `Team 1` across daily reviews.

```markdown
Figure 104: Column Chart with RelativeWidthMode

![Daily Performance Column Chart](https://example.com/daily-performance-column-chart.png)
```

### C#

The following code snippet demonstrates how to achieve the same functionality in C# using `FixedWidthMode`. The second Y value in each point specifies the width of the column explicitly.

```csharp
ChartSeries series1 = new ChartSeries("Series");
// 2nd Y value specifies the column width
series1.Points.Add(1, new double[] { 24, 25 });
series1.Points.Add(2, new double[] { 36, 25 });
series1.Points.Add(3, new double[] { 48, 25 });
chartControl1.Series.Add(series1);
chartControl1.ColumnWidthMode = ChartColumnWidthMode.FixedWidthMode;
```

### VB.NET

The corresponding VB.NET code snippet is as follows:

```vb
Dim series1 As ChartSeries = New ChartSeries("Series")
' 2nd Y value specifies the column width
series1.Points.Add(1, New Double() { 24, 25 })
series1.Points.Add(2, New Double() { 36, 25 })
series1.Points.Add(3, New Double() { 48, 25 })
chartControl1.Series.Add(series1)
chartControl1.ColumnWidthMode = ChartColumnWidthMode.FixedWidthMode
```

## API Reference

### Syncfusion.WinForms.Chart.Charts

- **ChartColumnWidthMode**: Enum for defining the column width mode of a column series.
  - **RelativeWidthMode**: Specifies that the column width is relative to a uniform column width.
  - **FixedWidthMode**: Specifies that the column width is explicitly defined by the second Y-value in each point.

### ChartSeries

- **Points.Add(int index, double[] point)**: Adds a point to the series at the specified index, with the second Y-value defining the column width.

## Cross References

See also:
- [Column Series](#column-series)
- [Customizing Column Widths](#customizing-column-widths)
- [ColumnChart](#columnchart)

<!-- tags: [winforms, charts, essential chart, column series, relative width mode, fixed width mode, vb.net, c#] -->
```