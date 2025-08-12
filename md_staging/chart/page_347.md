```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_347.jpeg
document_name: chart
page_number: 347
page_id: chart#page_347
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:35:15Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Explains how to implement TextFormat in a Column Chart.
- Demonstrates both series-wide and specific data point settings for TextFormat.

## Content

### Series wide setting

```csharp
this.chartControl1.Series[0].Style.TextFormat = "T = {0}";
```

```vb.net
Me.chartControl1.Series(0).Style.TextFormat = "T = {0}"
```

![Illustrates TextFormat](https://github.com/syncfusion-docs/images/blob/main/illustrates-text-format.png)
*Figure 220: TextFormat = "T = {0}"*

### Specific Data Point Setting

**TextFormats for individual data points are specified using below code.**

```csharp
chartControl1.Series[0].Styles[0].TextFormat = "YValue : {0}";
chartControl1.Series[0].Styles[1].TextFormat = "Dollars : {0:C}";
```

## API Reference

### Namespace: Syncfusion.Windows.Forms.Chart

#### Members
- **Style.TextFormat**: Specifies the formatting for the text displayed on the chart.
- **Series.Style**: Accesses style settings for an individual series.
- **Styles[0], Styles[1]**: Accesses specific styles for individual data points.

## Code Examples

### C#
```csharp
// Setting series-wide TextFormat
this.chartControl1.Series[0].Style.TextFormat = "T = {0}";

// Setting specific data point TextFormat
chartControl1.Series[0].Styles[0].TextFormat = "YValue : {0}";
chartControl1.Series[0].Styles[1].TextFormat = "Dollars : {0:C}";
```

### VB.NET
```vb.net
' Setting series-wide TextFormat
Me.chartControl1.Series(0).Style.TextFormat = "T = {0}"

' Setting specific data point TextFormat
chartControl1.Series(0).Styles(0).TextFormat = "YValue : {0}"
chartControl1.Series(0).Styles(1).TextFormat = "Dollars : {0:C}"
```

<!-- tags: [chart, windowsforms, textformat, series, datappoint, syncfusion] keywords: [chartcontrol, textformat, seriesstyle, data-points, windows forms, chart, windows forms chart] -->
```