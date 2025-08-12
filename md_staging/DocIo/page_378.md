```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_378.jpeg
document_name: DocIo
page_number: 378
page_id: DocIo#page_378
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:52:09Z
fidelity: lossless
-->
# Essential DocIO

## Overview
- Demonstrates how to protect a Word document to allow only comments using Visual Basic (VB).
- Utilizes the Microsoft.Office.Interop.Word library for Word document manipulation.
- Steps include initializing objects, starting the Word application, opening a document, setting protection, and saving the modified document.

## Content

### Protecting a Document to Allow Only Comments

The following VB code snippet illustrates how to protect a Word document to allow only comments. The example saves the modified document under a new file path.

```vb
Imports word = Microsoft.Office.Interop.Word

' Initialize objects
Dim nullobject As Object = System.Reflection.Missing.Value
Dim filepath As Object = "Document.doc"
Dim newFilePath As Object = "FileProtectionOffice.doc"
Dim noReset As Object = False
Dim password As Object = System.String.Empty
Dim useIRM As Object = False
Dim enforceStyleLock As Object = False

' Start the word application
Dim wordApp As word.Application = New word.Application()

' Open the word document that is to be protected
Dim doc As word.Document = wordApp.Documents.Open(filepath, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject)

wordApp.Visible = False

' Set "Allow only Comments" protection to word document
doc.Protect(word.WdProtectionType.wdAllowOnlyComments, noReset, password, useIRM, enforceStyleLock)

' Save the document
doc.SaveAs(newFilePath, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject)
```

### Explanation of Code

1. **Imports Statement**: Imports the `Microsoft.Office.Interop.Word` library to enable interaction with Word documents.
   
2. **Initializing Objects**:
   - `nullobject`: Represents `System.Reflection.Missing.Value` for optional parameters.
   - `filepath`: Specifies the path to the source document.
   - `newFilePath`: Specifies the path for the modified document to be saved.
   - `noReset`, `password`, `useIRM`, and `enforceStyleLock`: Parameters used in the `Protect` method to manage document protection settings.

3. **Starting the Word Application**: Creates a new instance of the Word Application.

4. **Opening the Document**: Uses the `Open` method to load the source document into the Word application.

5. **Setting Document Protection**:
   - The `Protect` method is called on the document object with the `WdProtectionType.wdAllowOnlyComments` parameter to restrict editing, allowing only comments.
   - Other parameters ensure that settings are not reset and do not enforce IRM or style locks.

6. **Saving the Document**: The document is saved with the new protection settings under the specified `newFilePath`.

<!-- tags: Essential DocIO, Microsoft.Office.Interop.Word, Document Protection, VB, Office Interop, iPad, DO NOT DELETE -->
```