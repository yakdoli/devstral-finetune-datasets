```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_141.jpeg
document_name: chart
page_number: 141
page_id: chart#page_141
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:24:11Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Chart Series Properties

The table below outlines key properties of the Three Line Break series:

| Property                    | Value          |
|-----------------------------|----------------|
| Number of Y values per point | 1              |
| Number of Series            | One            |
| Cannot be Combined with     | Pie, Bar       |

### Adding Three Line Break Series

Three Line Break series can be added to the chart using the following code:

#### [C#]

```csharp
// Create chart series and add data points into it.
ChartSeries series = this.chartControl1.Model.NewSeries ("Series Name", ChartSeriesType.ThreeLineBreak);
series.Points.Add (0, 1);
series.Points.Add (1, 3);
series.Points.Add (2, 4);

// Add series to the chart series collection.
this.chartControl1.Series.Add (series);
```

#### [VB.NET]

```vb.net
' Create chart series and add data points into it.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries ("Series Name", ChartSeriesType.ThreeLineBreak)
series.Points.Add (0, 1)
series.Points.Add (1, 3)
series.Points.Add (2, 4)

' Add series to the chart series collection.
Me.chartControl1.Series.Add (series)
```

### Customization Options

The following customization options are available for the chart series:

- DisplayShadow
- DisplayText
- DrawSeriesNameInDepth
- ElementBorders
- ImageIndex
- Images
- PriceDownColor
- PriceUpColor
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

## Page-Level Navigation/TOC (if applicable)
- Essential Chart for Windows Forms
  - Chart Series Properties
    - Adding Three Line Break Series
    - Customization Options

## Cross References
See also: [page_id: chart#page_141]

### [Note:] 
This page provides a concise overview of configuring and using Three Line Break series in charts.

```

<!-- tags: [chart, windows forms, syncfusion winforms, three line break series, customization options, series properties] keywords: [chart series, winforms, three line break, price down color, price up color, shadow settings, tag: "toolbar"] -->