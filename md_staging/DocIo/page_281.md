```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_281.jpeg
document_name: DocIo
page_number: 281
page_id: DocIo#page_281
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:46:59Z
fidelity: lossless
-->

## Essential DocIO

### Content

```vb
Dim doc As WordDocument = New WordDocument("Sample.doc")
Dim fieldname As String() = {"FirstName", "LastName"}
Dim fieldvalues As String() = {"John", "David"}
doc.MailMerge.ClearFields = False
doc.MailMerge.Execute(fieldname, fieldvalues)
```

#### 4.7 Security

DocIO provides support to protect a Word document. Here protection restricts the access to the elements present within the document. In MS Word, a document is protected through the **Protect Document** option in the **Tools** menu.

<Figure 1: Screenshot of Protect Document option in the Tools Menu>

<Figure 2: Screenshot of the Protect Document dialog box>

## API Reference
- This section would typically include a detailed reference to the `MailMerge`, `WordDocument`, and other relevant classes and methods used in the code example, but it is not provided here.

## Code Examples
```vb
Dim doc As WordDocument = New WordDocument("Sample.doc")
Dim fieldname As String() = {"FirstName", "LastName"}
Dim fieldvalues As String() = {"John", "David"}
doc.MailMerge.ClearFields = False
doc.MailMerge.Execute(fieldname, fieldvalues)
```

<!-- tags: [DocIOMailMerge, DocumentProtection, WordDocument] keywords: [WordMerge, DocumentSecurity, VB.NET] -->
```