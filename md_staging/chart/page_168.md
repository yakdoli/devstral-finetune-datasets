```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_168.jpeg
document_name: chart
page_number: 168
page_id: chart#page_168
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:26:34Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

```csharp
Me.sparkLine1.Markers.ShowHighPoint = True
Me.sparkLine1.Markers.ShowLowPoint = True
Me.sparkLine1.Markers.ShowStartPoint = True
Me.sparkLine1.Markers.ShowEndPoint = True
Me.sparkLine1.Markers.ShowNegativePoint = True

// To customize the marker color to low points
Me.sparkLine1.Markers.LowPointColor = new
BrushInfo(GradientStyle.BackwardDiagonal, Color.Blue, Color.Wheat)
```

![](image.png)

**Figure 94: Markers for WinLoss SparkLine**

### 4.5 Chart Series

#### Overview
- Provide data for the chart through the `ChartSeries`.
- `ChartSeries` acts as a wrapper around data that is to be displayed, and associates styles with the data.
- The data to be displayed is contained in either the `IChartSeriesModel` or the `IEditableChartSeriesModel` implementation.
- The style used to display the points is stored in a contained implementation of `IChartSeriesStylesModel`.

Here is some sample code to create a new series and add it to the chart.

```csharp
[C#]

// 1) One way to create a series:
ChartSeries series = new ChartSeries("Sales Performance",
ChartSeriesType.Bar);
series.Points.Add(0, 200);
series.Points.Add(1, 300);
// Remember to add the series to the chart.
chartControl1.Series.Add(series);
```

- **Copyright © 2013 Syncfusion. All rights reserved.** Page
```