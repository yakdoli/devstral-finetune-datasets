```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_270.jpeg
document_name: diagram
page_number: 270
page_id: diagram#page_270
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:25:06Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

```vb
End If
End Sub

Private Sub Model_MouseLeave(ByVal sender As Object, ByVal evtArgs As Syncfusion.Windows.Forms.Diagram.NodeMouseEventArgs)
    Me.toolTip1.Active = False
End Sub
```

## Overview
- Explains how to draw custom handles for nodes using the CustomHandleRenderer Property.
- Covers customization and implementation specifics for achieving custom appearances in node handles.

## How To Draw Custom Handles For Nodes Using the CustomHandleRenderer Property

Syncfusion Diagram provides users with the facility to draw their own handles for nodes using the `CustomHandleRenderer` property, which is available in the `View` class. This property accepts instances of the `UserHandleRenderer` class, which acts as a base class for custom Handle Renderers. By using this class, we can derive a class to create our own Handle Renderer and assign it to the `View.CustomHandleRenderer` property. If this property is assigned as `'Null'`, it will render the default style of the Handle.

![Default Appearance](figure.png)
*Figure 155: Default Appearance*

The `UserHandleRenderer` class methods are made as public virtual; this class duplicates the `HandleRenderer` functionality but has a more convenient structure for overriding the default appearance. It provides an option to implement the new handle renderer with minimal changes by deriving it. If you are having a source code license, you can see the complete source `UserHandleRenderer` in the following location for understanding more about handle renderers: Diagram.Base\\Src\\Utility\\HandleRenderer.cs.

Here is a sample code snippet.

```csharp
[C#]
public class MyHandleRenderer : UserHandleRenderer
{
```

## API Reference (if applicable)
- **Namespace**: Syncfusion.Windows.Forms.Diagram
- **Class**: `UserHandleRenderer`
  - **Inheritance**: Derived from `HandleRenderer`
  - **Properties**:
    - `CustomHandleRenderer`: Allows customization of node handles.
  - **Deriving Classes**: You can derive your own handle renderer by inheriting from `UserHandleRenderer`.

## Code Examples (multi-language supported)

### C#
```csharp
public class MyHandleRenderer : UserHandleRenderer
{
    // Implement customization logic here
}
```

## Page-level Navigation/TOC (if applicable)
- How To Draw Custom Handles For Nodes Using the CustomHandleRenderer Property

## Cross References
- See also: Node customization, Handle Renderer Classes, User Interface Customization.

<!-- tags: [Syncfusion, Windows Forms, Diagram, CustomHandleRenderer, UserHandleRenderer, HandleRenderer, Node Handles] keywords: [custom handles, node, rendering, customization, diagram API, HandleRenderer class, user interface customization] -->
```