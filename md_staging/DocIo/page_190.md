```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_190.jpeg
document_name: DocIo
page_number: 190
page_id: DocIo#page_190
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:39:55Z
fidelity: lossless
-->

# Getting Started with Essential DocIO

## Overview

- Demonstrates creating a new document and inserting a footnote using VB.NET syntax.
- Shows how to format footnotes and append text.
- Highlights the usage of the `Footnote` class with properties for initialization.

## Content

### Adding Footnotes in VB.NET

```vb
' Creating a new document
Dim document As WordDocument = New WordDocument

' Creating a section
Dim section1 As ISection = document.AddSection

' Adding a paragraph to a section
Dim paragraph As IParagraph = section1.AddParagraph

' Creating a footnote
Dim footnote As WFootnote = New WFootnote(document)

' Appending endnote
footnote = paragraph.AppendFootnote(Syncfusion.DocIO.FootnoteType.Endnote)

' Setting the footnote character format
footnote.MarkerCharacterFormat.SubSuperScript = SubSuperScript.SuperScript

' Inserting Text into the paragraph
paragraph.AppendText("Essential DocIO").CharacterFormat.Bold = True

' Adding footnote text
paragraph = footnote.TextBody.AddParagraph
paragraph.AppendText("Essential DocIO is a .NET library that has a simple yet powerful object model which provides the ability to customize the document to a great extent. ")

' Saving the document to disk
document.Save("Sample.doc", Syncfusion.DocIO.FormatType.Doc)
```

### 4.4.1.5.1 Footnote and Endnote Separators

A footnote or endnote separator is a line preserved between the body and the endnotes or footnotes in a Microsoft Word document. A footnote or endnote continuation separator is a line running across the top section indicating that the footnotes or endnotes are carried over from the preceding page if they run over to the second page. A footnote or endnote continuation notice is a special character or word preserved at the bottom of the footer area to indicate that the footnotes or endnotes continue to the next page.

#### 4.4.1.5.1.1 Properties
**Public Constructors**

| Name | Description |
| --- | --- |
| Footnote.Footnote(WordDocument) | Initializes a new instance of the Footnote class. |

---

<!-- tags: [syncfusion, docio, worddocument, footnote, endnote, separators, vb.net, winforms] keywords: [footnote, endnote, separators, document creation, footnotetype, endnote, markers, continuation, continuation notice, character formatting] -->
```