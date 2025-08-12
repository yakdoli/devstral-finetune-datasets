```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_348.jpeg
document_name: DocIo
page_number: 348
page_id: DocIo#page_348
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:51:11Z
fidelity: lossless
-->

# Essential DocIO

```vb
Imports word = Microsoft.Office.Interop.Word
' Initialize objects
Dim nullobject As Object = Missing.Value
Dim newFilePath As Object = "NewFileWatermark.doc"

' Start the application
Dim wordApp As word.Application = New word.Application()

' Create a new word document
wordApp.Documents.Add(nullobject, nullobject, nullobject, nullobject)
Dim doc As word.Document = wordApp.ActiveDocument

' Seek the current page header
wordApp.ActiveWindow.ActivePane.View.SeekView = word.WdSeekView.wdSeekCurrentPageHeader

' Add text watermark to the document
Dim watermark As word.Shape = wordApp.Selection.HeaderFooter.Shapes.AddTextEffect(Microsoft.Office.Core.MsoPresetTextEffect.msoTextEffect1, "Watermark", "Arial", 48, Microsoft.Office.Core.MsoTriState.msoTrue, Microsoft.Office.Core.MsoTriState.msoFalse, 0, 0, nullobject)

' Set watermark properties
watermark.Fill.Visible = Microsoft.Office.Core.MsoTriState.msoTrue
watermark.Line.Visible = Microsoft.Office.Core.MsoTriState.msoFalse
watermark.Fill.Solid()
watermark.Fill.ForeColor.RGB = CType(word.WdColor.wdColorGray30, Integer)

' Save document
doc.SaveAs(newFilePath, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject, nullobject)

' Close the document
doc.Close(nullobject, nullobject, nullobject)

' Quit application
wordApp.Quit()
```
```