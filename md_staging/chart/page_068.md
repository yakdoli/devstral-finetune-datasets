```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_068.jpeg
document_name: chart
page_number: 068
page_id: chart#page_068
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:19:59Z
fidelity: lossless
-->

## Chart Performance Optimization Properties

This section provides insights into key properties and settings within the Syncfusion Windows Forms Chart control that can be optimized for better performance.

| Property/Settings | Description |
|-------------------|-------------|
| CalcRegions       | This property by default is `true`. It controls the Tooltips, Autohighlighting properties, and RegionHit events. If these properties and events are not used, this property can be set to `false` for better performance. |
| ChartSeries.EnableStyles | Disabling this property will in turn disable the point symbols and point text, which speeds up the chart. |
| ChartSeries.Style.DisplayShadow | Setting this property to `false` will not render the series with shadow, which will increase the speed of the chart. <br> By default, this property is set to `false`. |
| Indexed           | The chart renders faster if the series is not indexed. This, of course, may or may not be possible in all cases. <br> By default, this property is `false`. |
| BackInterior      | The background style for the Chart control is specified using this property. If this property is not set with gradient or pattern style, it will help improve the performance of the chart. |

<!-- tags: [chart, performance, optimization, properties] keywords: [CalcRegions, ChartSeries, EnableStyles, DisplayShadow, Indexed, BackInterior, Tooltips, Autohighlighting, RegionHit, Speed, Render, Gradient, Pattern] -->
```