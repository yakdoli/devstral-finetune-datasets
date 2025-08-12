```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_281.jpeg
document_name: diagram
page_number: 281
page_id: diagram#page_281
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:25:57Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Content

### Code Example (C#)

```csharp
System.Drawing.Drawing2D.DashStyle.Dash;
    globelNode.LineStyle.LineWidth = 3;

    // Resetting the node with default values
    poly.FillStyle.Color = defaultColor;
    globelNode.LineStyle.DashStyle = System.Drawing.Drawing2D.DashStyle.Solid;
    globelNode.LineStyle.LineWidth = 1;
    }
}
```

### Code Example (VB.NET)

```vb
Private globelNode As Syncfusion.Windows.Forms.Diagram.Node
Private PolygonNode As Syncfusion.Windows.Forms.Diagram.Polygon
Public WithEvents timer1 As Timer

Private Sub diagram1_MouseMove(ByVal sender As Object, ByVal e As MouseEventArgs) Handles Diagram1.MouseMove
    Try
        ' Retrieves node under the mouse action
        Dim node As Syncfusion.Windows.Forms.Diagram.Node = CType(Me.Diagram1.Controller.GetNodeUnderMouse(New Point(e.X, e.Y)), Syncfusion.Windows.Forms.Diagram.Node)

        If Not node Is Nothing AndAlso (node.Name.ToString() <> "TextNode") Then
            Me.toolTip1.SetToolTip(Me.diagram1, node.Name)
            Me.toolTip1.Active = True

            globelNode = node
            PolygonNode = CType(IIf(TypeOf node Is Syncfusion.Windows.Forms.Diagram.Polygon, node, Nothing), Syncfusion.Windows.Forms.Diagram.Polygon)
            defaultColor = PolygonNode.FillStyle.Color

            Me.timer1.Start()
        Else
            Me.toolTip1.Active = False
            Me.timer1.Stop()
        End If
    Catch
        End Try
End Sub

Private Sub timer1_Tick(ByVal sender As Object, ByVal e As EventArgs) Handles timer1.Tick
```

## API Reference

### Namespaces and Classes Used
- `System.Drawing.Drawing2D`
- `Syncfusion.Windows.Forms.Diagram`
- `System.Windows.Forms`

### Methods Used
- `GetNodeUnderMouse(Point)`
- `SetToolTip(Control, String)`
- `Start()`
- `Stop()`

### Properties Used
- `Node.FillStyle.Color`
- `Node.LineStyle.DashStyle`
- `Node.LineStyle.LineWidth`
- `Name.ToString()`

### Events Handled
- `MouseMove`
- `Tick`

## Code Examples (Continued)

Refer to the above code examples for practical implementation details.

## Cross References

See also:
- [Syncfusion Diagram Control Documentation](https://www.syncfusion.com/documentation/windows-forms/diagram/)
- [Syncfusion Windows Forms Controls](https://www.syncfusion.com/products/windowsforms)

<!-- tags: [syncfusion, windowsforms, diagram, controls, winforms] keywords: [code examples, vb.net, csharp, mouse move, timer, tooltip, node properties, event handling] -->
```