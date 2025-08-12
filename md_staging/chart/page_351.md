```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_351.jpeg
document_name: chart
page_number: 351
page_id: chart#page_351
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:35:30Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Explains how to set the text orientation for chart series using C# and VB.NET.
- Demonstrates how to configure text color and orientation based on specific data points.

## Content
### C#

```csharp
// Text Orientation of chart series
this.chartControl.Series[1].Style.TextOrientation = ChartTextOrientation.RegionDown;
this.chartControl.Series[0].Style.TextOrientation = ChartTextOrientation.Up;
this.chartControl.Series[0].Style.TextColor = Color.Blue;
this.chartControl.Series[1].Style.TextColor = Color.Red;
```

### VB.NET

```vb.net
' Text Orientation of chart series
Private Me.chartControl.Series(1).Style.TextOrientation = ChartTextOrientation.RegionDown
Private Me.chartControl.Series(0).Style.TextOrientation = ChartTextOrientation.Up
Private Me.chartControl.Series(0).Style.TextColor = Color.Blue
Private Me.chartControl.Series(1).Style.TextColor = Color.Red
```

![Figure 222: Text Orientation set for the Chart Series](https://via.placeholder.com/600x400?text=Figure+222%3A+Text+Orientation+set+for+the+Chart+Series)

### Specific Data Point Setting

Text orientation for specific data points can be set using the `Series.Style[i].TextOrientation` property, where `i` represents the index of data points ranging from 0 to `n`.

## API Reference

- **Namespace:** Syncfusion.Windows.Forms.Chart
- **Class:** Series
- **Property:** Style.TextOrientation
  - **Type:** ChartTextOrientation
  - **Description:** Specifies the orientation of the text for a specific data point.
  - **Default:** ChartTextOrientation.Auto

## Code Examples

### C#

```csharp
// Setting specific data point orientation
this.chartControl.Series[0].Style[1].TextOrientation = ChartTextOrientation.Up;
```

### VB.NET

```vb.net
' Setting specific data point orientation
Private Me.chartControl.Series(0).Style(1).TextOrientation = ChartTextOrientation.Up
```

## RAG Annotations
<!-- tags: [chart, chartcontrol, textorientation, data points] keywords: [text orientation, chart series, specific data points, series style] -->
```