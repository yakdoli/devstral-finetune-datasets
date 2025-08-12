```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_121.jpeg
document_name: chart
page_number: 121
page_id: chart#page_121
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:23:06Z
fidelity: lossless
-->

# Chart for Windows Forms

| Number of Series | One. |
|---------------------|-------------------------------|
| Cannot be Combined with | Any other chart types. |

## Customization Options

Casting out;

### [C#]

```csharp
ChartSeries series1 = this.chartControl1.Model.NewSeries("Pyramid chart", ChartSeriesType.Pyramid);
series1.Points.Add(0, 25.3);
series1.Points.Add(1, 45.7);
series1.Points.Add(2, 97.3);
series1.Points.Add(3, 20.6);
series1.Points.Add(4, 125.8);
series1.Points.Add(5, 216.1);
this.chartControl1.Series.Add(series1);
```

### [VB.NET]

```vbnet
Dim series1 As ChartSeries = Me.chartControl1.Model.NewSeries("Pyramid chart", ChartSeriesType.Pyramid)
series1.Points.Add(0, 25.3)
series1.Points.Add(1, 45.7)
series1.Points.Add(2, 97.3)
series1.Points.Add(3, 20.6)
series1.Points.Add(4, 125.8)
series1.Points.Add(5, 216.1)
Me.chartControl1.Series.Add(series1)
```

- **Customization Options**
    - Border, DisplayText, DrawSeriesNameInDepth, FigureBase, GapRatio, HighlightInterior,
    - LabelPlacement, LabelStyle, PyramidMode, FancyToolTip, Font, Interior, LegendItem, Name,
    - PointsToolTipFormat, SmartLabels, Summary, Text, TextColor, TextFormat, TextOffset,
    - TextOrientation, Visible, ShowDataBindLabels

## 4.4.6 XY Charts (Bubble and Scatter)

### Overview
- XY Charts, also known as Bubble and Scatter charts, are used to visualize the relationship between two variables that relate to the same event.

<!-- tags: [chart, pyramid chart, XY charts, bubble, scatter, Syncfusion Winforms, version:11.4.0.26] keywords: [chart, series, customize, Bubble, Scatter, XY, relationship, two variables] -->
```