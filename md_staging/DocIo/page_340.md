```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_340.jpeg
document_name: DocIo
page_number: 340
page_id: DocIo#page_340
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:50:39Z
fidelity: lossless
-->

## Essentials: DocIO

### Overview
- **1.** Demonstrates how to insert a bookmark in a Word document using Interop.
- **2.** Explains the use of DocIO for inserting bookmarks efficiently.
- **3.** Compares Interop and DocIO methods for bookmark insertion.

### Content

```vb
[VB]

Imports word = Microsoft.Office.Interop.Word
---------------------
' Initialize objects
Dim nullobject As Object = Missing.Value
Dim newFilePath As Object = "NewFile.doc"

' Start the word application
Dim wordApp As word.Application = New word.Application()

' Create a new word document
wordApp.Documents.Add(nullobject, nullobject, nullobject, 
nullobject)
Dim doc As word.Document = wordApp.ActiveDocument

' Add a paragraph to the document
Dim oPara As word.Paragraph
oPara = doc.Content.Paragraphs.Add(nullobject)
oPara.Range.Text = "Bookmark with one word selected"

' Define the start and end positions of bookmark range
Dim startobj As Object = oPara.Range.Text.IndexOf("word")
Dim endobj As Object = oPara.Range.Text.LastIndexOf(" ")
Dim rng As Object = doc.Range(startobj, endobj)

' Add bookmark
doc.Bookmarks.Add("one_word", rng)

' Save the document
doc.SaveAs(newFilePath)

' Close the document
doc.Close(nullobject, nullobject, nullobject)

' Quit application
wordApp.Quit()
```

#### Using DocIO

The following code example shows how to insert the bookmark using DocIO. Here, the `AppendBookmarkStart()` and `AppendBookmarkEnd()` methods are used to add the bookmark.

### API Reference
- **Namespace:** `Syncfusion.DocIO`
- **Class:** `WordDocument`
  - **Methods:**
    - `AppendBookmarkStart(name As String)`
    - `AppendBookmarkEnd()`
  - **Properties:**
    - `Bookmarks`

### Code Examples

#### Example: Using DocIO to Insert a Bookmark

```vb
Imports Syncfusion.DocIO

' Create a new Word document
Dim wordDocument As New WordDocument()

' Add a paragraph and set the content
Dim builder As WordDocumentBuilder = wordDocument.AddSection().AddParagraph()
builder.Write("Bookmark with one word selected.")

' Define the start and end positions of the bookmark
Dim startIndex As Integer = builder.Document.LastParagraph.GetText().IndexOf("word")
Dim endIndex As Integer = builder.Document.LastParagraph.GetText().IndexOf(" ")

' Insert the bookmark
builder.BookmarkStart("one_word")
builder.WriteWord("word")
builder.BookmarkEnd("one_word")

' Save the document
wordDocument.Save("DocIOBookmark.docx", SaveFormat.Docx)
```

#### Example: Using Interop to Insert a Bookmark

**Refer to the VB code block above for Interop implementation.**

### See also:
- DocIO Documentation
- Word Manipulation

<!-- tags: [DocIO, WordDocument, Bookmark, Interop, DocIO_API, Winforms] keywords: [BookmarkInsertion, WordManipulation, DocIO_API] -->
```