```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_291.jpeg
document_name: pdf
page_number: 291
page_id: pdf#page_291
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:43:28Z
fidelity: lossless
-->

## Overview
- Demonstrates creating and adding digital signatures in PDF documents using C# and VB.NET.
- Shows how to handle certificate details and customize signature appearance.
- Includes instructions on embedding images and text into PDF signatures.

## Content

### Adding a Digital Signature to a PDF Document

This section describes how to add a digital signature to a PDF document, customize its appearance, and store the signed document.

#### C# Code Example

```csharp
PdfSignature signature1 = new PdfSignature(document, page, pdfCert, "Signature 2");

PdfBitmap bmp1 = new PdfBitmap(@"..\Image.jpg");
signature1.Bounds = new RectangleF(new PointF(5, 5), bmp.PhysicalDimension);
signature1.ContactInfo = "Roase@owned.us";
signature1.LocationInfo = "London, UAE";
signature1.Reason = "I am second author of this document.";
validto = "Valid To: " + signature1.Certificate.ValidTo.ToString();
validfrom = "Valid From: " + signature1.Certificate.ValidFrom.ToString();

brush = new PdfSolidBrush(new PdfColor(1, 1, 255));
pen = new PdfPen(brush, 1);
font = new PdfStandardFont(PdfFontFamily.Courier, 12, PdfFontStyle.Regular);
g = signature1.Appearance.Normal.Graphics;
g.DrawImage(bmp1, 100, 400);
g.DrawString(validfrom, font, pen, brush, 10, 30);
g.DrawString(validto, font, pen, brush, 10, 10);

// Store the document
document.Save("Sample1.pdf");
```

#### VB.NET Code Example

```vb
' Append shows empty fields
Dim doc As PdfDocument = New PdfDocument()
Dim page As PdfPageBase = doc.Pages.Add()

' Creating Certificate
Dim pdfCert As PdfCertificate = New PdfCertificate("..\.test.pfx", "111")

' Adding the signature
Dim signature As PdfSignature = New PdfSignature(doc, page, pdfCert, "Signature 1")
Dim bmp As PdfBitmap = New PdfBitmap("..\.PDFDemo.jpg")

' Setting the appearance of the signature
signature.Bounds = New RectangleF(New PointF(5, 5), bmp.PhysicalDimension)
signature.ContactInfo = "johndoe@owned.us"
signature.LocationInfo = "Honolulu, Hawaii"
signature.Reason = "I am author of this document."
    Dim validto As String = "Valid To: " & signature.Certificate.ValidTo.ToString()
    Dim validfrom As String = "Valid From: " & signature.Certificate.ValidFrom.ToString()

Dim brush As PdfSolidBrush = New PdfSolidBrush(New PdfColor(1, 1,
```

### Key Steps

1. **Create a PDF Document**: Initialize a new PDF document object.
2. **Add Pages**: Add a new page to the document.
3. **Generate a Certificate**: Create a PDF certificate using a PFX file and password.
4. **Create a Signature**: Instantiate a `PdfSignature` object with the document, page, certificate, and name of the signature.
5. **Customize Appearance**: Set the bounds, contact information, location, and reason properties of the signature.
6. **Embed Images and Text**: Draw an image and add text using `PdfSolidBrush`, `PdfPen`, and `PdfStandardFont`.
7. **Save the Document**: Save the signed PDF document to a file.

## API Reference

### Namespaces and Classes
- `PdfSignature`: Represents a digital signature in a PDF document.
- `PdfCertificate`: Represents a digital certificate used for signing.
- `PdfBitmap`: Represents an image that can be embedded in a PDF document.
- `PdfSolidBrush`, `PdfPen`, `PdfStandardFont`: Classes for customizing the appearance of the signature.

### Parameters
- `document`: The PDF document to which the signature is added.
- `page`: The specific page in the document for the signature.
- `pdfCert`: The digital certificate used for signing.
- `bounds`: The rectangular bounds for the signature.
- `contactInfo`, `locationInfo`, `reason`: Metadata for the signature.
- `validTo`, `validFrom`: Strings indicating the validity period of the certificate.
- `brush`, `pen`, `font`: Graphics objects used for drawing.

## Code Examples

The provided examples illustrate how to:
- Add a signature to a PDF document.
- Customize the signature's appearance with images and text.
- Save the resulting PDF document.

<!-- tags: [Syncfusion, PDF, digital signature, certificate, appearance, C#, VB.NET] keywords: [digital signature, PDF document, certificate, appearance, bounds, contact info, location, reason, valid from, valid to, image, text, brush, pen, font] -->
```