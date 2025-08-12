```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_110.jpeg
document_name: chart
page_number: 110
page_id: chart#page_110
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:21:40Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Code Example

```csharp
Dim series2 As ChartSeries = chartControl1.Model.NewSeries("Series2", ChartSeriesType.StackingArea100)
series2.Points.Add(0, 20)
series2.Points.Add(1, 10)
series2.Points.Add(2, 50)
series2.Points.Add(3, 15)
series2.Points.Add(4, 5)
Me.chartControl1.Series.Add(series2)

Dim series3 As ChartSeries = chartControl1.Model.NewSeries("Series3", ChartSeriesType.StackingArea100)
series3.Points.Add(0, 20)
series3.Points.Add(1, 40)
series3.Points.Add(2, 10)
series3.Points.Add(3, 5)
series3.Points.Add(4, 20)
Me.chartControl1.Series.Add(series3)
```

## Customization Options

- Border, DisplayText, DrawSeriesNameInDepth, ElementBorders, HighlightInterior, ImageIndex, Rotate, SeriesToolTipFormat, Spacing Between Series
- ZOrder, FancyToolTip, Font, Interior, LegendItem, Name, PointsToolTipFormat, SmartLabels, Summary, Text, TextColor, TextFormat, TextOffset, TextOrientation, Visible

### See Also

- StackedBar100 Chart
- StackedColumn100Chart

## 4.4.4.5 Step Area Chart

Step Area Charts are similar to regular area chart except that instead of a straight line tracing the shortest path between points, the values are connected by continuous vertical and horizontal lines forming a step-like progression.

The following image shows a sample Step Area Chart.

## Page-level Navigation/TOC

- Essential Chart for Windows Forms
  - Customization Options
  - Step Area Chart

## Cross References

- See Also: StackedBar100 Chart, StackedColumn100Chart

## API Reference

- Not explicitly detailed in the text.

## Code Examples

- See code example above.

<!-- tags: [syncfusion, winforms, chart, step area chart, customization options] keywords: [StackedBar100, StackedColumn100, Step Area Chart, Customization Options] -->
```
