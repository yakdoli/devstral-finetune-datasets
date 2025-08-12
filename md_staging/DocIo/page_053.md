```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_053.jpeg
document_name: DocIo
page_number: 053
page_id: DocIo#page_053
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:31:52Z
fidelity: lossless
-->

# Essential DocIO

```vb
[VB.NET]

Dim sfd As New SaveFileDialog() With {.DefaultExt = "doc", .FilterIndex = 1}
If sfd.ShowDialog() = True Then
    Using stream As Stream = sfd.OpenFile()
        document.Save(stream, FormatType.Doc)
    End Using
End If
```

## 3.5 Feature Summary

Essential DocIO provides support for the following features:

### General

- Creating and editing a new document.
- Modify existing MS Word documents.
- Open or Save a document as a Stream.
- Save a document as a Text file.
- Ability to create a docx Document.
- Ability to read docx file.
- Essential DocIO will support almost all the features in .docx which are available in .doc format.
- Ability to insert Ole objects from existing document to another document.
- Ability to Clone multiple documents and merge it into a single document.
- Ability to read and write Built-In and Custom Document properties.
- API to manipulate Page Setup settings.
- Ability to insert Vector Images.
- Ability to Watermark document with pictures and text.
- Ability to set the Background for a document.
- Ability to add or edit different types of Hyperlinks like Files, Images, Bookmarks and Email Hyperlinks.
- Ability to deploy applications with DocIO in medium trust.

### Formatting Support

- Ability to create Formatted Tables in the document.
- Format text in the document.
- Ability to format content using Custom Styles.

### Import and Export

- Unclear.

## API Reference (if applicable)

### Code Examples (multi-language supported)

- Extract ALL code exactly. Use fenced blocks with language: ```csharp, ```vb, ```xml, ```xaml, ```js, ```css, ```ts, ```python.
- Keep full signatures, imports/usings, comments, region markers.
- Inline code in text should be wrapped with backticks.

<!-- tags: [product, module, control, api, version?] keywords: [DocIO, Feature Summary, SaveFileDialog, stream, Ole objects, Document Properties, Page Setup, Vector Images, Hyperlinks, Medium Trust, Formatted Tables, Text Formatting, Custom Styles, Import, Export] -->
```