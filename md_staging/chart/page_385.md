```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_385.jpeg
document_name: chart
page_number: 385
page_id: chart#page_385
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:38:28Z
fidelity: lossless
-->

## Content

### [C#]

```csharp
// Create a new instance of the chart axis.
private ChartAxis secXAxis = new ChartAxis();

// Add the secondary axis to the chart axis collection.
this.chartControl1.Axes.Add(this.secXAxis);

// Specify this axis to be the axis for an existing series
this.chartControl1.Series[1].XAxis = this.secXAxis;
```

### [VB.NET]

```vb
' Create a new instance of the chart axis.
Private secXAxis As ChartAxis = New ChartAxis()

' Add the secondary axis to the chart axis collection.
Me.chartControl1.Axes.Add(Me.secXAxis)

' Specify this axis to be the axis for an existing series
Me.chartControl1.Series(1).XAxis = Me.secXAxis
```

#### Figure 250: ChartControl with a 2nd X-Axis (-2 to 8) stacked below the Primary X-Axis

![](https://i.imgur.com/figure_250_image_link.png)

**Opposed Position**

---

## Page-level Navigation/TOC (if applicable)

- Overview
  - Essential Chart for Windows Forms
- Content
  - [C#]
  - [VB.NET]
  - Figure 250: ChartControl with a 2nd X-Axis (-2 to 8) stacked below the Primary X-Axis
  - Opposed Position

<!-- tags: [syncfusion, winforms, chartcontrol, axis, secondaryaxis, csharp, vb.net] keywords: [chartaxis, syncfusion winforms, secondary axis, chart, figure, axis collection, series, x-axis, opposed position] -->
```