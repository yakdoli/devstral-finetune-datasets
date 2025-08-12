```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_493.jpeg
document_name: chart
page_number: 493
page_id: chart#page_493
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:45:19Z
fidelity: lossless
-->

## Inside the Chart Area

Use the `ChartInterior` property of the chart to customize the background of the chart area. By default, it is set to `White` color.

### C#

```csharp
this.chartControl1.ChartInterior = new Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.Horizontal, System.Drawing.Color.PaleTurquoise, System.Drawing.Color.LightBlue);
```

### VB.NET

```vb
this.chartControl1.ChartInterior = New Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.Horizontal, System.Drawing.Color.PaleTurquoise, System.Drawing.Color.LightBlue)
```

## Content

### Figure 317: ChartArea.BackInterior = "SkyBlue"

![](Images/BackInterior.png)

<!-- tags: [Syncfusion Windows Forms] keywords: [ChartArea.BackInterior, ChartInterior, gradient style, SkyBlue, PaleTurquoise, LightBlue, WinForms, chart controls, background customization] -->
```