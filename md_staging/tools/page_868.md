```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_868.jpeg
document_name: tools
page_number: 868
page_id: tools#page_868
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:39:41Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### ReadOnlyChanged

```csharp
Console.WriteLine(" ReadOnlyChanged event is raised ");
}
```

```vb
Private Sub maskedEditBox1_ReadOnlyChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" ReadOnlyChanged event is raised ")
End Sub
```

#### 3.5.8.8.4.13 `TextAlignChanged`

This event occurs when the `TextAlign` property is changed. The `TextAlign` property indicates how the text should be aligned for edit controls.

The event handler receives an argument of type `EventArgs` containing data related to this event.

**[C#]**

```csharp
private void maskedEditBox1_TextAlignChanged(object sender, EventArgs e)
{
    Console.WriteLine(" TextAlignChanged event is raised ");
}
```

**[VB.NET]**

```vb
Private Sub maskedEditBox1_TextAlignChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" TextAlignChanged event is raised ")
End Sub
```

### 3.5.8.8.4.14 `ThemesEnabledChanged`

This event occurs when the `ThemesEnabled` property is changed. The `ThemesEnabled` property specifies whether or not to use XP Themes when the `BorderStyle` property is set to 'Fixed3D'.

The event handler receives an argument of type `EventArgs` containing data related to this event.

**[C#]**

```csharp
private void maskedEditBox1_ThemesEnabledChanged(object sender, EventArgs e)
```

## Page-level Navigation/TOC (if applicable)
- Refer to section 3.5.8.8.4.13 for details on `TextAlignChanged`.
- Refer to section 3.5.8.8.4.14 for details on `ThemesEnabledChanged`.

<!-- tags: [syncfusion, winforms, essential tools] keywords: [readOnlyChanged, textAlignChanged, themesEnabledChanged, event handler, text align, themes, fixed3d, control events] -->
```