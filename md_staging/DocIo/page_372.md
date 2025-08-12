```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_372.jpeg
document_name: DocIo
page_number: 372
page_id: DocIo#page_372
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:52:42Z
fidelity: lossless
-->

## [VB]

```vb
' Create a new word document
Dim doc As WordDocument = New WordDocument()
Dim section As IWSection = doc.AddSection()

' Add a paragraph to the document
Dim para As IWParagraph = section.AddParagraph()
para.AppendText("New Text")
para.AppendComment("Comment goes here")

' Save the document
doc.Save("CommentDocIO.doc", FormatType.Doc)
```

### Removing Comments Using MS Office Interop

The comments can be removed from the word document when they have served their purpose. The following code examples show how to remove all comments in the word document using Office Automation.
```html
<!-- tags: [DocIo, comment management, MS Office Interop, document manipulation, word document, Syncfusion Winforms, version 11.4.0.26] keywords: [comments, remove comments, document, word document, MS Office, interop, document manipulation, Syncfusion, SDK, VB, VBA, automation, Office Automation] -->
```