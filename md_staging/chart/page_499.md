```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_499.jpeg
document_name: chart
page_number: 499
page_id: chart#page_499
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:44:24Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
Me.chartControl1.BorderAppearance.FrameThickness = New Syncfusion.Windows.Forms.Chart.ChartThickness(15F, 30F, 15F, 18F)
' This interior property settings will be effective when SkinStyle is Sunken, Etched and Raised.
Me.chartControl1.BorderAppearance.Interior.ForeColor = System.Drawing.Color.Maroon
Me.chartControl1.BorderAppearance.SkinStyle = Syncfusion.Windows.Forms.Chart.ChartBorderSkinStyle.Raised
```

## Chart Area Shadow

The chart area can also be rendered with a shadow. Turn this feature on by enabling the `ChartAreaShadow` property.

| Chart control Property | Description                                               |
|-------------------------|-----------------------------------------------------------|
| ChartAreaShadow        | Indicates whether chart area has a shadow.              |
| ShadowColor            | Specifies the color of the shadow.                       |
| ShadowWidth            | Specifies the width of the shadow.                       |

### Code Example in C#

```csharp
this.chartControl1.ChartAreaShadow = true;
this.chartControl1.ShadowColor = new Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.ForwardDiagonal, System.Drawing.Color.AntiqueWhite, System.Drawing.Color.Goldenrod);
this.chartControl1.ShadowWidth = 7;
```

### Code Example in VB.NET

```vb
Me.ChartControl1.ChartAreaShadow = True
Me.ChartControl1.ShadowColor = New Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.ForwardDiagonal, System.Drawing.Color.AntiqueWhite, System.Drawing.Color.Goldenrod)
Me.chartControl1.ShadowWidth = 7
```

<!-- tags: [Syncfusion, Windows Forms, Chart, ChartArea, Shadow, BorderAppearance, Theme, SkinStyle, GradientBrush] keywords: [chart area, shadow effect, chart control, theme customization, skin style, frame thickness, color properties, drawing brush] -->
```