```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_341.jpeg
document_name: DocIo
page_number: 341
page_id: DocIo#page_341
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:50:52Z
fidelity: lossless
--> 

# Essential DocIO

## Overview
- Demonstrates how to create and insert bookmarks in a Word document using both C# and VB.NET.
- Highlights the `AppendBookmarkStart` and `AppendBookmarkEnd` methods for defining bookmark boundaries.
- Shows how to save the document after inserting bookmarks.

## Content

### Creating Bookmarks in a Word Document

#### C#
```csharp
// Create a new word document
WordDocument doc = new WordDocument();
IWSection section = doc.AddSection();
IWParagraph paragraph = section.AddParagraph();
paragraph.AppendText("Simple Bookmark");
paragraph = section.AddParagraph();
paragraph.AppendText("Bookmark with one ");
// Insert bookmark
paragraph.AppendBookmarkStart("one_word");
paragraph.AppendText("word");
paragraph.AppendBookmarkEnd("one_word");
paragraph.AppendText(" selected");
// Save the document
doc.Save("Bookmarks.doc");
// Close the document
doc.Close();
```

#### VB
```vb
' Create a new word document
Dim doc As WordDocument = New WordDocument()
Dim section As IWSection = doc.AddSection()
Dim paragraph As IWParagraph = section.AddParagraph()
paragraph.AppendText("Simple Bookmark")
paragraph = section.AddParagraph()
paragraph.AppendText("Bookmark with one ")
' Insert bookmark
paragraph.AppendBookmarkStart("one_word")
paragraph.AppendText("word")
paragraph.AppendBookmarkEnd("one_word")
paragraph.AppendText(" selected")
' Save the document
doc.Save("Bookmarks.doc")
' Close the document
doc.Close()
```

### Explanation
- The code snippets above demonstrate how to programmatically create a Word document and insert bookmarks within specific text segments.
- The `AppendBookmarkStart` and `AppendBookmarkEnd` methods are used to define the start and end boundaries of the bookmark.
- The document is saved as "Bookmarks.doc" and properly closed after insertion.

## API Reference

### Methods Used
- `WordDocument`: Represents a Word document object in Syncfusion.DocIO.
- `AddSection`: Creates a new section in the document.
- `AddParagraph`: Adds a new paragraph to the section.
- `AppendText`: Adds text to the paragraph.
- `AppendBookmarkStart`: Marks the start of a bookmark.
- `AppendBookmarkEnd`: Marks the end of a bookmark.
- `Save`: Saves the document to a specified file path.
- `Close`: Closes the document object after operations are complete.

## Code Examples

The provided C# and VB.NET code examples illustrate the complete workflow of creating a Word document, inserting bookmarks, saving the document, and closing the object.

## Page-level Navigation/TOC
- This page focuses on creating bookmarks in a Word document using Syncfusion.DocIO.

## Cross References
- See also:
  - [Adding Headers and Footers](#adding-headers-and-footers-in-a-word-document)
  - [Inserting Images in a Word Document](#inserting-images-in-a-word-document)

<!-- tags: [DocIO, WordDocument, Bookmarks, C#, VB.NET, Syncfusion, version: 11.4.0.26] keywords: [bookmarks, word document, insert, save, close, append bookmark, Syncfusion DocIO, C#, VB.NET] -->
```