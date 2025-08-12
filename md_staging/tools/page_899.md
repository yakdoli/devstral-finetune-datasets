```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_899.jpeg
document_name: tools
page_number: 899
page_id: tools#page_899
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:42:22Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Configuring multiline text controls for automatic word wrapping and scrollbar visibility.
- Modifying scrollbar behavior in multiline edit controls.

## Content

### WordWrap

- Indicates if lines are automatically word-wrapped for multiline edit controls.

### ScrollBars

- Indicates for multiline edit controls, which scrollbars will be shown for this control.
- Includes the following options:
  - None,
  - Horizontal,
  - Vertical,
  - Both.

### Code Examples

#### C#

```csharp
this.textBoxExt1.Multiline = true;
this.textBoxExt1.WordWrap = true;
this.textBoxExt1.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
```

#### VB.NET

```vb
Me.textBoxExt1.Multiline = True
Me.textBoxExt1.WordWrap = True
Me.textBoxExt1.ScrollBars = System.Windows.Forms.ScrollBars.Vertical
```

### Note

- TextBoxExt is a textbox-derived control that can display different border colors and styles.

## API Reference

- **Namespace**: System.Windows.Forms
- **Property**: `Multiline`
  - Type: `bool`
  - Description: Enables or disables multiline text input.
- **Property**: `WordWrap`
  - Type: `bool`
  - Description: Enables or disables word-wrapping for the text.
- **Property**: `ScrollBars`
  - Type: `ScrollBars`
  - Description: Determines which scrollbars are displayed for the control.
    - Possible values: `None`, `Horizontal`, `Vertical`, `Both`.

## Figure: Multiline Text

![Multiline Text](Figure 574: Multiline Text)

<!-- tags: [syncfusion winforms, multiline text controls, word wrapping, scrollbars, textbox derived controls] keywords: [multiline, wordwrap, scrollbars, textboxext, textbox] -->
```