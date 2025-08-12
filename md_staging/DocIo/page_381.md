```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_381.jpeg
document_name: DocIo
page_number: 381
page_id: DocIo#page_381
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:53:25Z
fidelity: lossless
-->

## [C#]

```csharp
using word = Microsoft.Office.Interop.Word;
---------

// Initialize objects
object nullobject = System.Reflection.Missing.Value;
object filepath = "TOCDocument.doc";
object newFilePath = "TOCUpdatedOffice.doc";
object trueobj = true;

// Start the word application
word.Application wordApp = new word.Application();

// Open the word document
word.Document document = wordApp.Documents.Open(ref filepath, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject);

wordApp.Visible = false;

// Define range for TOC in document
object tocstart = 0;
object toend = 0;
word.Range rngToc = document.Range(ref tocstart, ref toend);

// Add TOC
word.TableOfContents toc = document.TablesOfContents.Add(rngToc, ref trueobj, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref trueobj, ref trueobj, ref trueobj, ref trueobj);

// Update TOC
toc.Update();

// Save the document
document.SaveAs(ref newFilePath, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject);

// Close the document
document.Close(ref nullobject, ref nullobject, ref nullobject);

// Quit the application
wordApp.Quit(ref nullobject, ref nullobject, ref nullobject);
```

<!-- tags: [DocIo, EssentialDocIo, WordInterop, TableOfContents, C#] keywords: [TOC, document, range, update, save, close, quit, application, document, tablesOfContents, add, trueobj, nullobject, visible, falses] -->
```