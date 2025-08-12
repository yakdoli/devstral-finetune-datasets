```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_250.jpeg
document_name: chart
page_number: 250
page_id: chart#page_250
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:30:28Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

![Figure: Column Chart with HighlightInterior](figure.png)
*Figure 148: Column Chart with HighlightInterior*

## Specific Data Point Setting

### Overview
- Learn how to apply individual interior highlighting styles to specific datapoints in a chart.
- Understand the syntax for setting gradient colors for highlighted regions.

## Content

### To set interior color for individual highlighted datapoints

#### C#
```csharp
series1.Styles[0].HighlightInterior = new
BrushInfo(GradientStyle.ForwardDiagonal, Color.Red, Color.White);
series1.Styles[1].HighlightInterior = new
BrushInfo(GradientStyle.ForwardDiagonal, Color.Green, Color.White);
series1.Styles[2].HighlightInterior = new
BrushInfo(GradientStyle.ForwardDiagonal, Color.Yellow, Color.White);
series1.Styles[3].HighlightInterior = new
BrushInfo(GradientStyle.ForwardDiagonal, Color.Pink, Color.White);
```

#### VB.NET
```vbnet
series1.Styles(0).HighlightInterior = New
BrushInfo(GradientStyle.ForwardDiagonal, Color.Red, Color.White)
series1.Styles(1).HighlightInterior = New
BrushInfo(GradientStyle.ForwardDiagonal, Color.Green, Color.White)
series1.Styles(2).HighlightInterior = New
BrushInfo(GradientStyle.ForwardDiagonal, Color.Yellow, Color.White)
series1.Styles(3).HighlightInterior = New
BrushInfo(GradientStyle.ForwardDiagonal, Color.Pink, Color.White)
```

### See Also
- Additional documentation or examples related to chart customization.

## Page-level Navigation/TOC (if applicable)
- Navigate to relevant sections or pages if applicable.

### Cross References
- Refer to related topics or similar examples for a broader understanding.

## RAG Annotations
<!-- tags: [chart, highlightinterior, gradientstyle, winforms, product, module, control, api, version?] keywords: [NumVariables, defVarargs, cmap, path, font, outline, detail] -->
```