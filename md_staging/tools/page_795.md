```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_795.jpeg
document_name: tools
page_number: 795
page_id: tools#page_795
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:36:24Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### 3.5.8.5.4.8 DoubleValueChanged

This event occurs when the `DoubleValue` property is changed. The `DoubleValue` property specifies the double value of the `PercentTextBox` control.

The event handler receives an argument of type `EventArgs` containing data related to this event.

#### Code: DoubleValueChanged

```csharp
[C#]
private void percentTextBox1_FormattedTextChanged(object sender, EventArgs e)
{
    Console.WriteLine(" DoubleValueChanged event is raised ");
}
```

```vbnet
[VB.NET]
Private Sub percentTextBox1_FormattedTextChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" DoubleValueChanged event is raised ")
End Sub
```

### 3.5.8.5.4.9 FormattedTextChanged

This event occurs when the `FormattedText` property is changed. The `FormattedText` property returns the formatted text with the formatting.

The event handler receives an argument of type `EventArgs` containing data related to this event.

#### Code: FormattedTextChanged

```csharp
[C#]
private void percentTextBox1_FormattedTextChanged(object sender, EventArgs e)
{
    Console.WriteLine(" FormattedTextChanged event is raised ");
}
```

```vbnet
[VB.NET]
Private Sub percentTextBox1_FormattedTextChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" FormattedTextChanged event is raised ")
End Sub
```

## API Reference

The document provides event handlers for `DoubleValueChanged` and `FormattedTextChanged` in both C# and VB.NET. These handlers are triggered when the respective properties are changed on a `PercentTextBox` control.

## Code Examples

### C#

```csharp
[C#]
private void percentTextBox1_FormattedTextChanged(object sender, EventArgs e)
{
    Console.WriteLine(" FormattedTextChanged event is raised ");
}
```

### VB.NET

```vbnet
[VB.NET]
Private Sub percentTextBox1_FormattedTextChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" FormattedTextChanged event is raised ")
End Sub
```

<!-- tags: [Syncfusion, WinForms, PercentTextBox, event handlers, EventArgs] keywords: [DoubleValueChanged, FormattedTextChanged, C#, VB.NET, event, handler, PercentTextBox, property change] -->
```