```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_286.jpeg
document_name: DocIo
page_number: 286
page_id: DocIo#page_286
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:46:09Z
fidelity: lossless
-->

## Overview
- Essential features and limitations of DocIO in converting documents.
- Conversion capabilities from Doc to HTML and RTF formats.
- Supported document elements and attributes.

## Content

### Essential DocIO

#### Supported Document Elements
- Document Background
- Watermark
- Nested Table
- Footnote / Endnote
- Lists
- Hyperlink
- Symbols [Not all symbols are supported]

#### Unsupported Document Elements
- OLE Object
- RTL

### Note
Currently Doc to RTF conversion is not supported in Silverlight application. Doc to HTML

#### Doc to HTML

You can now open or create Word documents and save to the HTML format, enabling HTML conversion by using DocIO.

The following example illustrates how to save a Word document to HTML format.

#### Code Examples

**[C#]**
```csharp
WordDocument doc = new WordDocument(@"...\\DocToHTML.doc");
HTMLExport htmlExport = new HTMLExport();
htmlExport.SaveAsXhtml(doc, "doctohtml_res.html");
```

**[VB.NET]**
```vb
Dim doc As New WordDocument("...\\DocToHTML.doc")
Dim htmlExport As New HTMLExport()
htmlExport.SaveAsXhtml(doc, "doctohtml_res.html")
```

### Document Elements

#### Summary of Supported Document Elements
DocIO supports the following document elements.

| Document Element | Attribute | Supported | Notes |
|-------------------|-----------|-----------|-------|
| Bookmark          | Position  | Yes       | -     |

## API Reference

### Objects and Attributes

- **Bookmark**: Supported with the `Position` attribute.

## Page-level Navigation/TOC

- **4.8.2 Doc to HTML**
  - Details on converting Word documents to HTML format.

<!-- tags: DocIO, WordDocument, HTMLExport, RTF, HTML, Bookmark, position, list, hyperlink, VB.NET code, C# code, Supported Document Elements, Unsupported Document Elements keywords: word, doc, html, conversion, bookmark, position, list, hyperlink, VB.NET, C# -->
```