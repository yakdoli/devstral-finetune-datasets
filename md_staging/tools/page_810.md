```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_810.jpeg
document_name: tools
page_number: 810
page_id: tools#page_810
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:36:08Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Configuring currency formatting in a textbox.
- Handling negative input pending selection in a textbox.

## Content

### Currency Formatting

#### Code Example: VB.NET
```vb
Me.currencyTextBox1.CurrencyDecimalDigits = 3
Me.currencyTextBox1.CurrencyDecimalSeparator = "."
Me.currencyTextBox1.CurrencyGroupSeparator = ","
Me.currencyTextBox1.CurrencyGroupSizes = New Integer() {3}
Me.currencyTextBox1.RemoveDecimalZeros = True
```

**Figure 513: CurrencyDecimalDigits = "3"; Separator = "."; GroupSeparator = ","; GroupSizes = "3"**
![Currency Format Image](https://example.com/figure513.png)
**Figure 514: RemoveDecimalZeros = "True"**
![Remove Decimal Zeros Image](https://example.com/figure514.png)

### Negative Part

**3.5.8.6.4.3**

The default negative sign `'-'` can be changed by the `NegativeSign` property to any other special characters. The behavior of the Currency TextBox can be customized using the `NegativeInputPendingOnSelectAll` property when its content is fully selected and the negative key is pressed by the user.

- **When `NegativeInputPendingOnSelectAll` is set to `True`:**
  - The current value is not changed when the negative key is pressed.
  - The next key stroke is taken to a new value, and the entire content of the TextBox is replaced by the negative value of the key stroke entered.

**Example:**
- If the current value of the TextBox is `1.00` with all the text being selected, and the user presses the negative key followed by key `5`, the value will be `-5.00`.

- **When `NegativeInputPendingOnSelectAll` is set to `false`:**
  - The current value is changed to the negative value immediately.
  - If the current value of the TextBox is `1.00` with all the text being selected, and the user presses the negative key, the value is `-1.00`.

### Configuring Negative Input

#### Code Example: C#
```csharp
this.currencyTextBox1.NegativeSign = "-";
this.currencyTextBox1.NegativeInputPendingOnSelectAll = true;
```

#### Code Example: VB.NET
```vb
Me.currencyTextBox1.NegativeSign = "-"
Me.currencyTextBox1.NegativeInputPendingOnSelectAll = True
```

## API Reference (if applicable)

To be completed based on the provided content.

## Code Examples (multi-language supported)

To be completed based on the provided content.

## Pages Navigation/TOC (if applicable)

To be completed based on the provided content.

## Cross References

To be completed based on the provided content.

<!-- tags: [Syncfusion Winforms, currency formatting, negative sign, negative input pending selection] keywords: [currencyTextBox, NegativeInputPendingOnSelectAll, NegativeSign, CurrencyDecimalDigits, CurrencyDecimalSeparator, CurrencyGroupSeparator, CurrencyGroupSizes, RemoveDecimalZeros] -->
```