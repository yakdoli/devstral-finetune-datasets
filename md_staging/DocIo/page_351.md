```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_351.jpeg
document_name: DocIo
page_number: 351
page_id: DocIo#page_351
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:50:32Z
fidelity: lossless
-->

## Overview
- Demonstrates how to create a Word document and add a text watermark using DocIO in VB.

## Content

```vb
[VB]

' Create a new word document
Dim doc As WordDocument = New WordDocument()
doc.EnsureMinimal()

' Add text watermark to the document
Dim TextWatermark As TextWatermark = New TextWatermark()
doc.Watermark = TextWatermark
TextWatermark.Size = 48
TextWatermark.Layout = WatermarkLayout.Horizontal
TextWatermark.Semitransparent = False
TextWatermark.Color = Color.Black
TextWatermark.Text = "Watermark"

' Save the document
doc.Save("Watermark.doc", FormatType.Doc)

' Close the document
doc.Close()
```

### Note: For more information on adding watermarks to a word document using DocIO, refer the following online documentation link:
- [http://help.syncfusion.com/Ug_101/Reporting/DocIO/Windows%20Forms/default.htm#!documents/4222watermark.htm](http://help.syncfusion.com/Ug_101/Reporting/DocIO/Windows%20Forms/default.htm#!documents/4222watermark.htm)

## Cross References
- See also:
  - [http://help.syncfusion.com/Ug_101/Reporting/DocIO/Windows%20Forms/default.htm#!documents/4222watermark.htm](http://help.syncfusion.com/Ug_101/Reporting/DocIO/Windows%20Forms/default.htm#!documents/4222watermark.htm)

<!-- tags: [DocIO, WordDocument, TextWatermark, Windows Forms, VB.NET, .NET] keywords: [DocIO, watermark, text watermark, VB.NET, document creation, Word, document manipulation, Syncfusion] -->
```