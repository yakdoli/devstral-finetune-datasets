```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_263.jpeg
document_name: diagram
page_number: 263
page_id: diagram#page_263
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:23:32Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

```csharp
null;
private Ellipse innerEllipse = null;

public MySymbol()
{
    // Add child nodes to the symbol programmatically.
    // Add an outer rectangle.
    this.outerRect = new Syncfusion.Windows.Forms.Diagram.Rectangle(0, 0, 120, 80);
    this.outerRect.Name = "Rectangle";
    this.outerRect.FillStyle.Color = Color.Khaki;
    this.AppendChild(outerRect);

    // Add an inner ellipse.
    this.innerEllipse = new Ellipse(10, 10, 100, 60);
    this.innerEllipse.Name = "Ellipse";
    this.AppendChild(innerEllipse);

    // Add Label.
    Label lbl = this.AddLabel("My Symbol", BoxPosition.Center);
    lbl.BackgroundStyle.Color = Color.Transparent;
}
}
```

### [VB.NET]

```vb
' Custom Symbol (MySymbol.vb)
Public Class MySymbol
    Inherits Symbol
    Private outerRect As Syncfusion.Windows.Forms.Diagram.Rectangle = Nothing
    Private innerEllipse As Syncfusion.Windows.Forms.Diagram.Ellipse = Nothing

    Public Sub New()
        ' Add child nodes to the symbol programmatically.

        ' Add an outer rectangle.
        Me.outerRect = New Syncfusion.Windows.Forms.Diagram.Rectangle(0, 0, 120, 80)
        Me.outerRect.Name = "Rectangle"
        Me.outerRect.FillStyle.Color = Color.Khaki
        Me.AppendChild(outerRect)

        ' Add an inner ellipse.
    End Sub
End Class
```

<!-- tags: [Syncfusion, Winforms, Diagram, MySymbol, Rectangle, Ellipse, Label, C#, VB.NET] keywords: [Syncfusion Winforms, Diagram control, custom symbol, inner ellipse, outer rectangle, label, C#, VB.NET] -->
```