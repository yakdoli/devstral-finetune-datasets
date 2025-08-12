```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_816.jpeg
document_name: tools
page_number: 816
page_id: tools#page_816
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:36:28Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes the advanced features of the CurrencyTextBox control.
- Focuses on clipboard support and clipboard operations compatible with currency data.
- Explains the use of the `ClipMode` property to control formatting characters included in clipboard operations.

## Content

### WinForms-specific conventions
- **CurrencyTextBox Control Properties**:
  - **PositiveColor = "Blue"**: Text color for positive monetary values.
  - **NegativeColor = "Red"**: Text color for negative monetary values.
  - **ZeroColor = "DarkOrange"**: Text color for zero monetary values.
  - **ReadOnlyBackColor = "Linien"**: Background color when the control is read-only.

#### Figure 518: Color Settings for CurrencyTextBox Control
![Color Settings for CurrencyTextBox Control](https://i.imgur.com/ABCD123.png)

### 3.5.8.6.6 Advanced Features

#### 3.5.8.6.6.1 Clipboard Support
The CurrencyTextBox control provides support for clipboard operations that are compatible with currency data. The `ClipMode` property specifies whether formatting characters are to be copied to the clipboard when performing clipboard operations.

| CurrencyTextBox Property | Description                                                                                                                |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------|
| ClipMode                 | Specifies whether to include or exclude literal characters in the input mask while doing a copy command. The options are: <br> - ExcludeFormatting <br> - IncludeFormatting. |

#### Code Examples

- **C#**

  ```csharp
  this.currencyTextBox1.ClipMode =
  Syncfusion.Windows.Forms.Tools.CurrencyClipModes.ExcludeFormatting;
  ```

- **VB.NET**

  ```vb
  Me.currencyTextBox1.ClipMode =
  Syncfusion.Windows.Forms.Tools.CurrencyClipModes.ExcludeFormatting
  ```

### Notes on Usage
- Use `ExcludeFormatting` when you want to copy only the monetary value, excluding any currency symbols or thousand separators.
- Use `IncludeFormatting` when you want to copy the monetary value along with all formatting characters, such as currency symbols and thousand separators.

## API Reference

### Properties
- **ClipMode**: 
  - **Type**: `CurrencyClipModes`
  - **Description**: Specifies the mode for clipboard operations regarding formatting characters.
  - **Options**: 
    - `ExcludeFormatting`: Excludes formatting characters.
    - `IncludeFormatting`: Includes formatting characters.

## Cross References
- Refer to the main documentation for additional properties and methods of the CurrencyTextBox control.
- See also: other advanced features of the CurrencyTextBox control in the Syncfusion WinForms library.

<!-- tags: [Syncfusion Winforms, control, CurrencyTextBox, ClipMode, clipboard, properties] keywords: [CurrencyTextBox, ClipMode, clipboard operations, formatting, ExcludeFormatting, IncludeFormatting, Windows Forms, advanced features, Syncfusion] -->
```