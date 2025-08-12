```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_723.jpeg
document_name: tools
page_number: 723
page_id: tools#page_723
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:31:33Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This page discusses the DomainUpDownExt control in Syncfusion Winforms, focusing on its themes, custom colors, and appearance settings.
- Includes examples in C# and VB.NET for applying custom colors.
- Provides a detailed explanation of appearance properties such as BorderStyle.

## Content

### Custom Colors

We can also apply custom colors to the DomainUpDownExt control by setting `ColorScheme` to "Managed" and specifying the custom color through the `ApplyManagedColors` method as follows.

#### Code Example: Applying Custom Colors

[C#]

```csharp
this.domainUpDownExt1.ColorScheme =
    Syncfusion.Windows.Forms.Office2007Theme.Managed;
Office2007Colors.ApplyManagedColors(this, Color.Orange);
```

[VB.NET]

```vbnet
Me.domainUpDownExt1.ColorScheme =
    Syncfusion.Windows.Forms.Office2007Theme.Managed
Office2007Colors.ApplyManagedColors(Me, Color.Orange)
```

#### Figure: Custom Color

![Custom Color = "Orange"](image_for_Figure_455)

*Figure 455: Custom Color = "Orange"*

### 3.5.8.2.3.4 Appearance Settings

This section discusses the border styles and back color that can be applied for DomainUpDownExt control.

The below table lists the appearance properties of DomainUpDownExt control.

| DomainUpDownExt Properties | Description |
|-----------------------------|-------------|
| BorderStyle                | Specifies the border style for the control. The options include FixedSingle, |

## API Reference

### Namespace: Syncfusion.Windows.Forms

#### Class: DomainUpDownExt

##### Properties
- **BorderStyle**: <br />
Specifies the border style for the control.

##### Methods
- **ApplyManagedColors**: <br />
Applies custom managed colors to the control.

## Code Examples

### C# Example: Applying Custom Colors

```csharp
this.domainUpDownExt1.ColorScheme =
    Syncfusion.Windows.Forms.Office2007Theme.Managed;
Office2007Colors.ApplyManagedColors(this, Color.Orange);
```

### VB.NET Example: Applying Custom Colors

```vbnet
Me.domainUpDownExt1.ColorScheme =
    Syncfusion.Windows.Forms.Office2007Theme.Managed
Office2007Colors.ApplyManagedColors(Me, Color.Orange)
```

## Page-level Navigation/TOC

- [Custom Colors]
- [Appearance Settings]
- [Code Examples]

## Cross References

- Refer to the Syncfusion Winforms documentation for more details on themes and styling.

## RAG Annotations

<!-- tags: [syncfusion-sdk, DomainUpDownExt, themes, custom colors, appearance settings, WinForms] keywords: [colorScheme, ApplyManagedColors, BorderStyle, Office2007Theme, customColor, orange] -->
```