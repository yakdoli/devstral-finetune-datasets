```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_181.jpeg
document_name: pdf
page_number: 181
page_id: pdf#page_181
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:35:15Z
fidelity: lossless
-->

# Free Text Annotation

## Overview
- This page explains the properties available for creating free text annotations in PDF documents using the Syncfusion Winforms library.
- It provides details on settings such as text content, color, font, background color, and border color for annotations.

## Content

### Free Text Annotation

**Figure 28: Free Text Annotation**

The image shows a screenshot of a PDF document in Adobe Acrobat Pro Extended, illustrating a free text annotation with a callout. The annotation is highlighted with a pink background and includes a drawn line.

---

### List of Properties

The following table lists the properties available for customizing free text annotations:

| Property        | Type        | Value It Accepts      | Description                                                                 |
|-----------------|-------------|-----------------------|-----------------------------------------------------------------------------|
| MarkupText     | String      | String               | Allows you to set the comment text.                                         |
| TextMarkupColor | Color       | PdfColor             | Allows you to set the color of the comment text.                           |
| Font            | Font        | PdfStandardFont/PdfTrueTypeFont | Allows you to set the font type for the comment text.                  |
| Color           | Color       | PdfColor             | Allows you to set the background color of the Annotation box.              |
| BorderColor     | Color       | PdfColor             | Allows you to set the border color of the Annotation box.                  |

---

## API Reference

### Properties
- **MarkupText**
  - Type: String
  - Value: String
  - Description: Allows setting the comment text content.

- **TextMarkupColor**
  - Type: Color
  - Value: PdfColor
  - Description: Allows setting the color of the comment text.

- **Font**
  - Type: Font
  - Value: PdfStandardFont/PdfTrueTypeFont
  - Description: Allows setting the font type for the comment text.

- **Color**
  - Type: Color
  - Value: PdfColor
  - Description: Allows setting the background color of the Annotation box.

- **BorderColor**
  - Type: Color
  - Value: PdfColor
  - Description: Allows setting the border color of the Annotation box.

## Code Examples

### Setting Free Text Annotation in C#

```csharp
using Syncfusion.Pdf;
using Syncfusion.Pdf.Graphics;
using Syncfusion.Pdf.Interactive;

// Create a new PDF document
PdfDocument document = new PdfDocument();

// Add a page
PdfPage page = document.Pages.Add();

// Create a PdfFreeTextAnnot
PdfFreeTextAnnot freeTextAnnot = new PdfFreeTextAnnot(new RectangleF(50, 50, 200, 100));
freeTextAnnot.MarkupText = "Free Text with Callouts";
freeTextAnnot.TextMarkupColor = PdfColor.Red;
freeTextAnnot.Font = new PdfStandardFont(PdfFontFamily.Helvetica, 12);
freeTextAnnot.Color = PdfColor.LightPink;
freeTextAnnot.BorderColor = PdfColor.Black;

// Add the annotation to the page
page.Annotations.Add(freeTextAnnot);

// Save the document
document.Save("FreeTextAnnotation.pdf");

// Close the document
document.Close();
```

---

<!-- tags: [Syncfusion Winforms, PDF, Annotation, Free Text Annotation, PdfColor, PdfStandardFont] keywords: [free text annotation, markup text, text markup color, font, background color, border color] -->
```