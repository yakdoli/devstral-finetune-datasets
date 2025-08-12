```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_214.jpeg
document_name: chart
page_number: 214
page_id: chart#page_214
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:28:02Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## 4.5.1.18 ElementBorders

### Overview
- Gets / sets the border settings for elements associated with the chart point.
- Allows specification of the inner and outer border.
- Currently used only by symbols rendered by the ChartPoint (inherited from ChartStyleInfo).

### Details

| **Possible Values** | **Border setting object** |
|---------------------|----------------------------|
| Default Value       | - Weight – Thin<br>- Width value – 1<br>- Style - Standard |
| 2D / 3D Limitations | No                       |
| Applies to Chart Element | All series and points |
| Applies to Chart Types | Area Charts, Bar Charts, Bubble Chart, Column Charts, Line Charts, Candle Chart, Renko chart, Three Line Break Chart, Box and Whisker Chart, Gantt Chart, Tornado Chart, Polar and Radar Chart |

### Here is some sample code.

### Series Wide Setting

#### C#
```csharp
// Setting Symbol for the ChartSeries
this.chartControl1.Series[0].Style.Symbol.Color = Color.Yellow;
this.chartControl1.Series[0].Style.Symbol.Shape = ChartSymbolShape.InvertedTriangle;
// Setting ElementBorder for a symbol
ChartBordersInfo cbi = new ChartBordersInfo();
cbi.Outer = new ChartBorder(ChartBorderStyle.Solid, Color.White);
cbi.Inner = new ChartBorder(ChartBorderStyle.DashDot, Color.Cyan);
this.chartControl1.Series[0].Style.ElementBorders = cbi;
```

#### VB.NET
```vb
' Setting Symbol for the ChartSeries
```

## Page-level Navigation/TOC (if applicable)

- **4.5.1.18 ElementBorders**

## RAG Annotations

<!-- tags: [elements, borders, chart, points, ChartPoint, ChartBordersInfo, ChartSymbolShape, ChartBorderStyle] keywords: [chart point, border settings, inner border, outer border, ChartPoint, ChartStyleInfo, Area Charts, Bar Charts, Bubble Chart, Column Charts, Line Charts, Candle Chart, Renko chart, Three Line Break Chart, Box and Whisker Chart, Gantt Chart, Tornado Chart, Polar Chart, Radar Chart] -->
```