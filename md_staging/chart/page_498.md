```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_498.jpeg
document_name: chart
page_number: 498
page_id: chart#page_498
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:47:54Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

| Property        | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| **BorderStyle** | Indicates the border style.                                                |
| **BorderWidth** | Specifies the width of the border.                                         |
| **BorderAppearance** |                                                                 |
| **BaseColor**   | Gets or sets the color of the base.                                        |
| **FrameThickness** | Gets or sets the frame thickness. This property setting will be effective, when **SkinStyle** is **Frame**. |
| **Interior**    | Sets the interior color of the border. This property settings will be effective when **SkinStyle** is **Sunken, Etched** and **Raised**. |
| **SkinStyle**   | Specifies the border skin style.                                           |

## Code Examples

### C#

```csharp
this.chartControl1.ChartArea.BorderColor = System.Drawing.Color.Goldenrod;
this.chartControl1.ChartArea.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
this.chartControl1.ChartArea.BorderWidth = 1;

this.chartControl1.BorderAppearance.BaseColor = System.Drawing.Color.DarkGray;
//This property setting will be effective, when SkinStyle is 'Frame'.
this.chartControl1.BorderAppearance.FrameThickness = new Syncfusion.Windows.Forms.Chart.ChartThickness(15F, 30F, 15F, 18F);
//This interior property settings will be effective when SkinStyle is Sunken, Etched and Raised.
this.chartControl1.BorderAppearance.Interior.ForeColor = System.Drawing.Color.Maroon;
this.chartControl1.BorderAppearance.SkinStyle = Syncfusion.Windows.Forms.Chart.ChartBorderSkinStyle.Raised;
```

### VB.NET

```vb
Me.ChartControl1.ChartArea.BorderColor = System.Drawing.Color.Goldenrod
Me.ChartControl1.ChartArea.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
Me.ChartControl1.ChartArea.BorderWidth = 1

Me.chartControl1.BorderAppearance.BaseColor = System.Drawing.Color.DarkGray
'This property setting will be effective, when SkinStyle is 'Frame'.
```

<!-- tags: [windows forms, chart, border, frame, sunken, etched, raised] keywords: [borderstyle, borderwidth, basecolor, framethickness, interior, skinstyle, chartcontrol1, chartarea] -->
```