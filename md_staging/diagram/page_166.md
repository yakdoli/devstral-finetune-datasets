```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_166.jpeg
document_name: diagram
page_number: 166
page_id: diagram#page_166
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:19:07Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

Some important properties are discussed below:

### FillStyle

#### FillStyle property is used to create brushes for filling the interior region of the Connection Points.

[C#]

```csharp
FillStyle m_styleFill = new FillStyle();
m_styleFill.Color = Color.Transparent;
m_styleFill.Type = FillStyleType.Solid;
m_styleFill.ColorAlphaFactor = 60;
```

[VB]

```vb
Dim m_styleFill As New FillStyle()
m_styleFill.Color = Color.Transparent
m_styleFill.Type = FillStyleType.Solid
m_styleFill.ColorAlphaFactor = 60
```

The following image illustrates the above settings.

<!-- tags: [diagram, windows forms, fillstyle, connection points, syncfusion, version 11.4.0.26] keywords: [FillStyle property, solid fill, color alpha factor, transparent color] -->
```