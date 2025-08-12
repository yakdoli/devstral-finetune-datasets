```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_900.jpeg
document_name: tools
page_number: 900
page_id: tools#page_900
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:41:27Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### WordWrap Property Set

![Figure 575: WordWrap property Set](#)

The following figures illustrate the WordWrap property settings:

- **TextBoxExt control with WordWrap = "False"**
- **TextBoxExt control with WordWrap = "True"**

### ScrollBars Set for TextBoxExt Control

![Figure 576: ScrollBars set for TextBoxExt Control](#)

### Important Note

**Note:** The `ScrollToCaret()` method can be used to scroll the contents of the control to the current caret position.

### OverflowIndicatorToolTipText

**OverflowIndicatorToolTipText** is the tooltip displayed when text overflows. Its behavior can be configured using the following properties:

#### Properties

- **OverflowIndicatorToolTipText**: Specifies the text displayed in the overflow indicator tooltip.
- **ShowOverflowIndicator**: Gets or sets the visibility of the overflow indicator.
- **ShowOverflowIndicatorToolTip**: Indicates whether the overflow indicator tooltip should be shown.

#### Implementation Examples

- **C#**
  ```csharp
  this.textBoxExt1.ShowOverflowIndicator = true;
  this.textBoxExt1.ShowOverflowIndicatorToolTip = true;
  this.textBoxExt1.OverflowIndicatorToolTipText = "Overflow";
  ```

- **VB.NET**
  ```vb
  Me.textBoxExt1.ShowOverflowIndicator = True
  Me.textBoxExt1.ShowOverflowIndicatorToolTip = True
  Me.textBoxExt1.OverflowIndicatorToolTipText = "Overflow"
  ```

## API Reference

### Properties of TextBoxExt

| TextBoxExt Properties               | Description                                                                 |
|--------------------------------------|----------------------------------------------------------------------------|
| OverflowIndicatorToolTipText        | Specifies the overflow indicator tooltip text.                          |
| ShowOverflowIndicator               | Gets / sets overflow indicator visibility.                               |
| ShowOverflowIndicatorToolTip        | Indicates whether to show the overflow indicator tooltip.               |

## Code Examples

- **C# Example**
  ```csharp
  this.textBoxExt1.ShowOverflowIndicator = true;
  this.textBoxExt1.ShowOverflowIndicatorToolTip = true;
  this.textBoxExt1.OverflowIndicatorToolTipText = "Overflow";
  ```

- **VB.NET Example**
  ```vb
  Me.textBoxExt1.ShowOverflowIndicator = True
  Me.textBoxExt1.ShowOverflowIndicatorToolTip = True
  Me.textBoxExt1.OverflowIndicatorToolTipText = "Overflow"
  ```

## RAG Annotations

<!-- tags: [Syncfusion Winforms, TextBoxExt, OverflowIndicatorToolTipText, WordWrap, ScrollBars] keywords: [TextBoxExt, overflow, tooltip, wordwrap, scrollbars, caret, showoverflowindicator] -->
```