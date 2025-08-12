```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_834.jpeg
document_name: tools
page_number: 834
page_id: tools#page_834
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:37:43Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

The value settings provide options to set the value to be displayed by the IntegerTextBox control. It provides options to indicate the null state of the control and customize its settings.

The maximum and minimum value of the control can also be set.

## Culture Settings

The `culture` to be used for formatting the numeric display can be set using the Culture property.

## Text Settings

Text can be selected, formatted, clipped and displayed from right to left using the text settings of the IntegerTextBox control.

## Appearance Settings

The background color and foreground color of the control can be set according to the needs of the user.

The foreground color can be set separately for the positive, negative and null values of the control.

## Behavior Settings

The integer value of the control can be reset or changed to a negative value by selecting its entire contents and pressing the negative key on the keyboard.

The control also allows to insert zeros before the beginning value of the integer value using the AllowLeadingZeros property.

## Border Settings

2D and 3D border styles can be applied to the IntegerTextBox.

The color of the border can also be set for the control using the BorderColor property.

## Key Settings

Keyboard support for entering large values is provided. Incrementing and decrementing of values can be done using the up and down arrow keys.

## API Reference

This section provides references to the methods, properties, and events associated with the IntegerTextBox control.

### Properties
- **Culture**: Specifies the culture used for formatting the numeric display.
- **AllowLeadingZeros**: Allows the insertion of zeros before the beginning value of the integer value.

### Methods
- **Increment()**: Increases the current value by a specified increment.
- **Decrement()**: Decreases the current value by a specified decrement.

### Events
- **ValueChanged**: Triggered when the value of the control changes.

## Code Examples

Here are examples of setting the Culture and using the Keyboard support:

```csharp
// Setting Culture
IntegerTextBox textBox = new IntegerTextBox();
textBox.Culture = System.Globalization.CultureInfo.GetCultureInfo("en-US");

// Using Keyboard support
textBox.Increment();
textBox.Decrement();
```

<!-- tags: [syncfusion, winforms, integertextbox, control, userinterface] keywords: [integertextbox, culture, textsettings, appearance, behavior, bordersettings, keysettings, keyboard] -->
```