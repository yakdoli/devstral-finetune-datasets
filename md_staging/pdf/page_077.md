```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_077.jpeg
document_name: pdf
page_number: 077
page_id: pdf#page_077
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:28:25Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Provides information on using `PdfPen` and `PdfBrushes` classes.
- Details about the `PdfFont` base class and its derived classes.
- Discusses the immutability of fonts and the capabilities of fonts caching.

## Content

### [C#]

```csharp
PdfPen pen = new PdfPen(Color.Black);
```

### [VB.NET]

```vb
Dim pen As Syncfusion.Pdf.Graphics.PdfPen = New Syncfusion.Pdf.Graphics.PdfPen(Color.Black)
```

#### PdfPens and PdfBrushes

If you do not want to create pens and brushes on your own, you can use static classes that provide you with static immutable pens and brushes. Each property is named after the color of the pen or brush that it returns.

### 4.1.1.4 Fonts

**PdfFont** is the base class for all the fonts. The design of the fonts is similar to Microsoft.NET fonts. Fonts are immutable objects, i.e., they cannot be modified, once created.

**Note:** There are special constructors that are used to create a new font from a prototype font, but with different settings.

The following are the features of the PDF fonts:

- PDF font objects do not have any size; the size is set only during text printing. This provides the advantage of being able to use the same fonts with different sizes.
- There are no Underline and Strikeout font styles in PDF. Underline and Strikeout font styles are emulated by drawing a line.

As mentioned above, all the fonts derived from `PdfFonts` are immutable. However, there are capabilities for fonts caching. It means, if there are two similar fonts that have different sizes and Underline or Strikeout styles, just one font object will be stored in the PDF file. So, if a lot of similar fonts with different sizes, and Underline or Strikeout styles are created, there is a huge benefit from the fonts caching in terms of speed and memory usage.

**Note:** Fonts caching works for all font types that are supported.

The following are the classes derived from `PdfFont`.

```html
<!-- tags: [pdf, fonts, pen, brush, immutable, caching, winsdk, version 11.4.0.26] keywords: [PdfPen, PdfBrushes, PdfFont, immutable fonts, fonts caching, Syncfusion Winforms, Essential PDF] -->
```