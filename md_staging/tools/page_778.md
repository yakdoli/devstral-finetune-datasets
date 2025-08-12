```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_778.jpeg
document_name: tools
page_number: 778
page_id: tools#page_778
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:34:12Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- This section discusses the ScrollBars set for the PercentTextBox control in Windows Forms.
- Covers ClipMode and FormattedText properties of the PercentTextBox control.

## Content

### Clip Mode

The formatting for the text can be enabled or disabled using the property given below.

#### Table: PercentTextBox Property

| PercentTextBox Property | Description                                                                                           |
|--------------------------|-------------------------------------------------------------------------------------------------------|
| ClipMode                 | Determines whether to include or exclude the literal characters in the input mask when doing a copy command. <br> It includes the below given options. <br> `IncludeFormatting` and <br> `ExcludeFormatting`. |

#### Code Examples

- **C#**
  ```csharp
  this.percentTextBox1.ClipMode =
  Syncfusion.Windows.Forms.Tools.CurrencyClipModes.IncludeFormatting;
  ```

- **VB.NET**
  ```vbnet
  Me.percentTextBox1.ClipMode =
  Syncfusion.Windows.Forms.Tools.CurrencyClipModes.IncludeFormatting
  ```

### Formatted Text

Formatted text can be displayed using the below given property.

#### Table: PercentTextBox Property

| PercentTextBox Property | Description                               |
|--------------------------|-------------------------------------------|
| FormattedText           | Returns the formatted text with the formatting. |

#### Code Examples

- **C#**
  ```csharp
  this.percentTextBox1.FormattedText = "Hello";
  ```

## API Reference

### Properties

- **ClipMode**  
  - Type: `Syncfusion.Windows.Forms.Tools.CurrencyClipModes`

- **FormattedText**  
  - Type: `String`

## Page-level Navigation/TOC

- Clipboard Mode for PercentTextBox Control
- Formatted Text in PercentTextBox Control

## Cross References

- Refer to [Syncfusion Windows Forms Documentation](https://www.syncfusion.com/documentation/windowsforms) for more details on controls and their properties.

<!-- tags: [Syncfusion, Windows Forms, PercentTextBox, ClipMode, FormattedText, Control Properties] keywords: [toolkit, UI, Windows Forms, control, property, PercentTextBox, formatting, Clipboard] -->
```
