```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_290.jpeg
document_name: pdf
page_number: 290
page_id: pdf#page_290
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:42:40Z
fidelity: lossless
-->

# Essential PDF

## Overview

- You can add signatures to an existing document using the `PdfSignature` class.
- You can create a document with multiple signatures.
- A new instance is created for the document after saving.

## Content

### Adding Multiple Signatures to a Document

The following code example demonstrates how to create a document with multiple signatures.

```csharp
[C#]

// Append shows empty fields
PdfDocument doc = new PdfDocument();
PdfPageBase page = doc.Pages.Add();

// Creating Certificate
PdfCertificate pdfCert = new PdfCertificate(@"..\test.pfx", "111");

// Adding the signature
PdfSignature signature = new PdfSignature(doc, page, pdfCert, "Signature 1");
PdfBitmap bmp = new PdfBitmap(@"..\PDFDemo.jpg");

// Setting the appearance of the signature
signature.Bounds = new RectangleF(new PointF(5, 5), bmp.PhysicalDimension);
signature.ContactInfo = "john@owner.us";
signature.LocationInfo = "Honolulu, Hawaii";
signature.Reason = "I am author of this document.";
string validto = "Valid To: " + signature.Certificate.ValidTo.ToString();
string validfrom = "Valid From: " + signature.Certificate.ValidFrom.ToString();

PdfSolidBrush brush = new PdfSolidBrush(new PdfColor(1, 1, 255));
PdfPen pen = new PdfPen(brush, 1);
PdfFont font = new PdfStandardFont(PdfFontFamily.Courier, 12, PdfFontStyle.Regular);
PdfGraphics g = signature.Appeareance.Normal.Graphics;
g.DrawImage(bmp, 0, 0);
g.DrawString(validfrom, font, pen, brush, 10, 30);
g.DrawString(validto, font, pen, brush, 10, 10);

// Storing the document
doc.Save("Sample.pdf");
doc.Close(true);

// Load the signed document
PdfLoadedDocument document = new PdfLoadedDocument("Sample.pdf");
page = document.Pages.Add();

// Adding a signature
```

## RAG Annotations
<!-- tags: [pdf, signature, certificate, document, winforms, essentialpdf, syncfusion, 11.4.0.26] keywords: [PdfSignature, PdfCertificate, pdfdocument, pdfpagebase, rectanglef, validto, validfrom, pdfsolidbrush, pdffont, pdfographics, appearance, graphics] -->
```