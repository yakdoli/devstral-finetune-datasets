```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_259.jpeg
document_name: chart
page_number: 259
page_id: chart#page_259
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:30:19Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Explains how to use the Interior property to customize the back color, gradient, or pattern style for data points in charts.
- Demonstrates setting the interior color for series using C# and VB.NET code examples.

## Pie Chart

### 4.5.1.41 Interior

This property will allow the user to set a solid back color, gradient or pattern style for the data points.

| Details       |                  |
|---------------|------------------|
| Possible Values | A BrushInfo object |
| Default Value | None             |
| 2D / 3D Limitations | No      |
| Applies to Chart Element | All series and points |
| Applies to Chart Types | All Chart Types |

### Series Wide Setting

The spline area interior brush can be customized using the `ChartSeries.Style.Interior` property as shown below.

The interior color of the chart series can be customized by using the `Interior` property of the `ChartStyleInfo` class. The following code illustrates this.

#### C#

```csharp
// This sets the interior color for the series. This can be done for
// any number of series.
this.chartControl1.Series[0].Style.Interior = new
BrushInfo(GradientStyle.Horizontal, Color.AliceBlue, Color.Green);
```

#### VB.NET

```vb.net
' This sets the interior color for the series. This can be done for
' any number of series.
Me.chartControl1.Series(0).Style.Interior = New
BrushInfo(GradientStyle.Horizontal, Color.AliceBlue, Color.Green)
```
```