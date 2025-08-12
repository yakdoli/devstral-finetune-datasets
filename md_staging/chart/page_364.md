```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_364.jpeg
document_name: chart
page_number: 364
page_id: chart#page_364
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:37:37Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview

- Explains how to use the `YType` property to render chart data.
- Demonstrates accessing the `YType` of a series using both C# and VB.NET.
- Shows a sample bar chart that displays different `YType` values.

## Content

### Properties of `YType`

| 2D / 3D Limitations | Applies to Chart Element | Applies to Chart Types |
|----------------------|--------------------------|-------------------------|
| No                  | Any Series               | All Chart Types         |

Here is sample code snippet using `YType`.

#### C#

```csharp
autoLabel1.Text = this.chartControl1.Series[0].YType.ToString();
```

#### VB.NET

```vb
Private autoLabel1.Text = Me.chartControl1.Series(0).YType.ToString()
```

### Example Chart

![Figure 232: Get the Y Value Type that is being Rendered](https://i.imgur.com/4JF65Qz.png)

**Figure 232: Get the Y Value Type that is being Rendered**

The chart displays daily performance data with values of different `YType` types rendered.

## See Also

- [Chart Types](http://#)
```
<!-- tags: [winforms, chart, YType, Essential Chart, C#, VB.NET] keywords: [Syncfusion Windows Forms, YType, chart series, data rendering, YType property, chart types] -->
```