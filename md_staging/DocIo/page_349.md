```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_349.jpeg
document_name: DocIo
page_number: 349
page_id: DocIo#page_349
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:51:19Z
fidelity: lossless
-->

# Essential DocIO

## Overview

- Understand how to add text and picture watermarks to a Word document using DocIO.
- Learn to insert a picture watermark into a Word document using C# and VB.NET examples.

## Content

### Using DocIO

DocIO enables you to add a text watermark and a picture watermark to a Word document. The following code example shows how to insert the picture watermark into the Word document.

#### C#

```csharp
// Create a new word document
WordDocument doc = new WordDocument();
doc.EnsureMinimal();

// Add picture watermark to the document
PictureWatermark picWatermark = new PictureWatermark();
picWatermark.Scaling = 120f;
picWatermark.Washout = true;
doc.Watermark = picWatermark;
picWatermark.Picture = Image.FromFile(ImagesPath + "Water lilies.jpg");

// Save the document
doc.Save("Watermark.doc", FormatType.Doc);

// Close the document
doc.Close();
```

#### VB.NET

```vb.net
' Create a new word document
Dim doc As WordDocument = New WordDocument()
doc.EnsureMinimal()

' Add picture watermark to the document
Dim picWatermark As PictureWatermark = New PictureWatermark()
picWatermark.Scaling = 120f
picWatermark.Washout = True
doc.Watermark = picWatermark
picWatermark.Picture = Image.FromFile(ImagesPath & "Water lilies.jpg")

' Save the document
doc.Save("Watermark.doc", FormatType.Doc)

' Close the document
doc.Close()
```

## Page-level Navigation/TOC (if applicable)

- **Using DocIO**
  - Code examples for inserting picture watermarks using C# and VB.NET.

## Cross References

- Refer to additional sections in the user guide for details on text watermarks and other DocIO features.

## RAG Annotations

<!-- tags: [DocIo, WordDocument, PictureWatermark, C#, VB.NET] keywords: [watermark, picture watermark, text watermark, Word document, Syncfusion, DocIO, watermark insertion] -->
```