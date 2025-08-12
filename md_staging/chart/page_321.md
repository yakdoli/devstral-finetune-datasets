```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_321.jpeg
document_name: chart
page_number: 321
page_id: chart#page_321
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:34:50Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates the usage of `ShowHistogramDataPoints` property and its effect on a Histogram Chart.
- Explains the functionality of the `ShowTicks` property for customizing chart display.

## Content

### Figure 201: ShowHistogramDataPoints set to False

![Histogram Chart with ShowHistogramDataPoints set to False](https://placehold.it/600x400?text=Figure%20201)

#### Description
This figure shows a Histogram Chart where the `ShowHistogramDataPoints` property is set to `False`. As a result, the data points are not individually marked, highlighting the bars without additional labels.

#### See Also
- [Histogram Chart](https://www.syncfusion.com/products/windowsforms/chart/histogram-chart)

### 4.5.1.72 ShowTicks

#### Overview
The `ShowTicks` property determines whether ticks should be displayed on the chart axes.

#### Details

| Field               | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| Possible Values     | - True - Displays ticks <br> - False - Hides ticks                        |
| Default Value       | True                                                                        |
| 2D / 3D Limitations | No                                                                         |
| Applies to Chart Element | Any Series                                                              |
| Applies to Chart Types | Pie Chart                                                                 |

#### Sample Code Snippet using ShowTicks
Here is a sample code snippet demonstrating the use of `ShowTicks`:

```csharp
chart1.PrimaryXAxis.ShowTicks = false;
chart1.PrimaryYAxis.ShowTicks = true;
```

### WinForms-specific conventions
- The `ShowTicks` property is applied to chart axes and can be used to customize the visibility of ticks.
- This property is applicable to any chart series, regardless of the chart type.

## API Reference
- **Namespace:** Syncfusion.Windows.Forms.Chart
- **Property:** ShowTicks
- **Type:** Boolean
- **Description:** Indicates whether ticks should be shown for the chart axes.
- **Default Value:** True

## Code Examples
Here is an example of how to use the `ShowTicks` property in a Windows Forms application:

```csharp
using Syncfusion.Windows.Forms.Chart;

// Assuming chart1 is an instance of SfChart
chart1.PrimaryXAxis.ShowTicks = true;
chart1.PrimaryYAxis.ShowTicks = false;
```

## RAG Annotations
- <!-- tags: [syncfusion, windowsforms, chart, histogram, showticks, api] -->
- <!-- keywords: [ShowHistogramDataPoints, Histogram Chart, ShowTicks, axis ticks, chart customization, essential chart] -->
```