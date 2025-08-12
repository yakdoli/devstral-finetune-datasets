```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_356.jpeg
document_name: chart
page_number: 356
page_id: chart#page_356
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:37:17Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Applies to Chart Types

| Entity                                      | Description                                                                 |
|---------------------------------------------|-----------------------------------------------------------------------------|
| Applies to Chart Types                     | Scatter Chart, Hilo Open Close Chart(3D), Column Charts, BarCharts, Bubble Chart, Line Charts, BoxandWhisker Chart, Tornado Chart, Combination Chart, Gantt Chart, Candle Chart, HiLo Chart(3D), PolarAndRadar, PieChart, Accumulation Charts, Area Charts |

Here is sample code snippet using ToolTipFormat in the Column chart.

### Series Wide Setting

#### [C#]

```csharp
this.chartControl1.ShowToolTips = true;
this.chartControl1.Series[1].Style.ToolTipFormat = "Y = {0}";
```

#### [VB.NET]

```vb
Me.chartControl1.ShowToolTips = True
Me.chartControl1.Series[1].Style.ToolTipFormat = "Y = {0}"
```

![Illustrates TooltipFormat](attachment:image.png)

**Figure 225: ToolTipFormat set for Chart Series**
```