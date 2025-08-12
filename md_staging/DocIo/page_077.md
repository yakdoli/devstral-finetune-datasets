```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_077.jpeg
document_name: DocIo
page_number: 077
page_id: DocIo#page_077
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:33:16Z
fidelity: lossless
-->

## Overview
- Describes how to use the Background Gradient class in the Word document.
- Discusses properties like Color2, ShadingStyle, and ShadingVariant.
- Details the method `Clone` for copying Gradient objects.
- Explains inserting a watermark into a Word document.
- Discusses Picture Watermark as one of the watermark types.

## Content

### Background Gradient

| Name         | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| Color2       | Gets or sets second color for gradient (used when TwoColors set to true). |
| ShadingStyle | Gets or sets shading style for gradient.                                 |
| ShadingVariant | Gets or sets shading variants.                                       |

#### Public Methods

| Name   | Description                               |
|--------|-------------------------------------------|
| Clone  | Clones current Gradient object.          |

The following example illustrates how to use the Background Gradient class.

#### C#

```csharp
IWordDocument doc = new WordDocument(true);
doc.Background.Type = BackgroundType.Gradient;
doc.Background.Gradient.Color1 = Color.White;
doc.Background.Gradient.Color2 = Color.Black;
doc.Background.Gradient.ShadingStyle = GradientShadingStyle.FromCenter;
doc.Background.Gradient.ShadingVariant = GradientShadingVariant.ShadingDown;
```

#### VB

```vb
Dim doc As IWordDocument = New WordDocument(True)
doc.Background.Type = BackgroundType.Gradient
doc.Background.Gradient.Color1 = Color.White
doc.Background.Gradient.Color2 = Color.Black
doc.Background.Gradient.ShadingStyle = GradientShadingStyle.FromCenter
doc.Background.Gradient.ShadingVariant = GradientShadingVariant.ShadingDown
```

### 4.2.2.2 Watermark

#### Overview
Watermark class represents printed watermark in the Word document.

#### Inserting a Watermark
To insert a watermark into the Word document, open the **Format** menu, point to **Background**, and then click **Printed Watermark**. There are two types of watermarks:
- **Picture Watermark**

## Page-level Navigation/TOC (if applicable)
- **Background Gradient**
- **Public Methods**
- **Watermark**

## Cross References
- See also: `BackgroundType`, `Gradient`, `GradientShadingStyle`, `GradientShadingVariant`, `Printed Watermark`.

## Code Examples
- Used C# and VB examples to demonstrate setting up a background gradient in a Word document.

<!-- tags: Watermark, Background Gradient, GradientShadingStyle, GradientShadingVariant, WordDocument, Syncfusion Winforms, DocIo, .NET controls keywords: Watermark, gradients, document formatting, Word documents, shading styles -->
```