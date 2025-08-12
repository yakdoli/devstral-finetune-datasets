```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_344.jpeg
document_name: DocIo
page_number: 344
page_id: DocIo#page_344
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:50:57Z
fidelity: lossless
-->

## Overview
- This page explains how to integrate the DoclO plugin to add functionality, such as adding a page number in the footer, using the VB language.
- The steps include starting the application, adding a new document, accessing the page footer, formatting the footer, adding page numbers, saving the document, closing the document, and quitting the application.

## Content

### Using DoclO

```vb
Imports word = Microsoft.Office.Interop.Word

' Initialize objects
Dim nullobject As Object = Missing.Value
Dim filePath As Object = "NewFile.doc"
Dim falseobj As Object = False

' Start the application
Dim wordApp As word.Application = New word.Application()

' Add a new word document
Dim document As word.Document = wordApp.Documents.Open(filePath, _
    nullobject, nullobject, nullobject, nullobject, nullobject, _
    nullobject, nullobject, falseobj, nullobject, nullobject, nullobject)
wordApp.Visible = False
document.Activate()

' Seek the page footer
wordApp.ActiveWindow.ActivePane.View.SeekView = _
    word.WdSeekView.wdSeekCurrentPageFooter

' Formatting for the footer
wordApp.Selection.Paragraphs.Alignment = _
    word.WdParagraphAlignment.wdAlignParagraphCenter
wordApp.ActiveWindow.Selection.Font.Name = "Arial"
wordApp.ActiveWindow.Selection.Font.Size = 8

' Add page numbers in footer
Dim CurrentPage As Object = word.WdFieldType.wdFieldPage
wordApp.ActiveWindow.Selection.Fields.Add(wordApp.Selection.Range, _
    CurrentPage, nullobject, nullobject)

' Save document
document.Save()

' Close the document
doc.Close(nullobject, nullobject, nullobject)

' Quit application
wordApp.Quit()
```

## Page-level Navigation/TOC (if applicable)
- This section details the use of the DoclO plugin in VB for managing Word documents, including steps for creation, formatting, and saving.

## Cross References
- Refer to the official documentation for additional features and parameters related toDoclO.

<!-- tags: [Syncfusion, DoclO, WinForms, VB.NET, Word Document API, Page Number Footer, Developer Guide] keywords: [DoclO, Syncfusion WinForms, VB.NET, Microsoft.Office.Interop.Word, Word Document, Footer, Page Number, Field Page, SeekView, Paragraph Alignment, Font, Save Document] -->
```