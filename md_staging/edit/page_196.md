```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_196.jpeg
document_name: edit
page_number: 196
page_id: edit#page_196
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:05:12Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Handles the `Closing` event of a Windows Forms application to manage saving changes before closing.
- Provides customization options for saving or discarding unsaved changes.
- Describes the use of `SaveOnClose` property and the `StreamCloseEventArgs` to handle close events.

## Content

### VB.NET

```vb
Private Sub Form1_Closing(ByVal sender As Object, ByVal e As System.ComponentModel.CancelEventArgs) Handles MyBase.Closing
    If Me.editControl.SaveOnClose = False Then
        If Me.editControl.SaveModified() = True Then
            ' Perform custom Save routine or show custom Save Changes dialog or set Cancel to False.
            If e.Cancel = False
                e.Cancel = False
            Else
                e.Cancel = True
            End If
        End If
    End If
End Sub 'Form1_Closing
```

### Saving Changes using the Save Changes Prompt

When the `SaveOnClose` property is set to `True`, the default **Save Changes** prompt appears on closing the **Edit Control** without saving the contents. Click **Yes** to save the changes, **No** to discard the changes, or **Cancel** to close the **Save Changes** prompt.

The above task can be further customized by handling the **Closing** event of the **Edit Control**. The **Closing** event is triggered just before a file or stream is closed in the **Edit Control**.

### C#

```csharp
[C#]

private void editControl_Closing(object sender, Syncfusion.Windows.Forms.Edit.StreamCloseEventArgs e)
{
    // Cancel the file or stream closing action.
    e.Action = SaveChangesAction.Cancel;

    // Close the file or stream without saving the unsaved contents, the changes will be lost forever.
    e.Action = SaveChangesAction.Discard;

    // Silently saves the unsaved contents to the currently open file or stream.
    // If the contents have not been saved to a file or stream as yet, the Save Changes prompt is displayed.
    e.Action = SaveChangesAction.Save;

    // Displays the default Save Changes prompt if there are unsaved contents when the file or stream is closed.
    e.Action = SaveChangesAction.ShowDialog;
}
```

## API Reference

### Save Changes Actions

- **SaveChangesAction.Cancel**: Cancels the file or stream closing action.
- **SaveChangesAction.Discard**: Closes the file or stream without saving unsaved contents.
- **SaveChangesAction.Save**: Silently saves the unsaved contents.
- **SaveChangesAction.ShowDialog**: Displays the default Save Changes prompt.

## Code Examples

### C# Example

```csharp
private void editControl_Closing(object sender, Syncfusion.Windows.Forms.Edit.StreamCloseEventArgs e)
{
    // Handle the closing event and determine the action.
    e.Action = SaveChangesAction.ShowDialog;
}
```

## Cross References
- See also: [Syncfusion.Edit Control Documentation](link)
- [Handling File Close Actions in Windows Forms](link)

<!-- tags: [syncfusion, windowsforms, editcontrol, closingevent, saveonclose, streamcloseeventargs, savechangesaction] keywords: [form_closing, editcontrol, saveonclose, savechanges, cancelclosing, fileclosing, streamclosing, customsave] -->
```