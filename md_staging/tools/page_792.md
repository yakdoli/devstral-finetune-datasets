```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_792.jpeg
document_name: tools
page_number: 792
page_id: tools#page_792
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:34:55Z
fidelity: lossless
-->

## Overview
- This section describes the `BindableValueChanged` and `Border3DStyleChanged` events in the Syncfusion WinForms control, showcasing how to handle these events with examples in C# and VB.NET.
- These events are triggered when the `BindableValue` and `Border3DStyle` properties are changed, respectively, and demonstrate how to implement event handlers for these events.

## Content

### 3.5.8.5.4.2 BindableValueChanged

This event occurs when the `BindableValue` property is changed. The `BindableValue` property is a wrapper property that indicates the value. This property can be used to set the value of the control to 'Null'.

- **Description**: 
  - The `BindableValueChanged` event is triggered when the `BindableValue` property of a control is modified.
  - The event handler receives an argument of type `EventArgs` containing data related to this event.

#### Usage Examples

##### C#

```csharp
[C#]

private void percentTextBox1_BindableValueChanged(object sender, EventArgs e)
{
    Console.WriteLine("BindableValueChanged event is raised ");
}
```

##### VB.NET

```vb
[VB.NET]

Private Sub percentTextBox1_BindableValueChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("BindableValueChanged event is raised ")
End Sub
```

### 3.5.8.5.4.3 Border3DStyleChanged

This event occurs when the `Border3DStyle` property is changed. The `Border3DStyle` property indicates the style of the 3D border.

- **Description**: 
  - The `Border3DStyleChanged` event is triggered when the `Border3DStyle` property of a control is modified.
  - The event handler receives an argument of type `EventArgs` containing data related to this event.

#### Usage Examples

##### C#

```csharp
[C#]

private void percentTextBox1_Border3DStyleChanged(object sender, EventArgs e)
{
    Console.WriteLine("Border3DStyleChanged event is raised ");
}
```

##### VB.NET

```vb
[VB.NET]

Private Sub percentTextBox1_Border3DStyleChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("Border3DStyleChanged event is raised ")
End Sub
```

## API Reference

### Events

#### `BindableValueChanged` Event

- **Type**: Event
- **Triggered When**: The `BindableValue` property is changed.
- **Event Arguments**: `EventArgs`

#### `Border3DStyleChanged` Event

- **Type**: Event
- **Triggered When**: The `Border3DStyle` property is changed.
- **Event Arguments**: `EventArgs`

## Code Examples

The examples provided demonstrate how to handle the `BindableValueChanged` and `Border3DStyleChanged` events in both C# and VB.NET.

### Links and References

- **Related Events**: Explore other events related to property changes for a comprehensive understanding of the control's behavior.
- **Documentation**: Refer to the full documentation for additional details on `BindableValue` and `Border3DStyle` properties.

<!-- tags: [Syncfusion Winforms, BindableValue, Border3DStyle, Events, C#, VB.NET, 11.4.0.26] keywords: [BindableValueChanged, Border3DStyleChanged, Event handling, Syncfusion, Windows Forms, property change] -->
```