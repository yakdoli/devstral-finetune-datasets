```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_334.jpeg
document_name: chart
page_number: 334
page_id: chart#page_334
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:35:17Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates the usage of the chart control in Windows Forms.
- Explains key attributes and properties of the chart control.
- Covers the rendering of step area charts and step line charts.

## Content

### Figure 212: Inverted = "True"

![](./image.png)

**Figure 212: Inverted = "True"**

**See Also**
- [StepAreaChart](#StepAreaChart)
- [StepLine Chart](#StepLine Chart)

### 4.5.1.79 Summary

**Summary**

Provides access to summary information such as minimum/maximum values contained in this series at any given moment.

### Details

| **Possible Values** |  |
| --- | --- |
|  | • **MaxX** - Returns the maximum X value. |
|  | • **MaxY** - Returns the maximum Y value. |
|  | • **MinX** - Returns the minimum X value. |
|  | • **MinY** - Returns the minimum Y value. |
|  | • **ModelImpl** - Returns the model implemented. |
|  | • **GetYPercentage** - This method returns percentage value of series point in a Pie |

## API Reference
- **Namespace**: Syncfusion.Windows.Forms.Chart
- **Class**: ChartSeries
- **Methods**:
  - **MaxX**: Returns the maximum X value.
  - **MaxY**: Returns the maximum Y value.
  - **MinX**: Returns the minimum X value.
  - **MinY**: Returns the minimum Y value.
  - **ModelImpl**: Returns the model implemented.
  - **GetYPercentage**: Returns the percentage value of a series point in a Pie chart.

## Code Examples

### Example 1: Accessing Summary Information

```csharp
// Accessing maximum X value
double maxXValue = chartSeries.MaxX;

// Accessing maximum Y value
double maxYValue = chartSeries.MaxY;

// Accessing minimum X value
double minXValue = chartSeries.MinX;

// Accessing minimum Y value
double minYValue = chartSeries.MinY;
```

### Example 2: Implementing Model

```csharp
// Retrieving the implemented model
object model = chartSeries.ModelImpl;
```

## Cross References
- **StepAreaChart**: A type of chart that displays step area series.
- **StepLine Chart**: A type of chart that displays step line series.

<!-- tags: [chart, windows forms, summary, step area chart, step line chart] keywords: [minX, minY, maxX, maxY, modelImpl, getYPercentage] -->
```