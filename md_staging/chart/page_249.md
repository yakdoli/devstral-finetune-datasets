<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_249.jpeg
document_name: chart
page_number: 249
page_id: chart#page_249
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:30:45Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Chart Properties Overview

### Property: HighlightInterior

| **Possible Values** | RGB values range from 0 to 255 |
| --- | --- |
| **Default Value** | None |
| **2D / 3D Limitations** | No |
| **Applies to Chart Element** | All series |
| **Applies to Chart Types** | Bar Charts, Pie, Funnel, Pyramid, Bubble, Column, Area, Stacking Area, Stacking Area100, Line Charts, Box and Whisker, Gantt Chart, Tornado Chart, Polar And Radar Chart, Hi Lo Chart, Hi Lo Open Close Chart |

## Series Wide Setting

Here is some sample code.

### C#

```csharp
this.chartControl1.AutoHighlight = true;
ChartSeries series1 = this.chartControl1.Series[0];
series1.Style.HighlightInterior = new
BrushInfo(GradientStyle.ForwardDiagonal, Color.Red, Color.White);
```

### VB.NET

```vb
Me.chartControl1.AutoHighlight = True
Dim series1 As ChartSeries = Me.chartControl1.Series(0)
series1.Style.HighlightInterior = New
BrushInfo(GradientStyle.ForwardDiagonal, Color.Red, Color.White)
```

## API Reference (if applicable)

### Example Usage

The `HighlightInterior` property is used to set the interior highlight style for a series. In the provided examples, the gradient style is set to `ForwardDiagonal`, and the colors are specified as `Color.Red` and `Color.White`.

<!-- tags: [essential chart, windows forms, highlight interior, chart elements, chart types, gradient style, c#, vb.net, Syncfusion, 11.4.0.26] keywords: [highlight interior,chart properties,chart elements,chart types,gradient style,series wide setting,sample code,c#,vb.net] -->