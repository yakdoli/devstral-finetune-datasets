```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_513.jpeg
document_name: chart
page_number: 513
page_id: chart#page_513
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:46:29Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- This page discusses the use of "Image" as a watermark within charts, demonstrated in Figure 329.
- It also explains the implementation of an interlaced grid background in charts, highlighting customization options.

## Content

### Image as Watermark
In Figure 329, the demonstration shows the chart implementing an "Image" as a watermark. The properties are defined as follows:
- **Opacity**: "60"
- **HorizontalAlignment**: "Near"
- **VerticalAlignment**: "Near"
- **ZOrder**: "Behind"

#### Figure 329
The chart displays the following:
- A graph titled "Car Sales."
- Sales percentages plotted over the years from 1996 to 2006.
- Multiple data series represented by different colored lines.

### Interlaced Grid Background
The chart supports an interlaced grid, which creates an alternative grid background along both the x-axis and y-axis. The color of the interlaced grid is customizable.

#### Implementation Details
The chart allows drawing an interlaced grid by enabling grid lines in both the primary x and y axes. The grid interior color can be set using the `BrushInfo` class.

#### Code Examples

##### C#
```csharp
this.chartControl1.PrimaryXAxis.InterlacedGrid = true;
this.chartControl1.PrimaryXAxis.InterlacedGridInterior = new Syncfusion.Drawing.BrushInfo(System.Drawing.Color.FromArgb(166, 184, 200));
this.chartControl1.PrimaryYAxis.InterlacedGrid = True;
this.chartControl1.PrimaryYAxis.InterlacedGridInterior = new Syncfusion.Drawing.BrushInfo(System.Drawing.Color.FromArgb(124, 144, 179));
```

##### VB.NET
```vb
Me.chartControl1.PrimaryXAxis.InterlacedGrid = True
Me.chartControl1.PrimaryXAxis.InterlacedGridInterior = new Syncfusion.Drawing.BrushInfo(System.Drawing.Color.FromArgb(166, 184, 200))
```

### Customization
- The interlaced grid's color can be adjusted to enhance visual appeal and readability.
- Users can select custom colors or patterns to match the overall chart theme.

## Notes
- The chart's interlaced grid feature is a useful tool for improving the readability of data series in complex charts.
- Adjustments to opacity and alignment can be tailored to suit the user's specific needs.

### References
See also: [General Chart Customizations](#chart-customizations), [Watermark Properties Overview](#watermark-overview)

<!-- tags: [Syncfusion, Winforms, Chart, Watermark, Interlaced Grid] keywords: [Customization, InterlacedGrid, ChartControls, WatermarkProperties, GridBackground] -->
```
