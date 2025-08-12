```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_382.jpeg
document_name: DocIo
page_number: 382
page_id: DocIo#page_382
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:52:28Z
fidelity: lossless
-->

# Essential DocIO

## Overview
- Demonstrates how to add and update a Table of Contents (TOC) in a Word document using VB.NET
- Utilizes the `Microsoft.Office.Interop.Word` library for interacting with Word documents
- Includes handling for document initialization, TOC range definition, and document saving

## Content

### Adding and Updating TOC in Word Documents

```vb
Imports word = Microsoft.Office.Interop.Word
' -------------------------

' Initialize objects
Dim nullobject As Object = System.Reflection.Missing.Value
Dim filepath As Object = "TOCDocument.doc"
Dim newFilePath As Object = "TOCUpdatedOffice.doc"
Dim trueobj As Object = True

' Start the application
Dim wordApp As word.Application = New word.Application()

' Open the document
Dim document As word.Document = wordApp.Documents.Open(filepath, _
                                                       nullobject, nullobject, nullobject, nullobject, _
                                                       nullobject, nullobject, nullobject, nullobject, _
                                                       nullobject, nullobject, nullobject, nullobject, _
                                                       nullobject, nullobject, nullobject)

wordApp.Visible = False

' Define range for TOC in document
Dim tocstart As Object = 0
Dim togend As Object = 0
Dim rngToc As word.Range = document.Range(tocstart, togend)

' Add TOC
Dim TOC As word.TableOfContents = _
    document.TablesOfContents.Add(rngToc, trueobj, nullobject, _
                                  nullobject, nullobject, trueobj, _
                                  trueobj, trueobj, trueobj)

' Update TOC
TOC.Update()

' Save the document
document.SaveAs(newFilePath, nullobject, nullobject, nullobject, _
                nullobject, nullobject, nullobject, nullobject, _
                nullobject, nullobject, nullobject, nullobject, _
                nullobject, nullobject)

' Close the document
doc.Close(nullobject, nullobject, nullobject)

' Quit the application
wordApp.Quit()
```

## Cross References
- For more details on `Microsoft.Office.Interop.Word`, refer to the official Microsoft documentation.
- Refer to Syncfusion’s documentation for further usage examples and best practices.

<!-- tags: [syncfusion, winforms, essentialdocio, wordprocessing, toc, tableofcontents, vb.net, microsoftofficeinteropword] keywords: [table of contents, toc, document processing, word document, vb.net, code example, synchronization] -->
```