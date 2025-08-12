```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_165.jpeg
document_name: edit
page_number: 165
page_id: edit#page_165
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:04:54Z
fidelity: lossless
-->

## Overview
- Events related to the ContextChoice window are detailed, including ContextChoiceClose, ContextChoiceItemSelected, and ContextChoiceSelectedTextInsert.
- Code samples in both C# and VB.NET are provided for handling these events.

## Content
### Event Descriptions

| Edit Control Event              | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| ContextChoiceClose              | This event occurs when the Context Choice window has been closed.          |
| ContextChoiceItemSelected       | This event is raised when a Context Choice list item is selected.           |
| ContextChoiceSelectedTextInsert | This event is raised when the editor is about to insert selected Context Choice item to the text. Action can be cancelled. |

### Code Samples

#### ContextChoiceClose Event

**C#**
```csharp
private void editControl1_ContextChoiceClose(Syncfusion.Windows.Forms.Edit.Interfaces.IContextChoiceController controller, System.Windows.Forms.DialogResult dialogresult)
{
    // Clear the Context Choice items.
    this.editControl1.ContextChoiceController.Items.Clear();
}
```

**VB.NET**
```vb
Private Sub editControl1_ContextChoiceClose(ByVal controller As Syncfusion.Windows.Forms.Edit.Interfaces.IContextChoiceController, ByVal dialogresult As System.Windows.Forms.DialogResult) Handles EditControl.ContextChoiceClose
    ' Clear the Context Choice items.
    Me.editControl1.ContextChoiceController.Items.Clear()
End Sub
```

#### ContextChoiceItemSelected Event

**C#**
```csharp
private void editControl1_ContextChoiceItemSelected(Syncfusion.Windows.Forms.Edit.Interfaces.IContextChoiceController sender, Syncfusion.Windows.Forms.Edit.ContextChoiceItemSelectedEventArgs e)
{
    // Gets the selected item.
    IContextChoiceController controller = sender as IContextChoiceController;
    string selectedItemText = e.SelectedItem.Text;
}
```

### Summary

This section explains the different events related to the ContextChoice functionality in Syncfusion WinForms. Detailed examples in both C# and VB.NET are provided to illustrate how to handle these events effectively.

### RAG Annotations
<!-- tags: [winforms, contextchoice, events, csharp, vb.net, syncfusion] keywords: [ContextChoiceClose, ContextChoiceItemSelected, ContextChoiceSelectedTextInsert, code samples, event handling] -->
```