```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_380.jpeg
document_name: chart
page_number: 380
page_id: chart#page_380
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:38:21Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Explains indexed X values in line charts.
- Discusses cases where the X values in a series are meaningless and represent categories.
- Describes how to use positional values instead of actual X-values in a chart.

## Content

### 4.6.1 Indexed X Values

By default, points in a series are plotted against their x and y values. However, in some cases, the x values are meaningless—they simply represent categories, and you do not want to plot the points against such x values. Such an x-axis that ignores the x-values and simply uses the positional value of a point in a series is said to be Indexed.

In the figure below, the first chart shows a line chart that is not-indexed while the second chart shows a line chart whose x-axis is indexed.

![Figure 246: Non-Indexed X Values](./figure246.png)

<!-- tags: [winforms, chart, indexed x values, line chart, series plotting, positional value, categories] keywords: [indexed, chart, x-axis, line chart, series, categories, non-indexed] -->
```