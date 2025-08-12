```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_282.jpeg
document_name: DocIo
page_number: 282
page_id: DocIo#page_282
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:45:57Z
fidelity: lossless
-->

# Essential DocIO

## Content

### Overview
- Explains how to protect Word documents using DocIO.
- Describes various protection types supported by Word documents.
- Provides examples of securing documents with passwords and protection types.

### Protection in Word Documents

**Figure 81: Protect Document Dialog Box**

DocIO supports protection while reading and writing Word documents for both `.doc` and `.docx` formats. This can be provided through the following APIs:

#### Supported Protection Types
- **AllowOnlyComments**: Only comments are allowed.
- **AllowOnlyFormFields**: Modification of form field values is allowed.
- **AllowOnlyRevisions**: Only revisions are allowed.
- **AllowOnlyReading**: Only reading is allowed.
- **NoProtection**: The document has no protection.

You can also provide a password to restrict the user from editing documents. You can enable or disable document protection by using the `WordDocument.ProtectionType` property, when the document is opened with DocIO.

#### Example: Using ProtectionType Property

**C#**
```csharp
IWordDocument doc = new WordDocument("sample.doc");
doc.Protect(ProtectionType.AllowOnlyComments, "password");
doc.Save("Protection.doc");
```

**VB.NET**
```vb
Dim doc As IWordDocument = New WordDocument("sample.doc")
doc.Protect(ProtectionType.AllowOnlyComments, "password")
doc.Save("Protection.doc")
```

### For More Information Refer:
- [Encryption and Decryption]

---

### 4.7.1 Encryption and Decryption

Encryption is a method of protecting the Word document. It is based on a password, which converts it into a form that cannot be understood. It restricts anonymous users from accessing a document.
```