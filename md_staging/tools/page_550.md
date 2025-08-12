<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_550.jpeg
document_name: tools
page_number: 550
page_id: tools#page_550
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:20:15Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Discusses the ComboDropDown control's edit portion and its properties.
- Explains how to modify the behavior of the edit portion using specific properties.
- Includes C# and VB.NET code examples for configuring properties.

## Content

### ComboDropDown Properties and Description

| ComboDropDown Properties      | Description                                                                                       |
|------------------------------|---------------------------------------------------------------------------------------------------|
| CharacterCasing              | Specifies the ComboDropDown control modifies the case of characters when they are typed in the edit portion. |
| NumberOnly                   | Specifies whether the user should be forced to enter only numbers in the edit portion of ComboDropDown. |
| ReadOnly                     | Specifies whether the text in the edit portion of ComboDropDown should be set to read-only or can be changed. By default it will be set to false. |

#### Code Examples

##### C#

```csharp
this.comboDropDown1.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper;
this.comboDropDown1.NumberOnly = true;
this.comboDropDown1.ReadOnly = true;

this.comboDropDown1.CaseSensitiveAutocomplete = false;
this.comboDropDown1.MatchFirstCharacterOnly = false;
```

##### VB.NET

```vb
Me.comboDropDown1.CharacterCasing = System.Windows.Forms.CharacterCasing.Upper
Me.comboDropDown1.NumberOnly = True
Me.comboDropDown1.ReadOnly = True

Me.comboDropDown1.CaseSensitiveAutocomplete = False
Me.comboDropDown1.MatchFirstCharacterOnly = False
```

### Banner Text Support

We can set banner text for the ComboBoxDropDown control. Refer to the `BannerTextProvider Component` topic for more details.

---

<!-- tags: [product, winforms, combodropdown, editportion, banner text] keywords: [essentials, windows forms, properties, character casing, number only, read only, case sensitive autocomplete, match first character only, banner text support] -->