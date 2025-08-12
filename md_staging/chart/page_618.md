```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_618.jpeg
document_name: chart
page_number: 618
page_id: chart#page_618
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:56:24Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrating how to add and customize trend lines in a chart.
- Explaining the use of conditional logic to color trend lines.
- Detailing the customization of data points using the `IChartSeriesIndexedModel` interface.

## Content

```csharp
tseries.Points.Add(ptEnd)
Me.chart.Series.Add(tseries)
tseries.LegendItem.Visible = False

' Specify the color for the lines.
If ptStart.YValues(0) < ptEnd.YValues(0) Then
    tseries.Style.Interior = New Syncfusion.Drawing.BrushInfo(Color.DarkGreen)
Else
    tseries.Style.Interior = New Syncfusion.Drawing.BrushInfo(Color.Red)
End If
```

![Custom Trend Line Chart](figure_373.png)
***Figure 373: Custom TrendLines added to Chart***

### How to customize the data points for Chart Series

You can customize the data points by exposing the `IChartSeriesIndexedModel` interface to the series. The default Series store is an implementation of the `IChartSeriesModel`. By implementing this interface, we can set it as the underlying data.

## API Reference (if applicable)

## Code Examples (multi-language supported)

## Page-level Navigation/TOC (if applicable)

## Cross References

## RAG Annotations
<!-- tags: [charts, trendlines, customization, IChartSeriesIndexedModel, SyncfusionWinforms, 11.4.0.26] keywords: [charts, trendlines, customization, data points, IChartSeriesIndexedModel] -->
```