```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_226.jpeg
document_name: chart
page_number: 226
page_id: chart#page_226
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:28:43Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

| **Possible Values** | - Circle - Renders the chart with a circular base.<br>- Square - Renders the chart with a square base. |
|---------------------|--------------------------------------------------------------------------------------------------------------------------|
| **Default Value**   | - Funnel Chart - Circle<br>- Pyramid Chart - Square                                                                     |
| **2D / 3D Limitations** | 3D Only                                                                                                               |
| **Applies to Chart Element** | All series                                                                                                         |
| **Applies to Chart Types** | Funnel and Pyramid                                                                                                   |

Here is some sample code.

```csharp
[C#]

// Setting FigureBase For Pyramid Chart
this.chartControl1.Series[0].ConfigItems.PyramidItem.FigureBase = ChartFigureBase.Circle;
this.chartControl1.Series[0].ConfigItems.PyramidItem.FigureBase = ChartFigureBase.Square;

// Setting FigureBase For Funnel Chart
this.chartControl1.Series[0].ConfigItems.FunnelItem.FigureBase = ChartFigureBase.Circle;
this.chartControl1.Series[0].ConfigItems.FunnelItem.FigureBase = ChartFigureBase.Square;
```

```vb.net
[VB.NET]

' Setting FigureBase For Pyramid
Me.chartControl1.Series(0).ConfigItems.PyramidItem.FigureBase = ChartFigureBase.Circle
Me.chartControl1.Series(0).ConfigItems.PyramidItem.FigureBase = ChartFigureBase.Square

' Setting FigureBase For Funnel Chart
Me.chartControl1.Series(0).ConfigItems.FunnelItem.FigureBase = ChartFigureBase.Circle
Me.chartControl1.Series(0).ConfigItems.FunnelItem.FigureBase = ChartFigureBase.Square
```

## Page-level Navigation/TOC (if applicable)

<!-- tags: [Windows Forms, Essential Chart, FigureBase, Funnel Chart, Pyramid Chart, 3D Chart, Chart Controls] keywords: [Syncfusion, C#, VB.NET, Chart, ChartFigureBase, Series, ConfigItems, FunnelItem, PyramidItem, Circular base, Square base, 3D, All series, Funnel Chart, Pyramid Chart] -->
```