```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_512.jpeg
document_name: chart
page_number: 512
page_id: chart#page_512
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:46:42Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Watermark Properties

The watermark properties allow you to add a watermark to your chart, specifying its alignment, opacity, and display order.

### Watermark Properties Table

| Property          | Description                                                                                   |
|-------------------|-------------------------------------------------------------------------------------------------|
| HorizontalAlign   | Sets watermark horizontally in the chart area.                                               |
| VerticalAlign     | Sets watermark vertically in the chart area.                                                 |
| Zorder            | Used to specify whether watermark should be shown on top of the chart.                       |

### Code Examples

#### C#

```csharp
this.chartControl1.ChartArea.WaterMark.Text = "Syncfusion Chart";
this.chartControl1.ChartArea.Watermark.Image = System.Drawing.Image.FromFile("Logo.bmp");
this.chartControl1.ChartArea.Watermark.Opacity = 60;
this.chartControl1.ChartArea.Watermark.HorizontalAlignment = ChartAlignment.Near;
this.chartControl1.ChartArea.Watermark.VerticalAlignment = ChartAlignment.Near;
this.chartControl1.ChartArea.Watermark.ZOrder = ChartWaterMarkOrder.Behind;
```

#### VB.NET

```vb
Me.chartControl1.ChartArea.WaterMark.Text = "Syncfusion Chart"
Me.chartControl1.ChartArea.Watermark.Image = System.Drawing.Image.FromFile("Logo.bmp")
Me.chartControl1.ChartArea.Watermark.Opacity = 60
Me.chartControl1.ChartArea.Watermark.HorizontalAlignment = ChartAlignment.Near
Me.chartControl1.ChartArea.Watermark.VerticalAlignment = ChartAlignment.Near
Me.chartControl1.ChartArea.Watermark.ZOrder = ChartWaterMarkOrder.Behind;
```

<!-- tags: [Syncfusion, Winforms, Chart, Watermark, Properties, C#, VB.NET, version: 11.4.0.26] keywords: [Syncfusion, Chart, Watermark, HorizontalAlign, VerticalAlign, Zorder, logo, opacity, alignment, behind, VB.NET, C#] -->
```