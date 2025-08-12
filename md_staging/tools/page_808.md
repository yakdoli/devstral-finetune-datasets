```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_808.jpeg
document_name: tools
page_number: 808
page_id: tools#page_808
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:36:01Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains the configuration of the CurrencyTextBox control's number part.
- Demonstrates how to customize the formatting of the number part in the CurrencyTextBox control.

## Content

### currencyTextBox Configuration

#### Example in C#
```csharp
this.currencyTextBox1.NumberDigits = 10;
this.currencyTextBox1.CurrencyPositivePattern = 1;
this.currencyTextBox1.CurrencyNegativePattern = 2;
```

#### Example in VB.NET
```vb.net
Me.currencyTextBox1.NumberDigits = 10
Me.currencyTextBox1.CurrencyPositivePattern = 1
Me.currencyTextBox1.CurrencyNegativePattern = 2
```

### Decimal Part

#### Description
The below properties let you decide the formatting of the CurrencyTextBox control's number part.

| CurrencyTextBox Properties       | Description                                                                                                                   |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| CurrencyDecimalDigits             | Gets or sets the maximum number of digits for the decimal portion of the currency. The default value is 2.                    |
| CurrencyDecimalSeparator          | Gets or sets the decimal separator character that will be used for the display. The default decimal character `'.'` can be overridden by other special characters that can be specified by this property. |
| CurrencyGroupSeparator            | Gets or sets the separator used for grouping the digits.                                                                     |
| CurrencyGroupSizes                | Gets or sets the grouping of CurrencyDigits in the CurrencyTextBox.                                                           |
| DecimalValue                      | Specifies the decimal value of the control. Decimal values can be entered in the CurrencyTextBox by clicking inside the decimal part of the text and then typing. Alternatively, the decimal character can be entered by clicking on the decimal character on the keyboard first and the cursor will move. |
