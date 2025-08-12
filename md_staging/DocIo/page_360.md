```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_360.jpeg
document_name: DocIo
page_number: 360
page_id: DocIo#page_360
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:51:45Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Demonstrates how to use the Microsoft Office Interop library to create and format a Word document programmatically.
- Utilizes the `Microsoft.Office.Interop.Word` namespace to interact with Word.
- Illustrates steps to open a new document, apply character formatting, save the document, and clean up resources.

## Content

### Basic Document Creation and Formatting
The following C# code sample demonstrates how to create a new Word document, apply character formatting to the text, save the document, and then properly clean up the resources.

```csharp
using word = Microsoft.Office.Interop.Word;

--------- 

// Initialize objects
object nullobject = System.Reflection.Missing.Value;
object newFilePath = "CharacterFormattingOffice.doc";
object falseObj = false;

// Start the word application
word.Application wordApp = new word.Application();

// Create a new word document
wordApp.Documents.Add(ref nullobject, ref nullobject, ref nullobject, ref nullobject);
word.Document doc = wordApp.ActiveDocument;

// Define range to which formatting to be applied
object start = 0;
object end = 0;
word.Range rng = doc.Range(ref start, ref end);
rng.Text = "New Text";
rng.Font.Name = "Arial";
rng.Font.Size = 14;

// Save the document
doc.SaveAs(ref newFilePath, ref nullobject, ref nullobject,
           ref nullobject, ref nullobject, ref nullobject, ref nullobject,
           ref nullobject, ref nullobject, ref nullobject, ref nullobject,
           ref nullobject);

// Close the document
document.Close(ref nullobject, ref nullobject, ref nullobject);

// Quit the application
wordApp.Quit(ref nullobject, ref nullobject, ref nullobject);
```

### Explanation of Key Steps
1. **Initialization**:  
   - `nullobject` is used to represent missing parameters where `null` is not allowed.
   - `newFilePath` specifies the path where the new Word document will be saved.
   - `falseObj` is used for boolean parameters requiring reference types.

2. **Starting the Word Application**:  
   - A new instance of the `word.Application` class is created.

3. **Creating a New Document**:  
   - The `Add` method is used to create a new Word document with default settings.

4. **Defining the Text Range**:  
   - A `Range` object is created to represent the text area where formatting will be applied.
   - The `Font` property of the `Range` object is used to set the font name to "Arial" and the font size to 14.

5. **Saving the Document**:  
   - The `SaveAs` method saves the document to the specified file path with default options for other parameters.

6. **Cleaning Up Resources**:  
   - The `Close` method is used to close the document without prompting the user.
   - The `Quit` method closes the Word application.

### Notes
- Ensure that the path specified for `newFilePath` is writable by the application.
- Always close and quit the Word application when done to release resources.

### API Reference
The code interacts with the following Word Automation APIs:
- `Microsoft.Office.Interop.Word.Application`: Represents the Word application instance.
- `Documents.Add`: Adds a new document to the application.
- `ActiveDocument`: Gets the document that is currently active.
- `Range`: Represents a contiguous portion of a document.
- `Font`: Represents the character formatting properties of the text.

### Code Examples
The provided C# code demonstrates a complete example of automating Word to create and format a document. It ensures proper resource management by closing the document and quitting the application after completion.

<!-- tags: [DocIo, Microsoft Office Interop, Word Document, Character Formatting, Programmatically, Syncfusion Winforms, Version: 11.4.0.26] keywords: [Microsoft.Office.Interop.Word, ActiveDocument, Range, Font, SaveAs, Close, Quit] -->
```