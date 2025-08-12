```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_742.jpeg
document_name: tools
page_number: 742
page_id: tools#page_742
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:32:08Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

Me. integerTextBox1. IntegerValue = (CLng (777))  
Me. integerTextBox1. DefaultValue = 0  
Me. integerTextBox1. BindableValue = 777  

*Figure 468: Integer Value Set*

## Null Value Settings

There are various settings that can be applied to the IntegerTextBox control when the value of the control is set to 'Null'. These settings are illustrated below.

| IntegerTextBox Properties       | Description                                                |
|---------------------------------|------------------------------------------------------------|
| NullString                      | Specifies the string to be displayed when the DecimalValue is Null. |
| NullFormat                      | Returns the NumberFormatInfo object for the null display. |
| IsNull                          | Specifies the Null State of the Control.                  |
| AllowNull                       | Specifies whether the control can be Nulled, Null String will be set when the control becomes null. |

### Code Examples

#### C#

```csharp
this. integerTextBox1. NullString = "Null Value";  
this. integerTextBox1. AllowNull = true;
```

#### VB.NET

```vb
Me. integerTextBox1. NullString = "Null Value"  
Me. integerTextBox1. AllowNull = True
```

*Figure 469: Null String Set*

## Footer Information
- Copyright: © 2013 Syncfusion. All rights reserved.
- Page Number: 742

<!-- tags: [Syncfusion Winforms, IntegerTextBox, Null Value Settings] keywords: [integer textbox, null settings, C#, VB.NET, decimal value, numberformatinfo, null state] -->
```