```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_273.jpeg
document_name: chart
page_number: 273
page_id: chart#page_273
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:32:06Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- A chart with a legend for the series, illustrating product performance.
- Overview of chart types and their application.
- Detailed explanation of the `NumberOfHistogramIntervals` property in histogram charts.

## Content

### Chart with Legend for the Series

#### Figure 162: Chart with Legend for the Series

![Chart with Legend for the Series](#)
*Illustrates Name*

The chart above demonstrates the performance of `Product1` across different categories, represented as bars with their corresponding values indicated by red dots.

### See Also

- Chart Types

### 4.5.1.48 NumberOfHistogramIntervals

#### Overview
Gets or sets the number of Histogram intervals.

#### Details

| Key                           | Description                                  |
|-------------------------------|----------------------------------------------|
| Possible Values               | Any numeric value                            |
| Default Value                 | 10                                          |
| 2D / 3D Limitations          | No                                           |
| Applies to Chart Element      | All Series Points                            |
| Applies to Chart Types       | Histogram Chart                              |

## API Reference

### NumberOfHistogramIntervals
- **Namespace**: `Syncfusion.Windows.Forms.Chart`
- **Class**: `SfChart`
- **Property**:
```csharp
public int NumberOfHistogramIntervals { get; set; }
```
**Parameters**:
- **Name** | **Type** | **Description** | **Default** | **Required**
  `NumberOfHistogramIntervals` | `int` | Gets or sets the number of Histogram intervals. | `10` | No

**Returns**:
- Type: `int`
  The number of intervals in a Histogram chart.

**Exceptions**:
- Not explicitly mentioned; typical validation for numeric properties applies.

## Code Examples

### Setting the Number of Histogram Intervals

Here is an example demonstrating how to set the `NumberOfHistogramIntervals` in a code snippet:

```csharp
// Create a new SfChart instance
SfChart chart = new SfChart();

// Create a Histogram series
HistogramSeries series = new HistogramSeries();

// Set the dataset for the series
series.DataSource = yourData;

// Set the number of intervals for the histogram
series.NumberOfHistogramIntervals = 15;

// Add the series to the chart
chart.Series.Add(series);

// Add the chart to the form
this.Controls.Add(chart);
```

## Page-level Navigation/TOC (if applicable)
- Chart with Legend for the Series
- See Also
- 4.5.1.48 NumberOfHistogramIntervals

## Cross References
- Chart Types

<!-- tags: [Syncfusion Windows Forms, Chart, Histogram, NumberOfHistogramIntervals, product] keywords: [chart, legend, series, histogram, intervals, performance, windows forms] -->
```