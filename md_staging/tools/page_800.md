```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_800.jpeg
document_name: tools
page_number: 800
page_id: tools#page_800
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:35:33Z
fidelity: lossless
-->

## Event Handler Examples

### Event Handler with EventArgs

The event handler receives an argument of type `EventArgs` containing data related to this event.

#### C#

```csharp
private void percentTextBox1_TextAlignChanged(object sender, EventArgs e)
{
    Console.WriteLine(" TextAlignChanged event is raised ");
}
```

#### VB.NET

```vb
Private Sub percentTextBox1_TextAlignChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" TextAlignChanged event is raised ")
End Sub
```

### ThemesEnabledChanged

#### Overview
This event occurs when the `ThemesEnabled` property is changed. The `ThemesEnabled` property specifies whether or not to use XP Themes when the `BorderStyle` property is set to 'Fixed3D'.

#### Code Example

- **C#**:

```csharp
private void percentTextBox1_ThemesEnabledChanged(object sender, EventArgs e)
{
    Console.WriteLine(" ThemesEnabledChanged event is raised ");
}
```

- **VB.NET**:

```vb
Private Sub percentTextBox1_ThemesEnabledChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" ThemesEnabledChanged event is raised ")
End Sub
```

### ValidationError

This event occurs when the input text is invalid for the current state of the control.

### Summary
- **ThemesEnabledChanged**: Triggered when the `ThemesEnabled` property is changed.
- **ValidationError**: Triggered when the input text is invalid for the current state of the control.

<!-- tags: [essential-tools, windows-forms, event-handlers, winforms, EventArgs, ThemesEnabled, fixed3D, validation, VisualBasic.NET, C#] keywords: [event handler, EventArgs, ThemesEnabled, fixed3D, ValidationError, XPThemes, BorderStyle] -->
```