```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_389.jpeg
document_name: tools
page_number: 389
page_id: tools#page_389
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:09:17Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Background Color

The background of the Calculator can be painted using the below properties.

| Calculatorcontrol Properties        | Description                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| BackColor                          | Specifies BackColor of the Calculator control.                                               |
| BackgroundColor                    | Sets the gradient background for the control. This setting overrides the BackColor property. |

### Example Code: Setting Background Properties

```csharp
[C#]
this.calculatorControl1.BackColor = System.Drawing.Color.WhiteSmoke;
this.calculatorControl1.BackColor = new Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.Vertical, System.Drawing.Color.WhiteSmoke, System.Drawing.Color.SlateGray);
```

```vbnet
[VB.NET]
Me.calculatorControl1.BackColor = System.Drawing.Color.WhiteSmoke
Me.calculatorControl1.BackColor = New Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.Vertical, System.Drawing.Color.WhiteSmoke, System.Drawing.Color.SlateGray)
```

**Figure 194: GradientStyle = "Vertical"; BackColor = "WhiteSmoke"; BackgroundColor = "SlateGray"**

## Background Image

The background of the Calculator control can be filled with an image using BackgroundImage property.

### Overview of Background Properties

1. **Back Color**: Specifies a solid color for the background.
2. **Background Color**: Sets a gradient background style.
3. **Background Image**: Allows the use of an image for the background.

### Summary

- **Background Properties**: Provide flexibility in customizing the appearance of the Calculator control.
- **Example Usage**: Demonstrates setting a vertical gradient background with specific colors.

### Cross References
- Refer to the documentation on **BackgroundImage** property for more details.

<!-- tags: [Syncfusion Winforms, GradientStyle, BackColor, BackgroundColor, BackgroundImage] keywords: [Calculator control, vertical gradient, background properties, custom background, gradient background] -->
```
