```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_365.jpeg
document_name: DocIo
page_number: 365
page_id: DocIo#page_365
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:52:24Z
fidelity: lossless
-->

# [VB]

```vb
Imports word = Microsoft.Office.Interop.Word

' Initialize objects
Dim null0bject As Object = System.Reflection.Missing.Value
Dim newFilePath As Object = "Table0ffice.doc"

' Start the word application
Dim wordApp As word.Application = New word.Application()

' Create a new document
wordApp.Documents.Add(null0bject, null0bject, null0bject, null0bject)
Dim doc As word.Document = wordApp.ActiveDocument

' Insert table
Dim start As Object = 0
Dim endobj As Object = 0
Dim tableLocation As word.Range = doc.Range(start, endobj)
doc.Tables.Add(tableLocation, 3, 2, null0bject, null0bject)

' Save the document
doc.SaveAs(newFilePath, null0bject, null0bject, null0bject, null0bject, null0bject, null0bject, null0bject, null0bject, null0bject, null0bject, null0bject, null0bject)

' Close the document
doc.Close(null0bject, null0bject, null0bject)

' Quit the application
wordApp.Quit()
```

## API Reference (if applicable)
The code snippet above demonstrates the use of the following APIs:

- **Microsoft.Office.Interop.Word**: This namespace provides the necessary classes and methods to interact with Microsoft Word documents programmatically.
- **System.Reflection.Missing.Value**: Used to specify missing parameters when interacting with COM objects.
- **word.Application**: Represents the Microsoft Word application.
- **word.Documents.Add**: Creates a new Word document.
- **word.Range.InsertTable**: Inserts a table into the document at the specified range.
- **doc.SaveAs**: Saves the document to a specified file path.
- **doc.Close**: Closes the active document.
- **wordApp.Quit**: Quits the Word application.

## Code Examples (multi-language supported)
The provided code example demonstrates how to:
- Initialize the Word application.
- Create a new document.
- Insert a table with specified rows and columns.
- Save the document to a specified file path.
- Close the document.
- Quit the Word application.

## Cross References
See also:
- The official Microsoft documentation for `Microsoft.Office.Interop.Word`.
- Additional examples on interacting with Word documents in VB.NET.

<!-- tags: [DocIo, Microsoft.Office.Interop.Word, VB.NET, Interop, Table, Microsoft Word] keywords: [Microsoft.Office.Interop.Word, VB.NET, Word document, Table insertion, Document creation, Document save, Word application, Interop API] -->
```