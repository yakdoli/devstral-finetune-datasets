```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_167.jpeg
document_name: DocIo
page_number: 167
page_id: DocIo#page_167
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:38:24Z
fidelity: lossless
-->

# `Essential DocIO`

## Overview
- Demonstrates how to insert bookmarks in a Word document using programmatic approaches.
- Covers examples in both C# and VB.NET for creating bookmarks and handling overlapping bookmarks.
- Offers code snippets to illustrate the usage of bookmarks in document sections.

## Content

### Inserting Bookmarks in a Word Document

#### C#

```csharp
paragraph.AppendText("is inside ");
paragraph.AppendBookmarkEnd("smaller_bookmark");
paragraph.AppendText("of the bigger bookmark");
paragraph.AppendBookmarkEnd("bigger_bookmark");

paragraph = section.AddParagraph();
paragraph.AppendBookmarkStart("multi_paragraph");
paragraph.AppendText("Bookmark starts here and ends in the next paragraph");

paragraph = section.AddParagraph();
paragraph.AppendText("This ");
paragraph.AppendBookmarkStart("overlapped bookmark");
paragraph.AppendText("bookmark over");
paragraph.AppendBookmarkEnd("multi_paragraph");
paragraph.AppendText("laps ");
paragraph.AppendBookmarkEnd("overlapped bookmark");
paragraph.AppendText("with previous one");

doc.Save("Bookmarks.doc");
```

#### VB.NET

```vb
Dim doc As IWordDocument = New WordDocument()
Dim section As ISection = doc.AddSection()
Dim paragraph As IParagraph = section.AddParagraph()
paragraph.AppendText("Book with one ")
paragraph.AppendBookmarkStart("one_word")
paragraph.AppendText("word")
paragraph.AppendBookmarkEnd("one_word")
paragraph.AppendText(" selected")

section.AddParagraph()
paragraph = section.AddParagraph()
paragraph.AppendBookmarkStart("beginning_paragraph")
paragraph.AppendText("Beginning of the paragraph selected")

section.AddParagraph()
paragraph = section.AddParagraph()
paragraph.AppendBookmarkStart("bigger_bookmark")
paragraph.AppendText("Smaller bookmark ")
paragraph.AppendBookmarkStart("smaller_bookmark")
paragraph.AppendText("is inside ")
paragraph.AppendBookmarkEnd("smaller_bookmark")
paragraph.AppendText("of the bigger bookmark")
paragraph.AppendBookmarkEnd("bigger_bookmark")
```

---

## API Reference
- **Namespace**: `Syncfusion.DocIO` or relevant namespace used in `DocIO`.
- **Class**: `WordDocument`, `Section`, `Paragraph`, etc.
- **Methods**:
  - `AppendText(string)`: Inserts text into the paragraph.
  - `AppendBookmarkStart(string)`: Marks the start of a bookmark in the paragraph.
  - `AppendBookmarkEnd(string)`: Marks the end of a bookmark in the paragraph.
  - `AddSection()`: Adds a new section to the document.
  - `AddParagraph()`: Adds a new paragraph to the section.
  - `Save(string)`: Saves the document to a file.

## Code Examples

### C# Example: Creating Bookmarks in a Section

```csharp
section.AddParagraph();
paragraph.AppendBookmarkStart("beginning_paragraph");
paragraph.AppendText("Beginning of the paragraph selected");

section.AddParagraph();
paragraph = section.AddParagraph();
paragraph.AppendBookmarkStart("bigger_bookmark");
paragraph.AppendText("Smaller bookmark ");
paragraph.AppendBookmarkStart("smaller_bookmark");
paragraph.AppendText("is inside ");
paragraph.AppendBookmarkEnd("smaller_bookmark");
paragraph.AppendText("of the bigger bookmark");
paragraph.AppendBookmarkEnd("bigger_bookmark");
```

### VB.NET Example: Adding a Single Word Bookmark

```vb
Dim paragraph As IParagraph = section.AddParagraph()
paragraph.AppendText("Book with one ")
paragraph.AppendBookmarkStart("one_word")
paragraph.AppendText("word")
paragraph.AppendBookmarkEnd("one_word")
paragraph.AppendText(" selected")
```

---

## Cross References
- Refer to the section on "Managing Document Sections" for more information on adding sections programmatically.

---

<!-- tags: [syncfusion-docio, word-document, bookmarks, csharp, vb.net, document-sections] keywords: [bookmarks, docio, word document, programmatic insertions, overlapping bookmarks, syncfusion] -->
```