```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_339.jpeg
document_name: DocIo
page_number: 339
page_id: DocIo#page_339
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:49:45Z
fidelity: lossless
-->

# Essential DocIO

[C#]

```csharp
using word = Microsoft.Office.Interop.Word;
---------
// Initialize objects
object nullobject = Missing.Value;
object newFilePath = "NewFile.doc";

// Start the word application
word.Application wordApp = new word.Application();

// Create a new word document
wordApp.Documents.Add(ref nullobject, ref nullobject, ref nullobject, ref nullobject);
word.Document doc = wordApp.ActiveDocument;

// Add a paragraph to the document
word.Paragraph oParal;
oParal = doc.Content.Paragraphs.Add(ref nullobject);
oParal.Range.Text = "Bookmark with one word selected";

// Define start and end positions of bookmark range
object start = oParal.Range.Text.IndexOf("word");
object end = oParal.Range.Text.LastIndexOf(" ");
object rng = doc.Range(ref start, ref end);

// Add bookmark
doc.Bookmarks.Add("one_word", ref rng);

// Save the document and quit the application
doc.SaveAs(ref newFilePath, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject);

// Close the document
document.Close(ref nullobject, ref nullobject, ref nullobject);

// Quit the application
wordApp.Quit(ref nullobject, ref nullobject, ref nullobject);
```

## API Reference
- **Namespace:** Microsoft.Office.Interop.Word
  - **Class:** Application
    - **Method:** Add()
    - **Method:** ActiveDocument()
    - **Method:** Content()
    - **Method:** Paragraphs()
    - **Method:** SaveAs()
    - **Method:** Quit()

## Code Examples
The example demonstrates how to:
1. Start a Word application.
2. Create a new document.
3. Add a paragraph with text.
4. Identify the "word" in the paragraph and define a range around it.
5. Create a bookmark using the defined range.
6. Save the document with the created bookmark.
7. Close the document and quit the application.

<!-- tags: [DocIO, Microsoft.Office.Interop.Word, Word Document Manipulation, Bookmark, Syncfusion SDK] keywords: [word application, document creation, paragraph addition, bookmark creation, text selection, range definition, document saving, document closing, application quitting] -->
```