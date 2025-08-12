```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_101.jpeg
document_name: diagram
page_number: 101
page_id: diagram#page_101
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:15:15Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

### TreeView Events

The following table lists the events associated with the `TreeView` control and their descriptions:

| **Event**             | **Description**                                                                 |
|-----------------------|---------------------------------------------------------------------------------|
| **AfterCheck**       | Occurs when a check box on a tree node has been checked or unchecked.           |
| **AfterCollapse**     | Occurs when a node has been collapsed.                                         |
| **AfterExpand**      | Occurs when a node has been expanded.                                          |
| **AfterLabelEdit**    | Occurs when the text of a node has been edited by the user.                    |
| **AfterSelect**      | Occurs when the selection has been changed.                                    |
| **BeforeCheck**      | Occurs when a check box on a tree node is about to be checked or unchecked.     |
| **BeforeCollapse**    | Occurs when a node is about to be collapsed.                                   |
| **BeforeExpand**     | Occurs when a node is about to be expanded.                                    |
| **BeforeLabelEdit**   | Occurs when the text of a node is about to be edited by the user.              |
| **BeforeSelect**     | Occurs when the selection is about to change.                                  |
| **DrawNode**         | Occurs in owner draw-mode, when a node needs to be drawn.                      |
| **NodeMouseClick**   | Occurs when a node is clicked with the mouse.                                  |
| **NodeMouseDoubleClick** | Occurs when a node is double-clicked with the mouse.                       |

### Programmatic Property Settings

Programmatically, the properties can be set as follows:

```csharp
documentExplorer1.AttachModel(model1);
documentExplorer1.Dock = DockStyle.Right;
documentExplorer1.BackColor = System.Drawing.SystemColors.Window;
documentExplorer1.Location = new System.Drawing.Point(0, 377);
documentExplorer1.Size = new System.Drawing.Size(200, 100);
documentExplorer1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
documentExplorer1.ShowNodeToolTips = true;
```

## API Reference

## Code Examples

## RAG Annotations
<!-- tags: [Syncfusion, WinForms, TreeView, Events, Programmatic Property Setting] keywords: [TreeView, AfterCheck, AfterCollapse, AfterExpand, AfterLabelEdit, AfterSelect, BeforeCheck, BeforeCollapse, BeforeExpand, BeforeLabelEdit, BeforeSelect, DrawNode, NodeMouseClick, NodeMouseDoubleClick, Programmatic Property Setting, C#] -->
```