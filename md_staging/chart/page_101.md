```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_101.jpeg
document_name: chart
page_number: 101
page_id: chart#page_101
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:21:43Z
fidelity: lossless
--> 

## Essential Chart for Windows Forms

### Code Example

```csharp
this.chartControl1.Series.Add(series1);
```

### VB.NET Code Example

```vb
Dim series1 As ChartSeries = Me.chartControl1.Model.NewSeries("Series", ChartSeriesType.StackingColumn100)
series1.Points.Add(0, 25.3)
series1.Points.Add(1, 45.7)
series1.Points.Add(2, 97.3)
series1.Points.Add(3, 20.6)
series1.Points.Add(4, 125.8)
series1.Points.Add(5, 216.1)
Me.chartControl1.Series.Add(series1)
```

### Customization Options

- Border
- ColumnWidthMode
- ColumnFixedWidth
- DisplayShadow
- DisplayText
- DrawSeriesNameInDepth
- ElementBorders
- ImageIndex
- Images
- LightAngle
- LightColor
- Rotate
- Spacing
- Spacing Between Series
- ShadingMode
- ShadowInterior
- ShadowOffset
- ZOrder
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

### See Also

- StackedArea100 Chart
- StackedBar100 Chart

---

## 4.4.4 Area Charts

**Overview**
- Area Charts emphasize the degree of change of the values over a period of time.
- Instead of rendering data as discreet bars or columns, an Area Chart renders them in a continuous ebb and flow pattern as defined against the y-axis.

### Features and Customization
- **Alpha-Blending Support**: Allows for layering of multiple series areas with adjustable opacity.
- **Customizable Look and Feel**: The user can easily tailor the appearance of the Area Chart.
- **Variety of Area Chart Types**: Essential Chart supports multiple variations of Area Charts, including:

### Supported Area Chart Types
- StackedArea100 Chart
- StackedBar100 Chart

## Summary

Area Charts are particularly effective for visualizing trends and changes over time, offering a host of customization options to suit various data presentation needs.

## References
- For additional details, refer to the StackedArea100 Chart and StackedBar100 Chart sections.

<!-- tags: [winforms, chart, area chart, stacking column, customization, series, essential chart] keywords: [stacked area, stacked bar, ebb, flow, alpha blending, customization, variety, stacking column] -->
```