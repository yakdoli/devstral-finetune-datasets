```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_084.jpeg
document_name: chart
page_number: 084
page_id: chart#page_084
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:20:53Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Code Examples

### C# Example

```csharp
// Create chart series and add data point into it.
ChartSeries series = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.StackingBar);
series.Points.Add(0, 1);
series.Points.Add(1, 3);
series.Points.Add(2, 4);

ChartSeries series2 = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.StackingBar);
series2.Points.Add(0, 2);
series2.Points.Add(1, 1);
series2.Points.Add(2, 1);

// Add the series to the chart series collection.
this.chartControl1.Series.Add(series);
this.chartControl1.Series.Add(series2);
```

### VB.NET Example

```vb.net
' Create chart series and add data points into it.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.StackingBar)
series.Points.Add(0, 1)
series.Points.Add(1, 3)
series.Points.Add(2, 4)

Dim series2 As ChartSeries = Me.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.StackingBar)
series2.Points.Add(0, 2)
series2.Points.Add(1, 1)
series2.Points.Add(2, 1)

' Add the series to the chart series collection.
Me.chartControl1.Series.Add(series)
Me.chartControl1.Series.Add(series2)
```

### Customization Options

Customization options for the chart control include:

- `Border`
- `ColumnDrawMode`
- `DisplayText`
- `DrawSeriesNameInDepth`
- `ElementBorders`
- `HighlightInterior`
- `ImageIndex`
- `Images`
- `LightAngle`
- `LightColor`
- `Rotate`
- `Spacing`
- `Spacing Between Series`
- `ShadingMode`
- `ShadowInterior`
- `ShadowOffset`
- `ZOrder`
- `FancyToolTip`
- `Font`
- `Interior`
- `LegendItem`
- `Name`

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.

## Cross References
- See also: Other sections or pages discussing chart customization and related topics.

<!-- tags: [Syncfusion, WinForms, Chart, Series, Customization, StackingBar] keywords: [essential chart, windows forms, chart series, data points, customization options, stacking bar chart, chart control, properties, methods, chart options] -->
```