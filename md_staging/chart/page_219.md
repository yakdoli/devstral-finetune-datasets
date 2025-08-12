```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_219.jpeg
document_name: chart
page_number: 219
page_id: chart#page_219
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:28:04Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Lists different marker shapes available for chart elements.
- Details the default value and limitations of marker shapes.
- Specifies which chart elements and types the marker shapes apply to.

## Content

### Marker Shapes for Chart Elements

| **Property**               | **Description**                                                                 |
|-----------------------------|-------------------------------------------------------------------------------|
| VertLine                   | A VerticalLine will be drawn as the marker.                                  |
| Cross                      | A Cross will be drawn as the marker.                                          |
| Hexagon                    | An Hexagon will be drawn as the marker.                                       |
| HorizLine                  | An Horizontal Line will be drawn as the marker.                               |
| Image                      | An Image will be drawn as the marker.                                         |
| InvertedTriangle           | A Inverted Triangle will be drawn as the marker.                              |
| Pentagon                   | A Pentagon will be drawn as the marker.                                       |
| Star                       | A Star will be drawn as the marker.                                           |

### Default Value
- **Diamond**

### 2D / 3D Limitations
- **No**

### Applies to Chart Element
- **All Series**

### Applies to Chart Types
- **Line Chart**

## Sample Code

Here is some sample code.

### C#

```csharp
this.chartControl1.Series[0].DrawErrorBars = true;
this.chartControl1.Series[0].ErrorBarsSymbolShape = ChartSymbolShape.Circle;
```

### VB.NET

```vb
Me.chartControl1.Series(0).DrawErrorBars = true
Me.chartControl1.Series(0).ErrorBarsSymbolShape = ChartSymbolShape.Circle
```

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.

## Cross References
- See also:
  - Related documentation or links specific to this page content.

## RAG Annotations
<!-- tags: [chart, marker shapes, error bars, default value, limitations, chart series, chart types, line chart, c#, vb.net, sample code] keywords: [chart, marker shapes, diamond, cross, hexagon, horizontal line, image, inverted triangle, pentagon, star, error bars, default value, 2d/3d limitations, all series, line chart] -->
```