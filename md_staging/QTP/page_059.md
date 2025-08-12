```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_059.jpeg
document_name: QTP
page_number: 059
page_id: QTP#page_059
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:04:57Z
fidelity: lossless
-->

# Essential QuickTest Professional Functions

## Content

### Tree Operations

| Method                     | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| SelectNode(string fullPath)| Selects the node in SingleSelect mode.                                    |
| RMouseDown(int x, int y)  | Performs a right mouse click.                                              |
| TreeNodeAdv GetNodeFromPath(string fullPath) | Gets the tree node from the path.                          |
| Point GetPointFromNode(TreeNodeAdv node) | Returns the TextBounds point of the specified node.           |
| RightClickNode(string fullPath) | Right-clicks the specified node.                                      |

### XPMenus Operations

| Method                    | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| Select(string text)      | Performs click on a bar item.                                               |
| string TraceParentRoot(string barItemText) | For the given text of the required menu, TraceParentRoot will retrieve the full path as recoded. |
| int MenuItemPos(string ParentText, string barItemText) | For the given text of the required menu, MenuItemPos will return the position of the menu item. |

### XPToolBar Operations

| Method               | Description                                                          |
|----------------------|----------------------------------------------------------------------|
| Select(string ID)   | Performs click in the baritem.                                         |
| Popup(string ID)    | Shows the popup of the parent bar item.                                |

### XPTaskBar Operations

| Method                   | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| Expand(string headerText)| Expands the content area of the task bar box.                          |
| Collapse(string headerText) | Collapses the content area of the task bar box.                     |
| ItemClick(string headerText, string itemTag) | Performs a click in the item described in the tag. |
```