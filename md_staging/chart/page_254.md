```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_254.jpeg
document_name: chart
page_number: 254
page_id: chart#page_254
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:30:41Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- This page demonstrates how to configure specific data point settings in a bubble chart using the Essential Chart for Windows Forms.
- The bubble chart visualizes capacity against range, with varying symbols at each data point.
- The example shows how to set specific styles, including images, size, and shape for individual data points.

## Content

### Product Comparison Chart
The following chart illustrates a product comparison using a bubble chart:

![Product Comparison Chart](#)
*Figure 150: Bubble Chart*

#### Specific Data Point Setting
This section explains how to configure specific data points with different symbols in a bubble chart.

##### C#
Below is the C# code to set specific data point symbols:

```csharp
//Symbol set for specific data points (first point)
series1.Styles[0].Images = new ChartImageCollection(this.imageList1.Images);
series1.Styles[0].Symbol.ImageIndex = 0;
series1.Styles[0].Symbol.Size = new Size(20, 20);
series1.Styles[0].Symbol.Shape = ChartSymbolShape.Image;

//Symbol set for specific data points (Second point)
series1.Styles[1].Images = new ChartImageCollection(this.imageList1.Images);
series1.Styles[1].Symbol.ImageIndex = 1;
series1.Styles[1].Symbol.Size = new Size(20, 20);
series1.Styles[1].Symbol.Shape = ChartSymbolShape.Image;
```

##### VB.NET
Here is the equivalent VB.NET code for setting specific data point symbols:

```vbnet
'Symbol set for specific data points (first point )
series1.Styles(0).Images = New ChartImageCollection(Me.imageList1.Images)
series1.Styles(0).Symbol.ImageIndex = 0
series1.Styles(0).Symbol.Size = New Size(20, 20)
```

## API Reference

### Methods and Properties
- `ChartImageCollection`: Represents a collection of images for chart symbol styles.
- `Symbol.ImageIndex`: Sets the image index for a specific data point.
- `Symbol.Size`: Configures the size of the symbol for a data point.
- `ChartSymbolShape.Image`: Specifies that the symbol uses an image as its shape.

## Code Examples

The above sections provide complete examples for configuring bubble chart symbols in both C# and VB.NET.

## Page-level Navigation/TOC
- **Product Comparison Chart**
- **Specific Data Point Setting**
  - C#
  - VB.NET
- **API Reference**

## Cross References
- Refer to the official Syncfusion documentation for more detailed information on customizing chart symbols and styles.

### RAG Annotations
<!-- tags: [bubble chart, data point setting, specific symbol] keywords: [product comparison chart, capacity, range, data point symbol, ChartImageCollection, Symbol Size, ChartSymbolShape] -->
```