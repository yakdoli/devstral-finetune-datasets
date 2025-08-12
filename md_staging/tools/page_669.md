```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_669.jpeg
document_name: tools
page_number: 669
page_id: tools#page_669
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:26:36Z
fidelity: lossless
-->

## Overview
- This page explains the essential tools for Windows Forms, focusing on the `GradientPanelExt` control and its methods for setting colors and styles using `BackColor` properties.

## Content

### GradientPanelExt with BackColor Set

![GradientPanelExt with BackColor Set](GradientPanel.png)

*Figure 411: GradientPanelExt with BackColor Set*

The colors and styles of the `GradientPanelExt` control can be set using the `BackColor` properties, which have been explained below:

- **Style** - The styles available are solid, pattern, and gradient.
- **BackColor** - User can select the required colors for the background using the `BackColor` property.
- **ForeColor** - Foreground color, for text or graphics, can be set using the `ForeColor` property.
- **PatternStyle** - Provides the pattern styles available for the selected style.
- **GradientColors** - This pops up the Color Collection Editor, which allows the user to add colors and get a combination of colors to display in the gradient panel with the specified style.

### GradientPanelExt Properties

| GradientPanelExt Properties       | Description                                                                |
|------------------------------------|----------------------------------------------------------------------------|
| **Style**                          | Specifies the brush style (Solid, Pattern, Gradient).                     |
| **BackColor**                      | Gets or sets the back color.                                             |
| **ForeColor**                      | Gets or sets the fore color.                                             |
| **PatternStyle**                   | Gets or sets specifies the pattern style.                                |
| **GradientColor**                  | Specifies the gradient colors, with the first color same as `BackColor` and the last color same as `ForeColor`. |
| **BackgroundImage**                | Specifies the background image for the control.                           |

## API Reference

### WinForms-specific Conventions

- The control names, namespaces, and types are treated exactly.
- Design-time vs. runtime features are distinguished.

### Properties

- **Style**: Specifies the brush style.
- **BackColor**: Gets or sets the back color.
- **ForeColor**: Gets or sets the fore color.
- **PatternStyle**: Specifies the pattern style.
- **GradientColor**: Specifies the gradient colors.
- **BackgroundImage**: Specifies the background image for the control.

### Code Examples

#### C# Example

```csharp
using Syncfusion.Windows.Forms.Tools;

GradientPanelExt gradientPanel = new GradientPanelExt();
gradientPanel.Style = GradientPanelExt.GradientPanelStyle.Gradient;
gradientPanel.BackColor = Color.Pink;
gradientPanel.ForeColor = Color.Navy;
gradientPanel.PatternStyle = GradientPanelExt.GradientPanelPatternStyle.Diagonal;
gradientPanel.GradientColors = new[] { Color.Pink, Color.Navy };

// Set the gradient colors manually
gradientPanel.GradientColors = new[] { Color.Yellow, Color.Blue, Color.Green };
gradientPanel.BackgroundImage = Properties.Resources.MyImage;

MyForm.Controls.Add(gradientPanel);
```

## Cross References

See also:
- Integration of `GradientPanelExt` with other controls in Windows Forms.
- Additional documentation on WinForms controls and their properties.

<!-- tags: Syncfusion, WinForms, tools, GradientPanelExt, BackColor, ForeColor, PatternStyle, GradientColors, BackgroundImage keywords: styles, colors, configuration, settings, gradient panel -->
```