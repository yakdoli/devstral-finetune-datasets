```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_867.jpeg
document_name: tools
page_number: 867
page_id: tools#page_867
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:40:39Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
}
```

### `MultilineChanged`
This event occurs when the `Multiline` property is changed. The `Multiline` property controls whether the text of the edit control can span more than one line or not.

The event handler receives an argument of type `EventArgs` containing data related to this event.

#### Code Example (C#)

```csharp
[C#]
private void maskedEditBox1_MultilineChanged(object sender, EventArgs e)
{
    Console.WriteLine(" MultilineChanged event is raised ");
}
```

#### Code Example (VB.NET)

```vbnet
[VB.NET]
Private Sub maskedEditBox1_MultilineChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" MultilineChanged event is raised ")
End Sub
```

### `ReadOnlyChanged`
This event occurs when the `ReadOnly` property is changed. The `ReadOnly` property controls whether the text in the edit control can be changed or not.

The event handler receives an argument of type `EventArgs` containing data related to this event.

#### Code Example (C#)

```csharp
[C#]
private void maskedEditBox1_ReadOnlyChanged(object sender, EventArgs e)
{
```

```csharp
}
```

#### Code Example (VB.NET)

```vbnet
[VB.NET]
Private Sub maskedEditBox1_ReadOnlyChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" ReadOnlyChanged event is raised ")
End Sub
```

```csharp
}
```

## API Reference (if applicable)

### Methods

- `maskedEditBox1_MultilineChanged(object sender, EventArgs e)`
- `maskedEditBox1_ReadOnlyChanged(object sender, EventArgs e)`

## Code Examples (multi-language supported)

### C#

```csharp
[C#]
private void maskedEditBox1_MultilineChanged(object sender, EventArgs e)
{
    Console.WriteLine(" MultilineChanged event is raised ");
}
```

```csharp
[C#]
private void maskedEditBox1_ReadOnlyChanged(object sender, EventArgs e)
{
}
```

### VB.NET

```vbnet
[VB.NET]
Private Sub maskedEditBox1_MultilineChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" MultilineChanged event is raised ")
End Sub
```

```vbnet
[VB.NET]
Private Sub maskedEditBox1_ReadOnlyChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" ReadOnlyChanged event is raised ")
End Sub
```

<!-- tags: [syncfusion, winforms, event handling, multiline property, readonly property, eventargs] keywords: [maskededitbox, multilinechanged, readonlychanged, eventargs, windows forms, event handler, control properties] -->
``` 
