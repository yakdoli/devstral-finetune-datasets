```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_732.jpeg
document_name: tools
page_number: 732
page_id: tools#page_732
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:31:14Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains the behavior of the Double TextBox control, including its overflow indicators, globalization support, and handling of specific key strokes.
- Highlights the ability to make the control active even when disabled, with detailed references to related features.
- Provides a code snippet for overriding specific keystroke behavior to clear text based on a configuration property.

## Content

### Overflow Indicator
The Overflow indicator will be shown when the value of Double TextBox goes beyond the control's size. Refer to **Overflow Indicator** of Currency textbox in detail.

### Globalization
The Double TextBox class is globalization aware and uses `System.Globalization.CultureInfo` for locale-specific information. Refer to **Globalization** of Currency textbox in detail.

### Active When Disabled
We can make the control active even when it is in Disable mode. Refer to **Active When Disabled** of Currency textbox in detail.

### 3.5.8.3.3.3 Overriding the Behavior of Certain KeyStrokes in a DoubleTextBox
This section explains how to override the behavior of certain keystrokes in a DoubleTextBox. Specifically, it shows an example of how to clear the text when the NegativeSign is changed. This can be achieved by overriding the `HandleSubtractKey()` method. The code snippet below demonstrates this behavior.

#### Code Example in C#
```csharp
public class DoubleTextBoxAdv : Syncfusion.Windows.Forms.Tools.DoubleTextBox
{
    public DoubleTextBoxAdv() : base() { }
    private bool deleteonnegative = false;
    public bool DeleteOnNegative
    {
        get
        {
            return deleteonnegative;
        }
        set
        {
            deleteonnegative = value;
        }
    }

    // Overrides the behavior of SubtractKey so that the text is cleared when the NegativeSign is changed.
    protected override Syncfusion.Windows.Forms.Tools.NumberModifyState HandleSubtractKey()
    {
        if (deleteonnegative == true)
        {
            // Code to clear the text goes here
            // ...
        }
    }
}
```

## References
- **Overflow Indicator**: Detailed explanation of the overflow indicator behavior.
- **Globalization**: Locale-specific information handling in the Double TextBox.
- **Active When Disabled**: Activating controls in disabled mode.

<!-- tags: windows forms, double text box, globalization, active when disabled, overflow indicator, key stroke behavior, override methods, syncfusion winforms, v11.4.0.26 -->
```