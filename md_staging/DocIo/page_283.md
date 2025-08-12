```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_283.jpeg
document_name: DocIo
page_number: 283
page_id: DocIo#page_283
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:46:05Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Overview of the encryption and decryption processes for Word documents.
- Demonstrating how to encrypt and decrypt a Word document using code examples in C# and VB.NET.
- Note on the Silverlight platform's limitations regarding encryption and decryption of MS Word 2013 documents.
- Information on the location of encryption and decryption sample code.

## Content

### Encryption and Decryption

**Definition:**
Decryption is the process of converting encrypted data back into its original form so that the data can be read from the document. A password for encrypting a Word document is set in Microsoft Word through the **Security** tab in the **Options** dialog box.

**Example:**
The following example illustrates how to encrypt and decrypt a Word document.

#### Code Examples

**C#:**
```csharp
// Encrypting the Word document with password.
document.EncryptDocument(password);

// Opening the encrypted Workbook.
WordDocument document = new WordDocument(filename, password);
```

**VB.NET:**
```vb
' Encrypting the Word document with password.
document.EncryptDocument(password)

' Opening the encrypted Workbook.
Dim document As New WordDocument(filename, password)
```

**Note:** Currently in the Silverlight platform, Essential DocIO does not support encryption and decryption techniques of MS Word 2013 format documents.

#### Encryption and Decryption Samples Installation Location:
To Locate the Encrypt and Decrypt samples:
`<DocIO.WPF\Samples\3.5\WindowsSamples\Prepare\Encrypt and Decrypt`

**Viewing Encryption and Decryption samples:**
1. Click **Start->All Programs->Syncfusion->Essential Studio <version number> -->Dashboard**.
2. Open **Reporting** edition samples. Click the drop-down button of **WPF** platform and select the **Explore samples** option.

For more information refer to section **2.2 Samples and Location**.

### 4.8 Conversion

## API Reference

## Code Examples

## RAG Annotations
<!-- tags: [encryption, decryption, Syncfusion, Word documents, C#, VB.NET, Silverlight platform, 11.4.0.26, MS Word 2013, Essential DocIO] keywords: [encryptDocument, password, WordDocument, data integrity, data security] -->
```