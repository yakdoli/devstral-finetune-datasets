```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_221.jpeg
document_name: edit
page_number: 221
page_id: edit#page_221
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:08:07Z
fidelity: lossless
 -->

# Essential Edit for Windows Forms

```xml
<format name="Number" Font="Courier New, 10pt, style=Bold" FontColor="Navy" />
```

## Overview

This page discusses the font customization capabilities of the `Edit` Control in Windows Forms using the `frmFormatsConfig` dialog box. Key features include:

- **Runtime font customization** through the `frmFormatsConfig` dialog box.
- Three main controls:
  - **ControlFormatSettings**
  - **ControlFormatsList**
  - **ControlLanguageSelector**
- Each control serves specific functions in managing and customizing the formatting settings and language configurations for the `Edit` Control.

## Content

### Font Customization through `frmFormatsConfig`

The `Edit` Control supports font customization at runtime using the `frmFormatsConfig` dialog box. This dialog box consists of three smaller controls:

1. **ControlFormatSettings**: This dialog box contains the actual controls to customize the rendering settings of the selected format, including font settings.
2. **ControlFormatsList**: This dialog box consists of the list of currently existing formats in the configuration file. It also supports creating new formats or deleting existing ones.
3. **ControlLanguageSelector**: This dialog box has a Combo Box containing the list of configuration languages supported by the `Edit` Control. The list is updated when a new configuration language is added or an existing one is removed.

### Example Code for Hooking Up Dialogs

The following C# code illustrates how to hook up these dialogs to the `Edit` Control:

```csharp
this.controlLanguageSelector1.EditControl = this.editControl1;
this.controlFormatsList1.EditControl = this.editControl1;
```

### Explanation

1. **ControlLanguageSelector1**: This control allows the user to choose the language of the configuration file. The `EditControl` property is set to associate it with the `editControl1` object.
2. **ControlFormatsList1**: This control displays the list of formats in the configuration file and allows the addition or removal of formats. Similar to the `ControlLanguageSelector`, it is also associated with `editControl1`.

#### Key Features of the `frmFormatsConfig` Dialog Box

The image shows the `Format Editor` dialog box, where users can customize settings for various elements of the text, such as:

- **Language Selection**: Choose the language (e.g., `C#`) for which the formatting will apply.
- **Text Settings**: Adjust font name, font size, style, and color for different formatting elements like `Keyword`, `Number`, `Comment`, etc.
- **Fill and Borders**: Customize background and border colors and styles for selected text formats.
- **Underlining**: Define underline weight, color, and style.

### Notes

The `Edit` Control provides a robust interface for customizing the appearance and behavior of text, making it highly configurable for different programming languages and styles.

### Screen Shot of the `Format Editor`

![Figure 70: Formats Editor](https://user-images.githubusercontent.com/123456789/123456789-123456789.png)

---

## RAG Annotations

<!-- tags: [winforms, formatting, font customization, frmFormatConfig, control customization] keywords: [Edit Control, fontsize, font, style, fontcolor, runtime, language selection, format editor, text settings, fill, borders, underlining, ControlFormatSettings, ControlFormatsList, ControlLanguageSelector, configuration languages, runtime customization, font customization, C#, dialog box] -->
```