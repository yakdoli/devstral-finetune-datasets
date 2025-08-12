<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_162.jpeg
document_name: HTMLUI
page_number: 162
page_id: HTMLUI#page_162
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:12:53Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

```csharp
private void button1_Click(object sender, System.EventArgs e)
{
    this.text1.Parent.Children.Remove(this.text1);
    this.btn1.Parent.Children.Remove(this.btn1);
    this.htmluiControl.Refresh();
}
```

### [VB.NET]

```vb
Private text1 As IHTMLElement
Private btn1 As IHTMLElement

Private button1 As System.Windows.Forms.Button
Private button1.Click += New System.EventHandler(Me.button1_Click)
Private htmluiControl.LoadFinished += New System.EventHandler(Me.htmluiControl_LoadFinished)

Private Sub htmluiControl_LoadFinished(ByVal sender As Object, ByVal e As System.EventArgs)
    Me.text1 = Me.htmluiControl1.Document.GetElementById("txt1")
    Me.btn1 = Me.htmluiControl1.Document.GetElementById("btn1")
End Sub

Private Sub button1_Click(ByVal sender As Object, ByVal e As System.EventArgs)
    Me.text1.Parent.Children.Remove(Me.text1)
    Me.btn1.Parent.Children.Remove(Me.btn1)
    Me.htmluiControl.Refresh()
End Sub
```

## 5.9 How To Enable the HTMLUI Control To Load HTML Documents That Have Been Dragged Onto the Control?

In order to enable the HTMLUI control to load HTML documents that have been dragged onto the control, you have to set the `AllowDrop` property of the HTMLUI control to `True`. This property helps in supporting the drag-and-drop operation in the HTMLUI control.

During the drag-and-drop operation, the file name of the document along with the location is collected, and when the mouse button is released, the specified document is loaded from the mentioned location through the `LoadHTML` method of the HTMLUI control.

<!-- tags: [Syncfusion Winforms, HTMLUI Control, Drag-and-Drop, LoadHTML, AllowDrop] keywords: [HTMLUI, drag-and-drop, LoadHTML, AllowDrop, Windows Forms] -->