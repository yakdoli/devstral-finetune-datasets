```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_242.jpeg
document_name: pdf
page_number: 242
page_id: pdf#page_242
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:39:48Z
fidelity: lossless
-->

## Signing a Document with Author's Signature

The following code example illustrates the signing of a document with the author's signature.

### Code Example

#### C#

```csharp
// Map the path of the certificate store.

// Get certificate.
PdfCertificate pdfCert = new PdfCertificate(@"..\..\Data\PDF.pfx", "syncfusion");

// Sign the document in the image.
signature = new PdfSignature(page, pdfCert, "Signature");
bmp = new PdfBitmap(@"..\..\Data\syncfusion_logo.gif");
signature.Bounds = new RectangleF(new PointF(5, 5), bmp.PhysicalDimension);

// Set the Author signature.
signature.Certificated = true;

// Set signature display properties.

// Set signature Info.
signature.ContactInfo = "johndoe@owned.us";
signature.LocationInfo = "Honolulu, Hawaii";
signature.Reason = "I am author of this document.";
```

#### VB

```vb
' Map the path of the certificate store.

' Get certificate.
Dim pdfCert As PdfCertificate = New PdfCertificate("..\\..\Data\PDF.pfx", "syncfusion")

' Sign the document in the image.
signature = New PdfSignature(page, pdfCert, "Signature")
bmp = New PdfBitmap("..\\..\Data\syncfusion_logo.gif")
signature.Bounds = New RectangleF(New PointF(5, 5), bmp.PhysicalDimension)

' Set the Author signature.
Private signature.Certificated = True

' Set signature display properties.

' Set signature Info.
signature.ContactInfo = "johndoe@owned.us"
```

### Notes
- The code demonstrates how to map the certificate store, retrieve a certificate, create a signature, and set various properties such as contact, location, and reason for the signature.
- The signature is embedded in the document, using an image for visual representation.
- Properties like `Certificated`, `ContactInfo`, `LocationInfo`, and `Reason` can be customized as needed.

### API Reference

The following APIs are used in the code example:

- **PdfCertificate**: Represents a digital certificate used for signing.
- **PdfSignature**: Represents a digital signature that can be added to a document.
- **PdfBitmap**: Represents a bitmap image that can be used as part of the signature.
- **RectangleF**: Represents a rectangle defined by its location and dimensions.
- **PointF**: Represents a point with X and Y coordinates.

## References

- **Digital Signatures in PDF Documents**: For more information on digital signatures, refer to the relevant sections in the Syncfusion documentation.
- **Certificate Management**: For detailed information on managing digital certificates, consult the appropriate documentation resources.

<!-- tags: [Syncfusion, Winforms, PDF, Digital Signature, Certificate, AuthorSignature] keywords: [PdfCertificate, PdfSignature, PdfBitmap, RectangleF, PointF, Digital Signature, Author Signature, Certificate Management, Syncfusion Winforms] -->
```
