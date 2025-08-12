```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_305.jpeg
document_name: chart
page_number: 305
page_id: chart#page_305
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:33:58Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Illustrates how to connect points in a scatter chart series using the `ScatterConnectType` property.
- Demonstrates using lines (`ScatterConnectType.Line`) and splines for visualization.
- Includes Code samples in C# and VB.NET.

## Content

### ScatterConnectType Property

#### Connecting Points with Straight Lines
Optionally, you can connect the points in the series through straight lines using the `ScatterConnectType` property.

**C# Example**
```csharp
series.ScatterConnectType = ScatterConnectType.Line;
```

**VB.NET Example**
```vb
series.ScatterConnectType = ScatterConnectType.Line
```

**Figure: Scatter Line Chart**
![Scatter Line Chart](https://example.com/image.jpg)

*Figure 189: Scatter Line Chart*

### Scatter Spline Chart

#### Connecting Points with Splines
Alternatively, you can connect the points in the series through splines using the `ScatterConnectType` property as shown below.

**Figure: Scatter Spline Chart**
*Illustrates the use of splines to connect points instead of straight lines.*

## RAG Annotations
<!-- tags: [Syncfusion Winforms, ScatterSeries, ScatterConnectType, Chart, Line, Spline, C#, VB.NET] keywords: [scatter chart, series, points, visualization, lines, splines, ScatterConnectType, charts] -->
```