```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_911.jpeg
document_name: tools
page_number: 911
page_id: tools#page_911
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:43:02Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

The event handler receives an argument of type `EventArgs` containing data related to this event.

```csharp
private void textBoxExt1_MaximumSizeChanged(object sender, EventArgs e)
{
    Console.WriteLine(" MaximumSizeChanged event is raised ");
}
```

```vb
Private Sub textBoxExt1_MaximumSizeChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" MaximumSizeChanged event is raised ")
End Sub
```

### 3.5.8.10.4.8 MinimumSizeChanged

This event occurs when the `MinimumSize` property is changed. The `MinimumSize` property gets / sets the minimum size of the control.

The event handler receives an argument of type `EventArgs` containing data related to this event.

```csharp
private void textBoxExt1_MinimumSizeChanged(object sender, EventArgs e)
{
    Console.WriteLine(" MinimumSizeChanged event is raised ");
}
```

```vb
Private Sub textBoxExt1_MinimumSizeChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" MinimumSizeChanged event is raised ")
End Sub
```

### 3.5.8.10.4.9 MultilineChanged

This event occurs when the `Multiline` property is changed. The `Multiline` property controls whether the text of the edit control can span more than one line.

```html
<!-- tags: [product, module, control, api, version?] keywords: [event handler, EventArgs, MinimumSize, Multiline, Syncfusion, WinForms] -->
``` 
```