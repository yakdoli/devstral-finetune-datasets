```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_048.jpeg
document_name: HTMLUI
page_number: 048
page_id: HTMLUI#page_048
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:05:31Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

```vb
' Event that is to be raised after the hyperlink was clicked and before the hyperlink tries to load
' a new resource.
Me.HtmluiControl1.LinkClicked += New
Syncfusion.Windows.Forms.HTMLUI.LinkForwardEventHandler(Me.HtmluiControl1_LinkClicked)

Private Sub htmluiControl1_LinkClicked(ByVal sender As Object, ByVal e As
Syncfusion.Windows.Forms.HTMLUI.LinkForwardEventArgs
    e.Cancel = True
    Dim form2 As Form2 = New Form2(GetFilesLocation() + e.Path)
    form2.Show()
End Sub
```

## LoadStarted Event

This event is raised when a new HTML document has started loading into the HTMLUI control from the specified resource.

### [C#]

```csharp
// Event that is to be raised when the HTMLUI control starts loading a new html document.
this.htmluiControl1.LoadStarted += new
System.EventHandler(this.htmluiControl1_LoadStarted);

private void htmluiControl1_LoadStarted(object sender, System.EventArgs e)
{
    Console.WriteLine("Started Loading...");
}
```

### [VB.NET]

```vb
' Event that is to be raised when the HTMLUI control starts loading a new html document.
Me.HtmluiControl1.LoadStarted += New
System.EventHandler(Me.htmluiControl1_LoadStarted)

Private Sub htmluiControl1_LoadStarted(ByVal sender As Object, ByVal e As System.EventArgs)
    Console.WriteLine("Started Loading...")
End Sub
```

## LoadFinished Event

This event is raised after the loading of HTML document inside the HTMLUI control is completed.

---
© 2013 Syncfusion. All rights reserved. 48 | Page
```
<!-- tags: [Syncfusion Winforms, HTMLUI, Events, LoadStarted, LoadFinished, LinkClicked, Navigation, Loading, Document, Control] keywords: [HTMLUI, linkforwardeventhandler, loadstarted, loadfinished, navigation, document loading, windows forms, event handling] -->
```