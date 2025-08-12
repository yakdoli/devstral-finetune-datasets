```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_734.jpeg
document_name: tools
page_number: 734
page_id: tools#page_734
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:31:37Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### Overview

- The page discusses overriding the behavior of certain keystrokes in the DoubleTextBox control within Windows Forms.
- It illustrates how specific key functionalities can be customized, particularly focusing on handling events.
- An example is provided on enabling fixed changes using shortcut keys for incrementing and decrementing values.

### Event Handling

#### 3.5.8.3.4.1 Enabling Fixed Change using Shortcut Keys

##### Content

Sometimes there may occur situations for incrementing or decrementing the value in DoubleTextBox. In such situations, it is better to use shortcut keys. The following implementation will give you an idea on how to achieve this. Here the Up and Down keys are used for incrementing and decrementing respectively. We cannot use `'-'` because it is already reserved to enter the minus sign.

#### Code Examples

[C#]

```csharp
private void doubleTextBox1_KeyDown(object sender, KeyEventArgs e)
{
    decimal v = doubleTextBox1.DoubleValue;
    switch (e.KeyCode)
    {
        // Up and Down keys are used for incrementing and decrementing respectively.
        case Keys.Up: v++; break;
        case Keys.Down: v--; break;
    }
    doubleTextBox1.DoubleValue = v;
}
```

[VB.NET]

```vbnet
Private Sub doubleTextBox1_KeyDown(ByVal sender As Object, ByVal e As KeyEventArgs)
    ' Implementation for VB.NET would follow a similar pattern to the C# example.
End Sub
```

## API Reference

The implementation provided uses the following APIs:
- `doubleTextBox1.DoubleValue`: Gets or sets the value of the DoubleTextBox control.
- `KeyEventArgs.KeyCode`: Gets the value of the pressed keyboard key.

### Code Examples (Continued)

##### C# Implementation

The provided C# code snippet demonstrates how to handle the `KeyDown` event for the `doubleTextBox1` control. It increments the double value when the Up arrow key is pressed and decrements it when the Down arrow key is pressed.

##### VB.NET Implementation

The VB.NET implementation can be written similarly to the C# example, though it is not explicitly shown here. It would involve subscribing to the `KeyDown` event and handling the key presses accordingly.

## Cross References

- See the Syncfusion documentation for more information on customizing behavior in Windows Forms controls.

## Page-level Navigation/TOC

- [3.5.8.3.4 Event Handling]
  - [3.5.8.3.4.1 Enabling Fixed Change using Shortcut Keys]

## RAG Annotations

<!-- tags: [syncfusion, winforms, doubletextbox, event handling, shortcut keys, version: 11.4.0.26] keywords: [increment, decrement, keystroke, behavior customization, windows forms] -->
```