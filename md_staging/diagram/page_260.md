```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_260.jpeg
document_name: diagram
page_number: 260
page_id: diagram#page_260
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:22:39Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

```csharp
selectedNode.LineStyle.LineWidth),
    Convert.ToInt32(selectedNode.Size.Height +
    selectedNode.LineStyle.LineWidth));
    
using (Graphics gr = Graphics.FromImage(bmp))
{
    System.Drawing.Drawing2D.Matrix m = new
        System.Drawing.Drawing2D.Matrix();
    m.Translate(Convert.ToInt32(-
    selectedNode.BoundingBox.Left), Convert.ToInt32(-
    selectedNode.BoundingBox.Top));
    gr.Transform = m;
    
    // This will render the node image in a graphics surface and we
    // can export it easily to any type of image.
    selectedNode.Draw(gr);
    bmp.Save("image.png", System.Drawing.Imaging.ImageFormat.Png);
    Process.Start("image.png");
}
}
```

### [VB.NET]

```vb
Dim selectedNode As Syncfusion.Windows.Forms.Diagram.Node = 
    Me.Diagram1.Controller.SelectionList(0)
If selectedNode IsNot Nothing Then
    ' Node size depends on the border line. So we have to calculate the
    ' Line width also.
    Dim bmp As New Bitmap(Convert.ToInt32(selectedNode.Size.Width +
    selectedNode.LineStyle.LineWidth),
    Convert.ToInt32(selectedNode.Size.Height +
    selectedNode.LineStyle.LineWidth))
    Using gr As Graphics = Graphics.FromImage(bmp)
        Dim m As New System.Drawing.Drawing2D.Matrix()
        m.Translate(Convert.ToInt32(-
        selectedNode.BoundingBox.Left), Convert.ToInt32(-
        selectedNode.BoundingBox.Top))
        gr.Transform = m
        
        ' This will render the node image in a graphics surface and we
        ' can export it easily to any type of image.
        selectedNode.Draw(gr)
        bmp.Save("image.png", System.Drawing.Imaging.ImageFormat.Png)
        Process.Start("image.png")
    End Using
End If
```

## API Reference
- `void Convert.ToInt32(object value)`
- `void Convert.ToInt32(string value)`
- `void System.Drawing.Drawing2D.Matrix.Translate(float dx, float dy)`
- `void System.Drawing.Imaging.ImageFormat.Png`

## Code Examples

### C#
```csharp
Bitmap bmp = new Bitmap(Convert.ToInt32(selectedNode.Size.Width + 
    selectedNode.LineStyle.LineWidth),
    Convert.ToInt32(selectedNode.Size.Height +
    selectedNode.LineStyle.LineWidth));

using (Graphics gr = Graphics.FromImage(bmp))
{
    System.Drawing.Drawing2D.Matrix m = new
        System.Drawing.Drawing2D.Matrix();
    m.Translate(Convert.ToInt32(-
    selectedNode.BoundingBox.Left), Convert.ToInt32(-
    selectedNode.BoundingBox.Top));
    gr.Transform = m;
    selectedNode.Draw(gr);
    bmp.Save("image.png", System.Drawing.Imaging.ImageFormat.Png);
    Process.Start("image.png");
}
```

### VB.NET
```vb
Dim bmp As New Bitmap(Convert.ToInt32(selectedNode.Size.Width +
    selectedNode.LineStyle.LineWidth),
    Convert.ToInt32(selectedNode.Size.Height +
    selectedNode.LineStyle.LineWidth))
Using gr As Graphics = Graphics.FromImage(bmp)
    Dim m As New System.Drawing.Drawing2D.Matrix()
    m.Translate(Convert.ToInt32(selectedNode.BoundingBox.Left),
        Convert.ToInt32(selectedNode.BoundingBox.Top))
    gr.Transform = m
    selectedNode.Draw(gr)
    bmp.Save("image.png", System.Drawing.Imaging.ImageFormat.Png)
    Process.Start("image.png")
End Using
```

<!-- tags: [windows-forms, essential-diagram, WinForms, Syncfusion, version: 11.4.0.26] keywords: [line width, node image, graphics surface, export, image format, PNG, bounding box, matrix translation, transform] -->
```