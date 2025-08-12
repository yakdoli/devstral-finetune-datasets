```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_199.jpeg
document_name: pdf
page_number: 199
page_id: pdf#page_199
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:37:27Z
fidelity: lossless
-->

# Essential PDF

## Content

### [VB.NET]

```vb
Dim signature As PdfSignature = New PdfSignature(page, pdfCert, "Signature")
' Setting the certified signature.
signature.Certificated = True
```

### Timestamp in digital signature

Essential PDF supports addition of timestamp in digital signatures. The date and time at which the document is signed can be added as a part of the signature. Timestamps are easier to verify when they're associated with a timestamp authority's trusted certificate. Including a timestamp helps to establish exactly when the document is signed and reduces the chances of an invalid signature. The timestamp can be obtained from a third-party timestamp authority or from the certificate authority that issued the digital ID.

Timestamps appear in the signature field and in the Signature Properties dialog box. If the timestamp is included, the certificate will appear in the **Date/Time** tab of the **Signature Properties** dialog box. If no timestamp is added, the signature field displays the local time of the computer at the moment of signing.

To apply timestamp using Essential PDF, the `TimeStampServer` property of the `PdfSignature` class has to be used. The parameters for the `TimeStampMethod` are the URI of digital server, username, and password.

The following code illustrates the method for adding timestamp in the digital signature.

### C#

```csharp
// Get certificate.
PdfCertificate pdfCert = new PdfCertificate(@"..\..\Data\PDF.pfx", "syncfusion");

// Sign the document with timestamp.
PdfSignature signature = new PdfSignature(page, pdfCert, "Signature");

// Add time stamp using the server URI and credentials.
signature.TimeStampServer = new TimeStampServer(
    new Uri("http://digistamp.syncfusion.com"), "user", "123456");
```

### [VB]

```vb
' Get certificate.
Dim pdfCert As New PdfCertificate("..\..\Data\PDF.pfx", "syncfusion")

' Sign the document with timestamp.
Dim signature As New PdfSignature(page, pdfCert, "Signature")
```

## API Reference

- **Namespace:** Essential PDF
- **Class:** `PdfSignature`
  - **Properties:**
    - `Certificated`: Indicates whether the signature is certified.
    - `TimeStampServer`: Specifies the time stamp server details.
  - **Methods:**
    - `AddTimestamp`: Adds a timestamp to the digital signature.
- **Parameters:**
  - `Uri`: URL of the digital server.
  - `Username`: Username for authentication.
  - `Password`: Password for authentication.

<!-- tags: [Essential PDF, Timestamp, Digital Signature, PDF, Syncfusion Winforms, 11.4.0.26] keywords: [digital signature, timestamp, certified signature, PDF, Syncfusion, time stamp server, signature properties, signature field, document signing, certificate authority] -->
```