```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_124.jpeg
document_name: chart
page_number: 124
page_id: chart#page_124
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:23:23Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
series.Styles[1].Symbol.Color = Color.Green;
series.Styles[1].Symbol.Shape = ChartSymbolShape.Hexagon;

series.Styles[2].Symbol = new ChartSymbolInfo();
series.Styles[2].Symbol.Color = Color.Blue;
series.Styles[2].Symbol.Shape = ChartSymbolShape.Cross;
```

```vb
' Specify the symbol info required for the Scatter chart.
series.Styles(0).Symbol = New ChartSymbolInfo()
series.Styles(0).Symbol.Color = Color.Red
series.Styles(0).Symbol.Shape = ChartSymbolShape.InvertedTriangle

series.Styles(1).Symbol = New ChartSymbolInfo()
series.Styles(1).Symbol.Color = Color.Green
series.Styles(1).Symbol.Shape = ChartSymbolShape.Hexagon

series.Styles(2).Symbol = New ChartSymbolInfo()
series.Styles(2).Symbol.Color = Color.Blue
series.Styles(2).Symbol.Shape = ChartSymbolShape.Cross
```

## Customization Options
- DisplayText
- DrawSeriesNameInDepth
- LightAngle
- LightColor
- PhongAlpha
- ScatterConnectType
- ScatterSplineTension
- ToolTip
- ToolTipFormat
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

## See Also
- [Bubble Chart](#)

### 4.4.6.2 Bubble Chart

Bubble Chart is an extension of the Scatter Chart (or XY-chart) where each data marker is represented by a circle whose dimension form a third variable. Consequently, bubble charts allow three-variable comparisons allowing for easy visualization of complex interdependencies that are not apparent in two-variable charts. Bubble charts are frequently used in market and product comparison studies.

<!-- tags: [Syncfusion Winforms, Bubble Chart, Scatter Chart, Chart Symbol Shape, Customization Options, 11.4.0.26] keywords: [Bubble Chart, Scatter Chart, ChartSymbolShape.Hexagon, ChartSymbolShape.Cross, ChartSymbolShape.InvertedTriangle, Customization Options, LightColor, TextOrientation, TextFormat, Name, ToolTip] -->
```