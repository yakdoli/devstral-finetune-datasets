```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_240.jpeg
document_name: DocIo
page_number: 240
page_id: DocIo#page_240
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:43:42Z
fidelity: lossless
-->

### [Essential DocIO](#)

```vb
Dim doc As IWordDocument = New WordDocument()
Dim section As IWSection = doc.AddSection()
Dim paragraph As IParagraph = section.AddParagraph()
section.PageSetup.DifferentFirstPage = True
section.PageSetup.DifferentOddAndEvenPages = True

' Main doc textboxes
paragraph.AppendText("Testing textboxes")

' 1 textbox
Dim mainTextbox As ITextBox = paragraph.AppendTextBox(150, 110)
mainTextbox.TextBoxBody.AddParagraph().AppendText("Textbox text 1")
mainTextbox.TextBoxFormat.FillColor = System.Drawing.Color.Blue
mainTextbox.TextBoxFormat.LineDashing = LineDashing.LongDashDotDotGEL
mainTextbox.TextBoxFormat.LineWidth = 4.0f

' 2 textbox
Dim mainTextbox1 As ITextBox = paragraph.AppendTextBox(150, 100)
mainTextbox1.TextBoxFormat.VerticalPosition = 500
mainTextbox1.TextBoxBody.AddParagraph().AppendText("Another textbox")
mainTextbox1.TextBoxFormat.FillColor = System.Drawing.Color.Yellow
mainTextbox1.TextBoxFormat.LineDashing = LineDashing.DashGEL
mainTextbox1.TextBoxFormat.LineWidth = 3.75f
mainTextbox1.TextBoxFormat.TextWrappingStyle = TextWrappingStyle.Through
mainTextbox1.TextBoxFormat.TextWrappingType = TextWrappingType.Both
mainTextbox1.TextBoxFormat.HorizontalAlignment = 
ShapeHorizontalAlignment.Center
mainTextbox1.TextBoxFormat.VerticalAlignment = ShapeVerticalAlignment.Bottom

' Header/footer textboxes
paragraph = New WParagraph(doc)
paragraph.AppendText("Hello textboxes")
Dim textbox As ITextBox = paragraph.AppendTextBox(20, 50)
textbox.TextBoxBody.AddParagraph().AppendText("Header textbox")
textbox.TextBoxFormat.FillColor = System.Drawing.Color.Blue
textbox.TextBoxFormat.LineDashing = LineDashing.LongDashDotDotGEL
textbox.TextBoxFormat.LineWidth = 4.0f

Dim textbox1 As ITextBox = paragraph.AppendTextBox(250, 50)
textbox1.TextBoxBody.AddParagraph().AppendText("Header textbox 2")
textbox1.TextBoxFormat.FillColor = System.Drawing.Color.Tomato
textbox1.TextBoxFormat.VerticalPosition = 250
textbox1.TextBoxFormat.LineStyle = TextBoxLineStyle.Triple
textbox1.TextBoxFormat.LineDashing = LineDashing.LongDashGEL
```

<!-- tags: [syncfusion, word document, textbox, text formatting, visual basic, winforms, essential docio, version 11.4.0.26] keywords: [document, section, paragraph, textbox, fill color, line dashing, line width, text wrapping, alignment, header, footer] -->
```