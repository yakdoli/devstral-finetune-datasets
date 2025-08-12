```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_796.jpeg
document_name: tools
page_number: 796
page_id: tools#page_796
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:35:13Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```vb
Private Sub percentTextBox1_FormattedTextChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("FormattedTextChanged event is raised ")
End Sub
```

## 3.5.8.5.4.10 HideSelectionChanged

This event occurs when the `HideSelection` property is changed. The `HideSelection` property indicates that the selection should be hidden when the edit control loses focus.

The event handler receives an argument of type `EventArgs` containing data related to this event.

### [C#]

```csharp
private void percentTextBox1_HideSelectionChanged(object sender, EventArgs e)
{
    Console.WriteLine("HideSelectionChanged event is raised ");
}
```

### [VB.NET]

```vb
Private Sub percentTextBox1_HideSelectionChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("HideSelectionChanged event is raised ")
End Sub
```

## 3.5.8.5.4.11 MinimumSizeChanged

This event occurs when the `MinimumSize` property is changed. The `MinimumSize` property gets / sets the minimum size of the control.

The event handler receives an argument of type `EventArgs` containing data related to this event.

### [C#]

```csharp
private void percentTextBox1_MinimumSizeChanged(object sender, EventArgs e)
{
    Console.WriteLine("MinimumSizeChanged event is raised ");
}
```

## API Reference
- Namespace: Syncfusion.Windows.Forms.Tools
- Class: `PercentTextBox`
- Event: `FormattedTextChanged`
- Event: `HideSelectionChanged`
- Event: `MinimumSizeChanged`

### Parameters

| Name      | Type       | Description                                                        |
|-----------|------------|--------------------------------------------------------------------|
| `sender`  | `Object`   | The source of the event.                                           |
| `e`       | `EventArgs`| Contains event data related to the event.                          |

## Code Examples

### [C#]

```csharp
private void percentTextBox1_FormattedTextChanged(object sender, EventArgs e)
{
    Console.WriteLine("FormattedTextChanged event is raised ");
}
```

```csharp
private void percentTextBox1_HideSelectionChanged(object sender, EventArgs e)
{
    Console.WriteLine("HideSelectionChanged event is raised ");
}
```

```csharp
private void percentTextBox1_MinimumSizeChanged(object sender, EventArgs e)
{
    Console.WriteLine("MinimumSizeChanged event is raised ");
}
```

## Page-level Navigation/TOC
- [3.5.8.5.4.10 HideSelectionChanged](#3-5-8-5-4-10-hideselectionchanged)
- [3.5.8.5.4.11 MinimumSizeChanged](#3-5-8-5-4-11-minimumsizechanged)

<!-- tags: [Syncfusion Winforms, PercentTextBox, FormattedTextChanged, HideSelectionChanged, MinimumSizeChanged, EventArgs] keywords: [FormattedTextChanged, HideSelection, MinimumSize, event handler, property, data, control, event, .NET, C#, VB.NET] -->
```