```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_973.jpeg
document_name: tools
page_number: 973
page_id: tools#page_973
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:45:36Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Overview of CheckBoxAdv with customizable color schemes using the Office2007ColorScheme property.
- Demonstrates how to apply custom colors programmatically.
- Shows examples in both C# and VB.

## Content

### Custom Color Schemes in CheckBoxAdv

![Figure 628: Office 2007 Color Schemes](insert_image_path)

**Figure 628: Office 2007 Color Schemes**

When the `Office2007ColorScheme` property is set to 'Managed', the CheckBox in the CheckBoxAdv can be displayed using custom colors supported by the control.

This can be done programmatically as follows.

#### [C#]

```csharp
this.checkBoxAdv1.Style =
    Syncfusion.Windows.Forms.Tools.CheckBoxAdvStyle.Office2007;
this.checkBoxAdv1.Office2007ColorScheme =
    Syncfusion.Windows.Forms.Office2007Theme.Managed;
Office2007Colors.ApplyManagedColors(this, Color.Pink);
```

#### [VB]

```vb
Me.checkBoxAdv1.Style =
    Syncfusion.Windows.Forms.Tools.CheckBoxAdvStyle.Office2007
Me.checkBoxAdv1.Office2007ColorScheme =
    Syncfusion.Windows.Forms.Office2007Theme.Managed
Office2007Colors.ApplyManagedColors(Me, Color.Pink)
```

![Figure 629: CheckBox displayed in "Pink"](insert_image_path)

**Figure 629: CheckBox displayed in "Pink"**

---

## API Reference

### Namespaces and Classes
- `Syncfusion.Windows.Forms.Tools`
  - **CheckBoxAdvStyle**: Defines the style for the CheckBoxAdv control.
  - **Office2007Theme**: Enum for Office 2007 color schemes.
  - **Office2007Colors**: Static class for applying custom colors.

### Methods
- **ApplyManagedColors**:
  - **Parameters**:
    - `control`: The control to apply the colors to.
    - `color`: The custom color to apply.
  - **Description**: Applies the specified custom color to the control when the theme is set to 'Managed'.

---

## Code Examples

The provided examples in both C# and VB demonstrate how to:
1. Set the style of the CheckBoxAdv to Office2007.
2. Configure the `Office2007ColorScheme` to 'Managed'.
3. Apply a custom color (e.g., `Color.Pink`) using the `ApplyManagedColors` method.

---

## Page-level Navigation/TOC
- [customizable color schemes](#custom-color-schemes-in-checkboxadv)
- [C# example](#c)
- [VB example](#vb)

---

<!-- tags: [CheckboxAdv, Office2007ColorScheme, Syncfusion, WinForms] keywords: [CustomColors, ManagedTheme, ApplyManagedColors, C#, VB] -->
```