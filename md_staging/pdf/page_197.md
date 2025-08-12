```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_197.jpeg
document_name: pdf
page_number: 197
page_id: pdf#page_197
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:36:09Z
fidelity: lossless
-->

# TimeStampServer

| TimeStampServer | Sets the timestamp for the signature. |
| --- | --- |

## Features

- **Appearance**: PdfAppearance allows you to draw and create custom appearance on the PdfSignature field.
- **Certificated**: Allows document recipients to know, if any changes have been made, contrary to the author's intent.
- **DocumentPermissions**: Allows you to set permissions on certificated document with help of the PdfCertificationFlags.
- **Visible / Invisible Signature**: Allows you to create visible or invisible signatures by enabling the Visible property.
- **TimeStampServer**: Allows you to include timestamp for the digital signature.

### PdfCertificate

When you use digital signatures, each user is given a digital certificate. This certificate is actually a small file on a disk or on another device, such as a smart card. Each certificate contains a unique code, and the certificate imprints this code on each signature you create with it. This means that all of your signatures can be traced back to your certificate, and the certificate itself can be traced back to you. In this way, digital signatures identify you through a clear chain of ownership.

It is a class that provides the functionality to use certificates for PdfSignature from PFX files or local Certification Storage. Certificates in local storage are found by using static methods FindByIssuer, FindBySubject, FindBySerialId. Also, there is the GetCertificates static method, which allows to get an array of all certificates from the local storage.

### Standard Signature

PdfCertificate class is used for getting the certificates from disk and PdfSignature class is used to sign a document with the given certificate. PdfSignature class has methods and properties that allow to set the signature information such as reason, location information, bounds where the signature has to be placed, and contact information.

The following code example illustrates this.

```csharp
[C#]
PdfCertificate pdfCert = new PdfCertificate("PDF.pfx", "111");
// Find certificate by Issuer.
```

## API Reference

### WinForms-specific conventions
- The document discusses properties and methods related to digital signatures, specifically `PdfCertificate` and `PdfSignature`.
- These classes handle certificate retrieval and document signing functionality.

## Code Examples

The example shown demonstrates how to create a `PdfCertificate` object and locate a certificate by its issuer, using the `PdfCertificate` class.

## Page-level Navigation/TOC (if applicable)

This page covers essential aspects of digital signatures in Syncfusion Winforms, focusing on `PdfCertificate` and `PdfSignature` classes, their features, and example usage.

## Cross References

Refer to related documentation or sections explaining PFX files, local certification storage, and methods like `FindByIssuer`, `FindBySubject`, and `FindBySerialId`.

<!-- tags: [syncfusion-sdk, syncfusion-winforms, pdfcertificate, pdfsignature, digital-signatures, certificatedocuments, timestamps, winforms-specific] keywords: [pdfappearance, pdfcertificationflags, visibleinvisiblesignature, timestampserver, documentspermissions, clearchainofownership, standardsignature, reason, location, bounds, contact] -->
```