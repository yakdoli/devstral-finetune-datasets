```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_632.jpeg
document_name: chart
page_number: 632
page_id: chart#page_632
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:54:04Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Sales Volume Comparison

![](https://via.placeholder.com/600x400 "Saab")

![](https://via.placeholder.com/600x400 "Volvo")

**Figure 378: Chart with customized Color Palette**

### 5.15 How to specify the position for a Floating Legend

When the `LegendPosition` property of the `ChartControl` is set to `ChartDock.Floating`, the position of the legend defaults to the top-right corner of the `ChartArea`. Once this is done, you can specify the coordinates via the `Legend.Location` property of the `ChartLegend`.

#### Code Examples

**[C#]**

```csharp
this.chartControl1.LegendPosition = ChartDock.Floating;
this.chartControl1.Legend.Location = new Point(20, 20);
```

**[VB.NET]**

```vb
Me.ChartControl1.LegendPosition = ChartDock.Floating
Me.ChartControl1.Legend.Location = New Point(20, 20)
```

### See Also

- [Chart Legend](Chart Legend)

```html
<!-- tags: [essential chart, windows forms, floating legend, chartcontrol, legendposition, legend, chartarea, synfusion winforms, sales volume, comparison chart, color palette] keywords: [legendposition, floating legend, chartdock, chartarea, sales volume comparison, customized color palette, legend location, chartlegend, c#, vb.net] -->
``` 
```