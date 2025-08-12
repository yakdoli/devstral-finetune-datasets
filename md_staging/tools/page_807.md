```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_807.jpeg
document_name: tools
page_number: 807
page_id: tools#page_807
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:37:10Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

We need to do the below settings to make Banner text feature available for the control.

```csharp
this.currencyTextBox1.AllowNull = true;
this.currencyTextBox1.NullString = "";
this.currencyTextBox1.Text = "";
```

```vbnet
Me.currencyTextBox1.AllowNull = True
Me.currencyTextBox1.NullString = ""
Me.currencyTextBox1.Text = ""
```

![Banner Text set for CurrencyTextBox](https://raw.githubusercontent.com/syncfusion/user-guide/assets/tools/page_807/Banner%20Text%20set%20for%20CurrencyTextBox.png)

Figure 511: Banner Text set for CurrencyTextBox

## 3.5.8.6.4.2 Number and Decimal Digits

The CurrencyTextBox text field has a number part and a decimal part. The properties which control the appearance and behavior of the text field are discussed in this section.

### Number part

The below properties let you decide the formatting of the number part of the CurrencyTextBox control.

| CurrencyTextBox Properties          | Description                                                                                                                             |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| CurrencyNumberDigits                | Specifies the number of digits for the number part. This is not part of the globalization structure. The default value is 27. |
| CurrencyPositivePattern             | This property specifies the pattern to use when the value is positive.                                                                |
| CurrencyNegativePattern             | This property specifies the pattern to use when the value is negative. For example, set CurrencyNegativePattern to be 2 or 3 and then hit -ve symbol, you will know the change of |

## Cross References

See also:
- CurrencyTextBox Properties
- Globalization Structure

<!-- tags: [windows forms, currencytextbox, banner text, number part, decimal digits] keywords: [currencytextbox, banner text, number part, decimal digits, formatting, globalization] -->
```