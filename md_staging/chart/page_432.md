```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_432.jpeg
document_name: chart
page_number: 432
page_id: chart#page_432
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:41:32Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates how to customize the location of the primary axes for better visibility and interpretation in a 3D chart.
- Provides code examples in C# and VB to set the X and Y axis crossings and activate 3D series.

## Content

### Sample Code

#### C#
```csharp
this.chartControl1.PrimaryXAxis.Crossing = 150;
this.chartControl1.PrimaryYAxis.Crossing = 6;
this.chartControl1.Series3D = true;
```

#### VB
```vb
Me.chartControl1.PrimaryXAxis.Crossing = 150
Me.chartControl1.PrimaryYAxis.Crossing = 6
Me.chartControl1.Series3D = True
```

### Resulting Chart

![Primary axes location customized](https://example.com/crossing_demo.png)
*Figure 278: Primary axes location customized*

#### Description
The figure shows a 3D chart with customized axis crossings. The X-axis is crossed at 150, and the Y-axis is crossed at 6. The Series3D feature is enabled, enhancing the chart's depth and visual appeal.

### Axis Label Placement

#### Overview
This feature allows you to specify the position of the label for an axis. You can place the label either inside or outside the plotted chart area.

---

## API Reference

### Methods/Properties

- `PrimaryXAxis.Crossing`: Sets the position where the X-axis crosses the Y-axis.
- `PrimaryYAxis.Crossing`: Sets the position where the Y-axis crosses the X-axis.
- `Series3D`: Activates or deactivates the 3D rendering of the chart series.

## Code Examples

### C#
```csharp
this.chartControl1.PrimaryXAxis.Crossing = 150;
this.chartControl1.PrimaryYAxis.Crossing = 6;
this.chartControl1.Series3D = true;
```

### VB
```vb
Me.chartControl1.PrimaryXAxis.Crossing = 150
Me.chartControl1.PrimaryYAxis.Crossing = 6
Me.chartControl1.Series3D = True
```

## Page-level Navigation/TOC
- [4.6.16 Axis Label Placement](#label-placement)

## Cross References
- Refer to the [Axis Customization](#axis-customization) section for more details on adjusting axis settings.

<!-- tags: [syncfusion, windows forms, chart, axis customization, 3d series, label placement] keywords: [chart control, axis crossing, 3D series, axis label, customization, winforms, chapter 4.6] -->
```