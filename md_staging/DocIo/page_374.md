```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_374.jpeg
document_name: DocIo
page_number: 374
page_id: DocIo#page_374
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:51:51Z
fidelity: lossless
-->

### Removing Comments Using DocIO

The `CommentsCollection` property holds all the comments present in the word document. The `Clear()` method can be called to remove all the comments. The following code examples illustrate how to remove the comments from the word document using DocIO.

```vb
Imports word = Microsoft.Office.Interop.Word
---------
' Initialize objects
Dim nullObject As Object = System.Reflection.Missing.Value
Dim filePath As Object = "Comments.doc"
Dim newFilePath As Object = "CommentsRemovedOffice.doc"

' Start the word application
Dim wordApp As word.Application = New word.Application()

' Open the word document
Dim document As word.Document = wordApp.Documents.Open(filePath, nullObject, nullObject, nullObject, nullObject, nullObject, _
                                                      nullObject, nullObject, nullObject, nullObject, nullObject, nullObject, _
                                                      nullObject, nullObject, nullObject, nullObject)
wordApp.Visible = False

' Delete all comments
document.DeleteAllComments()

' Save the document
document.SaveAs(newFilePath, nullObject, nullObject, nullObject, nullObject, nullObject, nullObject, nullObject, _
               nullObject, nullObject, nullObject, nullObject, nullObject, nullObject)

' Close the document
doc.Close(nullObject, nullObject, nullObject)

' Quit the application
wordApp.Quit()
```

## Getting Started

### Overview

- The `DocIO` component is a powerful library for working with Word documents in applications.
- It provides features like creating, editing, formatting, and converting Word documents.
- The code examples demonstrate how to perform operations such as removing comments from a Word document.

### Implementation Details

```vb
' Example usage of DocIO to remove comments

' Load the document
Dim document As New WordDocument("document.docx")

' Access and clear the comments collection
Dim comments As CommentCollection = document.Comments
comments.Clear()

' Save the modified document
document.Save("document_without_comments.docx", FormatType.Docx)
```

## API Reference

### Methods

- **DeleteAllComments()**: Removes all comments from the document.

### Properties

- **CommentsCollection**: Gets all the comments present in the Word document.

## Code Examples

### Using DocIO to Remove Comments

```vb
' Open a Word document
Dim document As New WordDocument("example.docx")

' Access and clear comments
Dim comments As CommentCollection = document.Comments
comments.Clear()

' Save the modified document
document.Save("example_without_comments.docx", FormatType.Docx)
```

## Cross References

- **DocIO Documentation**: For more information on using DocIO, refer to the official documentation.
- **Syncfusion WinForms Documentation**: For an overview of Syncfusion's WinForms components.

### Getting Started with DocIO

- Begin by downloading and installing the necessary libraries.
- Initialize the `DocIO` component and load the document for manipulation.

<!-- tags: [DocIO, Word, Comments, Removal, WinForms, Syncfusion, DocIO API, WordDocument, CommentCollection] keywords: [DocIO, Word, comments, Word document, CommentCollection, DeleteAllComments, Create, Edit, Format, Convert, Remove] -->
```