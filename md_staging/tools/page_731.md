```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_731.jpeg
document_name: tools
page_number: 731
page_id: tools#page_731
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:32:04Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Discusses how to set banner text for the DoubleTextBox control using the BannerTextProvider Component.
- Explains the necessary settings to enable Banner text for the control.
- Covers full appearance and behavior settings of the DoubleTextBox.

## Content

### Setting Banner Text for DoubleTextBox

We can set banner text for the DoubleTextBox control. Refer to the **BannerTextProvider Component** topic for more details.

We need to do the following settings to make the Banner text feature available for the control.

```csharp
this.doubleTextBox1.AllowNull = true;
this.doubleTextBox1.NullString = "";
this.doubleTextBox1.Text = "";
```

```vb
Me.doubleTextBox1.AllowNull = True
Me.doubleTextBox1.NullString = ""
Me.doubleTextBox1.Text = ""
```

![](https://unclear-link-to-figure-461)
**Figure 461:** Banner Text set for DoubleTextBox

### 3.5.8.3.3.2 Appearance and Behavior Settings

This section discusses the complete Appearance and behavior settings of Double TextBox.

#### Border Style

3D border styles and colors can be applied for the border of Double TextBox. Refer to **Border styles of Currency textbox** for details.

#### Color

Colors can be applied for Double textbox when its value is positive, negative or zero. Refer to **Color Settings of Currency textbox** for details.

#### Keyboard Support

Double TextBox supports keyboard support. Refer to **Clipboard Support of Currency textbox** in detail.

#### Overflow Indicator

---
© 2013 Syncfusion. All rights reserved.

Page 731

<!-- tags: [Syncfusion Winforms, DoubleTextBox, BannerTextProvider, Appearance, Behavior, Border Style, Color, Keyboard Support, Overflow Indicator] keywords: [DoubleTextBox, Banner text, Appearance settings, Behavior settings, Border styles, Color settings, Keyboard support, Overflow Indicator] -->
```