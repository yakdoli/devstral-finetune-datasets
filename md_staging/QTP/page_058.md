```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_058.jpeg
document_name: QTP
page_number: 058
page_id: QTP#page_058
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:04:58Z
fidelity: lossless
-->

# Essential QuickTest Professional

## Overview
- Lists the methods and their descriptions for interacting with different controls.
- Covers methods for managing text in `TextBoxExt`, state management in `ThemedCheckButton`, and node operations in `TreeViewAdv`.

## Content

### Text Box Methods
Below are the methods for the `TextBoxExt` control:

| Method                  | Description                            |
| ----------------------- | -------------------------------------- |
| `Set(string text)`     | Sets the text in the `TextBoxExt`.     |
| `SelectText(string selText, object start, object length)` | Selects the text in the `TextBoxExt`. |

### ThemedCheckButton Methods
Below are the methods for the `ThemedCheckButton` control:

| Method                  | Description                           |
| ----------------------- | ------------------------------------- |
| `Set(string chkState)` | Sets the `CheckState` of the `CheckBox` in the `DateTimeAdv`. |
| `string GetCheckState()` | Gets the `CheckState` of the `CheckBox` in the `DateTimeAdv`. |

### TreeViewAdv Methods
Below are the methods for managing nodes in the `TreeViewAdv` control:

| Method                                             | Description                                           |
| -------------------------------------------------- | ----------------------------------------------------- |
| `CollapseNode(string fullPath)`                  | Collapses the specified node.                          |
| `ExpandNode(string fullPath)`                    | Expands the specified node.                            |
| `SetCheckState(string fullPath, string checkState)` | Sets the specified state of the `CheckBox/OptionButton` for the specified node. |
| `SelectNodeWithModifierKeys(string fullPath, string ctrl, string shift)` | Selects the specified node according to the selection mode. |
| `BackupNodeDetails(string fullPath)`             | Backs up the node details before editing.             |
| `EditNode(string nodeText)`                      | Edits the specified node.                             |
| `DragDrop(string fullPath)`                      | Performs the drag and drop operation for nodes in the `SelectedNodes` list, added during the drag-over event. |
| `AddToSelectedNodeList(string fullPath)`         | Adds the specified node into the selected node list during the drag-over event. |
| `DoubleClick(string fullPath)`                   | Handles the double-click event of `TreeViewAdv`.       |

## API Reference (if applicable)
- **Namespace**: `Syncfusion.WinForms.Controls`
- **Class**: `TextBoxExt`
  - **Methods**:
    - `Set(string text)`
    - `SelectText(string selText, object start, object length)`
- **Class**: `ThemedCheckButton`
  - **Methods**:
    - `Set(string chkState)`
    - `string GetCheckState()`
- **Class**: `TreeViewAdv`
  - **Methods**:
    - `CollapseNode(string fullPath)`
    - `ExpandNode(string fullPath)`
    - `SetCheckState(string fullPath, string checkState)`
    - `SelectNodeWithModifierKeys(string fullPath, string ctrl, string shift)`
    - `BackupNodeDetails(string fullPath)`
    - `EditNode(string nodeText)`
    - `DragDrop(string fullPath)`
    - `AddToSelectedNodeList(string fullPath)`
    - `DoubleClick(string fullPath)`

## Code Examples (multi-language supported)
The methods can be used in your application as shown below:

```csharp
using Syncfusion.WinForms.Controls;

// Example for TextBoxExt
TextBoxExt textBox = new TextBoxExt();
textBox.Set("Hello, World!");
textBox.SelectText("Hello", 0, 5);

// Example for ThemedCheckButton
ThemedCheckButton checkBox = new ThemedCheckButton();
checkBox.Set("Checked");
string currentState = checkBox.GetCheckState();

// Example for TreeViewAdv
TreeViewAdv treeView = new TreeViewAdv();
treeView.CollapseNode("/NodePath");
treeView.EditNode("Node Text");
```

## Page-level Navigation/TOC (if applicable)
- **TextBoxExt Methods**
- **ThemedCheckButton Methods**
- **TreeViewAdv Methods**
- **API Reference**
- **Code Examples**

## Cross References
- See also: Methods for DateTimeAdv, CheckBox, OptionButton, and related controls.

## RAG Annotations
<!-- tags: [TextBoxExt, ThemedCheckButton, TreeViewAdv, Methods, Syncfusion Winforms, 11.4.0.26] keywords: [Set, SelectText, CheckState, Node, DragDrop, DoubleClick, Expand, Collapse] -->
```