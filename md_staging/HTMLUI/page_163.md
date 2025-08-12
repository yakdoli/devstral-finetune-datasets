```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_163.jpeg
document_name: HTMLUI
page_number: 163
page_id: HTMLUI#page_163
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T07:12:01Z
fidelity: lossless
-->

# Essential HTMLUI for Windows Forms

## Overview
- Demonstrates how to enable drag-and-drop functionality for an HTMLUI control in a Windows Forms application.
- Details the implementation of `DragDrop` and `DragEnter` events to handle drag events in C# and VB.NET.

## Content

### C#
```csharp
//To support drag events to the control
this.htmluiControl1.AllowDrop = true;

//DragDrop and DragEnter events declaration
this.htmluiControl1.DragDrop += new
System.Windows.Forms.DragEventHandler(this.htmluiControl1_DragDrop);
this.htmluiControl1.DragEnter += new
System.Windows.Forms.DragEventHandler(this.htmluiControl1_DragEnter);

private void htmluiControl1_DragEnter(object sender,
System.Windows.Forms.DragEventArgs e)
{
    if (e.Data.GetDataPresent(DataFormats.FileDrop))
        //Specifying the drop effect
        e.Effect = DragDropEffects.All;
    else
        e.Effect = DragDropEffects.None;
}

private void htmluiControl1_DragDrop(object sender,
System.Windows.Forms.DragEventArgs e)
{
    //Specifying the drop format and collecting the file name
    string[] files = (string[])e.Data.GetData("FileDrop", false);
    foreach (string fileName in files)
    {
        //Loading the specified file in to the HTMLUI control
        this.htmluiControl1.LoadHTML(fileName);
    }
}
```

### VB.NET
```vbnet
'To support drag events to the control
Private Me.htmluiControl1.AllowDrop = True

'DragDrop and DragEnter events declaration
Private Me.htmluiControl1.DragDrop += New
System.Windows.Forms.DragEventHandler(Me.htmluiControl1_DragDrop)
Private Me.htmluiControl1.DragEnter += New
System.Windows.Forms.DragEventHandler(Me.htmluiControl1_DragEnter)

Private Sub htmluiControl1_DragEnter(ByVal sender As Object, ByVal e As
System.Windows.Forms.DragEventArgs)
    If e.Data.GetDataPresent(DataFormats.FileDrop) Then
        'Specifying the drop effect
        e.Effect = DragDropEffects.All
    Else
        e.Effect = DragDropEffects.None
    End If
End Sub
```

## Cross References
- The `LoadHTML` method in the example suggests integration with presentation logic based on the content being dragged into the control.

<!-- tags: [syncfusion-sdk, WinForms, HTMLUI, drag-and-drop, C#, VB.NET] keywords: [HTMLUI control, WindowsForms, DragDrop, DragEnter, LoadHTML, FileDrop, DragDropEffects] -->
```