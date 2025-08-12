```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_179.jpeg
document_name: diagram
page_number: 179
page_id: diagram#page_179
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:18:12Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Properties

| Property        | Description                                                                 |
|-----------------|------------------------------------------------------------------------------|
| `BackgroundColor` | Specifies the back color for the ruler.                                   |
| `HighlightColor`  | Specifies the highlight color.                                           |
| `MajorLinesColor` | Specifies the color for the main line in the ruler.                      |
| `MarkerColor`     | Specifies the marker color in the ruler.                                 |
| `MinorLinesColor` | Specifies the color for the sub-division lines.                          |
| `TextStyle`       | Specifies the text style.                                                 |

## Programmatic Setup for Vertical Lines

```csharp
this.diagram1.VerticalRuler.BackgroundColor = System.Drawing.Color.Beige;
this.diagram1.VerticalRuler.HighlightColor = System.Drawing.Color.Yellow;
this.diagram1.VerticalRuler.MajorLinesColor = System.Drawing.Color.YellowGreen;
this.diagram1.VerticalRuler.MarkerColor = System.Drawing.Color.Thistle;
this.diagram1.VerticalRuler.MinorLinesColor = System.Drawing.Color.Turquoise;

this.diagram1.VerticalRuler.TextStyle.Bold = true;
this.diagram1.VerticalRuler.TextStyle.Italic = true;
this.diagram1.VerticalRuler.TextStyle.PointSize = 20;
this.diagram1.VerticalRuler.TextStyle.Strikeout = true;
this.diagram1.VerticalRuler.TextStyle.Style = System.Drawing.FontStyle.Bold;
this.diagram1.VerticalRuler.TextStyle.Underline = true;
this.diagram1.VerticalRuler.TextStyle.Unit = MeasureUnits.Point;
```

```vb
Me.diagram1.VerticalRuler.BackgroundColor = System.Drawing.Color.Beige
Me.diagram1.VerticalRuler.HighlightColor = System.Drawing.Color.Yellow
Me.diagram1.VerticalRuler.MajorLinesColor = System.Drawing.Color.YellowGreen
Me.diagram1.VerticalRuler.MarkerColor = System.Drawing.Color.Thistle
Me.diagram1.VerticalRuler.MinorLinesColor = System.Drawing.Color.Turquoise
```

## API Reference

<!-- tags: syncfusion, winforms, diagram, vertical ruler, properties, styles, colors keywords: ruler color, text style, highlight, major lines, minor lines, programmatic setup -->
```html
```