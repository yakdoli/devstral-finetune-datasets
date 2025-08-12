```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_261.jpeg
document_name: chart
page_number: 261
page_id: chart#page_261
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:31:28Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
series1.Styles[0].Interior = new
BrushInfo(PatternStyle.BackwardDiagonal, new
BrushInfoColorArrayList(new Color[] { Color.Yellow, Color.Blue }));
series1.Styles[1].Interior = new BrushInfo(PatternStyle.Cross, new
BrushInfoColorArrayList(new Color[] { Color.LightGreen, Color.Blue }));
series1.Styles[2].Interior = new BrushInfo(PatternStyle.SolidDiamond, new
BrushInfoColorArrayList(new Color[] { Color.Beige, Color.Blue }));
series1.Styles[3].Interior = new BrushInfo(PatternStyle.Wave, new
BrushInfoColorArrayList(new Color[] { Color.White, Color.Blue }));
series1.Styles[0].Text = "Server1";
series1.Styles[1].Text = "Server2";
series1.Styles[2].Text = "Server3";
series1.Styles[3].Text = "Server4";
```

### VB.NET
```vb
series1.Styles(0).Interior = New
BrushInfo(PatternStyle.BackwardDiagonal, New
BrushInfoColorArrayList(New Color() { Color.Yellow, Color.Blue }))
series1.Styles(1).Interior = New BrushInfo(PatternStyle.Cross, New
BrushInfoColorArrayList(New Color() { Color.LightGreen, Color.Blue }))
series1.Styles(2).Interior = New BrushInfo(PatternStyle.SolidDiamond, New
BrushInfoColorArrayList(New Color() { Color.Beige, Color.Blue }))
series1.Styles(3).Interior = New BrushInfo(PatternStyle.Wave, New
BrushInfoColorArrayList(New Color() { Color.White, Color.Blue }))
series1.Styles(0).Text = "Server1"
series1.Styles(1).Text = "Server2"
series1.Styles(2).Text = "Server3"
series1.Styles(3).Text = "Server4"
```

<!-- tags: [chart, windows forms, interior patterns, text labeling] keywords: [BrushInfo, PatternStyle, BrushInfoColorArrayList, interior, text label, server] -->
```