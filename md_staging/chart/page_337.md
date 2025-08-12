```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_337.jpeg
document_name: chart
page_number: 337
page_id: chart#page_337
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:35:46Z
fidelity: lossless
-->

## Chart Symbol in Column Chart Example

Here is a table summarizing the properties and settings related to chart symbols:

### Chart Symbol Overview

| Property                      | Value                   |
|-------------------------------|-------------------------|
| Offset                        | $0,0$                  |
| 2D / 3D Limitations          | No                     |
| Applies to Chart Element     | Any Series             |
| Applies to Chart Types       | Column Chart, Bar Chart, Bubble Chart, Financial Chart, Line Chart, BoxandWhisker Chart, Gantt chart, Tornado chart, Radar Chart, Polar Chart, Area Charts, Scatter Chart |

### Series Wide Setting Example

#### Sample Code Snippet in C#

```csharp
this.chartControl1.Series[0].Style.Symbol.Shape = ChartSymbolShape.Diamond;
this.chartControl1.Series[0].Style.Symbol.Color = Color.Green;
this.chartControl1.Series[0].Style.Symbol.Size = new Size(10, 10);
this.chartControl1.Series[0].Style.Symbol.Offset = new Size(1, 20);

// Sets the Color of the Symbol border.
this.chartControl1.Series[0].Style.Symbol.Border.Color = Color.Blue;
// Sets the Width of the Symbol border.
this.chartControl1.Series[0].Style.Symbol.Border.Width = 1;
// Sets the Alignment of the Symbol border.
this.chartControl1.Series[0].Style.Symbol.Border.Alignment = PenAlignment.Outlet;
// Sets the Dash style of the Symbol Border.
this.chartControl1.Series[0].Style.Symbol.Border.DashStyle = DashStyle.Solid;
```

#### Sample Code Snippet in VB.NET

```vb
Private Me.chartControl1.Series(0).Style.Symbol.Shape = ChartSymbolShape.Diamond
Private Me.chartControl1.Series(0).Style.Symbol.Color = Color.Green
Private Me.chartControl1.Series(0).Style.Symbol.Size = New Size(10, 10)
Private Me.chartControl1.Series(0).Style.Symbol.Offset = New Size(1, 20)

'Used to set the Color of the Symbol border.
```

### Additional Notes

This section demonstrates how to configure the symbol properties for a specific series (`Series[0]`) in a `ChartControl`. The properties include the shape, color, size, and offset of the symbol, as well as settings for the symbol's border, such as color, width, alignment, and dash style.

<!-- tags: [syncfusion, winforms, chart, symbol, column chart, series, style, alignment] keywords: [chartControl, Series, Style, Symbol, Shape, Color, Size, Offset, Border, DashStyle, PenAlignment, Outlet] -->
```