```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_727.jpeg
document_name: tools
page_number: 727
page_id: tools#page_727
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:31:49Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains how to programmatically browse through values in a DomainUpDownExt control.
- Introduces the DoubleTextBox control, which derives from Windows Forms framework text box control.

## Content

### 3.5.8.2.5.2 How to programmatically browse through values in a DomainUpDownExt control
We can programmatically browse through the previous and the next values, of the current value, by calling `UpButton()` and `DownButton()` methods.

```csharp
// Goes to the previous value.
this.domainUpDownExt1.UpButton();
// Goes to the Next value.
this.domainUpDownExt1.DownButton();
```

```vb.net
' Goes to the previous value.
Me.domainUpDownExt1.UpButton()
' Goes to the Next value.
Me.domainUpDownExt1.DownButton()
```

### 3.5.8.3 DoubleTextBox

#### Overview
- The `DoubleTextBox` is a text box-derived control that can display double data type values.
- Derived from Windows Forms framework text box control.
- Supports display and collection of double values.
- Handles user keyboard input and double formatting.
- Uses the globalization features of the .NET platform for locale-specific formatting.

![Figure 458: DoubleTextBox](https://imagetobestored.com/1e3f7.png)

#### 3.5.8.3.1 Features
- **Purpose:** Used to display and collect double values.
- **Handling Keyboard Input and Formatting:** Handles user keyboard input and double formatting with no code required.
- **Compatibility and Localization:** Fully compatible with the Windows Forms Text Box and uses the globalization features of the .NET platform for locale-specific formatting.
- **Precision Support:** Supports values with a precision of 15 characters.
- **Negative Value Display:** Supports displaying negative values in a different color and using different negative formats.

### Code Examples
C# and VB.NET examples are provided to demonstrate the usage of `DoubleTextBox`.

## Page-level Navigation/TOC (if applicable)
- 3.5.8.2.5.2 How to programmatically browse through values in a DomainUpDownExt control
- 3.5.8.3 DoubleTextBox
  - 3.5.8.3.1 Features

### Cross References
- See also: related controls and features in the documentation.

<!-- tags: [syncfusion, winforms, doubles, text box, globalization, formatting, domainupdownext, doubletextbox] keywords: [domainUpDownExt, DoubleTextBox, C#, VB.NET, keyboard input, double formatting, globalization, localization, precision, negative values] -->
```