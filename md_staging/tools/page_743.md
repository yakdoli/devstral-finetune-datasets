```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_743.jpeg
document_name: tools
page_number: 743
page_id: tools#page_743
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:32:48Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Min and Max Value Settings

The minimum and maximum values of the IntegerTextBox can be set using the below given properties.

| IntegerTextBox Properties | Description |
| --- | --- |
| MaxValue | Gets / sets the maximum value that can be set through the IntegerTextBox. The default value is set to '9223372036854775807'. |
| MinValue | Gets / sets the minimum value that can be set through the IntegerTextBox. The default value is set to '-9223372036854775808'. |

#### Code Examples

**[C\#]**

```csharp
this.integerTextBox1.MaxValue = 9223372036854775807;
this.integerTextBox1.MinValue = -9223372036854775808;
```

**[VB.NET]**

```vb
Me.integerTextBox1.MaxValue = 9223372036854775807
Me.integerTextBox1.MinValue = -9223372036854775808
```

### 3.5.8.4.3.2 Culture Settings

This section discusses the culture settings of the IntegerTextBox control.

| IntegerTextBox Properties | Description |
| --- | --- |
| Culture | Gets / sets the culture that is to be used for formatting the numeric display. |
| CurrentCultureRefresh | Indicates whether the Culture property is to be refreshed when the culture changes. |
| SpecialCultureValue | Gets / sets the mode for the cultures. <br><br> It includes the below given options. <br><br> None, |

<!-- tags: [Syncfusion, Winforms, IntegerTextBox, MinValue, MaxValue, Culture, CurrentCultureRefresh, SpecialCultureValue] keywords: [maximum value, minimum value, default value, numeric display, culture settings, IntegerTextBox control] -->
```