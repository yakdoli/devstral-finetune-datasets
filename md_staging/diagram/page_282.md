```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_282.jpeg
document_name: diagram
page_number: 282
page_id: diagram#page_282
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:25:53Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

```vb.net
' Convert node as polygon
Dim poly As Syncfusion.Windows.Forms.Diagram.Polygon = CType(If(TypeOf globalNode Is Syncfusion.Windows.Forms.Diagram.Polygon, globalNode, Nothing), Syncfusion.Windows.Forms.Diagram.Polygon)
Dim r As Random = New Random()
If Not poly Is Nothing Then
    ' Setting fillstyle for the polygon
    poly.FillStyle.Color = Color.FromArgb(r.Next(255), r.Next(255), r.Next(255))
    globalNode.LineStyle.DashStyle = System.Drawing.Drawing2D.DashStyle.Dash
    globalNode.LineStyle.LineWidth = 3

    ' Resetting the node with default values
    poly.FillStyle.Color = defaultColor
    globalNode.LineStyle.DashStyle = System.Drawing.Drawing2D.DashStyle.Solid
    globalNode.LineStyle.LineWidth = 1
End If
End Sub
```

A sample which demonstrates the node highlighting feature is available in the below sample installation location.

```
.\My Documents\Syncfusion\EssentialStudio\VersionNumber\Windows\Diagram.Windows\Samples\2.0\Getting Started\HighLightSample
```

## 5.2.2 How To Move / Place the Nodes Outside the Diagram Model's Bounds

Setting the model's `BoundaryConstraintsEnabled` property to `False` will let you place the nodes outside the bounds of the diagram model.

```csharp
[//]: # ([C#])

diagram1.Model.BoundaryConstraintsEnabled = false;
```

```vb.net
[//]: # ([VB.NET])

diagram1.Model.BoundaryConstraintsEnabled = False
```

---

## API Reference

### Namespace: Syncfusion.Windows.Forms.Diagram

#### Properties
- **BoundaryConstraintsEnabled**: Gets or sets a value indicating whether boundary constraints are enabled.
  - **Type**: `bool`
  - **Default**: `true`
  - **Returns**: `true` if boundary constraints are enabled; otherwise, `false`.

### Exceptions
- None

### Example Usage
```csharp
// Disable boundary constraints
diagram1.Model.BoundaryConstraintsEnabled = false;
```

## Code Examples

### C#
```csharp
diagram1.Model.BoundaryConstraintsEnabled = false;
```

### VB.NET
```vb.net
diagram1.Model.BoundaryConstraintsEnabled = False
```

## Page-level Navigation/TOC
- 5.2.2 How To Move / Place the Nodes Outside the Diagram Model's Bounds
  - Setting the model's `BoundaryConstraintsEnabled` property to `False`.
  - Code examples in C# and VB.NET.

## Cross References
- Refer to the Syncfusion Documentation for more details on Diagram properties:
  - [Syncfusion Diagram Documentation](https://help.syncfusion.com/windowsforms/diagram/getting-started)

<!-- tags: [syncfusion, windowsforms, diagram, boundaryconstraints] keywords: [boundary constraints, place nodes outside bounds, diagram model, diagram properties, winforms controls] -->
```