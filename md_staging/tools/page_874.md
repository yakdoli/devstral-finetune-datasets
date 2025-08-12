```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_874.jpeg
document_name: tools
page_number: 874
page_id: tools#page_874
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:40:23Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Explains how to set up and use properties of the `NumericUpDownExt1` control in Windows Forms.
- Demonstrates Increment property configuration in both C# and VB.NET.
- Describes methods and display settings associated with the `NumericUpDownExt` control.

## Content

### Increment and Value Properties Configuration

```csharp
this.numericUpdownExt1.Increment = new decimal(new int[] { 5, 0, 0, 0 });
```

#### [VB.NET]
```vb
Me.numericUpdownExt1.Value = New Decimal(New Integer() {25, 0, 0, 0})
Me.numericUpdownExt1.Hexadecimal = True
Me.numericUpdownExt1.Minimum = New Decimal(New Integer() {50, 0, 0, 0})
Me.numericUpdownExt1.Increment = New Decimal(New Integer() {5, 0, 0, 0})
```

The methods associated with the above properties are given below.

#### Methods

| **Method**       | **Description**                                                                 |
|-------------------|---------------------------------------------------------------------------------|
| DownButton       | Decrements the value of the spin box (also known as an up-down control).         |
| UpButton         | Increments the value of the spin box (also known as an up-down control).         |

### Display Settings

#### 3.5.8.9.3.2 Display Settings

This section discusses the Display settings of the `NumericUpDownExt` control.

The `NumericUpDownExt` provides the following properties to set the display characteristics associated with the integer value.

#### `NumericUpDownExt` Properties

| **Property**         | **Description**                                                                 |
|----------------------|---------------------------------------------------------------------------------|
| DecimalPlaces       | Gets / sets the number of decimal places to display in the spin box (also known as an up-down control). |
| ThousandsSeparator   | Gets / sets a value indicating whether a thousand separator is displayed in the spin box (also known as an up-down control) when appropriate. |

#### Code Example

```csharp
this.numericUpdownExt1.DecimalPlaces = 2;
this.numericUpdownExt1.ThousandsSeparator = true;
```

### Formatting and Display

The `NumericUpDownExt` offers versatile display features to enhance the user experience. Properties like `DecimalPlaces` and `ThousandsSeparator` allow fine-tuning the numeric format for ease of readability.

---

<!-- tags: [Syncfusion, WinForms, NumericUpDownExt, DecimalPlaces, ThousandsSeparator] keywords: [numeric up-down, spin box, decimal places, thousand separator, display settings] -->
```