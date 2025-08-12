```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_713.jpeg
document_name: tools
page_number: 713
page_id: tools#page_713
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:28:57Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains how to configure text settings in the CurrencyEdit control.
- Lists the properties that control the behavior of text in the CurrencyEdit control.
- Provides examples in both C# and VB.NET for setting these properties.

## Content

### Text Settings
The below properties will let you control the behavior of the text in the CurrencyEdit control.

| CurrencyEdit Properties           | Description                                                                                     |
|------------------------------------|-------------------------------------------------------------------------------------------------|
| **ShowTextBox**                   | Indicates whether to show the textbox or not.                                                 |
| **Text**                          | Specifies the text of the embedded control.                                                    |
| **TextBox**                       | Specifies the properties for customizing the embedded textbox.                                |
| **TextAlign**                     | Specifies the alignment of the text in the control.                                           |
| **TransferFromCalculator**        | Specifies whether to transfer the calculated value to the edit control.                        |
| **TransferToCalculator**          | Specifies whether to transfer the calculated value from the edit control.                      |
| **DecimalValue**                  | Specifies the decimal value of the currency control.                                          |

### Example: Setting CurrencyEdit Properties in C#

```csharp
this.currencyEdit1.ShowTextBox = true;
this.currencyEdit1.Text = "$400.00";
this.currencyEdit1.TextAlign = HorizontalAlignment.Right;
this.currencyEdit1.TransferFromCalculator = true;
this.currencyEdit1.TransferToCalculator = false;
this.currencyEdit1.TextBox.DecimalValue = new decimal(new int[] { 40000, 0, 0, 131072 });
```

### Example: Setting CurrencyEdit Properties in VB.NET

```vb
Me.currencyEdit1.ShowTextBox = True
Me.currencyEdit1.Text = "$400.00"
Me.currencyEdit1.TextAlign = HorizontalAlignment.Right
Me.currencyEdit1.TransferFromCalculator = True
Me.currencyEdit1.TransferToCalculator = False
Me.currencyEdit1.TextBox.DecimalValue = New Decimal(New Integer() { 40000, 0, 0, 131072 })
```

## RAG Annotations
<!-- tags: [CurrencyEdit, TextSettings, TextAlignment, DecimalValue, WindowsForms, SyncfusionSDK, C#, VB.NET] keywords: [currencyedit, text alignment, decimal value, windows forms, essential tools] -->
``` 
