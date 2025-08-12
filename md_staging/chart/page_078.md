```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_078.jpeg
document_name: chart
page_number: 078
page_id: chart#page_078
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:19:56Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Code Example

```csharp
// Add the series to the chart series collection.
this.chartControl1.Series.Add(series1);
```

##### [VB.NET]

```vbnet
' Create chart series and add data points into it.
Dim series1 As ChartSeries = Me.chartControl1.Model.NewSeries(" Series 1", ChartSeriesType.RotatedSpline)

series1.Points.Add(1, 326)
series1.Points.Add(2, 491)
series1.Points.Add(3, 382)
series1.Points.Add(4, 482)

' Add the series to the chart series collection.
Me.chartControl1.Series.Add(series1)
```

### Customization Options

- DisplayShadow
- DisplayText
- DrawSeriesNameInDepth
- ElementBorders
- HighlightInterior
- ImageIndex
- Images
- Spacing Between Series
- ShadowInterior
- ShadowOffset
- FancyToolTip
- Font
- Interior
- LegendItem
- Name
- PointsToolTipFormat
- SmartLabels
- Summary
- Text
- TextColor
- TextFormat
- TextOffset
- TextOrientation
- Visible

### 4.4.1.4 Step Line Chart

**Description:**  
Step Line Charts use horizontal and vertical lines to connect data points, resulting in a step-like progression.
```html

<!-- tags: [Syncfusion, Winforms, Chart, Step Line Chart, Series, Customization, API Reference, Code Examples, DisplayOptions, Legend, Tooltip, TextFormatting] keywords: [chart series, data points, step line chart, horizontal lines, vertical lines, step progression, customization options, display shadow, display text, chart series name, element borders, highlight interior, image index, shadow interior, shadow offset, fancy tooltips, text color, text orientation, visible, step line chart] -->
```