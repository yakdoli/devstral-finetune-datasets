```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_730.jpeg
document_name: tools
page_number: 730
page_id: tools#page_730
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:31:22Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Configuration options for the `DoubleTextBox` control in Syncfusion Winforms.
- Details on formatting properties such as decimal digits, separators, group sizes, and negative patterns.
- Instructions to set the maximum and minimum values for the editable field in the `DoubleTextBox` control.
- Information on enabling nullable settings and specifying a null string for the control.

## Content

### DoubleTextBox Configuration
The following code snippets demonstrate how to configure the `DoubleTextBox` control in both C# and VB.NET:

#### C#
```csharp
this.doubleTextBox1.NumberDecimalDigits = 3;
this.doubleTextBox1.NumberDecimalSeparator = "-";
this.doubleTextBox1.NumberGroupSeparator = ";";
this.doubleTextBox1.NumberGroupSizes = new int[] { 4 };
this.doubleTextBox1.NumberNegativePattern = 2;
```

#### VB.NET
```vb
Me.doubleTextBox1.AllowNull = True
Me.doubleTextBox1.NullString = ""
Me.doubleTextBox1.Text = ""
Me.doubleTextBox1.NumberDecimalDigits = 3
Me.doubleTextBox1.NumberDecimalSeparator = "-"
Me.doubleTextBox1.NumberGroupSeparator = ";"
Me.doubleTextBox1.CurrencyGroupSizes = New Integer() { 3 }
Me.doubleTextBox1.NumberNegativePattern = 2
```

### DoubleTextBox Value
The maximum and minimum value of the editable field in the `DoubleTextBox` control can be specified using the following properties:

#### DoubleTextBox Properties
| Property        | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| MaxValue        | Specifies the maximum value that can be set for the `DoubleTextBox`.         |
| MinValue        | Specifies the minimum value that can be set for the `DoubleTextBox`.         |

#### C#
```csharp
this.doubleTextBox1.MaxValue = 25;
this.doubleTextBox1.MinValue = 4;
```

#### VB.NET
```vb
Me.doubleTextBox1.MaxValue = 25
Me.doubleTextBox1.MinValue = 4
```

### Banner Text Support
The `DoubleTextBox` control supports displaying banner text.

---

## Page-level Navigation/TOC (if applicable)
- [DoubleTextBox Configuration](#doubletextbox-configuration)
- [DoubleTextBox Value](#doubletextbox-value)
- [Banner Text Support](#banner-text-support)

## Cross References
See also:
- Documentation on other numeric input controls in Syncfusion.
- Additional formatting options for numeric fields in Windows Forms.

<!-- tags: [product, module, control, api, version] keywords: [Windows Forms, DoubleTextBox, numeric input, decimal separators, group sizes, negative patterns, maximum value, minimum value, banner text support] -->
```