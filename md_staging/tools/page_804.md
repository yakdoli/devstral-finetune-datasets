```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_804.jpeg
document_name: tools
page_number: 804
page_id: tools#page_804
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:35:45Z
fidelity: lossless
-->


## Essential Tools for Windows Forms

### Overview
- Introduction to the CurrencyTextBox control.
- Features of the CurrencyTextBox, including text alignment and multiline settings.
- Explains the properties and methods used to customize and interact with the CurrencyTextBox control.

### Content

#### Overview of CurrencyTextBox

The figure below illustrates the components of a typical text field in a CurrencyTextBox:

![Figure 505: TextField of CurrencyTextBox](attachment:Figure_505)

#### Text Property

##### **3.5.8.6.4.1 Text**

The default text in the CurrencyTextBox can be edited through the `Text` property. The default value is `$2.00`. The text can be aligned to Left, Right, or Center using the `TextAlign` property.

```csharp
this.currencyTextBox2.Text = "$25.00";
this.currencyTextBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
```

```vbnet
Me.currencyTextBox2.Text = "$25.00"
Me.currencyTextBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
```

**Figure 506: Text = "$25.00"**

#### Multiline Feature

The CurrencyTextBox control can be made multiline by setting the `Multiline` property to `true`. Using the below properties, we can control the behavior of the control.

**Multiline Feature**

- The CurrencyTextBox control can be made multiline by setting the `Multiline` property to `true`.
- The `Lines` property can hold an array of string values.

| CurrencyTextBox Properties | Description |
|-----------------------------|-------------|
| Lines                      | This property can hold an array of string values. |

### API Reference

#### CurrencyTextBox Properties

- **Lines**: This property can hold an array of string values for multiline text.

### Code Examples

#### C#

```csharp
this.currencyTextBox2.Text = "$25.00";
this.currencyTextBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
```

#### VB.NET

```vbnet
Me.currencyTextBox2.Text = "$25.00"
Me.currencyTextBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Right
```

## Page-level Navigation/TOC (if applicable)
- [Multiline Feature](#multiline-feature)
- [API Reference](#api-reference)

## Cross References
- Refer to the main documentation for more details on the CurrencyTextBox control.

<!-- tags: [syncfusion, windows forms, text properties, multiline textbox, text alignment, currencytextbox] keywords: [currencytextbox, text property, multiline feature, horizontalalignment, multiline, lines property] -->
```