```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_081.jpeg
document_name: pdf
page_number: 081
page_id: pdf#page_081
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:28:40Z
fidelity: lossless
-->

# Essential PDF

## Example Code

### C#

```csharp
PdfLoadedDocument lDoc = new PdfLoadedDocument(filename);
page = lDoc.Pages.Add() as PdfPage;

PdfGraphics g = page.Graphics;
PdfFont font = new PdfStandardFont(PdfFontFamily.Helvetica, 14, PdfFontStyle.Bold);
g.DrawString("Polygon", font, PdfBrushes.DarkBlue, new PointF(50, 0));

lDoc.Save(filename);
lDoc.Close();
```

### VB

```vb
Dim lDoc As Syncfusion.Pdf.Parsing.PdfLoadedDocument = New Syncfusion.Pdf.Parsing.PdfLoadedDocument(filename)
page = TryCast(lDoc.Pages.Add(), PdfPage)

Dim g As Syncfusion.Pdf.Graphics.PdfGraphics = page.Graphics
Dim font As Syncfusion.Pdf.Graphics.PdfFont = New Syncfusion.Pdf.Graphics.PdfStandardFont(PdfFontFamily.Helvetica, 14, PdfFontStyle.Bold)
g.DrawString("Polygon", font, PdfBrushes.DarkBlue, New PointF(50, 0))

lDoc.Save(filename)
lDoc.Close()
```

## 2. Paginating the text Area

The `PdfTextElement` class represents the text area with the ability to span several pages. The `Layout` property of the `PdfLayoutFormat` class enables breaking the text into multiple pages. Unicode text is also supported by this method.

### C#

```csharp
// Create a text element with large amount of text.
PdfTextElement element = new PdfTextElement(text, font);

// Set the properties for the text element.
element.Brush = new PdfSolidBrush(Color.Black);

// Set the string format. This can be used for setting unicode text.
element.StringFormat = format;
```

<!-- tags: [pdf, paginating, text, element, synchronization, unicode, text, support] keywords: [pdfloadeddocument, pdfgraphics, pdffont, drawstring, element(string, font), pdftextelement, pdfstandardfont, pdfsolidbrush, stringformat, text breakage] -->
```