```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_600.jpeg
document_name: chart
page_number: 600
page_id: chart#page_600
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:52:20Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- The section discusses hit testing in the Essential Chart.
- It covers the conversion of mouse positions into Chart Coordinates.
- Focuses on retrieving values at specific points in the chart.

## Content

### 4.18 Hit Testing

The section covers the below topics:

#### 4.18.1 Chart Coordinates by Point

**Chart Coordinates by point**

**GetValueByPoint()**

Using the `GetValueByPoint` method, the mouse position in chart client-coordinates can be converted into a corresponding Chart Coordinate in terms of x, y values.

The below figure shows a chart where the tooltip text for each point shows the corresponding x, y value at that position.

![](https://example.com/image_url)

<!-- tags: [syncfusion, chart, windows forms, winforms, hit testing, chart coordinates, getvaluebypoint] keywords: [chart, windows forms, hit testing, chart coordinates, mouse position, x, y values] -->
```