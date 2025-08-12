```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_817.jpeg
document_name: tools
page_number: 817
page_id: tools#page_817
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:35:54Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the usage of `CurrencyTextBox` with clipboard interactions and overflow indicators.
- Explains how to configure tooltip settings for overflow indicators.

## Content

### Clipboard Menu in CurrencyTextBox
#### Clipboard Functions
The `CurrencyTextBox` control provides a clipboard menu with standard editing functionalities such as copying, pasting, cutting, and more. This menu can be accessed while interacting with the text box.

![Figure 519: CurrencyTextBox with Clipboard Menu](Figure 519: CurrencyTextBox with Clipboard Menu)

### Overflow Indicator

#### Overview
You can display an indicator in the textbox when the currency value exceeds its boundaries. Additionally, you can enable tooltips for the overflow indicator.

#### Setting Up Overflow Indicator

1. **Specifying Tooltip Text**: The tooltip text is set using the `OverflowIndicatorToolTipText` property.
2. **Displaying Overflow Indicator**: Enable the overflow indicator using the `ShowOverflowIndicator` property.
3. **Displaying Tooltip Text**: Enable the tooltip text using the `ShowOverflowIndicatorToolTip` property.

#### Example Code

**C#**
```csharp
this.currencyTextBox1.OverflowIndicatorToolTipText = "Overflow";
this.currencyTextBox1.ShowOverflowIndicator = true;
this.currencyTextBox1.ShowOverflowIndicatorToolTip = true;
```

**VB.NET**
```vbnet
Me.currencyTextBox1.OverflowIndicatorToolTipText = "Overflow"
Me.currencyTextBox1.ShowOverflowIndicator = True
Me.currencyTextBox1.ShowOverflowIndicatorToolTip = True
```

#### Visualization
![Figure 520: Overflow Indicator with ToolTip](Figure 520: Overflow Indicator with ToolTip)

## API Reference

- **Properties**
  - `OverflowIndicatorToolTipText`: Sets the tooltip text for the overflow indicator.
  - `ShowOverflowIndicator`: Enables or disables the display of the overflow indicator.
  - `ShowOverflowIndicatorToolTip`: Enables or disables the display of the tooltip text for the overflow indicator.

## Code Examples

The code examples demonstrate how to configure the `CurrencyTextBox` to handle overflow conditions and display appropriate indicators and tooltips.

### C# Example
```csharp
// Configure Overflow Indicator
this.currencyTextBox1.OverflowIndicatorToolTipText = "Overflow";
this.currencyTextBox1.ShowOverflowIndicator = true;
this.currencyTextBox1.ShowOverflowIndicatorToolTip = true;
```

### VB.NET Example
```vbnet
' Configure Overflow Indicator
Me.currencyTextBox1.OverflowIndicatorToolTipText = "Overflow"
Me.currencyTextBox1.ShowOverflowIndicator = True
Me.currencyTextBox1.ShowOverflowIndicatorToolTip = True
```

## Page-level Navigation/TOC (if applicable)
- **Clipboard Menu in CurrencyTextBox**
- **Overflow Indicator**
  - Overview
  - Setting Up Overflow Indicator
  - Example Code

## Cross References
- See also: [CurrencyTextBox Documentation](#CurrencyTextBox-Documentation)

<!-- tags: [CurrencyTextBox, OverflowIndicator, ClipboardMenu, Tooltip, SyncfusionWinforms] keywords: [CurrencyTextBox, OverflowIndicatorToolTipText, ShowOverflowIndicator, ShowOverflowIndicatorToolTip, clipboard functions, tooltip settings] -->
```
