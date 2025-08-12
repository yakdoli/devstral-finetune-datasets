```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_184.jpeg
document_name: chart
page_number: 184
page_id: chart#page_184
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:27:33Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates how to use `ImageBubbleType` charts in a bubble chart series.
- Shows how to style bubble chart series using `ChartImageCollection`.
- Illustrates the `ColumnDrawMode` for handling multiple series in column charts.

## Content

### [VB.NET]

The VB.NET code snippet below demonstrates how to set up an `ImageBubbleType` chart with styled bubbles:

```vb
Me.chartControl1.Series(0).Styles(0).Images = New ChartImageCollection(Me.imageList1.Images)
Me.chartControl1.Series(0).Styles(0).ImageIndex = 0
Me.chartControl1.Series(0).Styles(1).Images = New ChartImageCollection(Me.imageList1.Images)
Me.chartControl1.Series(0).Styles(1).ImageIndex = 1
```

#### Product Comparison Chart

![](https://i.imgur.com/)$empty$

The chart visualizes product data using bubbles, where:

- The size of the bubble represents capacity (Tones).
- The horizontal axis represents the range (Miles).
- Different colors and images indicate different product categories or attributes.

##### Figure 99: Image BubbleType Chart Series

### See Also
- Bubble Chart

### 4.5.1.4 ColumnDrawMode

Indicates the drawing mode of columns in charts when there are multiple series.

## Page-level Navigation/TOC (if applicable)
This section is part of the overall documentation structure. The content provides examples and explanations related to chart customization in Windows Forms.

## Cross References
See also:
- [Bubble Chart](#Bubble Chart)
- [ColumnDrawMode](#ColumnDrawMode)

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [Chart, BubbleType, ImageBubbleType, ColumnDrawMode, Windows Forms, Syncfusion] -->
```