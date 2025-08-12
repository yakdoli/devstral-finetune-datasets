```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_364.jpeg
document_name: DocIo
page_number: 364
page_id: DocIo#page_364
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:52:08Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Example demonstrating how to create and manipulate a Word document using the Microsoft Word Object Library in C#.
- Focuses on initializing the Word application, creating a new document, inserting a table, saving the document, and closing the application.

## Content

### Creating and Manipulating a Word Document

The following C# code snippet illustrates how to automate the creation of a Word document with a table using the Microsoft Word Object Library.

```csharp
using word = Microsoft.Office.Interop.Word;
--------
// Initialize objects
object nullobject = System.Reflection.Missing.Value;
object newFilePath = "TableOffice.doc";

// Start the word application
word.Application wordApp = new word.Application();

// Create a new document
wordApp.Documents.Add(ref nullobject, ref nullobject, ref nullobject, ref nullobject);
word.Document doc = wordApp.ActiveDocument;

// Insert table
object start = 0;
object end = 0;
word.Range tableLocation = doc.Range(ref start, ref end);
doc.Tables.Add(tableLocation, 3, 2, ref nullobject, ref nullobject);

// Save the document
doc.SaveAs(ref newFilePath, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject);

// Close the document
document.Close(ref nullobject, ref nullobject, ref nullobject);

// Quit the application
wordApp.Quit(ref nullobject, ref nullobject, ref nullobject);
```

### Explanation

1. **Initialization**:
   - The `Microsoft.Office.Interop.Word` namespace is used to access the Word object model.
   - Variables are initialized for optional parameters using `System.Reflection.Missing.Value`.

2. **Starting the Word Application**:
   - A new instance of the Word application is created.

3. **Creating a New Document**:
   - A new document is added to the application with default parameters.

4. **Inserting a Table**:
   - A `Range` object is used to specify the location where the table will be inserted.
   - A 3x2 table is added to the document using the `Add` method.

5. **Saving the Document**:
   - The document is saved with a specified file path using the `SaveAs` method. All optional parameters are passed as `nullobject` to maintain default behavior.

6. **Closing the Document**:
   - The document is closed using the `Close` method.

7. **Quitting the Application**:
   - The Word application is quit using the `Quit` method, ensuring cleanup.

## API Reference

### Namespace: Microsoft.Office.Interop.Word

#### Methods
- `Application()`: Creates a new instance of the Word application.
- `Documents.Add()`: Adds a new document to the application.
- `ActiveDocument`: Property to get the active document.
- `Range()`: Creates a range object representing a specific location in the document.
- `Tables.Add()`: Adds a table to the specified range in the document.
- `SaveAs()`: Saves the document with the specified file path and optional parameters.
- `Close()`: Closes the document.
- `Quit()`: Quits the Word application.

## Code Examples

### Example: Creating and Saving a Word Document with a Table

The provided C# code demonstrates the entire process of creating a new Word document, inserting a table, saving the document, closing it, and quitting the application.

## Cross References

See also:
- Documentation for the Microsoft Word Object Library.
- Additional Syncfusion Winforms resources for working with DOCX files.

<!-- tags: [DocIo, Syncfusion Winforms, C#, Word Object Model] keywords: [Word Document, Table, Interop, SaveAs, Close, Quit, C# Example] -->
```