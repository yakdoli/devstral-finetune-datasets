```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_144.jpeg
document_name: chart
page_number: 144
page_id: chart#page_144
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:24:47Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Overview
- Adding Box and Whisker series to a chart.
- Demonstrates how to create and customize charts using C# and VB.NET.

## Content

### Box and Whisker Series

Box and Whisker series can be added to the chart using the following code.

#### C#
```csharp
// Create chart series and add data points into it.
ChartSeries series1 = this.chartControl1.Model.NewSeries("Series 1", ChartSeriesType.BoxAndWhisker);
series1.Points.Add(1, 5, 8, 12, 15, 18);
series1.Points.Add(2, 4, 6, 10, 12, 14);
series1.Points.Add(3, 2, 4, 7, 14, 18);

ChartSeries series2 = this.chartControl1.Model.NewSeries("Series 2", ChartSeriesType.BoxAndWhisker);
series2.Points.Add(1, 6, 9, 15, 18, 20);
series2.Points.Add(2, 7, 9, 13, 15, 16);
series2.Points.Add(3, 6, 8, 10, 15, 19);

// Add the series to the chart series collection.
this.chartControl1.Series.Add(series1);
this.chartControl1.Series.Add(series2);
```

#### VB.NET
```vb
' Create chart series and add data points into it.
Dim series1 As ChartSeries = Me.chartControl1.Model.NewSeries("Series 1", ChartSeriesType.BoxAndWhisker)
series1.Points.Add(1, 5, 8, 12, 15, 18)
series1.Points.Add(2, 4, 6, 10, 12, 14)
series1.Points.Add(3, 2, 4, 7, 14, 18)

Dim series2 As ChartSeries = Me.chartControl1.Model.NewSeries("Series 2", ChartSeriesType.BoxAndWhisker)
series2.Points.Add(1, 6, 9, 15, 18, 20)
series2.Points.Add(2, 7, 9, 13, 15, 16)
series2.Points.Add(3, 6, 8, 10, 15, 19)

' Add the series to the chart series collection.
Me.chartControl1.Series.Add(series1)
Me.chartControl1.Series.Add(series2)
```

### Customization Options

- Border
- ColumnDrawMode
- DisplayShadow
- DisplayText
- ElementBorders
- HighlightInterior

## API Reference

### ChartSeries Members
- **Points**: Collection for adding data points.
- **Model.NewSeries**: Method for creating a new chart series.
- **ChartSeriesType.BoxAndWhisker**: Type for representing a Box and Whisker series.

### Customization Properties
- **Border**: Used for configuring borders around chart elements.
- **ColumnDrawMode**: Controls the rendering mode for columns.
- **DisplayShadow**: Enables or disables shadow display for chart elements.
- **DisplayText**: Controls the visibility of text on chart elements.
- **ElementBorders**: Configures borders for individual chart elements.
- **HighlightInterior**: Highlights the interior of the chart elements.

## Code Examples

The provided examples demonstrate how to:
1. Create instances of `ChartSeries` for Box and Whisker series.
2. Populate data points into each series.
3. Add the series to the `chartControl1` for display.

### Notes
- The `BoxAndWhisker` chart type is useful for visualizing data distributions and identifying outliers.
- Ensure the chart control is properly initialized before adding series.

## Tags and Keywords
<!-- tags: [WinForms, Chart, BoxAndWhisker, ChartSeries, Border, DisplayShadow, ElementBorders, HighlightInterior] keywords: [box and whisker, chart series, data points, customization, visualization] -->
```