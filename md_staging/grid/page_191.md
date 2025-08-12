```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_191.jpeg
document_name: grid
page_number: 191
page_id: grid#page_191
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:01:33Z
fidelity: lossless
-->

## Essentia Grid for Windows Forms

### Content

```csharp
gridControl1[2, 2].Interior = new BrushInfo(GradientStyle.Horizontal, Color.Yellow, Color.Blue);
gridControl1[3, 2].Interior = new
BrushInfo(PattenStyle.DashedHorizontal, Color.Black, Color.White);
```

#### Using VB.NET

```vb
[VB.NET]

gridControl1(2, 2).Interior = New BrushInfo(GradientStyle.Horizontal, color.Yellow, color.Blue)
gridControl1(3, 2).Interior = New
BrushInfo(PattenStyle.DashedHorizontal, color.Black, color.White)
```

### 2. Font

Let's specify the font for drawing text. The cells can be given required styles by using the Font property under `GridFontInfo`. GridFontInfo holds information on the font settings.

#### Using C#

```csharp
[C#]

GridFontInfo boldFont = new GridFontInfo();
boldFont.Bold = true;
boldFont.Size = 11;
boldFont.Underline = true;
gridControl1[3, 4].Font = boldFont;
```

#### Using VB.NET

```vb
[VB.NET]

Dim boldFont As GridFontInfo = New GridFontInfo()
boldFont.Bold = True
boldFont.Size = 11
boldFont.Underline = True
gridControl1(3, 4).Font = boldFont
```

### 3. Text Color

The color for the cell text can be set by using the `TextColor` property.

#### Using C#
```csharp

```

## API Reference (if applicable)
<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```