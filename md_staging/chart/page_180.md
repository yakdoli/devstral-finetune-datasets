```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_180.jpeg
document_name: chart
page_number: 180
page_id: chart#page_180
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:27:17Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Configures border style for chart series.
- Includes color, width, and style parameters.
- Applies to various chart types and elements.

## Content

### Chart Border Configuration

The line type can be configured using the `ChartSeries.Style.Border` property as in the following example.

| Details           |                                                                                                     |
|-------------------|-----------------------------------------------------------------------------------------------------|
| Possible Values   | Any Color, Width, Style for the Borders                                                           |
| Default Value     | - Color - Black<br>- Width value - 1<br>- DashStyle - Solid                                       |
| 2D / 3D Limitations | No                                                                                             |
| Applies to Chart Element | All series and points                                                                      |
| Applies to Chart Types | Pyramid, Funnel, Area, Bar, Bubble, Column Chart, Candle Chart, Renko chart, Three Line Break Chart, Box and Whisker Chart, Gantt Chart, Histogram Chart, Tornado Chart, Polar and Radar Chart and Pie Chart |

#### Example Code: Configuring Border Style

**[C#]**
```csharp
// Set the border style required for the column chart.
series.Style.Border.Width = 3;
series.Style.Border.Color = Color.White;

// Set the Series style
series.Style.DisplayShadow = true;
series.Style.ShadowInterior = new Syncfusion.Drawing.BrushInfo(Color.White);
series.Style.ShadowOffset = new Size(3, 3);
```

**[VB.NET]**
```vb
' Set the border style required for the column chart.
series.Style.Border.Width = 3
series.Style.Border.Color = Color.White

' Set the Series style
series.Style.DisplayShadow = True
series.Style.ShadowInterior = New Syncfusion.Drawing.BrushInfo(Color.White)
```

## Page-level Navigation/TOC (if applicable)

No Table of Contents present on this page.

## Cross References

See also: Chart customization, series properties.

<!-- tags: [chart, border, Windows Forms, C#, VB.NET] keywords: [border style, color, width, DashStyle, apply to chart element, chart types, pie chart, gantt chart, waterfall chart, funnel chart] -->
```