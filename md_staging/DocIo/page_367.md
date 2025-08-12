```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_367.jpeg
document_name: DocIo
page_number: 367
page_id: DocIo#page_367
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:51:39Z
fidelity: lossless
-->

## Essential DocIO

### Code Example Creating a Table using DocIO

```vb
' Create a new word document
Dim doc As IWordDocument = New WordDocument()

Dim section As ISection = doc.AddSection()

' Add a table to the document
Dim table As ITable = section.AddTable()

table.ResetCells(3, 2)

' Save the document
doc.Save("TableDocIO.doc")
```

#### Note:
For more information on creating tables using DocIO, refer to the following online documentation link:
[http://help.syncfusion.com/Ug_101/Reporting/DocIO/Windows%20Forms/default.htm#documents/433table.htm](http://help.syncfusion.com/Ug_101/Reporting/DocIO/Windows%20Forms/default.htm#documents/433table.htm)

### 5.12.9 Comments

Comments are used to include some additional information to a paragraph or text in a word document. Comments can be added and modified whenever needed and deleted when the comment has served its purpose. The comments are very useful when a document is reviewed. You can insert or delete the comments using DocIO and Office Automation.

#### Adding Comments Using MS Office Interop

The following code examples illustrate how to add comments to a word document. You need to define the range of text to which the comment is to be added.

#### Copyright Information
© 2013 Syncfusion. All rights reserved.
```

```html
<!-- tags: [DocIO, comments, tables, WinForms, interoperability, Syncfusion] keywords: [create tables, comment management, docio, word document, vb code, office automation, document manipulation, advanced document features] -->
```