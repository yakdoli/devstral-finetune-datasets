```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_244.jpeg
document_name: pdf
page_number: 244
page_id: pdf#page_244
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:38:38Z
fidelity: lossless
-->

# Essential PDF

## Content

### Overview
- Explains the process of applying a timestamp to a digital signature using Syncfusion's Essential PDF library.
- Details the use of the `TimeStampServer` property to integrate timestamp functionality.
- Provides guidance on setting up the `TimeStampMethod` parameters for secure timestamping.
- Includes example code for obtaining a certificate and applying a timestamp to a digital signature.

### Signature Properties
The image shows the properties of a digital signature, including validation details, timestamp information, and authority verification.

#### Timestamp Properties
- **Signature Validity**: The digital signature is valid and signed by `support@syncfusion.com`.
- **Timestamp Authority**: The timestamp is provided by `DigiStamp test <info@e-TimeStamp.cc>`.
- **Timestamp Policy**: The policy for this timestamp is represented by the identifier `1.3.6.1.4.1.8291.1.1`.

#### Figure: Timestamp properties of the digital signature
![Timestamp properties of the digital signature](Figure 53: Timestamp properties of the digital signature)

### Applying Timestamp with Essential PDF
To apply a timestamp using Essential PDF, the `TimeStampServer` property of the `PdfSignature` class has to be used. The parameters for the `TimeStampMethod` are the URL of the digital server, username, and password.

### Code Example for Adding Timestamp
The following code illustrates the method for adding a timestamp to the digital signature.

```csharp
// Get certificate.
PdfCertificate pdfCert = new PdfCertificate(@"..\Data\PDF.pfx", "syncfusion");
```

## Page-level Navigation/TOC
- [unclear]

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [Essential PDF, digital signature, timestamp, syncfusion, c#, PdfSignature, TimeStampServer, TimeStampMethod, PdfCertificate] -->
```