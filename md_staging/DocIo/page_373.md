```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_373.jpeg
document_name: DocIo
page_number: 373
page_id: DocIo#page_373
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:52:54Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Example using C# to manipulate Word documents and remove all comments.
- Integration with Microsoft Office Interop.Word to automate document processing.

## Content

### Example Code

[C#]

```csharp
using word = Microsoft.Office.Interop.Word;

// Initialize objects
object nullobject = System.Reflection.Missing.Value;
object filepath = "Comments.doc";
object newFilePath = "CommentsRemovedOffice.doc";

// Start the word application
word.Application wordApp = new word.Application();

// Open the word document
word.Document document = wordApp.Documents.Open(ref filepath, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject);

wordApp.Visible = false;

// Delete all comments
document.DeleteAllComments();

// Save the document
document.SaveAs(ref newFilePath, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject);

// Close the document
document.Close(ref nullobject, ref nullobject, ref nullobject);
```

---

## RAG Annotations
<!-- tags: [DocIO, Microsoft Office Interop, Word documents, comments, C#, Syncfusion Winforms] keywords: [documents, comments, Word, automation, C#, Microsoft Office, Interop, delete, save, close] -->
```