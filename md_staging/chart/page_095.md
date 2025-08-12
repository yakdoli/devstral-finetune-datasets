```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_095.jpeg
document_name: chart
page_number: 095
page_id: chart#page_095
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:20:55Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates how to add series to a chart using both C# and VB.NET.
- Explains customization options for column charts.
- Introduces the Column Range Chart, a variation of the standard column chart.

## Content

```csharp
// Add the series to the chart series collection.
this.chartControl1.Series.Add(series);
```

```vb
' Create chart series and add data points into it.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Column)
series.Points.Add(0, 1)
series.Points.Add(1, 3)
series.Points.Add(2, 4)

' Add the series to the chart series collection.
Me.chartControl1.Series.Add(series)
```

### Customization Options

- Border
- ColumnDrawMode
- ColumnWidthMode
- ColumnFixedWidth
- DisplayShadow
- DisplayText
- DrawColumnSeparatingLines
- ColumnType
- DrawErrorBars
- DrawSeriesNameInDepth
- ElementBorders
- ErrorBarsSymbolShape
- HighlightInterior
- ImageIndex
- Images
- LightAngle
- LightColor
- PhongAlpha
- Rotate
- Spacing
- Spacing Between Series
- ShadingMode
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

### 4.4.3.2 Column Range Chart

**Description**  
Column Range Chart is similar to the Column Chart except that each column is rendered over a range. Therefore, the user must specify the y-axis Starting and Ending values for each point.

**Example**  
The following figure shows a Column Range Chart.

<!-- tags: [Syncfusion Winforms, Chart, ColumnRangeChart, CustomizationOptions, Series, ColumnChart, ColumnWidth, ColumnRange] keywords: [ColumnRangeChart, y-axis, Starting, Ending, ColumnChart, Customization] -->
```