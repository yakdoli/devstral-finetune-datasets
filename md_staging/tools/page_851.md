```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_851.jpeg
document_name: tools
page_number: 851
page_id: tools#page_851
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:39:43Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Implements basic text manipulation features such as Cut, Copy, Paste, and Select for the textbox.
- Raises the CharacterCasingChanged event as needed.
- Provides control over the ClipMode property to dictate what gets copied.

## Content

### Textbox Operations

| Operation          | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| textbox.          |                                                                            |
| OnCharacterCasingChanged | Raises the CharacterCasingChanged event.                               |
| Cut               | Cuts the selected data to the clipboard.                                    |
| Copy              | Copies the content of the NumberTextBox to the clipboard. The ClipMode property dictates what gets copied. |
| Paste             | Pastes the data in the clipboard into the NumberTextBox control.           |
| Select            | Selects a range of text in the TextBox.                                    |

### Clip Mode

The formatting for the text can be enabled or disabled using the property given below.

| MaskedEditBox Property | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| ClipMode               | Specifies the format of the text that will be returned by the MaskedEditBox control. <br> It includes the below given options: <br> IncludeLiterals and ExcludeLiterals. |

#### Code Examples

- **C#**
  ```csharp
  this.maskedEditBox1.ClipMode =
  Syncfusion.Windows.Forms.Tools.ClipModes.IncludeLiterals;
  ```

- **VB.NET**
  ```vb
  Me.maskedEditBox1.ClipMode =
  Syncfusion.Windows.Forms.Tools.ClipModes.IncludeLiterals
  ```

### OverflowIndicatorToolTipText
- Specifies the tooltip text for the overflow indicator in the textbox.

<!-- tags: [product, Syncfusion Winforms, textbox, event, property, method, version: 11.4.0.26] keywords: [textbox, OnCharacterCasingChanged, Cut, Copy, Paste, Select, ClipMode, OverflowIndicatorToolTipText, Syncfusion.Windows.Forms.Tools, ClipModes, IncludeLiterals, ExcludeLiterals] -->
```