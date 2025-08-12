```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_358.jpeg
document_name: DocIo
page_number: 358
page_id: DocIo#page_358
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:50:58Z
fidelity: lossless
-->

## Overview
- Demonstrates how to open a Word document, add headers and footers to each section, and save the modified document using the DocIO library.
- Implements a VB.NET code snippet to achieve the above functionality.

## Content

```vb
' Open the word document
Dim doc As WordDocument = New WordDocument("original.doc")
' Add header and footer for each section in the document
For Each sec As WSection In doc.Sections
    ' Header
    Dim para As WParagraph = New WParagraph(doc)
    para.AppendField("page", FieldType.FieldPage)
    para.ParagraphFormat.HorizontalAlignment = HorizontalAlignment.Right
    sec.HeadersFooters.Header.Paragraphs.Add(para)
    ' Footer
    Dim paral As WParagraph = New WParagraph(doc)
    paral.AppendText("Internal")
    paral.ParagraphFormat.HorizontalAlignment = HorizontalAlignment.Left
    sec.HeadersFooters.Footer.Paragraphs.Add(paral)
Next
' Save the document
doc.Save("HeaderFooterDocIO.doc", FormatType.Doc)
' Close the document
doc.Close()
```

### Note:
For more information on inserting Headers and Footers to a word document using DocIO, refer the online documentation link below:
[http://help.syncfusion.com/Ug_101/Reporting/DocIO/Windows%20Forms/default.htm#!/documents/432headersandfooters.htm](http://help.syncfusion.com/Ug_101/Reporting/DocIO/Windows%20Forms/default.htm#!/documents/432headersandfooters.htm)

## References
- [Syncfusion DocIO Documentation]()

## Tags and Keywords
<!-- tags: DocIO, WordDocument, Headers, Footers, VB.NET, Word Processing, Syncfusion -> keywords: dociio, headers, footers, vb.net, document manipulation, word, syncfusion -->
```
