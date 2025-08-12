```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_295.jpeg
document_name: diagram
page_number: 295
page_id: diagram#page_295
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:25:31Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

```vb
Dim paletteToReturn As SymbolPalette = Nothing
Dim strFileName As String = "Basic Flowchart Shapes.vss"
'Create an instance of VisioStencilConverter
Dim converter As VisioStencilConverter = New VisioStencilConverter(strFileName)
converter.ShowProgressDialog = True
'Convert the stencil as SymbolPalette
paletteToReturn = converter.Convert()
paletteGroupBar1.AddPalette(paletteToReturn)
```

**Note:** You must have Visio installed in your machine to import the stencils.

## 5.39 How to Get a Node at a Point or under a Mouse Location?

### GetNodeAtPoint

You can use the `GetNodeAtPoint` method of `Controller` to get a node at a point. You have to convert the point to a model coordinate before using this method in order to get the exact result when a diagram document is panned and zoomed.

#### C#

```csharp
//Client location.
Point pt = new Point(200, 150);
//Convert client location to model location.
pt = diagram1.Controller.ConvertToModelCoordinates(pt);
//Get the node in model coordinates.
Node node = diagram1.Controller.GetNodeAtPoint(pt);
```

#### VB.NET

```vb
'Client location.
Dim pt As Point = New Point(200, 150)
'Convert client location to model location.
pt = diagram1.Controller.ConvertToModelCoordinates(pt)
'Get the node in model coordinates.
Dim node As Node = diagram1.Controller.GetNodeAtPoint(pt)
```

### GetNodeUnderMouse

You can use the `GetNodeUnderMouse` method of `Controller` to get a node at a current mouse point. You don't have to convert the mouse point to a model coordinate while using this method. You just need to pass the current mouse point to the model coordinate.

---

<!-- tags: [winforms, essential-diagram, controller, getnodeatpoint, getnodeundermouse, visioStencilConverter, node] keywords: [mouse location, model coordinates, diagram document, panning, zooming, node retrieval, mouse point, client location, model location, Syncfusion Windows Forms] -->
```