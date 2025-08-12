```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_910.jpeg
document_name: tools
page_number: 910
page_id: tools#page_910
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:42:31Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

The event handler receives an argument of type `EventArgs` containing data related to this event.

## Event Handlers with EventArgs

### CharacterCasingChanged

#### C#

The `CharacterCasingChanged` event is raised when the casing of the text in the control changes.

```csharp
private void textBoxExt1_CharacterCasingChanged(object sender, EventArgs e)
{
    Console.WriteLine(" CharacterCasingChanged event is raised ");
}
```

#### VB.NET

```vb
Private Sub textBoxExt1_CharacterCasingChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" CharacterCasingChanged event is raised ")
End Sub
```

### HideSelectionChanged

#### Description

This event occurs when the `HideSelection` property is changed. The `HideSelection` property indicates that the selection should be hidden when the edit control loses focus.

#### EventArgs

The event handler receives an argument of type `EventArgs` containing data related to this event.

#### C#

```csharp
private void textBoxExt1_HideSelectionChanged(object sender, EventArgs e)
{
    Console.WriteLine(" HideSelectionChanged event is raised ");
}
```

#### VB.NET

```vb
Private Sub textBoxExt1_HideSelectionChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" HideSelectionChanged event is raised ")
End Sub
```

### MaximumSizeChanged

#### Description

This event occurs when the `MaximumSize` property is changed. The `MaximumSize` property gets / sets the maximum size of the control.

#### EventArgs

The event handler receives an argument of type `EventArgs` containing data related to this event.

---

<!-- tags: [Syncfusion Winforms, tools, EventArgs, event handling, CharacterCasingChanged, HideSelectionChanged, MaximumSizeChanged] keywords: [EventHandlers, EventArgs, Windows Forms, Syncfusion, C#, VB.NET, CharacterCasing, HideSelection, MaximumSize] -->
```