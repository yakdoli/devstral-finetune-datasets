```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_178.jpeg
document_name: chart
page_number: 178
page_id: chart#page_178
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:26:02Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Explains how to configure the AngleOffset property for pie charts in Windows Forms.
- Demonstrates setting Chart Series type to Pie and configuring 3D effects.
- Includes sample code in C# and VB.NET for implementation.

## Content

### Properties of AngleOffset

| **Details**               | **Description**                                                                 |
|---------------------------|----------------------------------------------------------------------------------|
| Possible Values           | Accepts real values like 45f, 90f etc.                                        |
| Default Value             | 0                                                                              |
| 2D / 3D Limitations      | No                                                                             |
| Applies to Chart Element  | All Series                                                                     |
| Applies to Chart Types    | PieChart                                                                       |

### Sample Code

#### [C#]

```csharp
// Create chart series and add data points into it.
ChartSeries series1 = this.chartControl1.Model.NewSeries("Market");
series1.Points.Add(0, 20);
series1.Points.Add(1, 28);
series1.Type = ChartSeriesType.Pie;
// Add the series to the chart series collection.
this.chartControl1.Series.Add(series1);

this.chartControl1.Series3D = true;
this.chartControl1.Series[0].ConfigItems.PieItem.AngleOffset = 45f;
```

#### [VB.NET]

```vbnet
' Create chart series and add data points into it.
Private series1 As ChartSeries =
Me.chartControl1.Model.NewSeries("Market")
series1.Points.Add(0, 20)
series1.Points.Add(1, 28)
series1.Type = ChartSeriesType.Pie
' Add the series to the chart series collection.
Me.chartControl1.Series.Add(series1)

Me.chartControl1.Series3D = True
Me.chartControl1.Series(0).ConfigItems.PieItem.AngleOffset = 45f
```

## API Reference

### Methods

- `AngleOffset`: Configures the offset angle for pie slices in 3D mode.
- `Series3D`: Enables 3D rendering for chart series.

### Members

- **Name**: AngleOffset
- **Type**: Real number (float)
- **Default**: 0
- **Description**: Sets the starting angle offset for pie slices in the chart.

## Code Examples

### C#

```csharp
// Example of configuring a 3D pie chart with custom angle offset.
ChartSeries series = chartControl.Model.NewSeries("SampleData");
series.Points.Add(0, 50);
series.Points.Add(1, 30);
series.Type = ChartSeriesType.Pie;
chartControl.Series.Add(series);

chartControl.Series3D = true;
chartControl.Series[0].ConfigItems.PieItem.AngleOffset = 90f;
```

### VB.NET

```vbnet
' Example of configuring a 3D pie chart with custom angle offset.
Dim series As ChartSeries = chartControl.Model.NewSeries("SampleData")
series.Points.Add(0, 50)
series.Points.Add(1, 30)
series.Type = ChartSeriesType.Pie
chartControl.Series.Add(series)

chartControl.Series3D = True
chartControl.Series(0).ConfigItems.PieItem.AngleOffset = 90f
```

## Notes

- The AngleOffset property is particularly useful for rotating pie slices to improve visualization in 3D charts.

# Page-level Navigation/TOC (if applicable)
- Use the "For further information, see" or similar text for cross-references.

## Cross References
- Refer to documentation on Chart Series types and 3D rendering for more details.

## RAG Annotations
<!-- tags: [chart, piechart, windowsforms, angleoffset, 3d, syncfusion] keywords: [chartseries, series3d, angleoffset, piechart, windowsforms, 3d] -->
```