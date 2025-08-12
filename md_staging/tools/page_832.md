```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_832.jpeg
document_name: tools
page_number: 832
page_id: tools#page_832
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:37:28Z
fidelity: lossless
-->

## Drag and Drop Operations in EditableList Control

### Handling DragEnter Event

The `DragEnter` event can be utilized to allow dragging files into the text area of the `EditableList` control. This functionality is particularly useful for managing file operations in applications. The following examples illustrate how to handle the `DragEnter` event in both C# and VB.NET.

#### C# Code

```csharp
private void editableList1_DragEnter(object sender, System.Windows.Forms.DragEventArgs e)
{
    if (e.Data.GetDataPresent(DataFormats.FileDrop))
        e.Effect = DragDropEffects.All;
    else
        e.Effect = DragDropEffects.None;
}
```

#### VB.NET Code

```vbnet
Private Sub editableList1_DragEnter(ByVal sender As Object, ByVal e As System.Windows.Forms.DragEventArgs)
    If e.Data.GetDataPresent(DataFormats.FileDrop) Then
        e.Effect = DragDropEffects.All
    Else
        e.Effect = DragDropEffects.None
    End If
End Sub
```

### Handling DragDrop Event

The `DragDrop` event is useful for handling the action of dropping files within the `EditableList` control. This event can be triggered to append files to a list, allowing users to drag and drop multiple files into the control.

#### C# Code

```csharp
private void editableList1_DragDrop(object sender, System.Windows.Forms.DragEventArgs e)
{
    string[] files = (string[])e.Data.GetData("FileDrop", false);
    foreach (string s in files)
    {
        this.editableList1.ListBox.Items.Add(s.Substring(1 + s.LastIndexOf(@"\")));
    }
}
```

#### VB.NET Code

```vbnet
Private Sub editableList1_DragDrop(ByVal sender As Object, ByVal e As System.Windows.Forms.DragEventArgs)
    Dim files As String()
    files = CType(e.Data.GetData("FileDrop", False), String())
    Dim s As String
    For Each s In files
        editableList1.ListBox.Items.Add(CStr(s.Substring(1 + s.LastIndexOf("\"))))
    Next
End Sub
```

### Conclusion

By implementing the `DragEnter` and `DragDrop` event handlers, you can enable file dragging and dropping functionality within the `EditableList` control in your Windows Forms applications. This enhances user interaction by allowing easy file management directly within the application interface.

<!-- tags: [product, module, control, api, version?] keywords: [DragEnter, DragDrop, EditableList, FileDrag, Windows Forms, Syncfusion] -->
```