```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_663.jpeg
document_name: tools
page_number: 663
page_id: tools#page_663
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:27:41Z
fidelity: lossless
-->

## Tools in Windows Forms

### Overview
- This section introduces the tools feature in Syncfusion.Windows.Forms, focusing on the use of `ImagePrimitive` and `TextPrimitive` objects.
- Demonstrates how to configure appearance and alignment settings for these primitives.
- Explains integration and configuration of primitives within a gradient panel.

### Content

#### Working with Primitives
This example showcases the configuration of `ImagePrimitive` and `TextPrimitive` objects within a gradient panel.

```csharp
Private imagePrimitive2 As Syncfusion.Windows.Forms.Tools.ImagePrimitive
Private imagePrimitive3 As Syncfusion.Windows.Forms.Tools.ImagePrimitive
Private imagePrimitive4 As Syncfusion.Windows.Forms.Tools.ImagePrimitive
Private textPrimitive1 As Syncfusion.Windows.Forms.Tools.TextPrimitive
Private textPrimitive2 As Syncfusion.Windows.Forms.Tools.TextPrimitive
Me.gradientPanelExt1.Primitives.AddRange(New Syncfusion.Windows.Forms.Tools.Primitive() { Me.imagePrimitive1, Me.imagePrimitive2, Me.textPrimitive1, Me.textPrimitive2, Me.imagePrimitive3, Me.imagePrimitive4})
```

---

##### Configuring `imagePrimitive1`
```csharp
' imagePrimitive1
Private Me.imagePrimitive1.Image = (CType(resources.GetObject("imagePrimitive1.Image"), System.Drawing.Image))
Private Me.imagePrimitive1.PrimitiveBorderStyle = Syncfusion.Windows.Forms.Tools.PrimitiveBorderStyle.None
Private Me.imagePrimitive1.Size = New System.Drawing.Size(20, 20)
```

---

##### Configuring `imagePrimitive2`
```csharp
' imagePrimitive2
Private Me.imagePrimitive2.Alignment = Syncfusion.Windows.Forms.Tools.Alignment.Bottom
Private Me.imagePrimitive2.Image = (CType(resources.GetObject("imagePrimitive2.Image"), System.Drawing.Image))
Private Me.imagePrimitive2.Position = 2
Private Me.imagePrimitive2.PrimitiveBorderStyle = Syncfusion.Windows.Forms.Tools.PrimitiveBorderStyle.None
Private Me.imagePrimitive2.Size = New System.Drawing.Size(20, 20)
```

---

##### Configuring `textPrimitive1`
```csharp
' textPrimitive1
Private Me.textPrimitive1.Alignment = Syncfusion.Windows.Forms.Tools.Alignment.Left
Private Me.textPrimitive1.Position = 21
Private Me.textPrimitive1.Size = New System.Drawing.Size(150, 20)
Private Me.textPrimitive1.Text = "Text in Left Border"
Private Me.textPrimitive1.TextColor = System.Drawing.Color.DarkOliveGreen
Private Me.textPrimitive1.Font = New System.Drawing.Font("Arial", 9.75F, (CType((System.Drawing.FontStyle.Bold Or System.Drawing.FontStyle.Italic), System.Drawing.FontStyle)), System.Drawing.GraphicsUnit.Point, (CByte(0)))
```

---

##### Configuring `textPrimitive2`
```csharp
' textPrimitive2
Private Me.textPrimitive2.Alignment = Syncfusion.Windows.Forms.Tools.Alignment.Right
```

## API Reference
### Namespaces Used
- `Syncfusion.Windows.Forms.Tools`
- `System.Drawing`

### Methods/Properties
- `primitiveGradientPanelExt1.Primitives.AddRange`: Adds primitives to the gradient panel.
- `Primitive.Image`: Property to set the image for the `ImagePrimitive`.
- `Primitive.Alignment`: Property to set the alignment of primitives.
- `Primitive.PrimitiveBorderStyle`: Property to set the border style of primitives.
- `Primitive.Size`: Property to set the size of primitives.
- `TextPrimitive.Text`: Property to set the text content.
- `TextPrimitive.Font`: Property to define the font style, size, and other attributes of the text.

## Code Examples
The example demonstrates setting up and configuring multiple primitives, including image and text primitives, within a Syncfusion gradient panel. This can be useful for creating visually dynamic interfaces with alignment and styling options.

## Cross References
See also:
- [Handling Events in Windows Forms](#event-handling-in-winforms)
- [Customizing Controls with Syncfusion](#customizing-controls-with-syncfusion)

<!-- tags: [Syncfusion, Windows Forms, Gradient Panel, Primitive, ImagePrimitive, TextPrimitive] keywords: [PrimitiveBorderStyle, Alignment, GradientPanel, Image, Text] -->
```