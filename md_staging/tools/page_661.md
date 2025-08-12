```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_661.jpeg
document_name: tools
page_number: 661
page_id: tools#page_661
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:25:59Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

Images and text can be included as individual primitives for the **GradientPanelExt**.

The image to be included, should be referenced in the **Image** property available for the primitive in the **GradientPanelExt Collection Editor**.

The text for text primitive, can be specified using the **Text** property available for the primitive in the **GradientPanelExt Collection Editor**. The text font and color can also be defined for the text primitive, using the **TextFont** and **TextColor** properties, respectively.

```csharp
[C#]

// Defining Primitives and Adding them
private Syncfusion.Windows.Forms.Tools.ImagePrimitive imagePrimitive1;
private Syncfusion.Windows.Forms.Tools.ImagePrimitive imagePrimitive2;
private Syncfusion.Windows.Forms.Tools.ImagePrimitive imagePrimitive3;
private Syncfusion.Windows.Forms.Tools.ImagePrimitive imagePrimitive4;
private Syncfusion.Windows.Forms.Tools.TextPrimitive textPrimitive1;
private Syncfusion.Windows.Forms.Tools.TextPrimitive textPrimitive2;
this.gradientPanelExt1.Primitives.AddRange(new Syncfusion.Windows.Forms.Tools.Primitive[] {
    this.imagePrimitive1,
    this.imagePrimitive2,
    this.textPrimitive1,
    this.textPrimitive2,
    this.imagePrimitive3,
    this.imagePrimitive4});

// imagePrimitive1
this.imagePrimitive1.Image =
    (System.Drawing.Image)(resources.GetObject("imagePrimitive1.Image"));
this.imagePrimitive1.PrimitiveBorderStyle =
    Syncfusion.Windows.Forms.Tools.PrimitiveBorderStyle.None;
this.imagePrimitive1.Size = new System.Drawing.Size(20, 20);

// imagePrimitive2
this.imagePrimitive2.Alignment =
    Syncfusion.Windows.Forms.Tools.Alignment.Bottom;
this.imagePrimitive2.Image =
    (System.Drawing.Image)(resources.GetObject("imagePrimitive2.Image"));
this.imagePrimitive2.Position = 2;
this.imagePrimitive2.PrimitiveBorderStyle =
    Syncfusion.Windows.Forms.Tools.PrimitiveBorderStyle.None;
this.imagePrimitive2.Size = new System.Drawing.Size(20, 20);
```

```html
<!-- tags: [Windows Forms, GradientPanelExt, ImagePrimitive, TextPrimitive, primitive, image, text, C#, Syncfusion] keywords: [PrimitiveBorderStyle, Alignment, Position, ImagePrimitive, TextPrimitive, GradientPanelExt, resourceObject, size, alignment, design, textPrimitive1, textPrimitive2, imagePrimitive2, imagePrimitive1] -->
```