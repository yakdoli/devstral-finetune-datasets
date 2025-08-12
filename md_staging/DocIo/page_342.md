```html
<!-- source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_342.jpeg
document_name: DocIo
page_number: 342
page_id: DocIo#page_342
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:49:54Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- **DocIO** allows working with book-marks.
- **Page numbers** can be inserted in word documents.

## Content

### Note

For more information on working with **bookmarks using DocIO**, you can refer to the following online documentation link:  
<http://help.syncfusion.com/Ug_101/Reporting/DocIO/Windows%20Forms/default.htm#!documents/4413bookmark.htm>

### 5.12.4 Page numbers

**Page numbers** can be inserted to a word document in the header/footer section.

#### Using MS Office Interop

In the following code example, the page numbers are inserted to the footer of the word document by adding a page number field.

```csharp
using word = Microsoft.Office.Interop.Word;

// Initialize objects
object filepath = "NewFile.doc";
object nullobject = Missing.Value;

// Start the word application
word.Application wordApp = new word.Application();

// Open the word document
word.Document document = wordApp.Documents.Open(ref filepath, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject);

wordApp.Visible = false;
document.Activate();

// Seek the page footer
wordApp.ActiveWindow.ActivePane.View.SeekView = word.WdSeekView.wdSeekCurrentPageFooter;
```

## API Reference

Namespace: Microsoft.Office.Interop.Word

- **Application:** Represents an instance of the application.
- **Document:** Represents a single document.

## Code Examples

The provided C# code demonstrates how to use **MS Office Interop** to insert page numbers into the footer of a Word document. This is achieved by activating the document, seeking the footer, and inserting a page number field.

## Cross References

For additional details on **working with bookmarks using DocIO**, refer to the documentation link provided.

## RAG Annotations

The following tags and keywords are derived from the visible content:

```html
<!-- tags: [DocIO, VS.NET, word, page numbers, Interop, namespace, class, members, version: 11.4.0] keywords: [bookmarks, page number field, header/footer section, Microsoft.Office.Interop.Word, document, wordApp, footer, seekview] -->
```
```