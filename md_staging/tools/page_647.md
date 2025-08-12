```html
<!-------START OF META------->
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_647.jpeg
document_name: tools
page_number: 647
page_id: tools#page_647
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:26:42Z
fidelity: lossless
-->
<!-------END OF META-------

## Overview
- Demonstrates how to customize the appearance of a GradientPanel control by applying gradient backgrounds and modifying foreground text properties.
- Includes examples in both C# and VB.NET for setting the Font and ForeColor properties of the GradientPanel.

## Content

### Gradient Background
The background of the GradientPanel can be customized using properties such as `BackColor` and a gradient brush.

#### Example: Setting Gradient Background
```csharp
Me.gradientPanel1.BackColor = System.Drawing.Color.LightCoral
Me.gradientPanel1.BackColor = New Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.PathRectangle, System.Drawing.Color.AliceBlue, System.Drawing.Color.SteelBlue)
```
#### Result: Gradient Panel with Gradient Background
![Gradient Panel with Gradient Background](images/gradient_panel_gradient_background.png)

**Figure 396: Gradient Panel with Gradient Background**

### Foreground Settings
The foreground text in the control can be customized using the below properties.

#### Table: GradientPanel Properties and Descriptions
| GradientPanel Properties | Description |
|---------------------------|-------------|
| Font                      | Indicates the Font style of the text in the control. |
| ForeColor                 | Indicates the color of the text and graphics in the control. |

#### Example: Customizing Font and ForeColor in C#
```csharp
this.gradientPanel1.Font = new System.Drawing.Font("Verdana", 8.25F, System.Drawing.FontStyle.Bold);
this.gradientPanel1.ForeColor = System.Drawing.Color.Blue;
```

#### Example: Customizing Font and ForeColor in VB.NET
```vb.net
Me.GradientPanel1.Font = New System.Drawing.Font("Comic Sans MS", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(0, Byte))
this.gradientPanel1.ForeColor = System.Drawing.Color.Blue;
```

#### Result: Gradient Panel with FontStyle
![Gradient Panel with FontStyle](images/gradient_panel_font_styled.png)

**Figure 397: Gradient Panel with FontStyle**

### Page-Level Navigation/TOC
- Gradient Background
- Foreground Settings

### Cross References
- See also: Documentation on Customizing Controls in Syncfusion Winforms.

### RAG Annotations
<!-- tags: gradient panel, custom controls, winforms srv, gradient background, foreground settings, syncfusion winforms, version 11.4.0.26 -->
```