```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_811.jpeg
document_name: tools
page_number: 811
page_id: tools#page_811
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:37:22Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Maximum and Minimum Values for Currency

The maximum and minimum value of the currency can be specified by MaxValue and MinValue properties.

#### CurrencyTextBox Properties

| **Property**                          | **Description**                                                                                   |
|---------------------------------------|---------------------------------------------------------------------------------------------------|
| **MaxValue**                          | It sets the maximum value to the currency TextBox. The default value is 79228162514264337593543950335. |
| **MinValue**                          | It sets the minimum value to the currency TextBox. The default value is 79228162514264337593543950335. |
| **EnforceMinMaxDuringValidating**    | If the minimum and maximum values are not met, the validating event will be handled and cancelled if this property is set to true. |

#### Code Examples

**C#**

```csharp
this.currencyTextBox1.MaxValue = 10;
this.currencyTextBox1.MinValue = 0;
this.currencyTextBox1.EnforceMinMaxDuringValidating = true;
```

**VB.NET**

```vb
Me.currencyTextBox1.MaxValue = 10
Me.currencyTextBox1.MinValue = 0
Me.currencyTextBox1.EnforceMinMaxDuringValidating = True
```

### Null String

If you want to display a null string instead of actual `decimal` values, you can set the `NullString` property to any value. To display the null string, set the `AllowNull` property to `true`.

#### Properties

| **CurrencyTextBox Properties** | **Description**                                                                                   |
|---------------------------------|---------------------------------------------------------------------------------------------------|
| **NullString**                  | Sets the Null string to be displayed when the decimal value is zero.                           |
| **AllowNull**                   | Specifies if the `NullString` will be used when the value is `Null`. `NullString` must be set to `true`. |
```


<!-- tags: [syncfusion, winforms, currencytextbox, maxvalue, minvalue, nullstring, allownull] keywords: [currency textbox, maximum value, minimum value, validating event, null string, decimal, c#, vb.net] -->
```