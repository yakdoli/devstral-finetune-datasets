```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_212.jpeg
document_name: pdf
page_number: 212
page_id: pdf#page_212
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:36:41Z
fidelity: lossless
-->

# Essential PDF

## Content

### Overview
- Demonstrates how to create and save a PDF document.
- Includes drawing text with specified font and brush.
- Explains the usage of PDF graphics to render content.

### Detailed Steps

```csharp
// Draws the text.
g.DrawString("Hello world!", font, brush, new PointF(20, 20));

// Saves the document.
doc.Save("Sample.pdf");
```

```vb
' Creates a new PDF document.
Dim doc As PdfDocument = New PdfDocument()

' Adds a page to the document.
Dim page As PdfPage = doc.Pages.Add()

' Creates Pdf graphics for the page
Dim g As PdfGraphics = page.Graphics

' Creates a solid brush
Dim brush As PdfBrush = New PdfSolidBrush(Color.Black)

' Sets the font
Dim font As PdfFont = New PdfStandardFont(PdfFontFamily.Helvetica, fontSize)

' Draws the text
g.DrawString("Hello world!", font, brush, new PointF(20, 20))

' Saves the document.
doc.Save("Sample.pdf")
```

## API Reference

### Properties and Methods
- **PdfDocument**: The main class for creating and managing PDF documents.
  - **Add()**: Adds a new page to the document.
  - **Pages**: Collection of all pages in the document.
  - **Save(string)**: Saves the document to the specified file path.

- **PdfPage**: Represents a single page in the PDF document.
  - **Graphics**: Provides access to rendering tools for the page.

- **PdfGraphics**: Provides methods for drawing text, lines, and shapes.
  - **DrawString(string, PdfFont, PdfBrush, PointF)**: Renders text at the specified location.

- **PdfBrush**: Represents the brush used to fill drawing objects.
  - **PdfSolidBrush(Color)**: Creates a brush with a solid color.

- **PdfFont**: Represents fonts for rendering text.
  - **PdfStandardFont(PdfFontFamily, float)**: Creates a standard font with the specified font family and size.

## Code Examples

### C# Example

```csharp
PdfDocument doc = new PdfDocument();
PdfPage page = doc.Pages.Add();
PdfGraphics g = page.Graphics;

PdfBrush brush = new PdfSolidBrush(Color.Black);
PdfFont font = new PdfStandardFont(PdfFontFamily.Helvetica, 12);
g.DrawString("Hello world!", font, brush, new PointF(20, 20));

doc.Save("Sample.pdf");
```

### VB.NET Example

```vb
Dim doc As PdfDocument = New PdfDocument()
Dim page As PdfPage = doc.Pages.Add()
Dim g As PdfGraphics = page.Graphics

Dim brush As PdfSolidBrush = New PdfSolidBrush(Color.Black)
Dim font As PdfFont = New PdfStandardFont(PdfFontFamily.Helvetica, 12)
g.DrawString("Hello world!", font, brush, new PointF(20, 20))

doc.Save("Sample.pdf")
```

## Page-level Navigation/TOC

- **Creating PDF Documents**
  - Overview and API Reference
  - Code Examples

## Cross References

- See also: [PdfDocument Class Documentation](#) for detailed information on additional functionalities.

<!-- tags: [syncfusion, winforms, pdf, document, api, essential pdf] keywords: [pdf document, drawstring, text, font, brush, solidbrush, page, graphics, save] -->
```