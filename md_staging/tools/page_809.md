```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_809.jpeg
document_name: tools
page_number: 809
page_id: tools#page_809
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:35:22Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- 1. Overview of currency formatting options in Windows Forms.
- 2. Explanation of properties related to decimal places in currency text boxes.
- 3. Demonstration of how to specify group sizes through the `CurrencyGroupSizes` property.

## Content

### Currency Formatting Properties

| Property             | Description |
|----------------------|-------------|
| [Unclear]           | to the decimal part of the text. The decimal part is truncated based on the number of characters allowed. |
| RemoveDecimalZeros   | Specifies whether to remove last decimal zeros in the currency value. |

### Specifying GroupSize Through CurrencyGroupSizes Property

#### User Interface View

The screenshot illustrates the process of specifying group sizes through the `CurrencyGroupSizes` property in the context of a currency text box. The interface shows the properties grid and the collection editor for `Int32[] Array`.

#### Figure 512: Specifying the GroupSize Through CurrencyGroupSizes Property

![Specifying the GroupSize Through CurrencyGroupSizes Property](#)

#### Code Example in C#

```csharp
this.currencyTextBox1.CurrencyDecimalDigits = 3;
this.currencyTextBox1.CurrencyDecimalSeparator = ".";
this.currencyTextBox1.CurrencyGroupSeparator = ",";
this.currencyTextBox1.CurrencyGroupSizes = new int[] {3};
this.currencyTextBox1.RemoveDecimalZeros = true;
```

### Explanation

The code snippet demonstrates how to configure a currency text box (`currencyTextBox1`) to specify the number of decimal places, the decimal and group separators, and the group sizes. Additionally, it shows how to remove trailing zeros from the decimal part of the currency value.

## API Reference

### Properties

#### CurrencyDecimalDigits
- **Type**: int
- **Description**: Specifies the number of decimal places displayed in the currency value.

#### CurrencyDecimalSeparator
- **Type**: string
- **Description**: Specifies the character used to separate the integer and decimal parts of the currency value.

#### CurrencyGroupSeparator
- **Type**: string
- **Description**: Specifies the character used to separate groups of digits in the currency value.

#### CurrencyGroupSizes
- **Type**: int[]
- **Description**: Specifies the sizes of the groups of digits in the currency value.

#### RemoveDecimalZeros
- **Type**: bool
- **Description**: Specifies whether to remove trailing zeros from the decimal part of the currency value.

### Methods
<!-- Additional methods related to currency formatting can be described here. -->

### Events
<!-- Events related to currency formatting changes can be described here. -->

## Code Examples

#### Example: Configuring Currency Formatting

```csharp
// Example of configuring a currency text box
this.currencyTextBox1.CurrencyDecimalDigits = 3;
this.currencyTextBox1.CurrencyDecimalSeparator = ".";
this.currencyTextBox1.CurrencyGroupSeparator = ",";
this.currencyTextBox1.CurrencyGroupSizes = new int[] {3};
this.currencyTextBox1.RemoveDecimalZeros = true;
```

### Additional Notes
- The `CurrencyGroupSizes` property allows fine-tuning of the grouping behavior, enhancing the readability of large currency values.
- The `RemoveDecimalZeros` property ensures cleaner display by stripping unnecessary trailing zeros.

## Related Topics

- See also: `CurrencyFormatter` for more advanced currency formatting options.
- Refer to the `CurrencyGroupSizes` property documentation for detailed examples.

---

<!-- tags: [product, module, control, api, version?] keywords: [currency formatting, decimal places, group sizes, trailing zeros, Windows Forms, Syncfusion Windows Forms] -->
```