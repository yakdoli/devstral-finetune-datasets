```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_877.jpeg
document_name: tools
page_number: 877
page_id: tools#page_877
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:39:27Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Ensures compatibility and functionality of Windows Forms controls.
- Demonstrates customization and extension of controls.
- Explains event handling and property manipulation in Windows Forms.

## Content

### Custom Control Creation and Integration

The following code snippet illustrates the creation of a new custom class derived from a base control, showing how to add and manipulate `IntegerTextBox` controls in Windows Forms.

```csharp
// Constructor of the new class.
foreach (Control c in Controls)
{
    if (c is TextBox)
    {
        itb.Location = c.Location;
        itb.Size = c.Size;
        itb.Dock = c.Dock;
        itb.Anchor = c.Anchor;
        Controls.Add(itb);
        itb.BringToFront();
        itb.TextChanged += new EventHandler(itb_TextChanged);
    }
}

private void itb_TextChanged(object sender, EventArgs e)
{
    // Assigns the IntegerValue.
    Value = itb.IntegerValue;
}

public System.Drawing.Color NegativeColor
{
    get
    {
        return itb.NegativeColor;
    }
    set
    {
        itb.NegativeColor = value;
    }
}

protected override void OnValueChanged(EventArgs e)
{
    itb.Text = Value.ToString();
}
```

#### VB.NET Equivalent

The following snippet shows the equivalent implementation in VB.NET:

```vb
[VB.NET]

Class NumericupdownextDerived Inherits NumericUpDownExt
    Private itb As IntegerTextBox = New IntegerTextBox
```

### Event Handling

The `TextChanged` event ensures that any change in the `IntegerTextBox`'s content is captured and assigned to the `Value` property, providing a real-time update mechanism.

### Property Customization

The `NegativeColor` property is defined to allow customization of the negative color for the `IntegerTextBox`, enabling developers to set their desired visual style dynamically.

### Custom Behavior Override

The `OnValueChanged` method overrides the base control's behavior to update the `IntegerTextBox`'s text to reflect the new `Value`.

## API Reference

### Properties
- **NegativeColor**: Gets or sets the negative color for the `IntegerTextBox`.
  - Type: `System.Drawing.Color`
  - Description: Defines the visual representation for negative values in the `IntegerTextBox`.

### Methods
- **OnValueChanged(EventArgs e)**: Overrides the base method to update the text of the `IntegerTextBox` based on the new value.

### Events
- **TextChanged**: Triggered when the content of the `IntegerTextBox` changes, used to propagate the value change to the parent control.

## Code Examples

### C# Example

```csharp
// Example usage of the custom control
NumericupdownextDerived customControl = new NumericupdownextDerived();
customControl.NegativeColor = System.Drawing.Color.Red;
```

### VB.NET Example

```vb
Dim customControl As New NumericupdownextDerived()
customControl.NegativeColor = System.Drawing.Color.Red
```

## Cross References

See also:
- [Syncfusion WinForms Documentation](https://help.syncfusion.com/windowsforms/)
- [Custom Controls in Windows Forms](https://docs.microsoft.com/en-us/dotnet/desktop/winforms/controls/)
- [Event Handling in Windows Forms](https://docs.microsoft.com/en-us/dotnet/desktop/winforms/event-handling)

<!-- tags: [Syncfusion WinForms, Custom Controls, Event Handling, Windows Forms, Integration, API Reference, Code Example] keywords: [IntegerTextBox, NegativeColor, TextChanged, OnValueChanged, NumericUpDownExt, Customization, Overrides, Windows Forms, Control Integration, Event Handling] -->
```