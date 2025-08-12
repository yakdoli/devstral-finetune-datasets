```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_102.jpeg
document_name: diagram
page_number: 102
page_id: diagram#page_102
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:14:44Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

### Diagram Explorer Configuration

```vb
documentExplorer1.AttachModel(model1)
documentExplorer1.Dock = DockStyle.Right
documentExplorer1.BackColor = System.Drawing.SystemColors.Window
documentExplorer1.Location = New System.Drawing.Point(0, 377)
documentExplorer1.Size = New System.Drawing.Size(200, 100)
documentExplorer1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D
documentExplorer1.ShowNodeToolTips = True
```

![Document Explorer](image.png)

*Figure 59: Document Explorer*

### Sample code snippet for `documentExplorer1.AfterSelect` Event

```csharp
[C#]

documentExplorer1.AfterSelect += new TreeViewEventHandler(
    documentExplorer1_AfterSelect);

private void documentExplorer1_AfterSelect(object sender, TreeViewEventArgs e)
{
    // Update diagram's selection list depending on TreeNode Tag
    if (e.Node.Tag is Node)
}
```

## API Reference

### Events
- **AfterSelect**
  ```csharp
  event System.EventHandler<TreeViewEventArgs> AfterSelect;
  ```
  
  - **Description:** Triggered after a TreeNode is selected in the TreeView control.
  - **Parameters:** 
    - `sender`: The object that triggered the event.
    - `e`: Contains information about the TreeViewEventArgs.
  - **Usage:** Customize based on the(TreeNode) e.Node.Tag.

---

<!-- tags: [Syncfusion, WinForms, Diagram, DocumentExplorer, Events] keywords: [AfterSelect, C#, VB, TreeView, Tag, diagram, Windows Forms] -->
```