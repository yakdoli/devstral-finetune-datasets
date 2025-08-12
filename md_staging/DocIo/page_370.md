<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_370.jpeg
document_name: DocIo
page_number: 370
page_id: DocIo#page_370
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:51:30Z
fidelity: lossless
-->

## Overview
- Demonstrates the process of inserting text and adding a comment to it in a Word document using the Syncfusion DocIO library in VB.NET.
- Key steps: initializing objects, creating a new document, inserting text, adding a comment, and saving the document.
- Uses Microsoft Office Interop library for interacting with Word documents.

## Content

### Word Document Manipulation with Syncfusion DocIO

The following VB.NET code snippet illustrates how to create a new Word document, insert text into it, add a comment to the inserted text, and save the document using the Syncfusion DocIO library.

#### Code Example

```vb
Imports word = Microsoft.Office.Interop.Word

' Initialize objects
Dim nullobject As Object = System.Reflection.Missing.Value
Dim newFilePath As Object = GetPath("CommentOffice.doc")

' Start the word application
Dim wordApp As word.Application = New word.Application()

' Create a new document
wordApp.Documents.Add(nullobject, nullobject, nullobject, nullobject)
Dim doc As word.Document = wordApp.ActiveDocument

' Insert text to the word document
Dim startobj As Object = 0
Dim endobj As Object = 0

Dim rng As word.Range = doc.Range(startobj, endobj)
rng.Text = "New Text"

' Add comment to the inserted text
Dim text As Object = "Comment goes here"
doc.Comments.Add(rng, text)

' Save document and quit application
doc.SaveAs(newFilePath, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject)
```

### Explanation of Key Steps

1. **Initialize Objects**:
   - `nullobject` is used to represent `System.Reflection.Missing.Value` for optional parameters.
   - `newFilePath` specifies the path and name of the new Word document.

2. **Start the Word Application**:
   - A new instance of the Word application is created using `New word.Application()`.

3. **Create a New Document**:
   - A new document is added to the Word application using `wordApp.Documents.Add`.

4. **Insert Text**:
   - The `Range` object is used to specify the location for inserting text. The `startobj` and `endobj` parameters define the range where the text will be inserted.

5. **Add Comment**:
   - The `Comments.Add` method is used to add a comment to the specified range of text.

6. **Save and Quit**:
   - The document is saved with the specified path using `doc.SaveAs`. The application is then quit.

### Notes
- The `GetPath` method is assumed to be a custom function returning the file path where the new Word document will be saved.
- Ensure that Microsoft Word is properly installed and the necessary references are added to the project for the Microsoft Office Interop library.

## Page-level Navigation/TOC (if applicable)
- This section provides the main content and code example related to Word document manipulation using Syncfusion DocIO in VB.NET.

<!-- tags: [Syncfusion, WinForms, DocIO, Word Document, VB.NET] keywords: [Syncfusion DocIO, Word Document, Microsoft Office Interop, VB.NET, Comment, Text Insertion] -->