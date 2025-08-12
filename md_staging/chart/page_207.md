```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_207.jpeg
document_name: chart
page_number: 207
page_id: chart#page_207
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:27:24Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview

- Demonstrates how to add error bars to a `ColumnChart`.
- Explains the process of specifying error bars in a chart series.
- Code example provided for implementing error bars in a chart.

## Content

### Adding Error Bars to a ColumnChart

The following code snippet shows how to add error bars to a `ColumnChart` in a Windows Forms application:

```csharp
series.Points.Add(1, New Double() { 20, 5 })
series.Points.Add(2, New Double() { 70, 6 })
series.Points.Add(3, New Double() { 10, 3 })
series.Points.Add(4, New Double() { 40, 6 })
series.Text = series.Name

' Adding Series to the Chart
Me.chartControl1.Series.Add(series)

' Specifies the Error Bar in Column chart.
Private Me.chartControl1.Series(0).DrawErrorBars = True
```

### Visual Representation

#### Figure 116: ColumnChart with ErrorBars
![ColumnChart with ErrorBars](https://i.imgur.com/1234567.png)

This figure illustrates a `ColumnChart` with error bars displayed for each column.

#### Error Bars in a Line Chart
![Error Bars](https://i.imgur.com/ABCDEFG.png)

This figure shows error bars in a line chart with markers.

## API Reference

### Methods and Properties

- **`Add()`**: Adds points to a chart series.
- **`DrawErrorBars`**: A property to enable or disable the display of error bars in the chart.

### Parameters

- **`Series`**: Specifies the chart series to which the error bars are added.
- **`Points`**: Defines the data points for the chart series.

### Returns

- **True**: Indicates that error bars are drawn on the chart.
- **False**: Indicates that error bars are not drawn on the chart.

## Code Examples

The following example demonstrates how to implement error bars in a chart:

```csharp
series.Points.Add(1, New Double() { 20, 5 })
series.Points.Add(2, New Double() { 70, 6 })
series.Points.Add(3, New Double() { 10, 3 })
series.Points.Add(4, New Double() { 40, 6 })
series.Text = series.Name

' Adding Series to the Chart
Me.chartControl1.Series.Add(series)

' Specifies the Error Bar in Column chart.
Private Me.chartControl1.Series(0).DrawErrorBars = True
```

## RAG Annotations

<!-- tags: [chart, error bars, column chart, line chart, windows forms, series, points, draw error bars, essential chart, visual representation, api reference, parameters, returns] keywords: [syncfusion, winforms, error bars, chart series, points, column chart, line chart, visual representation, api reference, parameters, returns] -->
```