```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_236.jpeg
document_name: pdf
page_number: 236
page_id: pdf#page_236
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:38:15Z
fidelity: lossless
-->

## Essential PDF

### Note: Encryption Algorithm Selection
Note: 40-bit encryption will use RC4 algorithm by default and 256-bit encryption uses AES algorithm.

### Content

The following code example illustrates the protection of documents with user and owner password.

#### C#

```csharp
// Set encryption key.
doc.Security.KeySize = PdfEncryptionKeySize.Key128Bit;
doc.Security.Algorithm = PdfEncryptionAlgorithm.AES;

// Setting username and password to protect the document.
doc.Security.OwnerPassword = "syncfusion";
doc.Security.UserPassword = "password";

// Allow print with full quality.
doc.Security.Permissions = PdfPermissionsFlags.Print | 
PdfPermissionsFlags.FullQualityPrint;
```

#### VB.NET

```vbnet
' Set encryption key.
doc.Security.KeySize = PdfEncryptionKeySize.Key128Bit
doc.Security.Algorithm = PdfEncryptionAlgorithm.AES

' Setting username and password to protect the document.
doc.Security.OwnerPassword = "syncfusion"
doc.Security.UserPassword = "password"

' Allow print with full quality.
doc.Security.Permissions = PdfPermissionsFlags.Print Or 
PdfPermissionsFlags.FullQualityPrint
```

#### Overview

The following screen shot shows how to open an encrypted document.

---

**Figure:** How to open an encrypted document (image placeholder)
```html
<!-- tags: [essential pdf, encryption, c#, vb.net, document protection, user password, owner password, print permissions, 128-bit key, aes algorithm] keywords: [encryption algorithm, pdf encryption, key size, permissions, protect document] -->
```
```