```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_552.jpeg
document_name: tools
page_number: 552
page_id: tools#page_552
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:20:14Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes control appearance and styling properties.
- Demonstrates setting `FlatStyle` and `FlatBorderColor`.
- Provides code snippets for configuring `Border3DStyle` and `BorderSides`.
- Enhances the look and feel of the ComboDropDown using specific properties.

## Content

### Control Appearance Properties

| **Property**         | **Description**                                                                 |
|----------------------|--------------------------------------------------------------------------------|
|                      | Flat - The control and the button appear flat.<br>System - Appearance based on the OS used and<br><br>Standard - The control and button appears three-dimensional. |
| `FlatBorderColor`    | Specifies the border color for the control, when `FlatStyle` is set to "Flat". |

### Code Examples

#### C#

```csharp
this.comboDropDown1.Border3DStyle =
    System.Windows.Forms.Border3DStyle.RaisedInner;
this.comboDropDown1.BorderSides =
    System.Windows.Forms.Border3DSide.All;
```

#### VB.NET

```vb
Me.comboDropDown1.Border3DStyle =
    System.Windows.Forms.Border3DStyle.RaisedInner
Me.comboDropDown1.BorderSides =
    System.Windows.Forms.Border3DSide.All
```

### Figure and Description

![ComboDropDown with `Border3DStyle = "RaisedInner"` and `BorderSides = "All"`](images/figure_340.png)

**Figure 340:** `Border3DStyle = "RaisedInner"`; `BorderSides = "All"`

#### Note

`ComboDropDown.Style` property should be set to **Default** to effect the above settings. See **Themes and Styles** topic.

### Enhancing ComboDropDown Look and Feel

#### Properties

| **ComboDropDown Properties** | **Description**                                                                 |
|------------------------------|--------------------------------------------------------------------------------|
| `IgnoreThemeBackground`      | Specifies whether the control will ignore the theme's background color and draw the backcolor instead. |
| `Style`                      | Specifies advanced appearance and behavior of the ComboDropDown. The default value is *Default*.         |

#### Section Reference

3.5.5.1.3.3 Themes And Styles

The below given properties enhances the look and feel of the ComboDropDown.

## API Reference

### PROPERTY: `IgnoreThemeBackground`

- **Type:** `bool`
- **Description:** Specifies whether the control will ignore the theme's background color and draw the backcolor instead.

### PROPERTY: `Style`

- **Type:** `Enum`
- **Description:** Specifies advanced appearance and behavior of the ComboDropDown. The default value is **Default**.

## Code Examples (Additional)

```csharp
// Example usage of IgnoreThemeBackground
comboDropDown1.IgnoreThemeBackground = true;
comboDropDown1.BackColor = Color.LightBlue;

// Example usage of Style property
comboDropDown1.Style = ComboDropDownStyle.Advanced;
```

## Cross References

See also: **Themes and Styles** section for more details on appearance customization.

<!-- tags: [Syncfusion Winforms, ComboDropDown, FlatStyle, Border3DStyle, Themes and Styles] keywords: [ComboDropDown, FlatStyle, Border3DStyle, IgnoreThemeBackground, Advanced Appearance, Style Property] -->
```