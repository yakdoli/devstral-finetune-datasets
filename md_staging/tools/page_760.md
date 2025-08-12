```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_760.jpeg
document_name: tools
page_number: 760
page_id: tools#page_760
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:32:55Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Event handlers receive arguments of type `EventArgs` containing data related to specific events.
- Demonstrates handling events like `ClipTextChanged`, `FormattedTextChanged`, and `IntegerValueChanged`.
- Includes C# and VB.NET code examples for each event.

## Content

### Handling Events

#### ClipTextChanged Event

The `ClipTextChanged` event occurs when the `ClipText` property is changed. The event handler receives an argument of type `EventArgs` containing data related to this event.

**C# Example:**
```csharp
private void integerTextBox1_ClipTextChanged(object sender, EventArgs e)
{
    Console.WriteLine("ClipTextChanged event is raised ");
}
```

**VB.NET Example:**
```vb.net
Private Sub integerTextBox1_ClipTextChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("ClipTextChanged event is raised ")
End Sub
```

#### FormattedTextChanged Event

The `FormattedTextChanged` event occurs when the `FormattedText` property is changed. The `FormattedText` property returns the formatted text with the formatting. The event handler receives an argument of type `EventArgs` containing data related to this event.

**C# Example:**
```csharp
private void integerTextBox1_FormattedTextChanged(object sender, EventArgs e)
{
    Console.WriteLine("FormattedTextChanged event is raised ");
}
```

**VB.NET Example:**
```vb.net
Private Sub integerTextBox1_FormattedTextChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("FormattedTextChanged event is raised ")
End Sub
```

#### IntegerValueChanged Event

The `IntegerValueChanged` event occurs when the `IntegerValue` property is changed. The `IntegerValue` property specifies the integer value of the text.

## API Reference
- **Namespace:** [Unclear]
- **Event:** `ClipTextChanged`, `FormattedTextChanged`, `IntegerValueChanged`
- **Parameters:** `sender` (object), `e` (EventArgs)

## Code Examples

### C# Examples
```csharp
// Handling ClipTextChanged event
private void integerTextBox1_ClipTextChanged(object sender, EventArgs e)
{
    Console.WriteLine("ClipTextChanged event is raised ");
}

// Handling FormattedTextChanged event
private void integerTextBox1_FormattedTextChanged(object sender, EventArgs e)
{
    Console.WriteLine("FormattedTextChanged event is raised ");
}
```

### VB.NET Examples
```vb.net
' Handling ClipTextChanged event
Private Sub integerTextBox1_ClipTextChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("ClipTextChanged event is raised ")
End Sub

' Handling FormattedTextChanged event
Private Sub integerTextBox1_FormattedTextChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("FormattedTextChanged event is raised ")
End Sub
```

## Page-level Navigation/TOC (if applicable)
- 3.5.8.4.4.3 ClipTextChanged
- 3.5.8.4.4.4 FormattedTextChanged
- 3.5.8.4.4.4 IntegerValueChanged

## Cross References
See also:
- [Unclear - Additional documentation on event handling in Syncfusion WinForms]

<!-- tags: [WinForms, event handling, integer value, formatted text, clip text, C#, VB.NET] keywords: [ClipTextChanged, FormattedTextChanged, IntegerValueChanged, EventArgs, event handler, event, property, integer value, formatted text, clip text, C#, VB.NET] -->
```
