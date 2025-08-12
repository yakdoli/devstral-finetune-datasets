```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_355.jpeg
document_name: chart
page_number: 355
page_id: chart#page_355
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:35:44Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Discusses the configuration of tooltips for data points in charts.
- Provides information on setting the tooltip format for chart elements.
- Lists related chart types and their usage in Windows Forms applications.

## Content

### Figure: ToolTip set for Data Point in the Series

![Illustrates Tooltip](IllustratesTooltip.png)

**Figure 224:** ToolTip set for Data Point in the Series

#### See Also
- Scatter Chart
- Hilo Open Close Chart (3D)
- Column Charts
- BarCharts
- Bubble Chart
- Line Charts
- BoxandWhisker Chart
- Tornado Chart
- Combination Chart
- Gantt Chart
- Candle Chart
- HiLo Chart (3D)
- PolarAndRadar chart
- PieChart
- Accumulation Charts
- Area Charts

#### 4.5.1.88 ToolTipFormat
Sets the tooltip format of the style object associated with the series.

- **Description:** Sets the tooltip format string for the series.
- **Details:**

| **Parameter**            | **Description**                                                                 |
|---------------------------|---------------------------------------------------------------------------------|
| **Possible Values**      | Any string with '{0}' as the place holder for Y value.                        |
| **Default Value**        | Nil                                                                             |
| **2D / 3D Limitations** | No                                                                              |
| **Applies to Chart Element** | Any Series and Points                                                         |

## API Reference

### ToolTipFormat
- **Property Type:** string
- **Parameters:** 
  - **FormatString:** A string with the placeholder '{0}' for the Y-value.

### Code Example

```csharp
chart.Series[0].ToolTipFormat = "Value: {0}";
```

### Notes
- The `ToolTipFormat` property allows developers to customize the text displayed when a user hovers over a data point in the chart.

#### See also:
- [ToolTip in Chart](#toolTip-in-chart)
- [Customizing Chart Elements](#customizing-chart-elements)

## RAG Annotations
<!-- tags: [Syncfusion, WinForms, Chart, Tooltip, Windows Forms, .NET Framework, C#] keywords: [tooltipformat, chart tooltips, data points, series, custom formatting, place holder, chart elements, visual studio, .NET, WinForms application] -->
```