```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_289.jpeg
document_name: XlsIO
page_number: 289
page_id: XlsIO#page_289
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T11:07:59Z
fidelity: lossless
-->

## Essential XlsIO

```vb
' Creates a new Text Box.
Dim textbox As ITextBoxShape = sheet.TextBoxes.AddTextBox(3, 7, 25, 100)
textbox.Text = "Essential XlsIO"

' Reads a Text Box.
ITextBoxShape shape1 = sheet.TextBoxes(0)
shape1.Name = "First TextBox"
shape1.Fill.ForeColor = Color.Gold
shape1.Fill.BackColor = Color.Black
shape1.Fill.Pattern = ExcelGradientPattern.Pat_90_Percent
```

### Figure 96: TextBox created using XlsIO

![](https://example.com/TextBoxSample.png)
*Figure 96: TextBox created using XlsIO*

## 4.2.8.2 Check Box

<!-- tags: [essential_xlsio, textbox, gradientpattern, istringstream, syncfusion, winforms] keywords: [essentialxlsio, textboxcreation, fillproperties, goldblackgradient, textboxes] -->
```