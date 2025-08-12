```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_729.jpeg
document_name: tools
page_number: 729
page_id: tools#page_729
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:29:52Z
fidelity: lossless
--> 

## Overview

- The page describes the creation and customization of `DoubleTextBox` controls in Syncfusion Windows Forms.
- It highlights key properties and features of `DoubleTextBox` and other numeric input controls such as `IntegerTextBox`, `PercentTextBox`, and `CurrencyTextBox`.
- The example demonstrates programmatically creating and adding a `DoubleTextBox` to a control.

## Content

### Creating a DoubleTextBox Programmatically

The following code example shows how to create and add a `DoubleTextBox` control:

```csharp
Me.doubleTextBox1 = New Syncfusion.Windows.Forms.Tools.DoubleTextBox()
Me.Controls.Add(Me.doubleTextBox1)
```

#### Figure 460: DoubleTextBox Created Programmatically
![Figure 460: DoubleTextBox Created Programmatically](https://i.imgur.com/460.png)

### Concepts and Features

**3.5.8.3.3 Concepts and Features**

The following Editors controls (DoubleTextBox, IntegerTextBox, PercentTextBox, and CurrencyTextBox) have been revamped. Click [here](#) to see the details of revamping.

#### 3.5.8.3.3.1 Number Settings

The below table lists the properties illustrating the number settings for the `DoubleTextBox`.

| Double TextBox Properties          | Description                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------|
| DoubleValue                         | Specifies the double value of the control.                                 |
| NumberDecimalDigits                 | Gets or sets the maximum number of digits for the decimal portion of the number. |
| NumberDecimalSeparator               | Gets or sets the decimal separator character that will be used for the display. The default decimal character `'.'` can be overridden by other special characters using this property. |
| NumberGroupSeparator               | Gets or sets the separator used for grouping the digits.                     |
| NumberGroupSizes                   | Gets or sets the grouping of `NumberDigits` in the `DoubleTextBox`.            |
| NumberNegativePattern               | Gets or sets the pattern to use when the value is negative.                  |

### C#

<!-- [C#] -->

## API Reference

### Properties

- **DoubleValue**: Specifies the double value of the control.
- **NumberDecimalDigits**: Gets or sets the maximum number of digits for the decimal portion of the number.
- **NumberDecimalSeparator**: Gets or sets the decimal separator character used for the display.
- **NumberGroupSeparator**: Gets or sets the separator used for grouping the digits.
- **NumberGroupSizes**: Gets or sets the grouping of `NumberDigits` in the `DoubleTextBox`.
- **NumberNegativePattern**: Gets or sets the pattern to use when the value is negative.

## Code Examples

### Example: Using `DoubleTextBox`

```csharp
Me.doubleTextBox1 = New Syncfusion.Windows.Forms.Tools.DoubleTextBox()
Me.Controls.Add(Me.doubleTextBox1)

' Setting properties
Me.doubleTextBox1.NumberDecimalDigits = 2
Me.doubleTextBox1.NumberDecimalSeparator = ','
Me.doubleTextBox1.NumberGroupSeparator = ' '
Me.doubleTextBox1.NumberNegativePattern = "6"
```

## Summary

This page provides comprehensive details on using the `DoubleTextBox` control in Syncfusion Windows Forms, including how to create it programmatically and configure its number settings. Additionally, it briefly introduces recent updates to other numeric editor controls.

<!-- tags: [Syncfusion, WinForms, DoubleTextBox, NumberEditing, NumericControls, C#] keywords: [DoubleTextBox, NumberDecimalDigits, NumberDecimalSeparator, NumberGroupSeparator, NumberNegativePattern] -->
```