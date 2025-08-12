```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_379.jpeg
document_name: DocIo
page_number: 379
page_id: DocIo#page_379
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:52:14Z
fidelity: lossless
-->

# Using DocIO

**DocIO** uses the **ProtectionType** property to specify the protection type for a Word document. This property utilizes the following values:

- **AllowOnlyComments** - Allow only comments to be added to the document.
- **AllowOnlyFormFields** - Allow content to be added to the document only through form fields.
- **AllowOnlyRevisions** - Allow only revisions to be made to existing content.
- **NoProtection** - Do not apply protection to the document.

## Code Example

```csharp
// Open the Word document
WordDocument doc = new WordDocument("Document.doc");

// Set "Allow only Comments" protection to the Word document
doc.Protect(ProtectionType.AllowOnlyComments, "");

// Save the document
doc.Save("FileProtectionDocIO.doc");
```

<!-- tags: [DocIO, WordDocument, ProtectionType, Syncfusion Winforms, C#] keywords: [DocIO, WordDocument, ProtectionType, AllowOnlyComments, AllowOnlyFormFields, AllowOnlyRevisions, NoProtection] -->
```