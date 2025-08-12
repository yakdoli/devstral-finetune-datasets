<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_102.jpeg
document_name: tools
page_number: 102
page_id: tools#page_102
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:22:37Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates saving and restoring the state of a `CommandBar` control in Windows Forms.
- Uses the `AppStateSerializer` class to persist the `CommandBar` layout across application sessions.
- Implements saving selected radio button information in the Windows Registry.

## Content

### Saving CommandBar State on Form Closing

This section provides code examples in both C# and VB.NET for saving the state of a `CommandBar` when a form is closed.

#### C#
```csharp
private void Form1_Closing(object sender, System.ComponentModel.CancelEventArgs e)
{
    selRad = this.getSelRad();
    rootKey = Registry.CurrentUser.CreateSubKey("Config");
    rootKey.SetValue("PersistType", selRad);
    AppStateSerializer app = this.GetSerializer(selRad);
    if (app != null)
    {
        // Store the current layout state of CommandBar objects using AppStateSerializer class.
        this.commandBarController1.SaveCommandBarState(app);
        app.PersistNow();
    }
}

private string getSelRad()
{
    RadioButton radReturn = new RadioButton();
    foreach (Control ctrl in this.groupBox1.Controls)
    {
        RadioButton rad = ctrl as RadioButton;
        if (rad.Checked) radReturn = rad;
    }
    return (radReturn.Text);
}
```

#### VB.NET
```vb.net
Private Sub Form1_Closing(ByVal sender As Object, ByVal e As System.ComponentModel.CancelEventArgs)
    selRad = Me.getSelRad()
    rootKey = Registry.CurrentUser.CreateSubKey("Config")
    rootKey.SetValue("PersistType", selRad)
    Dim app As AppStateSerializer = Me.GetSerializer(selRad)
    If Not app Is Nothing Then
        ' Store the current layout state of CommandBar objects using AppStateSerializer class.
        Me.commandBarController1.SaveCommandBarState(app)
        app.PersistNow()
    End If
End Sub

Private Function getSelRad() As String
    Dim radReturn As New RadioButton
    For Each ctrl In Me.groupBox1.Controls
        Dim rad As RadioButton = TryCast(ctrl, RadioButton)
        If rad.Checked Then radReturn = rad
    Next
    Return radReturn.Text
End Function
```

### Explanation
1. **`Form1_Closing` Event**:
   - Triggered when the form is about to close.
   - Calls `getSelRad()` to determine the selected radio button.
   - Creates a registry key under `HKEY_CURRENT_USER` for persistence.
   - Sets a value in the registry with the selected radio button information.
   - Obtains an instance of `AppStateSerializer` to persist the state.
   - Saves the `CommandBar` state using `SaveCommandBarState` and persists it immediately.

2. **`getSelRad` Method**:
   - Iterates through the controls in a `GroupBox`.
   - Checks which `RadioButton` is selected and returns its text.

### Usage Context
- This code is typically used in scenarios where expensive operations need to be deferred until form closing, and restoring the state of the `CommandBar` is necessary for a user-friendly experience.

## API Reference

### Classes
- **`Registry`**: Provides access to Windows Registry keys.
- **`AppStateSerializer`**: Manages the state serialization and persistence for various controls.
- **`CommandBarController`**: Manages state for `CommandBar` controls.

### Methods
- **`CreateSubKey`**: Creates or opens a subkey in the registry.
- **`SetValue`**: Sets the data and type of a value in a registry key.
- **`SaveCommandBarState`**: Saves the layout state of a `CommandBar`.
- **`PersistNow`**: Immediately persists the serialized state.

## Code Examples

### Saving `CommandBar` State
The provided C# and VB.NET code examples demonstrate how to save the state of a `CommandBar` when the form is closed, ensuring that the layout is restored upon the next session.

### Retrieving `CommandBar` State
The examples do not include retrieval code but typically involve reversing the persistence steps and restoring the `CommandBar` state from the `AppStateSerializer`.

## RAG Annotations

<!-- tags: [syncfusion, winforms, toolbar, commandbar, state management, persistance] keywords: [registry, AppStateSerializer, CommandBar, form closing, layout] -->