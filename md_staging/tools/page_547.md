```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_547.jpeg
document_name: tools
page_number: 547
page_id: tools#page_547
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:20:16Z
fidelity: lossless
-->

Essential Tools for Windows Forms

## Drag and Drop Controls onto the Form

### Drag and Drop ComboBox and TreeView

2. Drag and drop a `ComboBox` and `TreeView` control from the toolbox onto the form.

#### Setting Up the Design

| Figure 335: ComboDropDown and TreeView Control in the Windows Form |
| --- |
| ![Figure 335: ComboDropDown and TreeView Control in the Windows Form](https://example.com/figure-335) |

### Adding Nodes and Configuring TreeView

3. Add nodes to the `TreeView` control and set the `HideSelection` property to `false`. The `HideSelection` property specifies whether the selected tree node remains highlighted even when the `TreeView` loses focus.

#### Configuring the TreeView Control

| Figure 336: Setting TreeView Control HideSelection Property |
| --- |
| ![Figure 336: Setting TreeView Control HideSelection Property](https://example.com/figure-336) |

## Summary

This section demonstrates how to drag and drop a `ComboBox` and `TreeView` control into a Windows Forms application and configure the `TreeView` control by adding nodes and setting the `HideSelection` property to `false`.

## API Reference

### TreeView Class Properties

- **ForeColor**: Specifies the foreground color of the text in the `TreeView`.
- **FullRowSelect**: Controls whether the entire row in the `TreeView` is selected or just the text portion.
- **GenerateMember**: Indicates whether the control generates member code.
- **HideSelection**: Specifies whether the selected tree node remains highlighted when the `TreeView` loses focus.
- **HotTracking**: Specifies whether the `TreeView` node shows a hover effect.
- **ImageIndex**: Specifies the index of the image in the `ImageList` to display next to the tree node.
- **ImageKey**: Specifies the key of the image in the `ImageList` to display next to the tree node.
- **ImageList**: Specifies the `ImageList` containing the images to display next to the tree nodes.

## Code Examples

### C# Example

```csharp
private void Form1_Load(object sender, EventArgs e)
{
    // Adding nodes to the TreeView
    TreeNode node0 = new TreeNode("Node0");
    TreeNode node1 = new TreeNode("Node1");
    TreeNode node2 = new TreeNode("Node2");
    TreeNode node3 = new TreeNode("Node3");
    TreeNode node6 = new TreeNode("Node6");

    treeView1.Nodes.Add(node0);
    node0.Nodes.Add(node1);
    node0.Nodes.Add(node2);
    treeView1.Nodes.Add(node3);
    node3.Nodes.Add(node6);

    // Setting HideSelection property
    treeView1.HideSelection = false;
}
```

### VB.NET Example

```vb
Private Sub Form1_Load(sender As Object, e As EventArgs) Handles MyBase.Load
    ' Adding nodes to the TreeView
    Dim node0 As New TreeNode("Node0")
    Dim node1 As New TreeNode("Node1")
    Dim node2 As New TreeNode("Node2")
    Dim node3 As New TreeNode("Node3")
    Dim node6 As New TreeNode("Node6")

    treeView1.Nodes.Add(node0)
    node0.Nodes.Add(node1)
    node0.Nodes.Add(node2)
    treeView1.Nodes.Add(node3)
    node3.Nodes.Add(node6)

    ' Setting HideSelection property
    treeView1.HideSelection = False
End Sub
```

## Cross References

- See also: [ComboBox Control Overview](#)
- See also: [TreeView Control Overview](#)

<!-- tags: [Windows Forms, ComboBox, TreeView, HideSelection, Node, Control, Properties, configuration] keywords: [ComboBox, TreeView, HideSelection, Node, Windows Forms, control configuration, C#, VB.NET] -->
```