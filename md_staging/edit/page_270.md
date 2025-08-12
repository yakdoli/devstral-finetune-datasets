```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_270.jpeg
document_name: edit
page_number: 270
page_id: edit#page_270
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:10:10Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

- TextChanging

## 4.14.24.1 TextChanged Event

This event is fired when the text in the Edit Control is changed.

The event handler receives an argument of type `EventArgs`.

### C#

```csharp
// Handle the TextChanged event.
this.editControl1.TextChanged += new EventHandler(editControl1_TextChanged);

// Set the text of the EditControl.
this.editControl1.Text = "Sample Text";

private void editControl1_TextChanged(object sender, EventArgs e)
{
    // The below statement can be seen in the output window at runtime.
    Console.WriteLine(" TextChanged event is raised ");
}
```

### VB.NET

```vbnet
' Handle the TextChanged event.
AddHandler Me.editControl1.TextChanged, AddressOf editControl1_TextChanged

' Set the text of the EditControl.
Me.editControl1.Text = "Sample Text"

Private Sub editControl1_TextChanged(ByVal sender As Object, ByVal e As EventArgs)
    ' The below statement can be seen in the output window at runtime.
    Console.WriteLine(" TextChanged event is raised ")
End Sub
```

## 4.14.24.2 TextChanging Event

This event is raised when the text is to be changed.

<!-- tags: [Syncfusion Windows Forms, TextChanged Event, TextChanging Event] keywords: [TextChanged, TextChanging, EventArgs, Edit Control, Event Handling, C#, VB.NET, Syncfusion Winforms, version 11.4.0.26] -->
```