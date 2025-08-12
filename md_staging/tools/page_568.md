```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_568.jpeg
document_name: tools
page_number: 568
page_id: tools#page_568
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:21:18Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

| ReadOnly                                       | Specifies whether the control can be made read only. By default it is set to false. |
|------------------------------------------------|--------------------------------------------------------------------------------------------|
| DropDownStyle                                  | Specifies the dropdown style of the ComboBoxAdv control. Based on its below options, it specifies whether the text in the control is editable or not. The styles are,                                      |
|                                                | Simple - The text portion is editable. The list portion is always visible.           |
|                                                | DropDown (default style) - The text portion is editable. Clicking the arrow button will display the list portion.                                      |
|                                                | DropDownList - The text portion is not editable. Clicking the arrow button will display the list portion.                                          |

### Behavior Settings

The below properties control the behavior of the text typed in the Textbox.

| ComboBoxAdv Properties | Description                                                                 |
|------------------------|------------------------------------------------------------------------------|
| NumberOnly            | Specifies whether the user should be allowed to enter only numbers in the edit portion of the ComboBoxAdv. |
| CharacterCasing       | Specifies the case of the characters that are entered in the textbox. The options are,                          |
|                        | Normal - Characters are left unchanged,                                      |
|                        | UpperCase - Changes the case of the characters to UPPERCASE                   |

### Code Examples

```csharp
[C#]

this.comboBoxAdv1.ReadOnly = true;
this.comboBoxAdv1.DropDownStyle = System.Windows.Forms.ComboBoxStyle.Simple;
```

```vb
[VB.NET]

Me.comboBoxAdv1.ReadOnly = True
Me.comboBoxAdv1.DropDownStyle = System.Windows.Forms.ComboBoxStyle.Simple
```

## Page-level Navigation/TOC (if applicable)

The document discusses the behavior settings of the ComboBoxAdv control in Windows Forms, specifically focusing on the ReadOnly and DropDownStyle properties. It also covers the behavior of text input controlled by other properties such as NumberOnly and CharacterCasing.

<!-- tags: [windowsforms, comboboxadv, read-only, dropdownstyle, numberonly, charactercasing] keywords: [readonly, comboboxadv, dropdownstyle, numberonly, charactercasing, windowsforms] -->
```