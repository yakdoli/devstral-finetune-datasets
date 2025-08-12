```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_842.jpeg
document_name: tools
page_number: 842
page_id: tools#page_842
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:38:11Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

The first group will contain the value for the first 3 ### characters of the mask (the number group) and the second group (the decimal group) will contain the 5 characters (.#.##). The default group alignment for the number group will be right and the alignment for the decimal group will be left. Refer to the information on **DataGroups** for more information on how this works.

## UsageMode Properties in MaskedEditBox

The MaxValue and MinValue properties are enforced only when the UsageMode is set to 'Numeric'.

```csharp
this.maskedEditBox1.ClipMode = Syncfusion.Windows.Forms.Tools.ClipModes.ExcludeLiterals;
this.maskedEditBox1.InputMode = Syncfusion.Windows.Forms.Tools.MaskInputMode.Normal;
this.maskedEditBox1.UsageMode = Syncfusion.Windows.Forms.Tools.MaskedUsageMode.Numeric;
```

### VB.NET

```vb.net
Me.maskedEditBox1.ClipMode = Syncfusion.Windows.Forms.Tools.ClipModes.ExcludeLiterals
Me.maskedEditBox1.InputMode = Syncfusion.Windows.Forms.Tools.MaskInputMode.Normal
Me.maskedEditBox1.UsageMode = Syncfusion.Windows.Forms.Tools.MaskedUsageMode.Numeric
```

## Display Settings

### 3.5.8.8.3.3 Display Settings

This section discusses the display settings of the MaskedEditBox control.

### Separators

The user data can be displayed along with separators at run time for specifying date, time, decimals, and thousands. It is not required to type separators at run time. Separators can be specified in the mask character itself.

| MaskedEditBox Properties  | Description                                                                                                                                     |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| DateSeparator             | Specifies the character to use when a date separator position is specified. <br> <br> The default separator is '/'.                                |
| DecimalSeparator          | Specifies the character to use when a decimal                                                                                                   |

## Footer

© 2013 Syncfusion. All rights reserved. 842 | Page

<!-- tags: [Syncfusion Winforms, MaskedEditBox, Display Settings, DataGroups, UsageMode, separators, DateSeparator, DecimalSeparator] keywords: [MaskedEditBox Control, Display Settings, Separators, DateSeparator, DecimalSeparator, UsageMode Enum, MaxValue, MinValue, Syncfusion.Windows.Forms.Tools, MaskedUsageMode] -->
```