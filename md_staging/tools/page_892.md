<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_892.jpeg
document_name: tools
page_number: 892
page_id: tools#page_892
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:41:00Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Event Notifications

```vb
yVal e As EventArgs)
    Console.WriteLine(" ReadOnlyChanged event is raised ")
End Sub
```

#### 3.5.8.9.4.6 ThemeChanged

This event occurs when the `ThemesEnabled` property is changed. The `ThemesEnabled` property indicates whether XP Themes (visual styles) should be used for this control when available.

The event handler receives an argument of type `EventArgs` containing data related to this event.

```csharp
[C#]

private void numericUpDownExt1_ThemeChanged(object sender, EventArgs e)
{
    Console.WriteLine(" ThemeChanged event is raised ");
}
```

```vb
[Vb.NET]

Private Sub numericUpDownExt1_ThemeChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" ThemeChanged event is raised ")
End Sub
```

#### 3.5.8.9.4.7 ValueChanged

This event occurs when the `Value` property is changed. The `Value` property gets / sets the value assigned to the spin box (also known as an up-down control).

The event handler receives an argument of type `EventArgs` containing data related to this event.

```csharp
[C#]

private void numericUpDownExt1_ValueChanged(object sender, EventArgs e)
{
    Console.WriteLine(" ValueChanged event is raised ");
}
```

```vb
[Vb.NET]

Private Sub numericUpDownExt1_ValueChanged(ByVal sender As Object, ByVal l e As EventArgs)
```

## Page-level Navigation/TOC (if applicable)
- Event Notifications
  - ThemeChanged
  - ValueChanged

## Cross References
- None

<!-- tags: [Syncfusion Winforms, Essential Tools, Event Notifications, ThemesEnabled, Value, C#, VB.NET] keywords: [ReadOnlyChanged, ThemesEnabled, Value, spin box, up-down control, Event Handler, EventArgs] -->