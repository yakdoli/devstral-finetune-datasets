```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_193.jpeg
document_name: pdf
page_number: 193
page_id: pdf#page_193
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:35:59Z
fidelity: lossless
-->

# Essential PDF

```csharp
document.Save("sample.pdf")
```

## 4.1.4 Security

Security features of Adobe enable to authenticate and authorize any person reviewing their PDF reports. This section demonstrates various security features supported by Essential PDF. It includes the following topics.

- Encryption - This topic demonstrates how the PDF file is encrypted and decrypted with password by using Essential PDF
- Signing - This topic demonstrates various signatures supported by Essential PDF and how they can be applied to a PDF document

**Note:** You must add the `Syncfusion.Pdf.Security` namespace to work with interactive features.

### 4.1.4.1 Encryption

The PDF document can be encrypted with 40, 128, and 256 bit key to protect its contents from unauthorized access. Document permissions are managed with owner and user passwords and access rights of the document.

<!-- tags: [Essential PDF, security, encryption, signing, Adobe, Syncfusion Winforms, 11.4.0.26] keywords: [PDF encryption, PDF signing, owner password, user password, document permissions, Syncfusion.Pdf.Security, password protection, 40 bit, 128 bit, 256 bit, unauthorized access] -->
```