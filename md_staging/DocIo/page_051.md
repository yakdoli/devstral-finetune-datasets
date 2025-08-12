```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_051.jpeg
document_name: DocIo
page_number: 051
page_id: DocIo#page_051
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:31:13Z
fidelity: lossless
-->

# 3.4 Saving the Word Document

This topic illustrates how to save the Word document created in an application.

Essential DocIO provides support to save the Word document to the following formats:

- Doc
- Docx
- Dot
- Rtf
- Html
- Text
- Xml
- Docm
- Dotm
- Dotx

## Saving the Word document in Windows Forms and WPF Applications

To use DocIO in Windows Forms and WPF applications, you must save the created document to disk. The following code example illustrates this.

### Code Example: Saving the Document to Disk

#### C#

```csharp
// Saving the document to disk.
doc.Save("Sample.doc", FormatType.Doc);
```

#### VB.NET

```vb
' Saving the document to disk.
doc.Save("Sample.doc", FormatType.Doc)
```

**Note:** Essential DocIO also provides support to save the document into the Stream. For details, see [Stream Support](Stream Support).

## Saving the Word document in ASP.NET Application

<!-- tags: [syncfusion-sdk, word-document, docio, windows-forms, wpf, asp.net] keywords: [DocIO, Word document, save, disk, stream, Windows Forms, WPF, ASP.NET] -->
```