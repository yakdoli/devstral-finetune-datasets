```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_109.jpeg
document_name: diagram
page_number: 109
page_id: diagram#page_109
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:15:40Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- An introduction to setting up and applying node property settings in the Essential Diagram control for Windows Forms.
- Explains property configurations and examples for customizing node style and behavior.

## Content

### Node Property Settings
The following code example demonstrates how to apply node property settings.

#### Figure 63: Diagram with Node Sample
![Diagram with Node Sample](#)

**Example: Applying Node Property Settings**

[C#]

```csharp
private void Form1_Load(object sender, EventArgs e)
{
    Syncfusion.Windows.Forms.Diagram.Ellipse ellipse = new Syncfusion.Windows.Forms.Diagram.Ellipse(10, 10, 110, 70);
    diagram1.Model.AppendChild(ellipse);
    ellipse.FillStyle.Color = System.Drawing.Color.AliceBlue;
    ellipse.FillStyle.ColorAlphaFactor = 100;
    ellipse.FillStyle.ForeColor = System.Drawing.Color.Aquamarine;
    ellipse.FillStyle.ForeColorAlphaFactor = 70;
    ellipse.FillStyle.Type = FillStyleType.PathGradient;
    ellipse.FillStyle.PathBrushStyle = PathGradientBrushStyle.RectangleCenter;

    ellipse.FillStyle.Type = FillStyleType.LinearGradient;
    ellipse.FillStyle.GradientAngle = 95;
    ellipse.FillStyle.GradientCenter = 0.5f;

    ellipse.EditStyle.AllowChangeHeight = true;
    ellipse.EditStyle.AllowChangeWidth = true;
    ellipse.EditStyle.AllowDelete = false;
    ellipse.EditStyle.AllowMoveX = true;
    ellipse.EditStyle.AllowMoveY = false;
    ellipse.EditStyle.AllowRotate = false;
    ellipse.EditStyle.AllowSelect = true;
}
```

### Notes
- The example demonstrates setting various properties of an ellipse node in a `Diagram` control, focusing on fill styles and edit styles.
- The fl style properties include color, opacity, and gradient patterns for custom visualization.
- The edit style properties control how the node interacts with user actions, such as resizing, moving, or selecting.

## API Reference
- **Namespace:** Syncfusion.Windows.Forms.Diagram
- **Class:** Diagram, Ellipse
- **Properties:**
  - FillStyle.Color
  - FillStyle.ColorAlphaFactor
  - FillStyle.ForeColor
  - FillStyle.ForeColorAlphaFactor
  - FillStyle.Type
  - FillStyle.PathBrushStyle
  - FillStyle.GradientAngle
  - FillStyle.GradientCenter
  - EditStyle.AllowChangeHeight
  - EditStyle.AllowChangeWidth
  - EditStyle.AllowDelete
  - EditStyle.AllowMoveX
  - EditStyle.AllowMoveY
  - EditStyle.AllowRotate
  - EditStyle.AllowSelect

### Parameters
| Name | Description |
|------|-------------|
| ellipse | The Ellipse object to apply property settings to. |

### Exceptions
- None explicitly defined in the example.

## Code Examples
- The example provided demonstrates how to integrate and customize node properties within a Windows Forms application using the Syncfusion Diagram control.

### Related Topics
- Refer to the documentation for further details on the advanced customization of nodes and styles.

<!-- tags: [diagram, windows forms, node property settings, fill style, edit style] keywords: [Syncfusion, ellipse, Windows Forms, Diagram, FillStyle, EditStyle] -->
```
