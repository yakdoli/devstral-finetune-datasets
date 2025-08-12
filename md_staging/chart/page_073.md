```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_073.jpeg
document_name: chart
page_number: 073
page_id: chart#page_073
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:20:07Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

The appearance of the lines and the points can be configured with options such as the colors used, thickness of the lines and the symbols displayed.

## Overview
- The chart can display line series in 3D mode.
- The chart supports customization of line appearance, including color and thickness.

## Content

### Chart Details

![Daily Server Load](chart_image.png)

*Figure 42: Chart displaying Line Series in 3D Mode*

#### Chart Details

| Details                        |                                |
| ------------------------------ | ------------------------------ |
| Number of Y values per point   | 1.                            |
| Number of Series               | One or More.                  |
| Cannot be Combined with        | Pie, Bar, Stacked Bar, Polar, Radar. |

### Adding Line Series to the Chart

Line series can be added to the chart using the following code.

#### [C#]

```csharp
// Create chart series and add data points into it.
ChartSeries series = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Line);
series.Points.Add(1, new double[] { 20, 8, 8 });
series.Points.Add(2, new double[] { 70, 5, 5 });
```
```html
<!-- tags: [chart, line series, 3D mode, customization, Essential Chart for Windows Forms, C#] keywords: [line series, 3D mode, chart appearance, customization, server load] -->
```