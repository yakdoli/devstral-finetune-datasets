```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_368.jpeg
document_name: DocIo
page_number: 368
page_id: DocIo#page_368
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:52:32Z
fidelity: lossless
-->

## Essential DocIO

```csharp
[C#]

using word = Microsoft.Office.Interop.Word;
--------

// Initialize objects
object nullobject = System.Reflection.Missing.Value;
object newFilePath = "CommentOffice.doc";

// Start the word application
word.Application wordApp = new word.Application();

// Create a new document
wordApp.Documents.Add(ref nullobject, ref nullobject, ref nullobject, ref nullobject);
word.Document doc = wordApp.ActiveDocument;

// Insert text to the word document
object start = 0;
object end = 0;
word.Range rng = doc.Range(ref start, ref end);
rng.Text = "New Text";

// Add comment to the inserted text
object text = "Comment goes here";
doc.Comments.Add(rng, ref text);

// Save the document
doc.SaveAs(ref newFilePath, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject);
```

<!-- tags: [DocIO, Word document, comments, text insertion, Microsoft.Office.Interop.Word] keywords: [Interop Word, SaveAs, Comments, Add, ActiveDocument, Range, newFilePath, nullobject] -->
```