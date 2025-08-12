```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_118.jpeg
document_name: chart
page_number: 118
page_id: chart#page_118
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:22:11Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Content

### Funnel Chart Example Code

```csharp
series1.Points.Add(5, 216.1);
this.chartControl1.Series.Add(series1);
```

```vb
[VB.NET]

Dim series1 As ChartSeries = Me.chartControl1.Model.NewSeries("Funnel chart", ChartSeriesType.Funnel)
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
- DisplayText
- DrawSeriesNameInDepth
- FigureBase
- FunnelMode
- GapRatio
- HighlightInterior
- LabelPlacement
- LabelStyle
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
- ShowDataBindLabels

### Pyramid Chart

Pyramid chart is similar to the funnel chart. It's often used for geographical purposes. The Pyramid Chart type displays the data, which when totalled will be 100%. This type of chart is a single series chart representing the data as portions of 100%, and this chart does not use any axes. Pyramid chart can be viewed as 2D or 3D.

The following images are some sample Pyramid Charts.

## API Reference

### Properties
- Border
- DisplayText
- DrawSeriesNameInDepth
- FigureBase
- FunnelMode
- GapRatio
- HighlightInterior
- LabelPlacement
- LabelStyle
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
- ShowDataBindLabels

## Code Examples

### C# Example

```csharp
series1.Points.Add(5, 216.1);
this.chartControl1.Series.Add(series1);
```

### VB.NET Example

```vb
[VB.NET]

Dim series1 As ChartSeries = Me.chartControl1.Model.NewSeries("Funnel chart", ChartSeriesType.Funnel)
series1.Points.Add(0, 25.3)
series1.Points.Add(1, 45.7)
series1.Points.Add(2, 97.3)
series1.Points.Add(3, 20.6)
series1.Points.Add(4, 125.8)
series1.Points.Add(5, 216.1)
Me.chartControl1.Series.Add(series1)
```

## Page-level Navigation/TOC

- [4.4.5.2 Pyramid Chart](#chart#page_118#pyramid-chart)
- [Customization Options](#chart#page_118#customization-options)

## Cross References

- See also: Funnel Chart, Chart Customization, Data Visualization

<!-- tags: [syncfusion, winforms, chart, funnel chart, pyramid chart, customization options, data visualization] keywords: [funnel chart, pyramid chart, custom options, visualization] -->
```