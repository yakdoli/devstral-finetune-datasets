```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_039.jpeg
document_name: edit
page_number: 039
page_id: edit#page_039
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:56:18Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
// Bind key combinations to the action name using the
// RegisteringDefaultKeyBindings event.
private void this.editControl1_RegisteringDefaultKeyBindings(object sender,
EventArgs e)
{
    this.editControl1.KeyBinder.BindToCommand(Keys.Control | Keys.O, "File.Open");
}

// Define the action that needs to be performed.
private void Command_Open()
{
    /* Do the desired task. */
}
```

### [VB.NET]

```vb
' Invoke the Editor Keys Binding dialog.
Me.editControl1.ShowKeysBindingEditor()

' Bind the action name to the action using the RegisteringKeyCommands and
' ProcessCommandEventHandler events.
Private Sub Me.editControl1_RegisteringKeyCommands(ByVal sender As Object,
ByVal e As EventArgs)
    Me.editControl1.Commands.Add("File.Open").ProcessCommand += New
ProcessCommandEventHandler(Command_Open)
End Sub

' Bind key combinations to the action name using the
' RegisteringDefaultKeyBindings event.
Private Sub Me.editControl1_RegisteringDefaultKeyBindings(ByVal sender As Object,
ByVal e As EventArgs)
    Me.editControl1.KeyBinder.BindToCommand(Keys.Control | Keys.O,
    "File.Open")
End Sub

' Define the action that needs to be performed.
Private Sub Command_Open()
    ' Do the desired task.
End Sub
```

## A sample which demonstrates Keys Binding is available in the following sample installation path.

<!-- tags: [Syncfusion Winforms, Essential Edit] keywords: [Keys Binding, Editor Keys Binding, RegisteringKeyCommands, ProcessCommandEventHandler, RegisteringDefaultKeyBindings, Control, File.Open, Keys.O, Command_Open, VB.NET, C#] -->
```