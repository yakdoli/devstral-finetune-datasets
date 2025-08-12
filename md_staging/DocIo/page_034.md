```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_034.jpeg
document_name: DocIo
page_number: 034
page_id: DocIo#page_034
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:30:02Z
fidelity: lossless
-->

## Overview
- Demonstrates saving a document to disk using C# and VB.NET code examples.
- Displays a sample Word document that has been created through the given procedure.

## Content

### Saving the Document to Disk

The following code snippets illustrate how to save a document to disk using both C# and VB.NET.

[C#]
```csharp
// Saving the document to disk.
document.Save("Sample.doc", FormatType.Doc);
```

[VB.NET]
```vbnet
' Saving the document to disk.
document.Save("Sample.doc", FormatType.Doc)
```

### Sample Word Document Created

The sample Word document created through the above procedure is shown below.

**Figure 17: Word Document**
![](https://example.com/figure17_word_document.png)

A Word document is created in the Windows application.

## References and Notes
- The sample demonstrates the use of `document.Save` with the specified format type.
- The output shows a basic Word document containing the text "Hello World!".

<!-- tags: [DocIO, Winforms, Word, DocumentSave, C#, VB.NET] keywords: [document, save, disk, format, Word, sample] -->
```