```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_930.jpeg
document_name: tools
page_number: 930
page_id: tools#page_930
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:43:35Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- Demonstrates how to apply Office 2007 color schemes to the FontComboBox control in Windows Forms.
- Provides examples in both C# and VB.NET for setting different Office 2007 themes and custom colors.
- Includes visual examples of the different color schemes and custom color application.

## Content

### Office 2007 Color Schemes for the FontComboBox Control

The following code snippet demonstrates how to apply different Office 2007 color schemes to a `FontComboBox` control using VB.NET:

```vb
Me.fontComboBox2VisualStyle = Syncfusion.Windows.Forms.Tools.ThemedComboBoxStyles.Office2007
Me.fontComboBox2.Office2007ColorTheme = Syncfusion.Windows.Forms.Office2007Theme.Silver
```

**Figure 593: Office2007 Color Schemes for the FontComboBox Control**

![Office2007 Color Schemes](image.png)

### Custom Colors

We can also apply custom colors to the FontComboBox control by setting `Office2007ColorTheme` to "Managed" and specifying the custom color through the `ApplyManagedColors` method as follows.

#### Example in C#

```csharp
this.fontComboBox2.Office2007ColorTheme = Syncfusion.Windows.Forms.Office2007Theme.Managed;
Office2007Colors.ApplyManagedColors(this, Color.Orchid);
```

#### Example in VB.NET

```vb
Me.fontComboBox2.Office2007ColorTheme = Syncfusion.Windows.Forms.Office2007Theme.Managed
Office2007Colors.ApplyManagedColors(Me, Color.Orchid)
```

**Figure 594: Custom Color = "Orchid"**

![Custom Color](image.png)

## API Reference

### Properties
- `VisualStyle`: Specifies the visual style of the control.
- `Office2007ColorTheme`: Specifies the color theme for the Office 2007 theme.
- `ApplyManagedColors`: Applies a custom color to the control.

### Methods
- `ApplyManagedColors`: Applies a custom color to the FontComboBox control.

## Code Examples

### C#

```csharp
this.fontComboBox2.Office2007ColorTheme = Syncfusion.Windows.Forms.Office2007Theme.Managed;
Office2007Colors.ApplyManagedColors(this, Color.Orchid);
```

### VB.NET

```vb
Me.fontComboBox2.Office2007ColorTheme = Syncfusion.Windows.Forms.Office2007Theme.Managed
Office2007Colors.ApplyManagedColors(Me, Color.Orchid)
```

## Page-level Navigation/TOC (if applicable)

- [Office 2007 Color Schemes for the FontComboBox Control](#office-2007-color-schemes-for-the-fontcombobox-control)
- [Custom Colors](#custom-colors)

## Cross References

See also:
- [Syncfusion Windows Forms Documentation](#syncfusion-windows-forms-documentation)

<!-- tags: [Syncfusion, Windows Forms, FontComboBox, Office 2007 Themes, Custom Colors, VB.NET, C#] keywords: [FontComboBox, Office 2007, Color Themes, Custom Colors, Visual Style, ApplyManagedColors] -->
```