```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_440.jpeg
document_name: chart
page_number: 440
page_id: chart#page_440
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:42:04Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

By default, a custom `ChartLegend` instance gets added to the `Legends` list in the control. You can access this default legend as follows.

```csharp
// Changing the position of the default legend
this.chartControl1.Legends[0].LegendPosition = Syncfusion.Windows.Forms.Chart.ChartDock.Top;
```

```vb.net
' Changing the position of the default legend
Me.chartControl1.Legends(0).LegendPosition = Syncfusion.Windows.Forms.Chart.ChartDock.Top
```

## Adding Custom Legends

You can add custom legends to the chart through the `Legends` list as follows:

```csharp
// Changing the position of the default legend
ChartLegend legend2 = new ChartLegend(chartControl1);
legend2.Name = "MyLegend";
chartControl1.Legends.Add(legend2);
```

```vb.net
Dim legend2 As New ChartLegend()
legend2.Name = "MyLegend"
chartControl1.Legends.Add(legend2)
```

You can then add custom legend items into the `ChartLegend` through the `CustomItems` property as explained in the next topic ([ChartLegendItem]).

You can also associate a `ChartSeries` to a custom `ChartLegend` as follows (then the legend item corresponding to that series will be rendered within the specified legend):

<!-- tags: [product, windows forms, chart, chartlegend, legdends, customitems, chartseries, chartdock] keywords: [chart, legend, windows forms, chartcontrol, custom legend, legend position, associating series, chartlegenditem] -->
```