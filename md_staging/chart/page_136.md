```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_136.jpeg
document_name: chart
page_number: 136
page_id: chart#page_136
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:24:06Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

This chart requires two y values, the high value and the low value for the specified period.

## Overview

- This chart uses a Point and Figure series to display data over a specified period.
- It requires two Y values per point: the high value and the low value.
- It is suitable for visualizing financial or stock market data.

## Content

### Three Line Break Chart Example

#### Chart Details

The provided example illustrates a "Three Line Break Chart for Microsoft" with stock price data over a weekly period.

**Figure 77: Chart displaying Point And Figure Series**

[Insert Image Here]

**Description**:
- The chart shows the price movement of Microsoft stocks over a period from January 01 to January 31.
- The X-axis represents the date, with weekly intervals.
- The Y-axis represents the stock price, ranging from $20 to $45.

**Table: Chart Details**

| Details                     | Value                        |
|-----------------------------|------------------------------|
| Number of Y values per point | 2                            |
| Number of Series             | One                          |
| Cannot be Combined with      | Pie, Bar                     |

### Adding Point and Figure Series to the Chart

Point and Figure series can be added to the chart using the following C# code:

```csharp
// Create chart series and add data points into it.
ChartSeries series = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.PointAndFigure);
// Arguments: X value, low value, high value
series.Points.Add(0, 1, 5);
series.Points.Add(1, 3, 7);
```

### Usage Notes
- The Point and Figure series is particularly useful for illustrating price movements in financial markets.
- The high and low values for each X (date) are used to calculate the visual representation of the chart.
- The series cannot be combined with Pie or Bar chart types.

## API Reference

### Adding a Point and Figure Series

- **Namespace**: 
  - `Syncfusion.Windows.Forms.Chart`
- **Class**:
  - `ChartSeries`
  - `ChartSeriesCollection`
- **Methods**:
  - `NewSeries(string name, ChartSeriesType type)`: Creates a new series with the specified name and type.
  - `Points.Add(double x, double low, double high)`: Adds a data point with the specified X value, low value, and high value.

### Parameters

| Name          | Type    | Description                                    | Default | Required |
|---------------|---------|------------------------------------------------|---------|----------|
| `name`        | string  | The name of the series.                       |         | Yes      |
| `type`        | ChartSeriesType | The type of the series to be created.     |         | Yes      |
| `x`           | double  | The X value (e.g., date).                     |         | No       |
| `low`         | double  | The low value for the data point.             |         | No       |
| `high`        | double  | The high value for the data point.            |         | No       |

### Returns

- Type: `ChartSeries`
- Description: Returns a new instance of the `ChartSeries` class.

## Code Examples

### C# Example

```csharp
// Example: Adding a Point and Figure series to the chart
ChartSeries series = this.chartControl1.Model.NewSeries("Stock Prices", ChartSeriesType.PointAndFigure);
series.Points.Add(0, 30, 35);
series.Points.Add(1, 32, 37);
series.Points.Add(2, 33, 36);
```

### VB.NET Example

```vb
' Example: Adding a Point and Figure series to the chart
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Stock Prices", ChartSeriesType.PointAndFigure)
series.Points.Add(0, 30, 35)
series.Points.Add(1, 32, 37)
series.Points.Add(2, 33, 36)
```

## Page-level Navigation/TOC
- This page discusses the Point and Figure series in the Essential Chart for Windows Forms.
- It covers how to add a Point and Figure series, its usage notes, and relevant API references.

<!-- tags: [essential chart, windows forms, point and figure series, stock price, data visualization, chart series] keywords: [point and figure, high value, low value, data points, stock chart, financial visualization] -->
```