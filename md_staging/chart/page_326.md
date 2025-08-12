```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_326.jpeg
document_name: chart
page_number: 326
page_id: chart#page_326
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:34:52Z
fidelity: lossless
-->

## Overview
- Specifies the space/width between data points in the x-axis in percentage (%).
- Determines how much of the interval width is used for rendering data points.
- Used only for chart types like column charts with a width component.
- Not applicable when ChartColumnWidth is set to FixedWidthMode.

## Content

This specifies the space/width between data points in the x axis. This value is specified in percentage (%) of interval width. So, for example, if the value of the property is 20%, then only 80% of the interval width is used for rendering the data point(s). If there are multiple series then the available width is divided between the data points in the different series. This of course is used only for appropriate chart types like the column chart which has a width component.

This property will not be used when ChartColumnWidth is set to FixedWidthMode.

### Details

| **Possible Values** | A double value (10 to 99) |
|---------------------|---------------------------|
| **Default Value**   | 30                        |
| **2D / 3D Limitations** | No                     |
| **Applies to Chart Element** | Any Series and points |
| **Applies to Chart Types** | Column Charts, BarCharts, Box and Whisker Chart, Gantt Chart, Tornado Chart, Candle Chart, Hilo Chart, Hilo Open Close Chart |

### Code Examples

- **C#**

```csharp
// Indicates the spacing width in percentage that is to be applied between the datapoints of the column chart.
this.chartControl1.Spacing = 50;
```

- **VB.NET**

```vb
' Indicates the spacing width in percentage that is to be applied between the data points of the column chart.
Me.chartControl1.Spacing = 50
```

## RAG Annotations
<!-- tags: [chart, chartcontrol, spacing, column chart, bar chart, gantt chart, candle chart, hilo chart] keywords: [space/width, percentage, chart types, fixedwidthmode, interval width, multiple series, data points] -->
```