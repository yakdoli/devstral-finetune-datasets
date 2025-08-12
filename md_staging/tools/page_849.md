```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_849.jpeg
document_name: tools
page_number: 849
page_id: tools#page_849
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:37:52Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Demonstrates how to set culture for the `MaskedEditBox` control in both C# and VB.NET.
- Explains the text settings of the `MaskedEditBox` control, including options for customizing text alignment, selected text, and character casing.

## Content

### Setting Culture for MaskedEditBox Control

#### C#
```csharp
this.maskedEditBox1.SpecialCultureValue = 
Syncfusion.Windows.Forms.Tools.SpecialCultureValues.None;
this.maskedEditBox1.UseUserOverride = true;
```

#### [VB.NET]
```vb.net
Me.maskedEditBox1.Culture = New System.Globalization.CultureInfo("ar-SA")
Me.maskedEditBox1.SpecialCultureValue = 
Syncfusion.Windows.Forms.Tools.SpecialCultureValues.None
Me.maskedEditBox1.UseUserOverride = True
```

![Figure 541: Culture Set for the MaskedEditBox Control](https://via.placeholder.com/80x60?text=777%20%28image%29)
*Figure 541: Culture Set for the MaskedEditBox Control*

### Text Settings

#### Overview
This section discusses the text settings of the `MaskedEditBox` control.

The text associated with the `MaskedEditBox` control can be set and customized using the following properties:

| MaskedEditBox Properties | Description |
|---------------------------|-------------|
| CharacterCasing | Gets / sets the case of character as they are typed.<br><br>It includes the below given options:<br><br>Normal, <br>Upper, <br>Lower. |
| TextAlign | Indicates how the text should be aligned for edit controls. |
| SelectedText | Gets / sets the selected text in the `MaskedEditBox`. |
| HideSelection | Indicates that the selection should be hidden |

## Page-Level Navigation/TOC (if applicable)
- **Setting Culture for MaskedEditBox Control**
- **Text Settings**

### Cross References
See also:
- [Cultural Settings in Syncfusion Controls](#)
- [Customizing Text in Edit Controls](#)

<!-- tags: [Syncfusion, Winforms, MaskedEditBox, Culture, TextSettings, CharacterCasing, TextAlign, SelectedText, HideSelection] keywords: [MaskedEditBox, Culture, Text, Setting, CharacterCasing, TextAlign, SelectedText, HideSelection] -->
```