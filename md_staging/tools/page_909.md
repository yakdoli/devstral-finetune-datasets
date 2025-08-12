<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_909.jpeg
document_name: tools
page_number: 909
page_id: tools#page_909
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:41:48Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

The event handler receives an argument of type `EventArgs` containing data related to this event.

### Event Handler Example

#### C#

```csharp
private void textBoxExt1_BorderSidesChanged(object sender, EventArgs e)
{
    Console.WriteLine(" BorderSidesChanged event is raised ");
}
```

#### VB.NET

```vb.net
Private Sub textBoxExt1_BorderSidesChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" BorderSidesChanged event is raised ")
End Sub
```

## BorderStyleChanged

### Overview

This event occurs when the `BorderStyle` property is changed. The `BorderStyle` property indicates whether the edit control should have a border.

### Event Handler Example

#### C#

```csharp
private void textBoxExt1_BorderStyleChanged(object sender, EventArgs e)
{
    Console.WriteLine(" BorderStyleChanged event is raised ");
}
```

#### VB.NET

```vb.net
Private Sub textBoxExt1_BorderStyleChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" BorderStyleChanged event is raised ")
End Sub
```

## CharacterCasingChanged

### Overview

This event occurs when the `CharacterCasing` property is changed. The `CharacterCasing` property gets / sets the case of the characters as they are typed.

### Event Handler Example

#### C#

```csharp
private void textBoxExt1_CharacterCasingChanged(object sender, EventArgs e)
{
    Console.WriteLine(" CharacterCasingChanged event is raised ");
}
```

#### VB.NET

```vb.net
Private Sub textBoxExt1_CharacterCasingChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" CharacterCasingChanged event is raised ")
End Sub
```

<!-- tags: [syncfusion, winforms, event handling, border style, character casing, eventargs] keywords: [Windows Forms, Event Handler, BorderStyle, CharacterCasing, EventArgs, C#, VB.NET] -->