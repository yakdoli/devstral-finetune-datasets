```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_060.jpeg
document_name: QTP
page_number: 060
page_id: QTP#page_060
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:05:09Z
fidelity: lossless
-->

# Helper Functions

| Function                | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| string GetTag(int itemIndex)          | Retrieves the tag information for the given itemIndex. |
| string GetHeaderText()                | Retrieves the group/header text of the task bar box called from. |
| string GetItemText(int itemIndex)     | Retrieves the item text for the given item index from the task bar box called. |
| int GetTaskBarBoxCount()              | Number of task bar boxes. |
| int GetExpandedTaskBarBoxCount()      | Number of expanded task bar boxes. |
| GetCollapsedTaskBarBoxCount()         | Number of collapsed task bar boxes. |
| bool FindItem(string itemText, out string headerText, out int itemIndex) | Helps to find if an item exists. |

## SplitContainerAdv

| Method                 | Description                               |
|------------------------|-------------------------------------------|
| MoveSplitter(int distance) | Adjusts the distance of the splitter. |
| CollapsePanel(string collapse) | Collapses the panel.              |

## TabSplitterContainer

| Method                  | Description                                       |
|-------------------------|---------------------------------------------------|
| Collapse(string collapse)       | Collapses the pane to the bottom.              |
| ChangeOrientation(string orientation) | Changes the orientation.                 |
| MoveSplitter(int position)      | Adjusts the position of the splitter.           |
| SwapPanes(string swap)          | Swaps primary and secondary panes.              |
| SelectPrimaryTab(int index)     | Selects the primary tab page based on the given index. |

<!-- tags: [Syncfusion Winforms, Helper Functions, SplitContainerAdv, TabSplitterContainer] keywords: [GetTag, GetHeaderText, GetItemText, GetTaskBarBoxCount, GetExpandedTaskBarBoxCount, GetCollapsedTaskBarBoxCount, FindItem, MoveSplitter, CollapsePanel, Collapse, ChangeOrientation, MoveSplitter, SwapPanes, SelectPrimaryTab] -->
```