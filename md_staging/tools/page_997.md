```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_997.jpeg
document_name: tools
page_number: 997
page_id: tools#page_997
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:47:02Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the CheckBoxAdv styles and Office 2007 Color Schemes.
- Explains how to apply custom colors to the RadioButtonAdv control programmatically.

## Content

### CheckBoxAdv Styles

**Figure 645: CheckBoxAdv Styles**

![Figure 645: CheckBoxAdv Styles](https://example.com/image645)

### Office 2007 Color Schemes

**Figure 646: Office 2007 Color Schemes**

![Figure 646: Office 2007 Color Schemes](https://example.com/image646)

When the `Office2007ColorScheme` property is set to 'Managed', the RadioButton in the `RadioButtonAdv` can be displayed using custom colors supported by the control.

This can be done programmatically as follows.

### C#

```csharp
this.radioButtonAdv1.Style =
    Syncfusion.Windows.Forms.Tools.RadioButtonAdvStyle.Office2007;
this.radioButtonAdv1.Office2007ColorScheme =
    Syncfusion.Windows.Forms.Office2007Theme.Managed;
Office2007Colors.ApplyManagedColors(this, Color.Red);
```

### VB

```vb
Me.radioButtonAdv1.Style =
    Syncfusion.Windows.Forms.Tools.RadioButtonAdvStyle.Office2007
Me.radioButtonAdv1.Office2007ColorScheme =
    Syncfusion.Windows.Forms.Office2007Theme.Managed
Office2007Colors.ApplyManagedColors(Me, Color.Red)
```

## API Reference

### Properties
- `Office2007ColorScheme`: Specifies the color scheme for the RadioButtonAdv. Can be set to 'Managed' to apply custom colors.

### Methods
- `ApplyManagedColors`: Applies custom colors to the control based on the provided parameters.

## Code Examples

### Example: Customizing RadioButtonAdv with Managed Colors

#### C#

```csharp
this.radioButtonAdv1.Style =
    Syncfusion.Windows.Forms.Tools.RadioButtonAdvStyle.Office2007;
this.radioButtonAdv1.Office2007ColorScheme =
    Syncfusion.Windows.Forms.Office2007Theme.Managed;
Office2007Colors.ApplyManagedColors(this, Color.Red);
```

#### VB

```vb
Me.radioButtonAdv1.Style =
    Syncfusion.Windows.Forms.Tools.RadioButtonAdvStyle.Office2007
Me.radioButtonAdv1.Office2007ColorScheme =
    Syncfusion.Windows.Forms.Office2007Theme.Managed
Office2007Colors.ApplyManagedColors(Me, Color.Red)
```

## See also
- CheckBoxAdv documentation
- Office2007Theme reference

<!-- tags: [Syncfusion Winforms, RadioButtonAdv, Office2007Themes, CustomColors] keywords: [CheckBoxAdv, Office2007ColorScheme, ManagedColors, ApplyManagedColors] -->
```