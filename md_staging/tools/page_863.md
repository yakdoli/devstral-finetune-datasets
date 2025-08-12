```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_863.jpeg
document_name: tools
page_number: 863
page_id: tools#page_863
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:40:28Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
Console.WriteLine("BorderSidesChanged event is raised");
}
```

```vb
[VB.NET]

Private Sub maskedEditBox1_BorderSidesChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("BorderSidesChanged event is raised")
End Sub
```

## 3.5.8.8.4.4 BorderSideChanged

This event occurs when the `BorderStyle` property is changed. The `BorderStyle` property indicates whether the edit control should have a border.

The event handler receives an argument of type `EventArgs` containing data related to this event.

```csharp
[C#]

private void maskedEditBox1_BorderStyleChanged(object sender, EventArgs e)
{
    Console.WriteLine("BorderStyleChanged event is raised");
}
```

```vb
[VB.NET]

Private Sub maskedEditBox1_BorderStyleChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("BorderStyleChanged event is raised")
End Sub
```

## 3.5.8.8.4.5 CharacterCasingChanged

This event occurs when the `CharacterCasing` property is changed. The `CharacterCasing` property gets / sets the case of the characters as they are typed.

The event handler receives an argument of type `EventArgs` containing data related to this event.

```csharp
[C#]

private void maskedEditBox1_CharacterCasingChanged(object sender, EventArgs e)
{
}
```

---
© 2013 Syncfusion. All rights reserved. 863 | Page
```