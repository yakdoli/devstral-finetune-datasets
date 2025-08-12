```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_662.jpeg
document_name: tools
page_number: 662
page_id: tools#page_662
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:27:16Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Code Examples (C#)

```csharp
// textPrimitive1
this.textPrimitive1.Alignment = Syncfusion.Windows.Forms.Tools.Alignment.Left;
this.textPrimitive1.Position = 21;
this.textPrimitive1.Size = new System.Drawing.Size(150, 20);
this.textPrimitive1.Text = "Text in Left Border";
this.textPrimitive1.TextColor = System.Drawing.Color.DarkOliveGreen;
this.textPrimitive1.TextFont = new System.Drawing.Font("Arial", 9.75F, (System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic)), System.Drawing.GraphicsUnit.Point, ((byte)(0)));

// textPrimitive2
this.textPrimitive2.Alignment = Syncfusion.Windows.Forms.Tools.Alignment.Right;
this.textPrimitive2.Position = 24;
this.textPrimitive2.Size = new System.Drawing.Size(150, 20);
this.textPrimitive2.Text = "Text in Right Border";
this.textPrimitive2.TextColor = System.Drawing.Color.DarkGreen;
this.textPrimitive2.TextFont = new System.Drawing.Font("Arial", 9.75F, (System.Drawing.FontStyle)((System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic)), System.Drawing.GraphicsUnit.Point, ((byte)(0)));

// imagePrimitive3
this.imagePrimitive3.Image = ((System.Drawing.Image)(resources.GetObject("imagePrimitive3.Image")));
this.imagePrimitive3.Position = 256;
this.imagePrimitive3.PrimitiveBorderStyle = Syncfusion.Windows.Forms.Tools.PrimitiveBorderStyle.None;
this.imagePrimitive3.Size = new System.Drawing.Size(20, 20);

// imagePrimitive4
this.imagePrimitive4.Alignment = Syncfusion.Windows.Forms.Tools.Alignment.Bottom;
this.imagePrimitive4.Image = ((System.Drawing.Image)(resources.GetObject("imagePrimitive4.Image")));
this.imagePrimitive4.Position = 256;
this.imagePrimitive4.PrimitiveBorderStyle = Syncfusion.Windows.Forms.Tools.PrimitiveBorderStyle.None;
this.imagePrimitive4.Size = new System.Drawing.Size(20, 20);
```

### Code Examples (VB.NET)

```vb
' Defining Primitives and Adding them
Private imagePrimitive1 As Syncfusion.Windows.Forms.Tools.ImagePrimitive
```

## RAG Annotations
<!-- tags: [Syncfusion Winforms, Essential Tools, Alignment, Text, Image, Primitive] keywords: [textPrimitive, imagePrimitive, Alignment, Position, Size, TextColor, TextFont, FontStyle, PrimitiveBorderStyle] -->
``` 
