```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_558.jpeg
document_name: tools
page_number: 558
page_id: tools#page_558
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:20:49Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Code Example

```vb
As String) As TreeNode
    For Each child As TreeNode In nodes
        If child.Text = text Then
            Return child
        End If
    Next child
    For Each child As TreeNode In nodes
        Dim matched As TreeNode = Me.FindNode(child.Nodes, text)
        If Not matched Is Nothing Then
            Return matched
        End If
    Next child
    Return Nothing
End Function
```

### Dropdown Event Handling

3. In the drop-down event, find the node whose text matches the text in the combo and make that the selected node, using the following code.

#### C#

```csharp
private void comboDropDown1_DropDown(object sender, System.EventArgs e)
{
    // Before the drop-down is shown, select a TreeNode based on the text in the combo.
    if (this.comboDropDown1.Text != String.Empty)
    {
        TreeNode matchedNode = this.FindNode(this.treeView1.Nodes, this.comboDropDown1.Text);
        this.treeView1.SelectedNode = matchedNode;
    }
}
```

#### VB.NET

```vb
Private Sub comboDropDown1_DropDown(ByVal sender As Object, ByVal e As System.EventArgs) Handles comboDropDown1.DropDown

    ' Before the drop-down is shown, select a TreeNode based on the text in the combo.
    If Me.comboDropDown1.Text <> String.Empty Then
        Dim matchedNode As TreeNode = Me.FindNode(Me.treeView1.Nodes, Me.comboDropDown1.Text)
        Me.treeView1.SelectedNode = matchedNode
    End If
End Sub
```
```html
<!-- tags: [Syncfusion Winforms, dropdown event, TreeView, TreeNode, combo box, selected node] keywords: [dropdown event, Syncfusion Winforms, TreeView, TreeNode, combo box, selected node, C#, VB.NET, code example] -->
```