```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_098.jpeg
document_name: chart
page_number: 098
page_id: chart#page_098
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:21:03Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Daily Performance

![Figure: Daily Performance Chart displaying Stacking Column Series](image.png)
*Figure 54: Chart displaying Stacking Column Series*

### Chart Details

| **Details**               |
|----------------------------|
| Number of Y values per point | 1                 |
| Number of Series           | Two or more (A single series will render just like a bar chart). |
| Cannot be Combined with    | Pie, Bar, Stacked Bar charts, Polar, Radar. |

Stacking column series can be added to the chart using the following code.

### Code Example

```csharp
[C#]

// Create chart series and add data points into it.
ChartSeries series = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.StackingColumn);
series.Points.Add(0, 1);
series.Points.Add(1, 3);
series.Points.Add(2, 4);

ChartSeries series2 = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.StackingColumn);
series2.Points.Add(0, 2);
series2.Points.Add(1, 1);
```

<!-- tags: [Windows Forms, Stacking Column Series, Chart, Syncfusion Winforms, Daily Performance] keywords: [Stacking, Column Series, Chart Details, C#, Code Example, Daily Performance, Team 1, Team 2] -->
```