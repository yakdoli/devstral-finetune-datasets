```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_894.jpeg
document_name: tools
page_number: 894
page_id: tools#page_894
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:41:30Z
fidelity: lossless
-->

## Overview

This page discusses the customization options for the TextBoxExt control in Syncfusion WinForms. It covers setting border colors, layout settings, and applying themes. Key features such as different border colors, text overflow indicators, and theme support are highlighted. Additionally, a step-by-step guide for creating a TextBoxExt control using both the designer and a programmatic approach is provided.

## Main Content

### TextBoxExt Control Properties

#### BorderColor Property
- The color of the border can be set for the control using the `BorderColor` property.

#### Layout Settings
- The maximum and minimum size of the control can be set.

#### Applying Themes
- Themed appearance can be provided for the TextBoxExt control.

### Key Features of TextBoxExt
- **Provides different border colors and styles.**
- **Provides options to show text overflow indicators and overflow indicator tooltips.**
- **Supports themes.**

### Creating TextBoxExt

#### Section 3.5.8.10.2: Creating TextBoxExt
This section provides a step-by-step procedure to design a TextBoxExt control through the designer and also through a programmatic approach.

##### Through Designer

1. Create or open a Windows Forms project.
2. [Insert additional step if needed]
3. Click on the TextBoxExt Control in the toolbox and add it to the form by dragging and dropping it onto the form or by double-clicking the control.

##### Figure 567: TextBoxExt in Toolbox

![TextBoxExt in Toolbox](https://example.com/figure_567.png "Figure 567: TextBoxExt in Toolbox")

## API Reference

### Properties: `BorderColor`
- **Description**: The `BorderColor` property controls the color of the border around the TextBoxExt control.
- **Type**: Color
- **Default Value**: Instance specific (typically the default system color)

### Properties: `MinimumSize` and `MaximumSize`
- **Description**: These properties allow setting the maximum and minimum size of the control.
- **Type**: Size
- **Default Value**: Instance specific (default is no restriction)

### Properties: `Theme`
- **Description**: The `Theme` property enables applying specific themes to the TextBoxExt control for a consistent appearance.
- **Type**: Theme
- **Default Value**: Instance specific (typically the default system theme)

## Code Examples

### Programmatic Approach

```csharp
using Syncfusion.Windows.Forms.Tools;
using System.Drawing;
using System.Windows.Forms;

public class Form1 : Form
{
    private TextBoxExt textBoxExt1;

    public Form1()
    {
        InitializeComponent();
    }

    private void InitializeComponent()
    {
        textBoxExt1 = new TextBoxExt();
        this.Controls.Add(textBoxExt1);

        // Setting BorderColor
        textBoxExt1.BorderColor = Color.Orange;

        // Setting MinimumSize and MaximumSize
        textBoxExt1.MinimumSize = new Size(100, 20);
        textBoxExt1.MaximumSize = new Size(200, 40);

        // Applying Theme
        textBoxExt1.ThemeName = "Windows7";
    }
}
```

## Cross References

- **Related Controls**: Other Syncfusion WinForms controls such as CurrencyEdit, CurrencyTextBox, DoubleTextBox, etc.
- **Additional Documentation**: Refer to the full Syncfusion WinForms documentation for more advanced customization options and examples.

<!-- tags: [TextBoxExt, Windows Forms, BorderColor, Layout Settings, Themes, Designer, Programmatic, Syncfusion] keywords: [TextOverflow, KeyFeatures, ControlProperties, DesignProcedure, ThemeName, MinimumSize, MaximumSize, BorderColor, Theme] -->
```