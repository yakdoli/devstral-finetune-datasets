```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_197.jpeg
document_name: edit
page_number: 197
page_id: edit#page_197
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:06:51Z
fidelity: lossless
--> 

## Essential Edit for Windows Forms

### Handling File or Stream Closing Actions

```vb
[VB.NET]

Private Sub editControl1_Closing(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Edit.StreamCloseEventArgs) Handles editControl1.StreamClose
    ' Cancel the file or stream closing action.
    e.Action = SaveChangesAction.Cancel
    
    ' Close the file or stream without saving the unsaved contents; the changes will be lost forever.
    e.Action = SaveChangesAction.Discard
    
    ' Silently saves the unsaved contents to the currently open file or stream. If the contents have not been saved to a file or stream as yet, the Save Changes prompt is displayed.
    e.Action = SaveChangesAction.Save
    
    ' Displays the default Save Changes prompt if there are unsaved contents when the file or stream is closed.
    e.Action = SaveChangesAction.ShowDialog
End Sub
```

**Note:** The default value of `e.Action` is `SaveChangesAction.ShowDialog`.

### Close Method

This method closes the currently open file or stream and displays the Edit Control in read-only mode until a new file or stream is opened.

| Edit Control Method | Description |
|---------------------|-------------|
| Close              | Closes stream, makes control read-only. |

### Code Examples

**C#**

```csharp
// Closes the currently open file or stream in the Edit Control.
this.editControl1.Close();
```

**VB.NET**

```vb
' Closes the currently open file or stream in the Edit Control.
Me.editControl1.Close()
```

See Also

© 2013 Syncfusion. All rights reserved.
```