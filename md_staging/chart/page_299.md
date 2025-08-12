```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_299.jpeg
document_name: chart
page_number: 299
page_id: chart#page_299
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:32:29Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
ptIndices;
this.chartControl1.Series[1].Styles[5].RelatedPoints.Color = Color.Green;
this.chartControl1.Series[1].Styles[5].RelatedPoints.Alignment = System.Drawing.Drawing2D.PenAlignment.Center;
this.chartControl1.Series[1].Styles[5].RelatedPoints.DashStyle = System.Drawing.Drawing2D.DashStyle.Solid;
this.chartControl1.Series[1].Styles[5].RelatedPoints.Width = 3f;
```

### [VB.NET]

```vbnet
' Related Points for first series
Dim ptIndices As Integer() = New Integer() {2, 4}
Me.chartControl1.Series(0).Styles(3).RelatedPoints.Points = ptIndices
Me.chartControl1.Series(0).Styles(3).RelatedPoints.Color = Color.Red
Me.chartControl1.Series(0).Styles(3).RelatedPoints.Alignment = System.Drawing.Drawing2D.PenAlignment.Right
Me.chartControl1.Series(0).Styles(3).RelatedPoints.DashStyle = System.Drawing.Drawing2D.DashStyle.Custom
Me.chartControl1.Series(0).Styles(3).RelatedPoints.Width = 3f
Dim dash As Single() = New Single() {1.5f, 2.4f }
Me.chartControl1.Series(0).Styles(3).RelatedPoints.DashPattern = dash
' Related Points for second series
Dim ptIndices As Integer() = New Integer() { 1 }
Me.chartControl1.Series(1).Styles(5).RelatedPoints.Points = ptIndices
Me.chartControl1.Series(1).Styles(5).RelatedPoints.Color = Color.Green
Me.chartControl1.Series(1).Styles(5).RelatedPoints.Alignment = System.Drawing.Drawing2D.PenAlignment.Center
Me.chartControl1.Series(1).Styles(5).RelatedPoints.DashStyle = System.Drawing.Drawing2D.DashStyle.Solid
Me.chartControl1.Series(1).Styles(5).RelatedPoints.Width = 3f
```

```html
<!-- tags: [chart, windowsforms, Syncfusion, relatedpoints, styles, alignment, dashstyle, color, width] keywords: [RelatedPoints, chartControl1, Series, Styles, PenAlignment, DashStyle, Color, Width] -->
``` 
