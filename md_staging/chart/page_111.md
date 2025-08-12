```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_111.jpeg
document_name: chart
page_number: 111
page_id: chart#page_111
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:21:49Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Step Area Series

### Chart Details

#### Figure 60: Chart displaying Step Area Series
![Chart displaying Step Area Series](source_image.png)

The chart details are as follows:

| Details                        |                                                                   |
|--------------------------------|-------------------------------------------------------------------|
| **Number of Y values per point** | **1**                                                              |
| **Number of Series**           | **One or More.**                                                   |
| **Cannot be Combined with**    | **Pie, Bar, Stacked Bar charts, Polar and Radar.**                  |

### Adding Step Area Series to the Chart

Step Area series can be added to the chart using the following C# code:

```csharp
// Create chart series and add data points into it.
ChartSeries series = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.StepArea);
series.Points.Add(0, 1);
series.Points.Add(1, 3);
series.Points.Add(2, 4);
series.Points.Add(3, 2);
series.Points.Add(4, 3);

// Add the series to the chart series collection.
```

### Notes

- The chart series is created with a specified name and type as `StepArea`.
- Data points are added to the series using the `Points.Add` method.
- The series is then added to the chart's series collection.

## Additional Information

Step Area Series is a visualization technique used to represent data trends over time. It features vertical lines connecting data points, forming stepped areas that make it easier to compare data across different categories or time periods.

## Copyright Notice

© 2013 Syncfusion. All rights reserved.

## Page Footer

Page 111 | Syncfusion Winforms Documentation
```

### RAG Annotations
```html
<!-- tags: [Essential Chart, Windows Forms, Step Area Series, C# code example] keywords: [Step Area Series, Chart, Windows Forms, Syncfusion, Data Visualization, C#] -->
```