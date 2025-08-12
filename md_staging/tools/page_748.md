```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_748.jpeg
document_name: tools
page_number: 748
page_id: tools#page_748
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:32:11Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Explains the RightToLeft property feature.
- Details the OverflowIndicatorToolTipText feature of the IntegerTextBox control.
- Demonstrates properties for setting the overflow indicator tooltip text, visibility, and tooltip display.

![Text displayed from Right To Left](image.png "Figure 473: Text displayed from Right To Left")

### Note:
The `ResetRightToLeft()` method can be used to reset the `RightToLeft` property to its default value.

## Content

### OverflowIndicatorToolTipText

| IntegerTextBox Properties                  | Description                                                                 |
|--------------------------------------------|-----------------------------------------------------------------------------|
| OverflowIndicatorToolTipText               | Specifies the overflow indicator tooltip text.                         |
| ShowOverflowIndicator                      | Gets / sets overflow indicator visibility.                              |
| ShowOverflowIndicatorToolTip               | Indicates whether to show the overflow indicator tooltip.              |

#### Code Example: C#

```csharp
this.integerTextBox1.OverflowIndicatorToolTipText = "Overflow";
this.integerTextBox1.ShowOverflowIndicator = true;
this.integerTextBox1.ShowOverflowIndicatorToolTip = true;
```

#### Code Example: VB.NET

```vb
Me.integerTextBox1.OverflowIndicatorToolTipText = "Overflow"
Me.integerTextBox1.ShowOverflowIndicator = True
Me.integerTextBox1.ShowOverflowIndicatorToolTip = True
```

![Overflow Indicator ToolTip Text Set](image1.png "Figure 474: Overflow Indicator ToolTip Text Set")

### Sample Demonstration
A sample demonstrating the Text, Text Align, and Overflow Indicator features of the IntegerTextBox control is available in the below sample installation path.

## API Reference
- **Namespace:** Syncfusion.Windows.Forms.Tools
- **Class:** IntegerTextBox
- **Properties:**
  - **OverflowIndicatorToolTipText:** Sets the text for the overflow indicator tooltip.
  - **ShowOverflowIndicator:** Controls the visibility of the overflow indicator.
  - **ShowOverflowIndicatorToolTip:** Enables or disables the display of the overflow indicator tooltip.

## Code Examples
- C# and VB.NET examples are provided above to configure the IntegerTextBox control for overflow indicator tooltip features.

<!-- tags: [Syncfusion, WinForms, IntegerTextBox, RightToLeft, OverflowIndicator, Tooltip] keywords: [RightToLeft property, OverflowIndicatorToolTipText, IntegerTextBox, default value, text alignment, OverflowIndicatorToolTip, sample path] -->
```