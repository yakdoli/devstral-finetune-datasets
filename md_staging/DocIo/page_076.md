```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_076.jpeg
document_name: DocIo
page_number: 076
page_id: DocIo#page_076
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:32:53Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Demonstrates the use of the Fill Effects Dialog Box in DocIO.
- Explains how to access and configure background gradient options using the WordDocument.Background.Gradient option.

## Content

### Fill Effects Dialog Box

![Figure 28: Fill Effects Dialog Box](#)

Using DocIO, you can access background gradient options through the `WordDocument.Background.Gradient` option. Background Gradient will be set as the background fill effect when the `WordDocument.Background.Type` option is set to `BackgroundType.Gradient`.

#### Gradient Properties
- **Color1 and Color2** properties of `Background Gradient` define the gradient colors.
- **GradientShadingStyle** and **GradientShadingVariant** properties define the type of the different variants of the gradient.

### Public Properties

| Name    | Description                          |
|---------|--------------------------------------|
| **Color1** | Gets or sets first color for gradient. |

## API Reference

- **Namespace:** Syncfusion.Windows.Forms
- **Class:** WordDocument
- **Property:** Background
  - **Type:** Background
  - **Description:** Represents the background of the document.
  - **Subproperties:**
    - **Type:** BackgroundType
    - **Description:** Specifies the type of background fill effect (e.g., Gradient).

## Code Examples

### Example: Setting a Gradient Background

```csharp
using Syncfusion.DocIO;
using Syncfusion.DocIO.Drawing;

// Create a new Word document
WordDocument document = new WordDocument();

// Configure the background as a gradient
document.Background.Type = BackgroundType.Gradient;
document.Background.Gradient.Color1 = Color.Blue;
document.Background.Gradient.Color2 = Color.Red;
document.Background.Gradient.GradientShadingStyle = SdType.ShadingStyle.DIAGONALUP;

// Save the document
document.Save("GradientBackground.docx", FormatType.Docx);
```

## Cross References
- **Related Features:** For more information on configuring other fill effects, see the section on `Texture`, `Pattern`, and `Picture` filling options.

<!-- tags: [DocIO, WinForms, Gradient, Background, Fill Effects, WordDocument, BackgroundType, GradientShadingStyle, GradientShadingVariant] keywords: [background gradient, DocIO, WinForms, fill effects dialog, gradient properties, color configuration, shading style, gradient variant] -->
```