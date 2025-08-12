<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_077.jpeg
document_name: chart
page_number: 077
page_id: chart#page_077
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:20:18Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- This page describes the usage of the Rotated Spline Series in Windows Forms charts.
- It provides details on how to add a Rotated Spline series to a chart using C# code.

## Content

### Chart Details
#### Figure 44: Chart displaying a Rotated Spline Series

The following table provides details about the Rotated Spline Series:

| **Details**                    | **Description**                                 |
|--------------------------------|------------------------------------------------|
| Number of Y values per point   | 1                                              |
| Number of Series                | One or More.                                   |
| Cannot be Combined with        | Pie, Bar, Stacked Bar, Polar, Radar.          |

Rotated Spline series can be added to the chart using the following code:

```csharp
[C#]

// Create chart series and add data points into it.
ChartSeries series1 = this.chartControl1.Model.NewSeries(" Series 1", ChartSeriesType.RotatedSpline );

series1.Points.Add(1, 326);
series1.Points.Add(2, 491);
series1.Points.Add(3, 382);
series1.Points.Add(4, 482);
```

## API Reference
- `ChartSeries`: Represents a series in the chart.
- `Model.NewSeries`: Creates a new series with the specified name and type.
- `Points.Add`: Adds a data point to the series with the given X and Y values.

## Code Examples
The provided C# code snippet demonstrates how to add a Rotated Spline series to a chart and populate it with data points. This example shows how to create a series, set its type to `RotatedSpline`, and add four data points.

## Page-level Navigation/TOC
- Chart Details
- Rotated Spline Series Code Example

## Cross References
- See also: `ChartControl.Model`, `ChartSeriesType`, `Points` for more details on related components.

<!-- tags: [syncfusion, winforms, chart, rotated-spline-series, version:11.4.0.26] keywords: [chart, series, rotated spline, windows forms, data points, C# code] -->