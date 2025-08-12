```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_296.jpeg
document_name: chart
page_number: 296
page_id: chart#page_296
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:33:57Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates how to configure a radar chart with a circle-style axis in WinForms.
- Includes code examples in C# and VB.NET to set the radar style.

## Content

### Configuring Radar Style
To display a radar chart with a circular axis style, you can use the following code:

```csharp
[C#]
this.chartControl1.RadarStyle = ChartRadarAxisStyle.Circle;
```

```vbnet
[VB.NET]
Me.chartControl1.RadarStyle = ChartRadarAxisStyle.Circle
```

### Visual Representation
The figure below illustrates a radar chart with a circular axis style:

![Radar Chart with Circle RadarStyle](https://example.com/figure182.png)
*Figure 182: Radar Chart with Circle RadarStyle*

This figure shows a radar chart with an axis style configured to a circle, providing a clear visual comparison of data points.

## API Reference

### Members
- **RadarStyle**:  
  - **Type**: `ChartRadarAxisStyle`  
  - **Description**: Specifies the style of the radar axis.  
  - **Values**:  
    - `Circle`: Displays the radar plot with a circular axis style.  

## Code Examples

### C#
```csharp
this.chartControl1.RadarStyle = ChartRadarAxisStyle.Circle;
```

### VB.NET
```vbnet
Me.chartControl1.RadarStyle = ChartRadarAxisStyle.Circle
```

## See also
- [Radar Chart](#radar-chart)
- [Axis Styles](#axis-styles)

<!-- tags: [Syncfusion Winforms, Chart, RadarChart, RadarStyle, CircleAxisStyle] keywords: [winforms, radar chart, circle style, axis style, chart control] -->
```