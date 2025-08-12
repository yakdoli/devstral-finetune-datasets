```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_376.jpeg
document_name: chart
page_number: 376
page_id: chart#page_376
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:38:10Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates setting an empty point in a chart using VB.NET code.
- Highlights the visual effect of setting a point as empty.

## Content

### Chart Configuration to Set an Empty Point

```vb
' This sets the specified point as empty point.
Me.chartControl1.Series[1].Points[0].IsEmpty = True
```

The following images illustrate the same. The second image displays after setting Point1 as an empty point.

![Figure 242: Chart without Empty Point](https://.../image_source)

### Description of the Images

#### Figure 242: Chart without Empty Point
This figure shows a bar chart with multiple data points over time. The chart is labeled "Point1 Visible," and the bars represent various values across different years. Point1 is highlighted, indicating its visibility. The chart clearly displays all data points without any being set as empty.

---

## Page-level Navigation/TOC (if applicable)
- Essential Chart for Windows Forms
- Chart Configuration to Set an Empty Point
- Description of the Images

## Cross References
- Refer to related documentation or examples for further details on chart customization and handling empty points.

<!-- tags: [chart, essential-chart, windows-forms, vb.net, empty-point] keywords: [chart control, setting empty point, visual basic, chart visibility, windows forms, series data] -->
```