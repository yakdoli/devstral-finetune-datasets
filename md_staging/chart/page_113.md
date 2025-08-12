```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_113.jpeg
document_name: chart
page_number: 113
page_id: chart#page_113
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:22:31Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Displays a RangeArea Chart with a "Profit Range" dataset.
- Includes detailed chart specifications and C# code for adding Step Area series to the chart.

## Content

### RangeArea Chart

![RangeArea Chart](https://chartControl1.png)
**Figure 61: RangeArea Chart**

#### Chart Details
| Details                |                 |
|------------------------|-----------------|
| Number of Y values per point | 2          |
| Maximum Number of Series | Unlimited |
| Minimum Number of Series  | 1           |

#### Step Area Series Addition
Step Area series can be added to the chart using the following C# code:

```csharp
ChartSeries series1 = this.chartControl1.Model.NewSeries("Profit Range", ChartSeriesType.RangeArea);
series1.Points.Add(0, 18, 50);
series1.Points.Add(1, 20, 49);
series1.Points.Add(2, 18, 52);
```

### Chart Description
The chart titled "chartControl1" visualizes a "Profit Range" over a span of years. It uses a RangeArea series type, with data points representing different profit ranges for each year. The range area chart effectively illustrates the variation in profit over a period, with upper and lower bounds for each point.

#### Chart Key Features
- **Y-axis:** Represents "Profit Range."
- **X-axis:** Represents the years over which the profit data is plotted.
- **Data Points:** Include specific profit values for each year, such as 50, 49, 52, etc.

## Code Examples

The provided C# code demonstrates how to create and configure a RangeArea Chart using `Syncfusion`'s chart control for Windows Forms. This example adds a "Profit Range" series and populates it with sample data points to illustrate the profit variation over time.

## API Reference

This section references the API used in the code example:
- **`ChartSeries`**: Represents a series in the chart.
- **`Model.NewSeries`**: Creates a new series with the specified name and type.
- **`Points.Add`**: Adds a data point to the series.

## Notes
- The chart is designed to show a detailed view of the profit range over a specified period.
- The use of a RangeArea chart is ideal for visualizing variability and can help in making informed decisions based onprofit trends.

<!-- tags: [essential chart, windows forms, rangearea chart, profit range, step area series, syncfusion, chartcontrol] keywords: [rangearea, profit range, chart series, windows forms, chart control, csharp, step area] -->
```