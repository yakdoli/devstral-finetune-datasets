```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_096.jpeg
document_name: chart
page_number: 096
page_id: chart#page_096
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:21:50Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Daily Performance Chart

### Overview

- **Purpose**: Displays daily performance metrics for two teams.
- **Key Features**:
  - **Team 1 and Team 2**: Performance is represented by two columns per day.
  - **Daily Review**: Tracks performance over five days.
  - **Range Series**: Indicates the range of task completion.

### Chart Details

| **Details**                   | **Description**                                                                 |
| ------------------------------ | -------------------------------------------------------------------------------- |
| Number of Y values per point  | 2                                                                                |
| Number of Series              | One or More                                                                     |
| Cannot be Combined with       | Pie, Bar, Stacked Bar charts, Polar, Radar.                                     |

### Implementation Details

The following code snippet illustrates how to create and configure a `ColumnRange` series in a chart using C# and VB.NET.

#### C#

```csharp
// Create chart series and add data points into it.
ChartSeries series = this.ChartControl1.Model.NewSeries("Series 0", ChartSeriesType.ColumnRange);
series.Points.Add(0, 100, 400);
series.Points.Add(2, 300, 600);
series.Points.Add(4, 200, 700);
series.Text = series.Name;

// Add the series to the chart series collection.
this.ChartControl1.Series.Add(series);
```

#### VB.NET

```vb
' Create chart series and add data point into it.
```

## API Reference

### Creating a `ColumnRange` Series

- **Namespace**: `Syncfusion.Windows.Forms.Chart`
- **Class**: `ChartSeries`
- **Methods**:
  - `NewSeries(string name, ChartSeriesType type)`: Creates a new chart series.
  - `Points.Add(int x, int y1, int y2)`: Adds a data point with a range to the series.
  - `Series.Add(ChartSeries series)`: Adds a series to the chart.

### Parameters

| **Name**        | **Type**    | **Description**                                                                 | **Default** | **Required** |
|----------------- |------------- |--------------------------------------------------------------------------------- |------------ |------------- |
| `name`          | `string`    | The name of the series.                                                        | `null`      | Yes          |
| `type`          | `ChartSeriesType` | The type of the series (e.g., `ColumnRange`).                             | `null`      | Yes          |
| `x`             | `int`       | The x-coordinate of the data point.                                           | `0`         | Yes          |
| `y1`            | `int`       | The lower range value of the data point.                                      | `0`         | Yes          |
| `y2`            | `int`       | The upper range value of the data point.                                      | `0`         | Yes          |

## Code Examples

### Establishing a Chart with `ColumnRange` Series

The provided C# code demonstrates the creation of a `ColumnRange` series, where each data point represents a range of values over time. The series is then added to the chart control.

## Cross References

- See also: Documentation on other chart types and series in the Syncfusion Winforms Chart control.

<!-- tags: [chart, columnrange, windows forms, syncfusion winforms, version: 11.4.0.26] keywords: [daily performance, range series, column series, task completion, team performance chart] -->
```
