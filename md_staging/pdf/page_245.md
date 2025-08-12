```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_245.jpeg
document_name: pdf
page_number: 245
page_id: pdf#page_245
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:39:03Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Overview of signing a document with a timestamp and certificate.
- Example code in both C# and VB to demonstrate adding a timestamp server and signing the document.

## Content

### Example Code for Signing a Document with Timestamp

#### C#

```csharp
//Sign the document with timestamp.
PdfSignature signature = new PdfSignature(page, pdfCert, "Signature");

//Add time stamp using the server URI and credentials.
signature.TimeStampServer = new TimeStampServer(
    new Uri("http://digistamp.syncfusion.com"), "user", 
    "123456");
```

#### VB

```vb
'Get certificate.
Dim pdfCert As New PdfCertificate("...\\Data\\PDF.pfx", "syncfusion")

'Sign the document with timestamp.
Dim signature As New PdfSignature(page, pdfCert, "Signature")

'Add time stamp using the server URI and credentials.
signature.TimeStampServer = New TimeStampServer(New 
Uri("http://digistamp.syncfusion.com"), "user", "123456")
```

## Document Example

The following shows a document signed with the timestamp.

## Conclusion

This section demonstrates how to add a timestamp to a signed PDF document, ensuring that the document is authenticated with a verified timestamp server. The provided code examples illustrate the process in both C# and VB, making it accessible to a broader audience.

<!-- tags: [syncfusion pdf, pdf signing, timestamp server, digital signature] keywords: [pdf, signing, timestamp, certificate, document, certified, authentic, authenticated, Syncfusion, WinForms, synchronous, asynchronous] -->
```