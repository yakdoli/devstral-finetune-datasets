```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_799.jpeg
document_name: tools
page_number: 799
page_id: tools#page_799
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:36:38Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
{
    Console.WriteLine(" RightToLeftChanged event is raised ");
}
```

### [VB.NET]

```vb
Private Sub percentTextBox1_RightToLeftChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" RightToLeftChanged event is raised ")
End Sub
```

## 3.5.8.5.4.16 SetNull

This event occurs when the NULL state is to be set based on a value.

The event handler receives an argument of type `SetNullEventArgs` containing data related to this event. The following `SetNullEventArgs` members provide information specific to this event.

| Members | Description |
|---------|-------------|
| Cancel  | Gets / sets a value indicating whether the event should be cancelled. |
| NullValue | Returns the NULL value. |

### [C#]

```csharp
private void percentTextBox1_SetNull(object sender, Syncfusion.Windows.Forms.Tools.SetNullEventArgs e)
{
    Console.WriteLine(" SetNull event is raised ");
}
```

### [VB.NET]

```vb
Private Sub percentTextBox1_SetNull(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Tools.SetNullEventArgs)
    Console.WriteLine(" SetNull event is raised ")
End Sub
```

## 3.5.8.5.4.17 TextAlignChanged

This event occurs when the `TextAlign` property is changed. The `TextAlign` property indicates how the text should be aligned for edit controls.

---
```html
<!-- tags: [Windows Forms, SetNull, TextAlignment, ControlProperties, EventHandling, Syncfusion Winforms, version] keywords: [SetNull, TextAlignChanged, TextAlignment, Control Properties, Event, WindowsForms, Syncfusion] -->
```