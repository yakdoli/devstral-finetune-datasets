```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_285.jpeg
document_name: diagram
page_number: 285
page_id: diagram#page_285
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:26:13Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Overview
- Demonstrates adding symbols programmatically from a palette to a diagram.
- Explains how to link two symbols using the LinkCmd class.

## Content

### 5.25 How To Programmatically Add a Symbol From the Palette

The following code sample demonstrates how you can programmatically add a symbol from the symbol palette to a diagram.

#### C#

```csharp
if (paletteGroupView1.Palette.Nodes.Count > 0)
{
    Node nc = (Node)paletteGroupView1.Palette.Nodes[0].Clone();
    diagram1.Model.AppendChild(nc);
}
```

#### VB.NET

```vbnet
If paletteGroupView1.Palette.Nodes.Count > 0 Then
    Dim nc As Node = DirectCast(paletteGroupView1.Palette.Nodes(0).Clone(), Node)
    diagram1.Model.AppendChild(nc)
End If
```

### 5.26 How To Programmatically Link Two Symbols

The Syncfusion.Windows.Forms.Diagram.LinkCmd command class can be used to programmatically link symbols.

The following code sample shows how to create a link between two symbols, `symbol1` and `symbol2`.

```csharp
// Create a LinkCmd object.
LinkCmd linkcommand = new LinkCmd();
linkcommand.Link = new Link(Link.Shapes.Line);
```

## API Reference

### Syncfusion.Windows.Forms.Diagram.LinkCmd
- **Method**: AppendChild(Node)
  - Description: Adds a cloned node to the diagram model.
  - Parameters:
    - `Node`: The node to be appended.
  - Returns: None.

### Namespace
- Syncfusion.Windows.Forms.Diagram

### Important Attributes
- **paletteGroupView1**: The view containing the symbol palette.
- **diagram1**: The target diagram to which symbols are added.
- **LinkCmd**: The command class used for linking symbols.

## Code Examples

- **C#**
  ```csharp
  // Add a symbol from the palette
  if (paletteGroupView1.Palette.Nodes.Count > 0)
  {
      Node nc = (Node)paletteGroupView1.Palette.Nodes[0].Clone();
      diagram1.Model.AppendChild(nc);
  }

  // Link two symbols
  LinkCmd linkcommand = new LinkCmd();
  linkcommand.Link = new Link(Link.Shapes.Line);
  ```

- **VB.NET**
  ```vbnet
  ' Add a symbol from the palette
  If paletteGroupView1.Palette.Nodes.Count > 0 Then
      Dim nc As Node = DirectCast(paletteGroupView1.Palette.Nodes(0).Clone(), Node)
      diagram1.Model.AppendChild(nc)
  End If

  ' Link two symbols
  Dim linkcommand As New LinkCmd()
  linkcommand.Link = New Link(Link.Shapes.Line)
  ```

## Page-level Navigation/TOC
- 5.25 How To Programmatically Add a Symbol From the Palette
- 5.26 How To Programmatically Link Two Symbols

## Cross References
- See also: Diagram symbols, Node cloning, LinkCmd API, Diagram linking.

<!-- tags: [Syncfusion, Windows Forms, Diagram, Palette, LinkCmd, Symbols, Programming] keywords: [add symbol, palette view, diagram model, LinkCmd, link symbols, append child, symbols, nodes, cloning, linking] -->
```