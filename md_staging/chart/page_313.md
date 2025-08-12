```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_313.jpeg
document_name: chart
page_number: 313
page_id: chart#page_313
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:34:25Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## ColumnChart with SkyBlue Shadow

![](media/figure_195.png)

Figure 195: ColumnChart with SkyBlue Shadow

## Specific Data Point Setting

To specify different shadow colors for individual points, use the `Series.Series[0].ShadowInterior` property.

### Example Code

#### C#

```csharp
this.chartControl1.Series[0].Styles[0].ShadowInterior = new BrushInfo(GradientStyle.None, Color.SteelBlue, Color.SteelBlue);
this.chartControl1.Series[0].Styles[0].ShadowInterior = new BrushInfo(GradientStyle.None, Color.Gray, Color.Gray);
```

#### VB.NET

```vb
Private Me.chartControl1.Series(0).Style.ShadowInterior = New BrushInfo(GradientStyle.None, Color.SteelBlue, Color.SteelBlue)
Private Me.chartControl1.Series(0).Style.ShadowInterior = New BrushInfo(GradientStyle.None, Color.Gray, Color.Gray)
```

### See Also

- Column Charts
- Bar Charts
- Line Charts
- Candle Chart
- Kagi Chart
- BoxandWhisker chart
- Histogram chart
- Polar and Radar Chart
- Point and Figure Chart
- Renko Chart
- Three Line Break Chart
- Gantt Chart
- Tornado Chart
- Pie Chart
- Area Chart
- Step Area Chart

#### Footer

© 2013 Syncfusion. All rights reserved. 313 | Page
```