```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_513.jpeg
document_name: tools
page_number: 513
page_id: tools#page_513
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:17:00Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This page discusses customization options for the ColorUIControl, including changing the font style and appearance settings.
- Focuses on border styles, size settings, and font customization for the ColorUIControl.

## Content

### Figure 299: Custom Text for Color Group Tabs

![](https://example.com/figure299.png)

**Figure 299: Custom Text for Color Group Tabs**

**Note:** We can also change the font style of the tab text using `ColorUIControl.Font` property.

#### 3.5.4.1.4 ColorUIControl Appearance

This section discusses the appearance, border styles, and size settings of the ColorUIControl.

##### Border Styles

The border styles for the ColorUIControl can be set through the `BorderStyle` property.

| ColorUIControl Properties | Description                                                                                   |
|---------------------------|-----------------------------------------------------------------------------------------------|
| `BorderStyle`            | Sets border style for the control. The options are, <br> - `FixedSingle`, <br> - `Fixed3D` (default) and <br> - `None`. |

**C#**

```csharp
this.colorUIControl1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
```

## API Reference

### Namespace: Syncfusion.Windows.Forms.Tools

#### Properties

- **`BorderStyle`** (Type: `System.Windows.Forms.BorderStyle`)
  - **Description:** Sets the border style for the control.
  - **Options:** `FixedSingle`, `Fixed3D`, `None`
  - **Default:** `Fixed3D`
  - **Required:** No

#### Code Example

Setting the border style to `FixedSingle`:

```csharp
this.colorUIControl1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
```

## See also

- [ColorUIControl Overview](#coloruicontrol-overview)
- [Customizing Tab Text Style](#customizing-tab-text-style)

<!-- tags: [winforms, coloruicontrol, borderstyle, customtext, tabtext, appearence,controls] keywords: [coloruicontrol, borderstyle, fixedsingle, fixed3d, none, fontproperty, tabtext, customtext, appearance, style] -->
```