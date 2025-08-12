```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_288.jpeg
document_name: pdf
page_number: 288
page_id: pdf#page_288
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:41:23Z
fidelity: lossless
-->

# Essential PDF

## Overview
- Explains how to merge multiple PDF documents from streams.
- Demonstrates merging two files using the `Append` method.
- Illustrates merging pages of different documents by importing all pages from one document to another.

## Content

### Merging Multiple PDF Documents from Streams

It is also possible to merge multiple PDF documents from stream. The following code example illustrates this.

#### C#

```csharp
Stream[] streams = { stream1, stream2 };
PdfDocumentBase.Merge(doc, streams);
doc.Save("sample.pdf");
```

#### VB.NET

```vb.net
Dim streams As Stream() = {stream1, stream2}
PdfDocumentBase.Merge(doc, streams)
doc.Save("sample.pdf")
```

### Merging Two Files using Append Method

You can also merge two files, by appending one file after another. The following code example illustrates this.

#### C#

```csharp
// Append PDFDocument.
doc1.Append(doc2);
```

#### VB.NET

```vb.net
' Append PDFDocument.
doc1.Append(doc2)
```

### Merging Pages of Different Documents

Yet another way of merging will be, to import all the pages from one document to another. The following code example illustrates this.

#### C#

```csharp
// Import all the pages to another document
doc2.ImportPageRange(doc2, 0, doc.Pages.Count);
```

### Legacy Footer Information

© 2013 Syncfusion. All rights reserved. 288 | Page
<!-- tags: [pdf, merging, multiple documents, files, append, pages, import, streams, Syncfusion Winforms, 11.4.0.26] keywords: [merging pdf documents, appending files, importing pages, streams, Syncfusion, C#, VB.NET] -->
```