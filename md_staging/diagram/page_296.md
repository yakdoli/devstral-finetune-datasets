```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_296.jpeg
document_name: diagram
page_number: 296
page_id: diagram#page_296
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:25:22Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

### Interaction with Nodes

The provided code examples demonstrate how to retrieve the top node under the current mouse location in a diagram within a Windows Forms application. This functionality is useful for interactive UI elements where precise node identification is required based on mouse movement.

#### C# Code Example

```csharp
private void diagram1_MouseMove(object sender, MouseEventArgs e)
{
    // Gets the top node under the current mouse location.
    INode node = diagram1.Controller.GetNodeUnderMouse(e.Location);
}
```

#### VB.NET Code Example

```vb.net
Private Sub diagram1_MouseMove(ByVal sender As Object, ByVal e As MouseEventArgs)
    ' Gets the top node under the current mouse location.
    Dim node As INode = diagram1.Controller.GetNodeUnderMouse(e.Location)
End Sub
```

### Functionality Explanation

In both code examples, the `diagram1_MouseMove` event handler is triggered when the mouse moves over the diagram control (`diagram1`). The `GetNodeUnderMouse` method retrieves the topmost node located at the current mouse position (`e.Location`). This is particularly useful for implementing hover effects, selection mechanics, or node-specific actions based on user interactions.

### API Reference

- **Controller.GetNodeUnderMouse(PointF location)**
  - **Parameters:**
    - `location`: Type `PointF` representing the mouse position in the diagram's coordinate system.
  - **Return Type:**
    - `INode`: The topmost node located at the specified mouse position. If no node is found, it returns `null`.
  - **Purpose:**
    - Identifies the node at a specific location within the diagram, enabling interaction with the node based on mouse actions.

### Code Examples in Context

The provided examples illustrate how to integrate the `GetNodeUnderMouse` functionality into a Windows Forms application. Both C# and VB.NET implementations achieve the same result but are tailored to the respective language syntax conventions.

### RAG Annotations

<!-- tags: [product, module, control, api, version] keywords: [Syncfusion, WinForms, Diagram, MouseMove, INode, GetNodeUnderMouse] -->
```