```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_149.jpeg
document_name: HTMLUI
page_number: 149
page_id: HTMLUI#page_149
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:11:45Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

`' Return the selected text displayed in the control`
`Me.label1.Text = Me.HtmluiControl1.SelectedText`

## CopyTextToClipboard

The HTMLUI control allows the user to copy the text selected in the HTMLUI control to the Clipboard, and paste it in other applications. The following code snippet shows how this feature is implemented with the HTMLUI control.

### C#
```csharp
string text = this.htmluiControl.SelectedText.ToString();
if (text != "\"")
{
    //Copying the selected text to the Clipboard
    Clipboard.SetDataObject(text);
}
```

### VB.NET
```vb
Private text As String = Me.htmluiControl.SelectedText.ToString()
If text <> "" Then
    ' Copying the selected text to the Clipboard
    Clipboard.SetDataObject(text)
End If
```

## 4.23.1 HTMLUITextSelection Sample

This sample demonstrates the support for Text Selection in HTMLUI.

<!-- tags: [Syncfusion Winforms, HTMLUI, Text Selection, Clipboard, Control] keywords: [TextSelection, HTMLUI, Clipboard, CopyTextToClipboard, sample, Windows Forms] -->
```