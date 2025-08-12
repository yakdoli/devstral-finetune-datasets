```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_146.jpeg
document_name: chart
page_number: 146
page_id: chart#page_146
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:23:51Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Cannot be Combined with

| Description                                        |
|---------------------------------------------------|
| Any other chart types.                            |

## Adding Pie Series to the Chart

Pie series can be added to the chart using the following code.

### Code Example in C#

```csharp
// Create chart series and add data points into it.
ChartSeries series = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Pie);
series.Points.Add(0, 1);
series.Points.Add(1, 3);
series.Points.Add(2, 4);

// Add the series to the chart series collection.
this.chartControl1.Series.Add(series);
```

### Code Example in VB.NET

```vb
' Create chart series and add data points into it.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Pie)
series.Points.Add(0, 1)
series.Points.Add(1, 3)
series.Points.Add(2, 4)

' Add the series to the chart series collection.
Me.chartControl1.Series.Add(series)
```

### Customization Options

- AngleOffset
- Border
- DisplayShadow
- DisplayText
- DoughnutCoefficient
- DrawSeriesNameInDepth
- ElementBorders
- ExplodedAll
- ExplodedIndex
- ExplosionOffset
- FillMode
- Gradient
- HeightByAreaDepth
- HeightCoefficient
- HighlightInterior
- InSideRadius
- OptimizePiePointPositions
- PieType
- ShadowInterior
- ShadowOffset
- ShowTicks
- VisibleAllPies
- FancyToolTip
- Font
- Interior
- LegendlItem
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

## See Also

- [unclear]
```


<!-- tags: [Windows Forms, Chart, Pie Series, Customization Options] keywords: [Windows Forms, Chart, Syncfusion, Pie Series, Customization Options, Code Examples, C#, VB.NET] -->
```