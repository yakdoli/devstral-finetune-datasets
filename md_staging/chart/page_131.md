```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_131.jpeg
document_name: chart
page_number: 131
page_id: chart#page_131
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:22:50Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Chart displaying Hi Lo Open Close Series.
- Understanding the chart details and implementation using C#.

## Content

### Chart Displaying Hi Lo Open Close Series

#### Figure 74: Chart displaying Hi Lo Open Close Series

![](attachment:Stock_Price_Summary)

---

#### Chart Details

| Details                  | Description                                       |
|--------------------------|---------------------------------------------------|
| Number of Y values per point | 4.                                            |
| Number of Series          | One or More.                                    |
| Cannot be Combined with   | Pie, Bar, Stacked Bar charts, Polar, Radar    |

---

#### Hi Lo Open Close Series Addition

Hi Lo Open Close series can be added to the chart using the following C# code:

```csharp
// Create chart series and add data point into it.
ChartSeries series = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.HiLoOpenClose);
// Arguments: X value, High, Low, Open, Close
series.Points.Add(0, 5, 1, 3, 4);
series.Points.Add(1, 8, 7, 4, 7);
series.Points.Add(2, 8, 4, 5, 6);
```

## Footer
© 2013 Syncfusion. All rights reserved. 131 | Page

<!-- tags: [chart, windows forms, syncfusion winforms, his lo open close series, c# implementation, api] keywords: [chart, windows forms, syncfusion, his lo open close, stock price summary, c#, chartcontrol, newseries, point, series type, high, low, open, close, pie chart, bar chart, stacked bar chart, polar chart, radar chart, documentation] -->
```