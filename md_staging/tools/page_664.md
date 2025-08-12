```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_664.jpeg
document_name: tools
page_number: 664
page_id: tools#page_664
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:27:07Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates configuring and using **text primitives** and **image primitives** in Windows Forms applications.
- Shows how to position, size, and style text and images within a **GradientPanelExt**.
- Illustrates the use of **alignment**, **positioning**, and **border styles** for primitives.

## Content

### Configuring Text and Image Primitives

#### Text Primitive Example
Below is an example of configuring a `textPrimitive2`:

```csharp
Private Me.textPrimitive2.Position = 24
Private Me.textPrimitive2.Size = New System.Drawing.Size(150, 20)
Private Me.textPrimitive2.Text = "Text in Right Border"
Private Me.textPrimitive2.TextColor = System.Drawing.Color.DarkGreen
Private Me.textPrimitive2.TextFont = New System.Drawing.Font("Arial", 9.75F, (CType((System.Drawing.FontStyle.Bold Or System.Drawing.FontStyle.Italic), System.Drawing.FontStyle)), System.Drawing.GraphicsUnit.Point, (CByte(0)))
```

#### Image Primitive Examples
Here are examples of configuring `imagePrimitive3` and `imagePrimitive4`:

```csharp
' imagePrimitive3
Private Me.imagePrimitive3.Image = (CType(resources.GetObject("imagePrimitive3.Image"), System.Drawing.Image))
Private Me.imagePrimitive3.Position = 256
Private Me.imagePrimitive3.PrimitiveBorderStyle = Syncfusion.Windows.Forms.Tools.PrimitiveBorderStyle.None
Private Me.imagePrimitive3.Size = New System.Drawing.Size(20, 20)

' imagePrimitive4
Private Me.imagePrimitive4.Alignment = Syncfusion.Windows.Forms.Tools.Alignment.Bottom
Private Me.imagePrimitive4.Image = (CType(resources.GetObject("imagePrimitive4.Image"), System.Drawing.Image))
Private Me.imagePrimitive4.Position = 256
Private Me.imagePrimitive4.PrimitiveBorderStyle = Syncfusion.Windows.Forms.Tools.PrimitiveBorderStyle.None
```

#### Visual Representation
The following figure illustrates the use of a **GradientPanelExt** with text and image primitives:

![GradientPanelExt with Image and Text](image_and_text_primitives.png)

**Figure 408: GradientPanelExt with Image and Text**

### Explanation of Key Properties

- **Position**: Specifies the placement of the primitive within the container.
- **Size**: Defines the dimensions of the primitive.
- **Text**: Sets the text content for text primitives.
- **TextColor**: Sets the color of the text.
- **TextFont**: Specifies the font, size, style, and unit for the text.
- **Image**: Sets the image for image primitives.
- **PrimitiveBorderStyle**: Determines the border style for the primitive (e.g., `None`, `Flat`, `Rounded`, etc.).
- **Alignment**: Controls the positioning alignment for image primitives.

## See Also

### Additional Resources
- Documentation on **Syncfusion.Windows.Forms.Tools** for more details on configuring and using primitives.
- Examples and tutorials on customizing Windows Forms controls with advanced styling and positioning techniques.

<!-- tags: [winforms, primitives, text, image, gradientpanel, alignment, border styles] keywords: [text primitives, image primitives, GradientPanelExt, alignment, positioning, font styles, image alignment, border style] -->
```