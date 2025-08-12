```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_198.jpeg
document_name: pdf
page_number: 198
page_id: pdf#page_198
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:37:05Z
fidelity: lossless
-->

# Essential PDF

```csharp
PdfCertificate findByIssuer = PdfCertificate.FindByIssuer(sType, pdfCert.IssuerName);

// Draw the signature.
PdfSignature signature = new PdfSignature(page, pdfCert, "Signature");
signature.Bounds = new RectangleF(0, 0, 250, 100);

// Set Signature info.
signature.Reason = "I am author of this document.";
```

### [VB.NET]

```vb
Dim pdfCert As PdfCertificate = New PdfCertificate("PDF.pfx", "111")

' Find certificate by Issuer.
Dim findByIssuer As PdfCertificate = PdfCertificate.FindByIssuer(sType, pdfCert.IssuerName)

' Draw the signature.
Dim signature As PdfSignature = New PdfSignature(page, pdfCert, "Signature")
signature.Bounds = New RectangleF(0, 0, 250, 100)

' Set Signature info.
signature.Reason = "I am author of this document."
```

## Author Signature

By default, documents are signed with standard signature types. The `Certificated` property of PdfSignature is used to create an author signature. When signed with this type of signature, any modification after signing will be detected, and hence does not provide support to add multiple signatures.

**Note:** This implementation of certification will only work in Acrobat 7 and higher versions.

The following code example illustrates this.

### [C#]

```csharp
PdfSignature signature = new PdfSignature(page, pdfCert, "Signature");
// Setting the certified signature.
signature.Certificated = true;
```
```