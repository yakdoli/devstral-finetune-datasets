<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_072.jpeg
document_name: chart
page_number: 072
page_id: chart#page_072
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:20:09Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Chart Types

The following table lists various chart types supported by the Essential Chart for Windows Forms:

| Chart Type          | Axes | Series | Legend |
|---------------------|------|--------|--------|
| Scatter Charts      | 1    | Unlimited | 1 |
| Spline Area Charts  | 1    | Unlimited | 1 |
| Spline Charts       | 1    | Unlimited | 1 |
| Stacking Area Charts | 2    | Unlimited | 1 |
| Stacking Bar Charts | 2    | Unlimited | 1 |
| Stacking Column Charts | 2    | Unlimited | 1 |
| Step Area Charts    | 1    | Unlimited | 1 |
| Step Line Charts    | 1    | Unlimited | 1 |
| Three Line Break Charts | 1    | Unlimited | 1 |
| Tornado Charts      | 1    | Unlimited | 2 |

### 4.4.1 Line Charts

#### Overview

Line charts are visualizations that use a line to connect different data points in a series. These lines can be straight, splines, or steps. Line charts are simpler and allow you to visualize multiple series without overlapping, unlike in a bar chart.

#### Different Types of Line Charts

##### 4.4.1.1 Line Chart

- **Description**: Line Charts join points on a plot using straight lines, showing trends in data at equal intervals. They treat the input as non-numeric, categorical information, equally spaced along the x-axis. This is suitable for categorical data, such as text labels, but can produce unexpected results when X values consist of numbers.
- **3D Rendering**: When rendered in 3D, the plot looks like a ribbon, and such types are also referred to as Ribbon or Strip Charts.

## API Reference

### Chart Properties

- **Axes**: Specifies the number of axes in the chart.
- **Series**: Defines the number of series that can be displayed.
- **Legend**: Indicates the number of legend entries supported.

## Code Examples

### C#

```csharp
// Example of creating a Line Chart
SfChart chart = new SfChart();
LineSeries lineSeries = new LineSeries();
lineSeries.DataSource =dataSource;
chart.PrimaryXAxis = new CategoryAxis();
chart.PrimaryYAxis = new NumericalAxis();
chart.Series.Add(lineSeries);
this.Controls.Add(chart);
```

### References

- **See also**:
  - Scatter Charts
  - Spline Charts
  - Stacking Area Charts
  - Step Line Charts

<!-- tags: [syncfusion, winforms, chart, types, line charts, tutorial] keywords: [line charts, stacking charts, step line charts, data visualization, syncfusion winforms] -->