```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_503.jpeg
document_name: chart
page_number: 503
page_id: chart#page_503
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:44:37Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
this.chartControl1.Font = new System.Drawing.Font("Arial", 11.25F, System.Drawing.FontStyle.Bold);
this.chartControl1.ForeColor = System.Drawing.Color.Bisque;
this.chartControl1.TextPosition = ChartTextPosition.Top;
```

### [VB.NET]

```vb
Me.ChartControl1.Text = "Illustrates Foreground Settings"
Me.chartControl1.Font = New System.Drawing.Font("Arial", 11.25F, System.Drawing.FontStyle.Bold)
Me.chartControl1.ForeColor = System.Drawing.Color.Bisque
Me.chartControl1.TextPosition = ChartTextPosition.Top
```

![Figure 323: Illustrates changes affecting the Title Text](https://via.placeholder.com/600)

## General Text Related settings

The following text related properties affect all the text rendered in the chart.

| Chart control Property       | Description                                                                                                              |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| TextRenderingHint            | Specifies the way the text is drawn. Possible values:                                                               |
|                              | - **AntiAlias** - each character is drawn using its anti-aliased glyph bitmap without hinting.                          |
|                              | - **AntiAliasGridFit** - each character is drawn using its anti-aliased                                                 |

<footer>
© 2013 Syncfusion. All rights reserved. 503 | Page
</footer>
```

<!-- tags: [Syncfusion Winforms, TextRelatedSettings, ChartControl, FontProperties, ForeColor, TextPosition, TextRenderingHint, AntiAlias, AntiAliasGridFit] -->
<!-- keywords: [Syncfusion, Winforms, Chart, Control, Text, RenderingHints, Anti-Aliasing, GridFit, TextProperties, Font, Forecolor, TextPosition] -->
```