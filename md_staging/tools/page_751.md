```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_751.jpeg
document_name: tools
page_number: 751
page_id: tools#page_751
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:33:19Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains how to configure foreground colors based on value conditions.
- Demonstrates setting positive, negative, and zero colors for a control.
- Provides code examples for both C# and VB.NET.

## Content

### Foreground Color Properties

The following table describes the properties used to set foreground colors based on value conditions:

| Property        | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| PositiveColor   | Gets / sets the forecolor when the current value is positive.               |
| NegativeColor   | Gets / sets the forecolor when the current value is negative. The default value is set to 'Red'. |
| ZeroColor       | Gets / sets the forecolor when the current value is zero.                  |

#### Example Code

##### C#

```csharp
this.integerTextBox1.PositiveColor = System.Drawing.Color.DarkOrange;
this.integerTextBox1.NegativeColor = System.Drawing.Color.SteelBlue;
this.integerTextBox1.ZeroColor = System.Drawing.Color.OliveDrab;
```

##### VB.NET

```vb
Me.integerTextBox1.PositiveColor = System.Drawing.Color.DarkOrange
Me.integerTextBox1.NegativeColor = System.Drawing.Color.SteelBlue
Me.integerTextBox1.ZeroColor = System.Drawing.Color.OliveDrab
```

### Foreground Settings of IntegerTextBox

The following figure illustrates the application of the above settings:

![Background: Foreground Settings of IntegerTextBox](image_of_integerTextBox_with_colors.png)

**Figure 477: Foreground Settings of IntegerTextBox**

### Methods

The methods associated with the above properties are given below:

| Methods               | Description                           |
|-----------------------|---------------------------------------|
| ResetForeColor        | Resets the forecolor of the control to its default value. |
| ResetPositiveColor    | Resets the `PositiveColor` property to its default value. |

---

## API Reference

### Properties

- **PositiveColor**: Gets or sets the foreground color when the current value is positive.
- **NegativeColor**: Gets or sets the foreground color when the current value is negative. Default value is `Red`.
- **ZeroColor**: Gets or sets the foreground color when the current value is zero.

### Methods

- **ResetForeColor**: Resets the foreground color of the control to its default value.
- **ResetPositiveColor**: Resets the `PositiveColor` property to its default value.

## Code Examples

### Setting Colors in C#

```csharp
this.integerTextBox1.PositiveColor = System.Drawing.Color.DarkOrange;
this.integerTextBox1.NegativeColor = System.Drawing.Color.SteelBlue;
this.integerTextBox1.ZeroColor = System.Drawing.Color.OliveDrab;
```

### Setting Colors in VB.NET

```vb
Me.integerTextBox1.PositiveColor = System.Drawing.Color.DarkOrange
Me.integerTextBox1.NegativeColor = System.Drawing.Color.SteelBlue
Me.integerTextBox1.ZeroColor = System.Drawing.Color.OliveDrab
```

## RAG Annotations

<!-- tags: [Syncfusion, WinForms, IntegerTextBox, Foreground Color, Properties, Methods, Example Code] keywords: [PositiveColor, NegativeColor, ZeroColor, ResetForeColor, ResetPositiveColor] -->
```