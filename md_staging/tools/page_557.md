```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_557.jpeg
document_name: tools
page_number: 557
page_id: tools#page_557
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:19:40Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Handling ComboBox DropDown in TreeView

### C#

```csharp
else
    this.comboDropDown1.Text = String.Empty;

// Close the combodropdown.
this.comboDropDown1.PopupContainer.HidePopup(PopupCloseType.Done);
```

### [VB.NET]

```vb
Private Sub treeView1_DoubleClick(sender As Object, e As System.EventArgs) Handles treeView1.DoubleClick
    If Not (Me.treeView1.SelectedNode Is Nothing) Then

        ' Set the combodropdown's text to be the TreeNode's text.
        Me.comboDropDown1.Text = Me.treeView1.SelectedNode.Text
    Else
        Me.comboDropDown1.Text = String.Empty
    End If

    ' Close the combodropdown.
    Me.comboDropDown1.PopupContainer.HidePopup(PopupCloseType.Done)
End Sub
```

### Recursive Node Matching

2. Simply traverses the tree structure recursively to find the matching node using the `FindNode` method discussed below.

### C#

```csharp
private TreeNode FindNode(TreeNodeCollection nodes, string text)
{
    foreach (TreeNode child in nodes)
        if (child.Text == text)
            return child;
    foreach (TreeNode child in nodes)
    {
        TreeNode matched = this.FindNode(child.Nodes, text);
        if (matched != null)
            return matched;
    }
    return null;
}
```

### [VB.NET]

```vb
Private Function FindNode(ByVal nodes As TreeNodeCollection, ByVal text
```

### Page Footer

© 2013 Syncfusion. All rights reserved.
```