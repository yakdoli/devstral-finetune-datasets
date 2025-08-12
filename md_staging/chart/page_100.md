```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_100.jpeg
document_name: chart
page_number: 100
page_id: chart#page_100
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:22:09Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Overview

- Essential Chart-Stacked 100% Chart
- Displaying data as a stacked column chart with three series: Series1 (orange), Series2 (blue), and Series3 (red).
- Each column in the chart represents a data point, stacked vertically to indicate contributions from each series.

### Detailed Analysis

#### Visual Representation

- The chart includes five data points labeled as -1, 0, 1, 2, 3, and 4 on the x-axis.
- On the y-axis, the values range from 0 to 100, indicating the contributions as percentages.
- The stacked columns visually represent the proportional contributions of each series to the total value at each data point.

#### Chart Specifications

| **Details**                 | **Values**                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| Number of Y values per point| 1.                                                                         |
| Number of Series            | Two or more.                                                               |
| SupportMarker               | No.                                                                        |
| Cannot be Combined with     | Doughnut, Pie, Bar, Stacked Bar charts, Polar, Radar, Pyramid, or Funnel. |

### Code Example

#### C# Implementation

To create a 100% stacked column chart using C#:

```csharp
ChartSeries series1 = this.chartControl1.Model.NewSeries("Series 1",
    ChartSeriesType.StackingColumn100);
series1.Points.Add(0, 25.3);
series1.Points.Add(1, 45.7);
series1.Points.Add(2, 97.3);
series1.Points.Add(3, 20.6);
series1.Points.Add(4, 125.8);
series1.Points.Add(5, 216.1);
```

### Notes

- The chart demonstrates how data is proportionally represented across multiple series.
- Each data point's series contributions are stacked to equal 100%, showing relative proportions.
- This chart type is suitable for showing how different series contribute to the total value at each data point.

### RAG Annotations

<!-- tags: [chart, stacked column, chart series, Syncfusion Winforms, 100% stacking] keywords: [Essential Chart, Stacked Column, Series, Data Points, Proportional Contributions, Syncfusion, Winforms, C#] -->
```