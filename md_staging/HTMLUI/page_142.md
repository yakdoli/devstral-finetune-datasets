<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_142.jpeg
document_name: HTMLUI
page_number: 142
page_id: HTMLUI#page_142
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:11:37Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

```vb
[VB.NET]

' Document Initialization
Private Sub PrintPreviewButton_Click(ByVal sender As Object, ByVal e As System.EventArgs)
    Dim pd As HTMUIPrintDocument = New HTMUIPrintDocument(Me.htmluiControl1.Document)

    ' Initialize the new instance of the System.Windows.Forms.PrintPreviewDialog Class
    Dim dlg As PrintPreviewDialog = New PrintPreviewDialog()
    dlg.Document = pd
    dlg.ShowDialog()
End Sub
```

The following figure shows the Print preview page that appears when the corresponding button is clicked. This illustrates the Printing feature in HTMLUI.

![Print Preview Page](image_url_for_print_preview_page)

## Page-level Navigation/TOC (if applicable)
- None

## Cross References
- None

## RAG Annotations
<!-- tags: [htmlui, windows forms, print preview, document initialization] keywords: [print, preview, document, htmlui, printpreviewdialog, pdf, window forms, buttons, print dialog, essentials suite, component libraries, print feature] -->