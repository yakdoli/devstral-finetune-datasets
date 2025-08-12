```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_264.jpeg
document_name: diagram
page_number: 264
page_id: diagram#page_264
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:23:04Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

```vb
Me.innerEllipse = New Syncfusion.Windows.Forms.Diagram.Ellipse(10, 10, 100, 60)
Me.innerEllipse.Name = "Ellipse"
Me.AppendChild(innerEllipse)

' Add Label.
Dim lbl As Label = Me.AddLabel("My Symbol", BoxPosition.Center)
lbl.BackgroundStyle.Color = Color.Transparent
End Sub ' New
End Class ' MySymbol
```

## Using the Symbol in the Form

### [C#]

```csharp
// Register InsertTool for MySymbol.
this.diagram1.Controller.RegisterTool(new InsertSymbolTool("InsertMySymbol", typeof(MySymbol)));

// Activate InsertTool for MySymbol.
this.diagram1.ActivateTool("InsertMySymbol");
```

### [VB.NET]

```vb
' Register InsertTool for MySymbol.
Me.diagram1.Controller.RegisterTool(New InsertSymbolTool("InsertMySymbol", GetType(MySymbol)))

' Activate InsertTool for MySymbol.
Me.diagram1.ActivateTool("InsertMySymbol")
```

## 5.11 How To Create a Directional Link

Links can be provided with end point decorators to convey the direction. The following code snippet shows how to create a directional link by adding a 'Filled Arrow' end point visual to the head port edge of the link.

### [C#]

```csharp
// Create a directional link.
Link link = new Link(pts);
```

## References

- See also: "End Point Decorators," "Directional Links," "Link Customization."

<!-- tags: [Syncfusion, Winforms, Diagram, Directional Link] keywords: [Directional Link, End Point Decorators, Link Customization] -->
```