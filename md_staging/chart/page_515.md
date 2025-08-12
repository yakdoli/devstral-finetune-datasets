```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_515.jpeg
document_name: chart
page_number: 515
page_id: chart#page_515
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:45:10Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
this.chartControl1.PrimaryXAxis.DrawMinorGrid = true;
this.chartControl1.PrimaryXAxis.MinorGridLineType.DashStyle = DashStyle.DashDotDot;
this.chartControl1.PrimaryXAxis.MinorGridLineType.Width = 2;
this.chartControl1.PrimaryXAxis.MinorGridLineType.ForeColor = Color.Red;
chartControl1.PrimaryXAxis.SmallTicksPerInterval = 1;
```

### [VB.NET]

```vb
Me.chartControl1.PrimaryXAxis.DrawMinorGrid = True
Me.chartControl1.PrimaryXAxis.MinorGridLineType.DashStyle = DashStyle.DashDotDot
Me.chartControl1.PrimaryXAxis.MinorGridLineType.Width = 2
Me.chartControl1.PrimaryXAxis.MinorGridLineType.ForeColor = Color.Red
chartControl1.PrimaryXAxis.SmallTicksPerInterval = 1
```

**Note:** In the above code we have specified value for `SmallTicksPerInterval` property. No of minor grids lines depends on the value of this property of Chart Axis. Default value is 0; So, `MinorGridLines` will not appear in the chart by default. To see the minor grid lines in the chart, set `SmallTicksPerInterval` property to 1 or greater that 1.

![Figure 331](https://i.imgur.com/1Xr0s4j.png)

The preceding image illustrates custom minor grid lines on the x-axis.

---

<!-- tags: [syncfusion, windows-forms, chart, essential-chart, minor-grid-lines, x-axis, c#, vb.net] keywords: [syncfusion, windows forms, essential chart, minor grid lines, x-axis, small ticks per interval, dash style, red color, custom lines] -->
```