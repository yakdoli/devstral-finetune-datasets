```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_672.jpeg
document_name: tools
page_number: 672
page_id: tools#page_672
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:27:36Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes GradientPanelExt with a Background Image
- Details customization of text properties using Font and ForeColor
- Provides code samples for altering text and color properties in C# and VB.NET

## Content

### GradientPanelExt with a Background Image

![Figure 414: GradientPanelExt with a Background Image](assets/tools-gradientpanelext-background-image.png)

Figure 414: GradientPanelExt with a Background Image

#### Foreground

The control's text can be customized by altering its **Font** properties. The **ForeColor** property represents the GradientPanelExt's text color. Using the following code snippet customizes the foreground of the GradientPanelExt.

#### Code Snippets

##### C#

```csharp
this.gradientPanelExt1.Font = new System.Drawing.Font(
    "Comic Sans MS",
    9.75F,
    ((System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic | System.Drawing.FontStyle.Underline))),
    System.Drawing.GraphicsUnit.Point,
    ((byte)(0))
);
this.gradientPanelExt1.ForeColor = System.Drawing.Color.DarkGreen;
```

##### VB.NET

```vb
Private Me.gradientPanelExt1.Font = New System.Drawing.Font(
    "Comic Sans MS",
    9.75F,
    (CType(((System.Drawing.FontStyle.Bold Or System.Drawing.FontStyle.Italic) Or System.Drawing.FontStyle.Underline), System.Drawing.FontStyle)),
    System.Drawing.GraphicsUnit.Point,
    (CByte(0))
)
Private Me.gradientPanelExt1.ForeColor = System.Drawing.Color.DarkGreen
```

## API Reference

### Properties

- **Font**: Represents the font used to display the text.
- **ForeColor**: Represents the text color of the GradientPanelExt.

## Code Examples

The provided examples demonstrate how to modify the font and foreground color properties of the GradientPanelExt control.

## See also

- Syncfusion Winforms documentation for further customization options.

<!-- tags: [product, gradientpanelext, font, forecolor, windowsforms] keywords: [gradientpanelext, font, forecolor, windowsforms, customization, text properties, code snippet] -->
```