```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_912.jpeg
document_name: tools
page_number: 912
page_id: tools#page_912
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:42:10Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

The event handler receives an argument of type `EventArgs` containing data related to this event.

## MultilineChanged Event

### C#
```csharp
private void textBoxExt1_MultilineChanged(object sender, EventArgs e)
{
    Console.WriteLine(" MultilineChanged event is raised ");
}
```

### VB.NET
```vbnet
Private Sub textBoxExt1_MultilineChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" MultilineChanged event is raised ")
End Sub
```

### ReadOnlyChanged Event

This event occurs when the `ReadOnly` property is changed. The `ReadOnly` property controls whether the text in the edit control can be changed or not.

The event handler receives an argument of type `EventArgs` containing data related to this event.

### C#
```csharp
private void textBoxExt1_ReadOnlyChanged(object sender, EventArgs e)
{
    Console.WriteLine(" ReadOnlyChanged event is raised ");
}
```

### VB.NET
```vbnet
Private Sub textBoxExt1_ReadOnlyChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" ReadOnlyChanged event is raised ")
End Sub
```

### TextAlignChanged Event

This event occurs when the `TextAlign` property is changed. The `TextAlign` property indicates how the text should be aligned for edit controls.

The event handler receives an argument of type `EventArgs` containing data related to this event.

### C#
```csharp
private void textBoxExt1_TextAlignChanged(object sender, EventArgs e)
{
    Console.WriteLine(" TextAlignChanged event is raised ");
}
```

### Remarks
- `ReadonlyChanged` and `TextAlignChanged` are similar to `MultilineChanged`.

<!-- tags: [Syncfusion Winforms, Event Handling, EventArgs, ReadOnly, TextAlign, Multiline] keywords: [args, event handler, multiline, readonly, text alignment] -->
```