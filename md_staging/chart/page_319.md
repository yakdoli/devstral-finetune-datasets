```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_319.jpeg
document_name: chart
page_number: 319
page_id: chart#page_319
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:33:28Z
fidelity: lossless
-->

## Overview
- Demonstrates a Pyramid Chart featuring data-bound labels.
- Explains the `ShowHistogramDataPoints` property and its effects on displaying data points in histograms.

## Content

### Chart Data From Database

#### Pyramid Chart with Data-Bound Labels

![Figure 199: Pyramid Chart with Data-Bound Labels](#)

The figure shows a Pyramid Chart with data represented for different cities. The pyramid is segmented into layers, each labeled with a city name and its corresponding data value.

**Legend:**

- New York: 13
- Houston: 6
- Tokyo: 17
- London: 15
- Los Angeles: 11

#### See Also
- [Pie Chart](#)
- [Doughnut Chart](#)
- [Funnel Chart](#)
- [Pyramid Chart](#)

### 4.5.1.71 ShowHistogramDataPoints

**Indicates if the histogram data points should be shown.**

The `ShowHistogramDataPoints` property is used to control the visibility of data points in a histogram chart. It determines whether the individual data points are displayed or hidden.

| Details |  |
| --- | --- |
| Possible Values | • True - Displays the datapoints.<br/>• False - Hides the datapoints. |
| Default Value | True |

## API Reference

### ShowHistogramDataPoints

**Property:**
- Name: `ShowHistogramDataPoints`
- Type: `Boolean`

**Description:**
Indicates whether the histogram data points should be shown.

**Possible Values:**
- **True:** Displays the data points.
- **False:** Hides the data points.

**Default Value:**
- **True**

## Code Examples

```csharp
// Example of setting ShowHistogramDataPoints in C#
chart1.Series[0].ShowHistogramDataPoints = true;
```

### Cross References
- [Pyramid Chart](#)
- [Funnel Chart](#)
- [Histogram Chart](#)

<!-- tags: [Syncfusion, WinForms, Chart, Pyramid Chart, ShowHistogramDataPoints, Histogram, Data Points] keywords: [chart, data-bound labels, pyramid chart, histogram, data points visibility, Syncfusion WinForms] -->
```