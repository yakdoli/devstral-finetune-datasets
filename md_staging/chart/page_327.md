```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_327.jpeg
document_name: chart
page_number: 327
page_id: chart#page_327
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:33:55Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview

- Explains the `Spacing` property in Essential Chart.
- Demonstrates how spacing affects the layout of chart series.
- Describes the `SpacingBetweenSeries` property for controlling the spacing between series in a chart.

## Content

### Chart with 50 Percent Spacing

![Example Chart](http://example.com/image.png)
**Figure 206:** Series rendered with 50 percent Spacing

#### See Also

- Column Charts
- BarCharts
- Box and Whisker Chart
- Gantt Chart
- Tornado Chart
- Candle Chart
- Hilo Chart
- Hilo Open Close Chart

### 4.5.1.75 SpacingBetweenSeries

Essential Chart provides support to control the spacing between series using the `SpacingBetweenSeries` property.

#### Details

| **Possible Values**        | A double value (10 to 100) |
|----------------------------|-----------------------------|
| **Default Value**          | 10                          |
| **2D / 3D Limitations**   | No                          |
| **Applies to Chart Element** | Any Series                 |
| **Applies to Chart Types** | Area Charts, BarCharts, Line Charts, Bubble Chart, Financial Charts, Gantt Chart, Histogram chart, Tornado Chart, Combination Chart, Box |

## API Reference

- **Property:** `SpacingBetweenSeries`
  - **Type:** double
  - **Description:** Controls the spacing between series in a chart.
  - **Default:** 10
  - **Range:** 10 to 100

### WinForms-specific Examples

```csharp
// Example of setting SpacingBetweenSeries in C#
chart1.SpacingBetweenSeries = 50;
```

### Related Documentation

- [Column Charts](#)
- [BarCharts](#)
- [Box and Whisker Chart](#)
- [Gantt Chart](#)
- [Tornado Chart](#)
- [Candle Chart](#)
- [Hilo Chart](#)
- [Hilo Open Close Chart](#)

## RAG Annotations
<!-- tags: [windows-forms, chart, spacing, series, api, version:11.4.0.26] keywords: [SpacingBetweenSeries, Essential Chart, Series Spacing, WinForms, Chart Types, BarCharts, Line Charts, Gantt Chart, Tornado Chart, Candle Chart, Hilo Chart, Histogram] -->
```