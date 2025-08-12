```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_336.jpeg
document_name: DocIo
page_number: 336
page_id: DocIo#page_336
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:50:21Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- This page displays a VB code snippet that demonstrates how to use the `Microsoft.Office.Interop.Word` library to perform a "Find and Replace" operation in a Word document.
- The script opens a template document, replaces occurrences of a specific text phrase, saves the updated document, and closes it programmatically.

## Content

### Using Word Interop in VB

```vb
Imports word = Microsoft.Office.Interop.Word

' Initialize objects
Dim nullobject As Object = Missing.Value
Dim filePath As Object = "FindAndReplaceTemplate.doc"
Dim newFilePath As Object = "FindAndReplace.doc"
Dim item As Object = word.WdGotoItem.wdGotoPage
Dim whichItem As Object = word.WdGotoDirection.wdGotoFirst
Dim replaceAll As Object = word.WdReplace.wdReplaceAll
Dim forward As Object = True
Dim matchAllWord As Object = True
Dim matchCase As Object = False
Dim originalText As Object = "Hello"
Dim replaceText As Object = "World"
Dim save As Object = True
Dim falseObj As Object = False

' Start the word application
Dim wordApp As word.Application = New word.Application()

' Open the word document
Dim doc As word.Document = wordApp.Documents.Open(filePath, _
    nullobject, nullobject, nullobject, nullobject, nullobject, _
    nullobject, nullobject, nullobject, nullobject, nullobject, _
    nullobject, falseObj, nullobject, nullobject, nullobject)

wordApp.Visible = False

' Search for text and replace
doc.GoTo(item, whichItem, nullobject, nullobject)

For Each rng As word.Range In doc.StoryRanges
    rng.Find.Execute(originalText, matchCase, matchAllWord, _
    nullobject, nullobject, nullobject, forward, nullobject, _
    nullobject, replaceText, replaceAll, nullobject, nullobject, _
    nullobject, nullobject)
Next

' Save the document
doc.SaveAs(newFilePath, nullobject, nullobject, nullobject, _
    nullobject, nullobject, nullobject, nullobject, nullobject, _
    nullobject, nullobject, nullobject, nullobject, nullobject)

' Close the document
doc.Close(nullobject, nullobject, nullobject)

' Quit the application
wordApp.Quit(nullobject, nullobject, nullobject)
```

## Cross References
- This page provides an example that can be integrated into an automation or document processing task using Syncfusion libraries for WinForms applications.

<!-- tags: Word Interop, DocIO, Find and Replace, Microsoft Office Interop Word, VB.NET keywords: Microsoft.Office.Interop.Word, Find and Replace, Word, Template Document -->
```