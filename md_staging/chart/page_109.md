```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_109.jpeg
document_name: chart
page_number: 109
page_id: chart#page_109
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:22:12Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Adds a stack area chart type with properties and configuration options.
- Demonstrates the usage of `StackArea100` chart type in C# and VB.NET.
- Highlights the inability to combine it with other chart types.

## Content

| **SupportMarker**       | **No**                          |
|--------------------------|---------------------------------|
| **Cannot be Combined with** | **Any other chart types.**  |

### [C#]

```csharp
ChartSeries series1 = chartControl1.Model.NewSeries("Series1", ChartSeriesType.StackingArea100);
series1.Points.Add(1, 20);
series1.Points.Add(2, 30);
series1.Points.Add(3, 10);
series1.Points.Add(4, 15);
series1.Points.Add(5, 25);
this.chartControl1.Series.Add(series1);

ChartSeries series2 = chartControl1.Model.NewSeries("Series2", ChartSeriesType.StackingArea100);
series2.Points.Add(1, 20);
series2.Points.Add(2, 10);
series2.Points.Add(3, 50);
series2.Points.Add(4, 15);
series2.Points.Add(5, 5);
this.chartControl1.Series.Add(series2);

ChartSeries series3 = chartControl1.Model.NewSeries("Series3", ChartSeriesType.StackingArea100);
series3.Points.Add(1, 20);
series3.Points.Add(2, 40);
series3.Points.Add(3, 10);
series3.Points.Add(4, 5);
series3.Points.Add(5, 20);
this.chartControl1.Series.Add(series3);
```

### [VB.NET]

```vb
Dim series1 As ChartSeries = chartControl1.Model.NewSeries("Series1", ChartSeriesType.StackingArea100)
series1.Points.Add(0, 20)
series1.Points.Add(1, 30)
series1.Points.Add(2, 10)
series1.Points.Add(3, 15)
series1.Points.Add(4, 25)
Me.chartControl1.Series.Add(series1)
```

### Conclusion
This page provides examples in both C# and VB.NET for implementing a `StackArea100` chart type within a Windows Forms application using Syncfusion controls.

## API Reference
- **Namespace**: Syncfusion.Windows.Forms.Chart
- **Class**: `ChartSeries`
- **Members**:
  - `NewSeries(name As String, type As ChartSeriesType)`: Creates a new chart series.
  - `Points.Add(x As Integer, y As Integer)`: Adds data points to the series.
  - `Series.Add(series As ChartSeries)`: Adds the series to the chart control.

## Code Examples
The provided code examples demonstrate how to create and configure a `StackArea100` chart series, add data points, and integrate it into the main chart control.

## Cross References
- Refer to the documentation for `ChartSeriesType` and `ChartSeries` for more details on available chart types and properties.
- See the main chart control documentation for additional design and event handling details.

<!-- tags: [syncfusion, winforms, chart, stack area, chart control] keywords: [chart series, C#, VB.NET, StackArea100, ChartControl, chart properties] -->
```