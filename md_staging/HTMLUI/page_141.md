```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_141.jpeg
document_name: HTMLUI
page_number: 141
page_id: HTMLUI#page_141
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:11:11Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Content

### Print and Print Preview Feature

The following sections highlight the integration of printing and print preview functionalities within the HTMLUI control.

#### Document Initialization and Print Setup

```csharp
[C#]
//Document initialization
HTMLUIPrintDocument pd = new HTMLUIPrintDocument(this.htmluiControl1.Document);

//Print Preview
PrintPreviewDialog dlg = new PrintPreviewDialog();
dlg.Document = pd;
dlg.ShowDialog();

//Print
PrintDialog dg = new PrintDialog();
dg.AllowSomePages = true;
dg.Document = pd;
if (dg.ShowDialog() == DialogResult.OK)
pd.Print();
```

```vbnet
[VB.NET]
'Document initialization
Dim pd As New HTMLUIPrintDocument(Me.HtmluiControl1.Document)

'Print Preview
Dim dlg As New PrintPreviewDialog()
dlg.Document = pd
dlg.ShowDialog()

'Print
Dim dg As New PrintDialog()
dg.AllowSomePages = True
dg.Document = pd
If dg.ShowDialog() = DialogResult.OK Then
pd.Print()
End If
```

Along with the printing feature, HTMLUI control supports reviewing of the document before printing. The following code snippet demonstrates how the print preview feature is enabled in HTMLUI.

```csharp
[C#]
// Document Initialization
private void PrintPreviewButton_Click(object sender, System.EventArgs e)
{
    HTMLUIPrintDocument pd = new HTMLUIPrintDocument(this.htmluiControl1.Document);

    // Initialize the new instance of the System.Windows.Forms.PrintPreviewDialog Class
    PrintPreviewDialog dlg = new PrintPreviewDialog();
    dlg.Document = pd;
    dlg.ShowDialog();
}
```

This demonstrates the seamless integration of print and print preview functionalities, enhancing the user experience by allowing direct interaction with the document content.

### References

- HTMLUIPrintDocument
- PrintPreviewDialog
- PrintDialog
- DialogBox

#### Notes and Key Points

This guide focuses on enabling effective printing and preview capabilities within the HTMLUI control, utilizing various classes and methods provided by Syncfusion for Windows Forms development.

### Page-level Navigation/TOC (if applicable)

This section provides a concise guide as part of the tutorial series. Additional reference sections and code examples are available in the HTMLUI user guide for enhanced functionality and customization of the HTMLUI control.

<!-- tags: [syncfusion, htmlui, windows forms, printing, print preview, htmlui control, document control, print dialog, print preview dialog, wxeml, print functionality, .NET development, csharp, vb.net] keywords: [printing, print preview, htmlui, document initialization, print dialog, print preview dialog, windows forms, csharp, vb.net, syncfusion, htmlui control, document control, wxeml, print functionality, print documentation, user guide] -->
```