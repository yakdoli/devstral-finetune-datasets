```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_396.jpeg
document_name: chart
page_number: 396
page_id: chart#page_396
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:39:13Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- This page discusses how to modify the size of the Primary X-Axis in a chart using AutoSize mode and custom sizing.

## Content

### Charts in AutoSize Mode

#### Figure 255: Chart rendered in AutoSize Mode
![Figure 255: Chart rendered in AutoSize Mode](https://example.com/image1.png)

The chart shown above is rendered in AutoSize mode. The X-axis automatically adjusts to fit the chart data.

### Customizing the Primary X-Axis Size

#### Figure 256: Chart rendered with a custom size for the Primary X-Axis
![Figure 256: Chart rendered with a custom size for the Primary X-Axis](https://example.com/image2.png)

This chart demonstrates how setting custom size properties for the Primary X-Axis affects the chart rendering.

### Code Examples

#### C#
```csharp
this.chartControl1.PrimaryXAxis.AutoSize = false;
this.chartControl1.PrimaryXAxis.Size = new Size(50, 20);
```

#### VB
```vb
Me.ChartControl1.PrimaryXAxis.AutoSize = False
Me.ChartControl1.PrimaryXAxis.Size = New Size(50, 20)
```

By setting `AutoSize` to `false` and specifying a `Size` for the Primary X-Axis, you can customize the appearance of the X-axis in your chart.

## Footer
© 2013 Syncfusion. All rights reserved. 396 | Page

<!-- tags: [Syncfusion, Winforms, Chart, X-Axis, AutoSize, Size] keywords: [AutoSize, PrimaryXAxis, CustomSize, ChartControl, X-Axis Size, Windows Forms, Syncfusion Winforms] -->
``` 
