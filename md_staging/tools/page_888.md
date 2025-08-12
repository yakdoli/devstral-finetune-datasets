```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_888.jpeg
document_name: tools
page_number: 888
page_id: tools#page_888
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:40:42Z
fidelity: lossless
-->

## Overview

- Describes how to customize the appearance of `NumericUpDownExt` control in Windows Forms using Syncfusion's `ColorScheme` property set to 'Managed'.
- Demonstrates programmatically setting Office 2007 Visual Styles and applying custom colors.
- Includes sample code snippets for C# and VB.NET, along with a note about the `ThemesEnabled` property.
- Mentions a sample project path for further exploration of themes and styles.

## Content

### Essential Tools for Windows Forms

#### Office 2007 Visual Styles

**Figure 564: Office 2007 Visual Styles**

When the `ColorScheme` property is set to 'Managed', the `NumericUpDownExt` control can be displayed using custom colors supported by the control.

**This can be done programmatically as follows.**

##### C#

```csharp
this.numericUpdownExt1.VisualStyle = 
Syncfusion.Windows.Forms.VisualStyle.Office2007;
this.numericUpdownExt1.ColorScheme = 
Syncfusion.Windows.Forms.Office2007Theme.Managed;
Office2007Colors.ApplyManagedColors(this, Color.Orange);
```

##### VB.NET

```vb.net
Me.numericUpdownExt1.VisualStyle = 
Syncfusion.Windows.Forms.VisualStyle.Office2007
Me.numericUpdownExt1.ColorScheme = 
Syncfusion.Windows.Forms.Office2007Theme.Managed;
Office2007Colors.ApplyManagedColors(Me, Color.Orange)
```

**Figure 565: `NumericUpDownExt` displayed in "Orange"**

---

**Note:** The `ThemesEnabled` property should be set to 'True' for the above settings to take effect.

A sample which demonstrates the `ThemesEnabled` property and Office 2007 Visual Styles of `TextBoxExt` control is available in the below sample installation path:

```
..My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Tools.Windows\Samples\2.0\Editors Package\EditorControls
```

### 3.5.8.9.4 `NumericUpDownExt` Events

**The list of events and a detailed explanation about each of them is given in the following sections.**

---

## API Reference

### Events
- Detailed information about each `NumericUpDownExt` event is covered in subsequent sections.

## Code Examples

### Customizing Colors in `NumericUpDownExt`
The provided C# and VB.NET code snippets show how to apply custom colors to the `NumericUpDownExt` control using the `Office2007Colors.ApplyManagedColors` method.

## Page-level Navigation/TOC

### Local TOC
- [x] Office 2007 Visual Styles
- [x] `NumericUpDownExt` Events

## Cross References

See also:
- [ThemesEnabled property](#)
- [Office 2007 Colors](#)
- [Sample Installation Path](#)

## RAG Annotations

<!-- tags: [Syncfusion Winforms, NumericUpDownExt, Office 2007 Visual Styles, ThemesEnabled] keywords: [NumericUpDownExt, ColorScheme, Managed, Office2007Colors, ApplyManagedColors, ThemesEnabled, Office2007Theme, VisualStyle, custom colors, sample installation path, C#, VB.NET] -->
```