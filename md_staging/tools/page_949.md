```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_949.jpeg
document_name: tools
page_number: 949
page_id: tools#page_949
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:44:12Z
fidelity: lossless
--> 

## Overview
- Explains gradient styles and colors in Windows Forms.
- Demonstrates configuring `GradientStyle` and `GradientColors` properties.
- Provides C# and VB.NET code examples for setting gradient styles in labels.

## Content

### GradientStyle
The `GradientStyle` property specifies how the gradient colors transition between each other. The available styles are:
- `ForwardDiagonal`
- `BackwardDiagonal`
- `Horizontal`
- `Vertical`
- `PathRectangle`
- `PathEllipse`

The default value is set to `Vertical`.

### GradientColors
The `GradientColors` property specifies the gradient colors. The first entry in this list will be the same as the `BackColor` property, and the last entry will be the same as the `ForeColor` property.

## Code Examples

### C#
```csharp
this.gradientLabel1.BackColor = new
Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.PathRectangle,
    new System.Drawing.Color[] { System.Drawing.Color.LavenderBlush,
    System.Drawing.Color.LemonChiffon, System.Drawing.Color.DarkKhaki,
    System.Drawing.Color.SandyBrown, System.Drawing.Color.LightSeaGreen });
```

### VB.NET
```vb
Me.gradientLabel1.BackColor = New
Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.PathRectangle,
    New System.Drawing.Color() { System.Drawing.Color.LavenderBlush,
    System.Drawing.Color.LemonChiffon, System.Drawing.Color.DarkKhaki,
    System.Drawing.Color.SandyBrown, System.Drawing.Color.LightSeaGreen })
```

### Figure: GradientLabel Sample
![GradientLabel Sample](https://example.com/image-url)

## Page-level Navigation/TOC (if applicable)

## API Reference (if applicable)
- Namespace: Syncfusion.Drawing
- Class: BrushInfo
- Properties:
  - `GradientStyle`
  - `GradientColors`

## Cross References
See also: `GradientLabel`, `BrushInfo`, `GradientStyle`, `GradientColors`

## RAG Annotations
<!-- tags: Windows Forms, Gradient Styles, Brushes, Syncfusion, Code Examples, C#, VB.NET keywords: GradientStyle, GradientColors, BrushInfo, label, Windows Forms, gradient, colors -->
``` 
