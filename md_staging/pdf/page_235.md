```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_235.jpeg
document_name: pdf
page_number: 235
page_id: pdf#page_235
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:40:04Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Describes the techniques used to protect a PDF document, including Encryption and Digital Signature.
- Focuses on the features of Essential PDF for document protection and security.

## Content

### Encryption
A PDF document is encrypted to protect its contents from unauthorized access. Encryption applies to all strings and streams in the document. Essential PDF provides support for 40, 128, and 256-bit encryption. Essential PDF also provides support for restricted document operations like:

- Allow EditContent
- Allow Copy Content
- Allow Edit Annotations
- Allow AccessibilityCopyContent
- Allow AssembleDocument
- Allow Print
- Allow FullQualityPrint

You can also protect a document with a user and owner password.

**Note:** You must add the `Syncfusion.Pdf.Security` namespace to work with security settings.

### Encryption Algorithms
Adobe supports Advanced Encryption Standard (AES) in Adobe version 7.0 and later. Essential PDF also supports strong encryption using 128 and 256-bit AES algorithm. In order to achieve this, specify the type of encryption algorithm in the **Algorithm** property of the Security class.

The following code snippet illustrates this:

```csharp
// C#

// Set 128 bit AES encryption mode.
doc.Security.KeySize = PdfEncryptionKeySize.Key128Bit;
doc.Security.Algorithm = PdfEncryptionAlgorithm.AES;
```

## API Reference

### Members
- **Algorithm**: Specifies the type of encryption algorithm used (e.g., AES).
- **KeySize**: Specifies the key size for encryption (e.g., Key128Bit).

## Code Examples

### C#
```csharp
doc.Security.KeySize = PdfEncryptionKeySize.Key128Bit;
doc.Security.Algorithm = PdfEncryptionAlgorithm.AES;
```

## Tags and Keywords
<!-- tags: [pdf, encryption, digital signature, security, essential pdf, document protection] keywords: [encryption algorithms, aes, key size, document operations, security settings, user password, owner password] -->
```