```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_746.jpeg
document_name: tools
page_number: 746
page_id: tools#page_746
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:32:20Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Methods associated with the "SelectAllOnFocus" property are described.
- Operations such as getting clipped text, cutting, copying, deleting, pasting, and selecting all text are detailed.
- Text formatting options using the ClipMode property are explained.

## Figure 472: "SelectAllOnFocus" Property Set

### Methods and Descriptions

| **Methods**        | **Description**                                                                 |
|--------------------|---------------------------------------------------------------------------------|
| GetClipText        | Gets / sets the clipped text without the formatting.                          |
| Cut                | Cuts the selected data to the clipboard.                                      |
| Copy               | Copies the content of the NumberTextBox to the clipboard. The ClipMode property dictates what gets copied. |
| Delete             | Deletes the current selection of the TextBox.                                 |
| Paste              | Pastes the data in the clipboard into the NumberTextBox control.              |
| SelectAll          | Selects all text in the TextBox.                                              |

### Clip Mode

#### The formatting for the text can be enabled or disabled by using the property given below.

| **IntegerTextBox Property** | **Description**                                                                                                                                           |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| ClipMode                    | Determines whether to include or exclude the literal characters in the input mask when doing a copy command. <br><br> It includes the below given options: <br><br> IncludeFormatting and <br> ExcludeFormatting. |

### Code Example: Setting ClipMode in C#

```csharp
this.integerTextBox1.ClipMode = Syncfusion.Windows.Forms.Tools.CurrencyClipModes.IncludeFormatting;
```

## API Reference

### Properties
- **ClipMode**: Determines whether to include or exclude the literal characters in the input mask when doing a copy command. Options are:
  - IncludeFormatting
  - ExcludeFormatting

## Related Documentation
- Refer to the official documentation for Syncfusion WinForms for detailed examples and additional properties.

### Additional Information
- Syncfusion version: 11.4.0.26
- This page provides a technical reference for methods and properties associated with the "SelectAllOnFocus" property and ClipMode in the IntegerTextBox control.

<!-- tags: [syncfusion winforms, integertextbox, clipmode, selectallonfocus, property set] keywords: [getcliptext, cut, copy, delete, paste, selectall, clipmode, includeformatting, excludeformatting] -->
```