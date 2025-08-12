```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_063.jpeg
document_name: diagram
page_number: 063
page_id: diagram#page_063
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:10:30Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

```csharp
printDlg.AllowSomePages = true;

if (printDlg.ShowDialog(this) == DialogResult.OK)
{
    printDoc.PrinterSettings = printDlg.PrinterSettings;
    printDoc.Print();
}
```

## Diagram Builder Tools

### Editing Options

| Edit Menu Items | Description                                                                 | Code Snippet                                                         |
|------------------|-----------------------------------------------------------------------------|----------------------------------------------------------------------|
| Undo             | Reverts the latest modification done.                                        | `Diagram1.Model.HistoryManager.Undo();`                             |
| Redo             | Steps forward to operation history records and redoes the last undone task. | `Diagram1.Model.HistoryManager.Redo();`                             |
| Cut              | Removes the currently selected nodes from the diagram and moves them to the clipboard. | `Diagram1.Controller.Cut();`                                         |
| Copy             | Copies the currently selected nodes to the clipboard.                        | `Diagram1.Controller.Copy();`                                       |
| Paste            | Pastes the contents of the clipboard to the diagram.                         | `Diagram1.Controller.Paste();`                                      |
| Select All      | Adds all nodes in the diagram model to the SelectionList.                   | `Diagram1.Controller.SelectAll();`                                  |

### Pan & Zoom Tool

The following screen shot illustrates the pan and zoom tools.

<!-- tags: [diagram, windows forms, editing options, pan, zoom, syncfusion winforms, version 11.4.0.26] keywords: [Undo, Redo, Cut, Copy, Paste, Select All, HistoryManager, Controller] -->
```