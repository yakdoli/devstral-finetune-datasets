```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_349.jpeg
document_name: chart
page_number: 349
page_id: chart#page_349
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:36:23Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates the use of the `TextOffset` property in a bar chart to adjust the placement of text labels.
- Explains how to set specific data point text offsets using `Series.Styles[0].TextOffset`.

## Content

### Illustrates TextOffset

#### Figure 221: Text Offset set to 10.0F

![Bar Chart](#chart#page_349-bar-chart)

The bar chart above illustrates the `TextOffset` property, where text labels are adjusted to display specific offsets from the data points.

#### Specific Data Point Setting

The `TextOffset` for data points can be specified using the `Series.Styles[0].TextOffset` property.

##### Code Examples

**C#**
```csharp
this.chartControl1.Series[0].Styles[0].TextOffset = 10.0F;
this.chartControl1.Series[0].Styles[1].TextOffset = 15.0F;
```

**VB.NET**
```vb
Me.chartControl1.Series(0).Styles(0).TextOffset = 10.0F
Me.chartControl1.Series(0).Styles(1).TextOffset = 15.0F
```

#### See Also
- [Chart Types](#chart-types)

---

## 4.5.1.86 TextOrientation

### Summary
Describes the `TextOrientation` property and how it can be configured to present text in different orientations on a chart.

### See Also
- [TextOrientation](#text-orientation)

## Page-level Navigation/TOC (if applicable)
- [Chart Types](#chart-types)
- [TextOrientation](#text-orientation)

## Cross References
- Related topics: TextOffset, Chart Styles, Data Point Properties

<!-- tags: [Syncfusion, WinForms, ChartControl, TextOffset, TextOrientation, SeriesStyles] keywords: [chart, text offset, data point, styles, series, vb.net, c#, synchronization, windows forms, series styles, text orientation] -->
```