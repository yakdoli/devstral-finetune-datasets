<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_330.jpeg
document_name: DocIo
page_number: 330
page_id: DocIo#page_330
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:48:58Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Demonstrates how to perform a mail merge in C# using the Microsoft Word Interop library.
- Utilizes a sample database (`Northwind.mdb`) and an SQL query to fetch data for merging into a Word document.
- Provides an example of handling mail merge in a non-interactive mode for batch processing.

## Content

### Mail Merge using C#

Below is a C# example demonstrating how to perform a mail merge in a Word document using the Microsoft Word Interop library. This example includes initializing objects, opening a document, performing mail merge, and saving the merged output to a new document.

```csharp
using word = Microsoft.Office.Interop.Word;

// Initialize objects
object nullobject = Missing.Value;
object filepath = "EmployeesReportDemo.doc";
object sqlStmt = "SELECT * FROM [Employees]";
string sDBPath = "Northwind.mdb";

// Start the word application
word.Application wordApp = new word.Application();

// Open the word document
word.Document document = wordApp.Documents.Open(ref filepath, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject);

wordApp.Visible = false;

// Perform Mail Merge
document.MailMerge.OpenDataSource(sDBPath, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref nullobject, ref sqlStmt, ref nullobject, ref nullobject, ref nullobject);

document.MailMerge.Execute(ref nullobject);

// Send output of Mail Merge to a new document
document.MailMerge.Destination = word.WdMailMergeDestination.wdSendToNewDocument;

// Close the document
document.Close(ref nullobject, ref nullobject, ref nullobject);

// Quit the application
wordApp.Quit(ref nullobject, ref nullobject, ref nullobject);
```

### Explanation
- **Initialization:** The `Microsoft.Office.Interop.Word` namespace is used to interact with Microsoft Word.
- **Objects:** `nullobject` is used to handle missing parameters required by the Word Interop methods. `filepath` specifies the Word document to be opened, `sqlStmt` is the SQL query to fetch data, and `sDBPath` is the path to the database.
- **Opening the Document:** The `Documents.Open` method is used to open the Word document with the specified file path. The `nullobject` placeholder is used for parameters that are not required.
- **Mail Merge:** The `MailMerge.OpenDataSource` method establishes a connection to the database and executes the SQL query to fetch data. The `MailMerge.Execute` method performs the actual mail merge.
- **Destination:** The `MailMerge.Destination` property is set to `wdSendToNewDocument` to ensure the merged output is saved to a new document.
- **Closing and Quitting:** The document is closed, and the Word application is quit to complete the process.

## API Reference

### Namespaces
- `Microsoft.Office.Interop.Word`

### Classes
- `Application`
- `Document`
- `MailMerge`

### Methods
- `Applications.Open`: Opens a document.
- `MailMerge.OpenDataSource`: Establishes a data source for mail merge.
- `MailMerge.Execute`: Performs the mail merge operation.
- `Document.Close`: Closes the document.
- `Application.Quit`: Quits the Word application.

### Properties
- `MailMerge.Destination`: Specifies the destination for the mail merge output.

## Code Examples

The provided C# example demonstrates a complete mail merge workflow, including opening a document, performing mail merge, and handling output to a new document.

## Cross References

- Refer to the Microsoft Office Interop documentation for detailed information on the Word Interop API.
- For more examples of mail merge in different programming environments, consult the Syncfusion WinForms documentation.

<!-- tags: [docio, mailmerge, csharp, wordinterop, syncfusionwinforms] keywords: [office, interop, document, database, sql, merge, application] -->