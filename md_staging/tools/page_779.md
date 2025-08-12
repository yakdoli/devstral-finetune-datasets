```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_779.jpeg
document_name: tools
page_number: 779
page_id: tools#page_779
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:35:15Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the use of the `PercentTextBox` control in displaying formatted text.
- Explains the `RightToLeft` property and its application for RTL languages.
- Details how to handle overflow of text using the `OverflowIndicatorTooltipText` property.

## Content

### RightToLeft

The text can be displayed from right to left for RTL languages using this property.

| PercentTextBox Property    | Description                                                                                          |
|-----------------------------|------------------------------------------------------------------------------------------------------|
| RightToLeft                | Indicates whether the component should draw right-to-left for RTL languages. The default value is set to 'False'. |

> **Note:** The `RightToLeft` property will be automatically set to 'True' for RTL languages.

```csharp
[C#]

this.percentTextBox1.RightToLeft = System.Windows.Forms.RightToLeft.Yes;
```

```vb
[VB.NET]

Me.percentTextBox1.RightToLeft = System.Windows.Forms.RightToLeft.Yes
```

![Text displayed from Right To Left](https://i.imgur.com/placeholder.png)
*Figure 495: Text displayed from Right To Left*

> **Note:** The `ResetRightToLeft()` method can be used to reset the `RightToLeft` property to its default value.

### OverflowIndicatorTooltipText

The tooltip that should be displayed when an overflow of text occurs can be set using the below given properties.

| PercentTextBox Properties            | Description                                      |
|---------------------------------------|--------------------------------------------------|
| OverflowIndicatorTooltipText         | Specifies the overflow indicator tooltip text. |

## API Reference

- **Properties**
  - `RightToLeft`: Indicates whether the component should draw right-to-left for RTL languages. Default value is 'False'.
  - `OverflowIndicatorTooltipText`: Specifies the tooltip text for overflow indication.

## Code Examples

### C#

```csharp
this.percentTextBox1.FormattedText = "Hello";
this.percentTextBox1.RightToLeft = System.Windows.Forms.RightToLeft.Yes;
this.percentTextBox1.OverflowIndicatorTooltipText = "TextOverflowTip";
```

### VB.NET

```vb
Me.percentTextBox1.FormattedText = "Hello"
Me.percentTextBox1.RightToLeft = System.Windows.Forms.RightToLeft.Yes
Me.percentTextBox1.OverflowIndicatorTooltipText = "TextOverflowTip"
```

## Page-level Navigation/TOC (if applicable)

- RightToLeft
- OverflowIndicatorTooltipText

## Cross References

See also:
- PercentTextBox control
- RTL language settings
- Tooltip customization

<!-- tags: [Syncfusion Winforms, PercentTextBox, RightToLeft, OverflowIndicatorTooltipText] keywords: [formatted text, RTL, tooltip, text overflow, right-to-left text] -->
```