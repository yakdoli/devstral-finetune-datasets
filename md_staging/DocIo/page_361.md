```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_361.jpeg
document_name: DocIo
page_number: 361
page_id: DocIo#page_361
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:52:12Z
fidelity: lossless
-->

## Essential DocIO

```vb
Imports word = Microsoft.Office.Interop.Word
----------
' Initialize objects
Dim nullobject As Object = System.Reflection.Missing.Value
Dim newFilePath As Object = "CharacterFormattingOffice.doc"
Dim falseObj As Object = False

' Start the word application
Dim wordApp As word.Application = New word.Application()

' Create a new word document
wordApp.Documents.Add(nullobject, nullobject, nullobject, nullobject)
Dim doc As word.Document = wordApp.ActiveDocument

' Define range to which formatting to be applied
Dim start As Object = 0
Dim endobj As Object = 0
Dim rng As word.Range = doc.Range(start, endobj)

rng.Text = "New Text"
rng.Font.Name = "Arial"
rng.Font.Size = 14

' Save the document
doc.SaveAs(newFilePath, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject)

' Close the document
doc.Close(nullobject, nullobject, nullobject)

' Quit the application
wordApp.Quit()
```

### Using DocIO

The following code examples illustrate how to apply the character formatting to the word document using DocIO.

<!-- tags: [syncfusion-docio, micorosft-office-interop, character-formatting, docio, winforms, essential-docio] keywords: [DocIO, character formatting, MICorosoft Word, code examples, document editing, text formatting, document manipulation, font name, font size] -->
```