```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_514.jpeg
document_name: chart
page_number: 514
page_id: chart#page_514
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:48:46Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates how to enable and customize interlaced grids in charts using Syncfusion.
- Highlights the minor grid lines feature and customization options for charts.

## Content

### Code Example: Enabling Interlaced Grid
```csharp
Me.chartControl1.PrimaryYAxis.InterlacedGrid = True
Me.chartControl1.PrimaryYAxis.InterlacedGridInterior = new Syncfusion.Drawing.BrushInfo(System.Drawing.Color.FromArgb(124, 144, 179))
```

#### Figure Illustrating Interlaced Grid
![](https://i.imgur.com/ExampleFigure330.png)  
*Figure 330: Interlaced Grid*

The preceding image illustrates interlaced grid background for the chart.

A sample which illustrates the Interlaced Grid for the Chart is available in the below sample installation location:

```
<Sample location>\Syncfusion\EssentialStudio\Version Number\Windows\Chart.Windows\Samples\2.0\Chart Appearance\Interlaced Grid
```

### 4.10.9 Minor Grid Lines

Chart comes with minor lines support which will draw lines along the intervals provided. The appearance of these line is also customizable similar to the major grid lines.

#### Code Example: Minor Grid Lines
```csharp
[C#]
```

## Page-level Navigation/TOC (if applicable)
- Essential Chart for Windows Forms
  - Enabling Interlaced Grid
  - Minor Grid Lines

## RAG Annotations
<!-- tags: [syncfusion, winforms, chart, interlaced grid, minor grid lines, customization, example code] keywords: [interlaced grid, minor grid lines, chart customization, winforms, Syncfusion] -->
```