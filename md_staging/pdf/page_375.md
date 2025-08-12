```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_375.jpeg
document_name: pdf
page_number: 375
page_id: pdf#page_375
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:48:57Z
fidelity: lossless
-->

## Content

### Working with PDF Forms

```vb
listBox.Items.Add(New PdfListItem("German", "German"))

' Select the item
listBox.SelectedIndex = 2

' Set the multiselect option
listBox.MultiSelect = True

Dim submitAction As PdfSubmitAction = New PdfSubmitAction("http://stevex.net/dump.php")
submitAction.DataFormat = SubmitDataFormat.Html

Dim resetAction As PdfResetAction = New PdfResetAction()

' Create submit button to transfer the values in the form
Dim submitButton As PdfButtonField = New PdfButtonField(page, "submitButton")
submitButton.Bounds = New RectangleF(100, 420, 90, 20)
submitButton.Font = font
submitButton.Text = "Submit"
submitButton.Actions.MouseUp = submitAction
document.Form.Fields.Add(submitButton)

' Create reset button to reset all the values
Dim resetButton As PdfButtonField = New PdfButtonField(page, "resetButton")
resetButton.Bounds = New RectangleF(210, 420, 90, 20)
resetButton.Font = font
resetButton.Text = "Reset"
resetButton.Actions.MouseUp = resetAction
document.Form.Fields.Add(resetButton)
```

### 5.4 PDF Converter

This section shows some specific tasks that are supported in a PDF document creation.

#### 5.4.1 How To Convert Secure Webpages?

The `HtmlConverter` class provides support to access secured webpages. To access secured webpages, you have to pass the username and password information as arguments to the `ConvertToImage` method. The following code example illustrates this.

```vb
Dim htmlConverter As New HtmlConverter()
Dim htmlContent As String = ""
Dim stream As MemoryStream = Nothing
' Get the secured web content using System.Net.WebClient()
Dim webclient As New System.Net.WebClient()
Dim secureWebContent As String = webclient.DownloadString("https://example.com/securepage")
htmlContent = htmlContent + secureWebContent
stream = New MemoryStream()
Dim customImage As Bitmap = htmlConverter.ConvertToImage(htmlContent, stream, 600, 60, streamSettings)
```

<!-- tags: [pdf, pdf forms, pdf converter, html conversion, secure webpages, syncfusion winforms] keywords: [PdfSubmitAction, PdfResetAction, PdfButtonField, HtmlConverter, ConvertToImage, secure webpages, password protection, PDF document creation] -->
```