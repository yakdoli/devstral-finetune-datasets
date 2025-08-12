```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_506.jpeg
document_name: tools
page_number: 506
page_id: tools#page_506
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:17:45Z
fidelity: lossless
-->

## Overview
- Explains the discrepancy between the .NET framework's color dialog control and the ColorUIControl provided by Essential Tools.
- Details how to use the ColorUIControl for color selection at runtime within Windows Forms applications.

## Content

### ColorUIControl Overview

**Figure 292: ColorUIControl**

The .NET framework provides a color dialog control which allows applications to collect color information from users. However, the color dialog control does not provide any way to place a control within the layout of the application in order to collect color information. The Essential Tools ColorUIControl provides an easy-to-use color palette control that can be placed inline in applications.

The ColorUIControl implements a palette-type visual interface for selecting colors at runtime. The ColorUIControl class offers a selection of colors that are divided into four color groupings, which are arranged as tabs. The four color groupings are:

- **SystemColors**: Consisting of colors defined within the SystemColors class.
- **StandardColors**: Consisting of basic colors.
- **CustomColors**: Providing a customizable color palette.
- **UserColors**: Providing different shades of user-defined colors.

## API Reference

### Namespace and Class
- Namespace: `Syncfusion.Windows.Forms.Tools`
- Class: `ColorUIControl`

### Properties
- **ColorUIControl.Events**: Handles events for color selection.
- **ColorUIControl.TabItems**: Defines the tabs for different color groupings.

## Code Examples

### C# Example

```csharp
using Syncfusion.Windows.Forms.Tools;

// Create instance of ColorUIControl
ColorUIControl colorUIControl = new ColorUIControl();

// Add ColorUIControl to Form
this.Controls.Add(colorUIControl);

// Handle Color Selection
colorUIControl.ColorSelected += new ColorUISelectedEventHandler(ColorUI_Selected);

void ColorUI_Selected(object sender, ColorUISelectedEventArgs e)
{
    // Retrieve selected color
    Color selectedColor = e.SelectedColor;
    // Use selected color as needed
}
```

## Cross References
- Refer to the "ColorUIControl Methods" section for more method-specific details.
- For a comprehensive color palette implementation, consult the "SystemColors" and "CustomColors" sections.

<!-- tags: [coloruicontrol, windowsforms, syncfusion, colordialogcontrol] keywords: [color palette, color selection, runtime selection, windows forms, color dialog, coloruiimplementation] -->
```