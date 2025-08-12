```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_793.jpeg
document_name: tools
page_number: 793
page_id: tools#page_793
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:34:16Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### BorderColorChanged

#### Overview

- This section describes the `BorderColorChanged` event, which occurs when the `BorderColor` property is changed.
- The `BorderColor` property indicates the color of the 2D border.

#### Content

**Event Details:**

- The `BorderColorChanged` event is triggered when the `BorderColor` property is modified.
- The `BorderColor` property specifies the border color of the 2D border.

**Event Handler:**

- The event handler receives an argument of type `EventArgs`, which contains data related to the event.

**Example Code:**

```csharp
[C#]
private void percentTextBox1_BorderColorChanged(object sender, EventArgs e)
{
    Console.WriteLine("BorderColorChanged event is raised ");
}
```

```vb.net
[VB.NET]
Private Sub percentTextBox1_BorderColorChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("BorderColorChanged event is raised ")
End Sub
```

### BorderSidesChanged

#### Overview

- This section describes the `BorderSidesChanged` event, which occurs when the `BorderSides` property is changed.
- The `BorderSides` property indicates the border sides of the panel.

#### Content

**Event Details:**

- The `BorderSidesChanged` event is triggered when the `BorderSides` property is modified.
- The `BorderSides` property specifies the border sides of the panel.

**Event Handler:**

- The event handler receives an argument of type `EventArgs`, which contains data related to the event.

**Example Code:**

```csharp
[C#]
private void percentTextBox1_BorderSidesChanged(object sender, EventArgs e)
{
    Console.WriteLine("BorderSidesChanged event is raised ");
}
```

```vb.net
[VB.NET]
Private Sub percentTextBox1_BorderSidesChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("BorderSidesChanged event is raised ")
End Sub
```

---

### Conclusion

- Both `BorderColorChanged` and `BorderSidesChanged` events are crucial for handling changes in the visual properties of panels or other controls in Windows Forms applications.
- These events allow developers to react to changes in border properties dynamically, enhancing the interactivity and responsiveness of the user interface.

---

## API Reference

### Events

- **BorderColorChanged**: Triggered when the `BorderColor` property is changed.
- **BorderSidesChanged**: Triggered when the `BorderSides` property is changed.

### Parameters

- **sender**: The object that raises the event.
- **e**: `EventArgs` containing data related to the event.

## Code Examples

### C#

```csharp
[C#]
private void percentTextBox1_BorderColorChanged(object sender, EventArgs e)
{
    Console.WriteLine("BorderColorChanged event is raised ");
}

[C#]
private void percentTextBox1_BorderSidesChanged(object sender, EventArgs e)
{
    Console.WriteLine("BorderSidesChanged event is raised ");
}
```

### VB.NET

```vb.net
[VB.NET]
Private Sub percentTextBox1_BorderColorChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("BorderColorChanged event is raised ")
End Sub

[VB.NET]
Private Sub percentTextBox1_BorderSidesChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("BorderSidesChanged event is raised ")
End Sub
```

---

<!-- tags: [Syncfusion, Windows Forms, BorderColor, BorderSides, Border, Event, Property] keywords: [BorderColorChanged, BorderSidesChanged, EventArgs, Panel, 2D border, Border properties, Interactivity, Event handling, Windows Forms, C#, VB.NET] -->
```