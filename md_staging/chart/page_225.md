```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_225.jpeg
document_name: chart
page_number: 225
page_id: chart#page_225
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:29:21Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates creating and customizing a StackingBar chart with a FancyToolTip.
- Explains configuring the appearance of tooltips and markers in a chart.
- Highlights the use of properties such as Angle, Style, Symbol, and Visibility for tooltips.

```vb
[VB.NET]
Me.chartControl1.Series(0).FancyToolTip.Angle = 180
Me.chartControl1.Series(0).FancyToolTip.Style = MarkerStyle.SmoothRectangle
Me.chartControl1.Series(0).FancyToolTip.Symbol = ChartSymbolShape.Hexagon
Me.chartControl1.Series(0).FancyToolTip.Visible = True
```

## Content

### StackingBar Chart with FancyToolTip

The following chart illustrates a StackingBar chart with enhanced tooltips:

![StackingBar Chart with FancyToolTip](./figures/StackingBar_Chart_with_FancyToolTip.png)

**Figure 128: StackingBar Chart with FancyToolTip**

#### Key Features
- **Cylinder Shape**: Shown in orange bars, representing one data series.
- **Box Shape**: Shown in blue bars, representing another data series.
- **Tooltip configuration**: A hexagonal shape tooltip displays the time and value for the selected data point.

### See Also
- Chart Types

## 4.5.1.26 FigureBase

This section specifies the drawing style for the funnel or pyramid chart base.

### Details
Specifies the drawing style for the funnel or pyramid chart base.

## API Reference

### Methods
- **FigureBase**: Specifies the drawing style for the funnel or pyramid chart base.

## Code Examples

### VB.NET Example

```vb
[VB.NET]
Me.chartControl1.Series(0).FancyToolTip.Angle = 180
Me.chartControl1.Series(0).FancyToolTip.Style = MarkerStyle.SmoothRectangle
Me.chartControl1.Series(0).FancyToolTip.Symbol = ChartSymbolShape.Hexagon
Me.chartControl1.Series(0).FancyToolTip.Visible = True
```

## Cross References
- Chart Types

## RAG Annotations
<!-- tags: [chart, windows forms, stacking bar, fancytooltip, funnel, pyramid, .NET, VB.NET] keywords: [stackingbar chart, fancytooltip, cylinder shape, box shape, marker style, tooltip visibility, figurebase, drawing style] -->
```