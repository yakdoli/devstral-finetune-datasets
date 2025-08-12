```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_569.jpeg
document_name: tools
page_number: 569
page_id: tools#page_569
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:20:23Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Properties and behaviors of the ComboBoxAdv control in Syncfusion Winforms.
- Configuring text case, selection visibility, word wrapping, text entry, and character limits.
- Setting banner text for the ComboBoxAdv control.

## Content

### Control Properties

| Property | Description |
|----------|-------------|
| **LowerCase** | Changes the case of the characters to lowercase. |
| **TextBox.HideSelection** | When set to false, will always highlight the selected text in the edit portion, even if the control loses focus. |
| **TextBox.WordWrap** | Indicates whether the textbox automatically wraps words to the beginning of the next line. Note that the multiline property should be set to true to make the word wrap feature effective. |
| **AllowNewText** | Indicates whether the user is allowed to enter new text at runtime. |
| **MaxLength** | Specifies the maximum number of characters allowed in the edit portion of the ComboBoxAdv control. Default (32767). |

---

### Code Examples

#### C#
```csharp
this.comboBoxAdv1.NumberOnly = true;
this.comboBoxAdv1.CharacterCasing = CharacterCasing.Upper;
this.comboBoxAdv1.TextBox.HideSelection = false;
this.comboBoxAdv1.TextBox.WordWrap = true;

this.comboBoxAdv1.AllowNewText = true;
this.comboBoxAdv1.MaxLength = 32766;
```

#### VB.NET
```vb
Me.comboBoxAdv1.NumberOnly = True
Me.comboBoxAdv1.CharacterCasing = CharacterCasing.Upper
Me.comboBoxAdv1.TextBox.HideSelection = False
Me.comboBoxAdv1.TextBox.WordWrap = True

Me.comboBoxAdv1.AllowNewText = True
Me.comboBoxAdv1.MaxLength = 32766
```

---

### Banner Text Support

We can set banner text for the ComboBoxAdv control. Refer to the **BannerTextProvider Component** topic for more details.

---

### Example of Banner Text

![Select the Country](https://example.com/image.png)

---

### Footer
© 2013 Syncfusion. All rights reserved. 569 | Page

## API Reference
- **Properties:**
  - `NumberOnly`: Boolean
  - `CharacterCasing`: CharacterCasing
  - `TextBox.HideSelection`: Boolean
  - `TextBox.WordWrap`: Boolean
  - `AllowNewText`: Boolean
  - `MaxLength`: Int32

## RAG Annotations
<!-- tags: [ComboBoxAdv, WinForms, Syncfusion, CharacterCasing, BannerTextProvider] keywords: [ComboBoxAdv, TextCase, WordWrap, MaxLength, BannerText] -->
```