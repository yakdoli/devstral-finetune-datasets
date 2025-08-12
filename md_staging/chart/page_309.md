```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_309.jpeg
document_name: chart
page_number: 309
page_id: chart#page_309
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:34:09Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates how to format tooltips for series elements in various chart types using `SeriesToolTipFormat`.
- Includes examples in C# and VB.NET for configuring the tool tip format.
- Explains supported chart types and series for this feature.

## Content

### Chart Element and Types
| Applies to Chart Element | Applies to Chart Types |
|-------------------------|-------------------------|
| Any Series              | Area Charts, Radar Chart, Polar Chart, ThreeLineBreak Chart, PointAndFigure Chart, StepLine Chart, Spline Chart, HiloOpenClose(3D), RotatedSpline, Kagi Chart |

### Sample Code
Here is some sample code to set the tooltip format for a series.

#### C#
```csharp
this.chartControl1.Series[1].SeriesToolTipFormat="{0}";
```

#### VB.NET
```vb
Private Me.chartControl1.Series(1).SeriesToolTipFormat="{0}"
```

### Visual Example
![Figure 192: SeriesToolTipFormat set = "{0}"](image-1.png)

*Figure 192: SeriesToolTipFormat set = "{0}"*

### Explanation
- The chart demonstrates the use of `SeriesToolTipFormat` to format tooltips for the series elements.
- The figure illustrates an example chart with customized tooltips.

## See Also
- Area Charts
- Radar Chart
- Polar Chart
- ThreeLineBreak Chart
- PointAndFigure Chart
- StepLine Chart
- Spline Chart
- HiloOpenClose(3D)
- RotatedSpline
- Kagi Chart

<!-- tags: [chart, windowsforms, seriestooltipformat, tool tip, area charts, radar chart, polar chart, three line break chart, point and figure chart, step line chart, spline chart, hilo open close, rotated spline, kagi chart, syncfusion] keywords: [chart, windowsforms, series tooltip format, tool tip, chart types, series, area, radar, polar, three line break, point and figure, step line, spline, hilo open close, rotated spline, kagi] -->
```