```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_083.jpeg
document_name: QTP
page_number: 083
page_id: QTP#page_083
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:06:40Z
fidelity: lossless
-->

## Overview
- Demonstrates the use of the `GetCheckState` method to get the check state of a `CheckBoxAdv` control.
- Explains how to collapse and expand nodes in `TreeViewADV` using the `CollapseNode` and `ExpandNode` methods.

## Content

### GetCheckState Method
The GetCheckState method retrieves the check state of the `CheckBoxAdv` control.

| GetCheckState | public string GetCheckState() | string |
|---------------|---------------------------------|--------|
| Get the check state of the `CheckBoxAdv` control in **Essential Tools**. |  |  |

#### Applying GetCheckState Method in QTP
The following code example illustrates how to use the `GetCheckState` method.

```csharp
SwfWindow("QTPCheckBoxAdv").SwfObject("checkBox").GetCheckedState.Set "On"
MsgBox(SwfWindow("QTPCheckBoxAdv").SwfObject("checkBox").GetCheckedState())
```

#### 7.3.3 How to collapse and expand the specified node in TreeViewADV
- **Supported method to collapse and expand the specified node in TreeViewADV**
  - The `CollapseNode` method is used to collapse the specified node in `TreeViewADV`. The path of the node must be passed in the `CollapseNode` method.
  - The `ExpandNode` method is used to expand the specified node in `TreeViewADV`.

**Use Case Scenarios**
This feature enables you to collapse and expand the specified node in `TreeViewADV` in QTP testing.

### Methods Table

| Method       | Description                                   | Parameters                             | Return Type |
|--------------|-----------------------------------------------|----------------------------------------|--------------|
| CollapseNode | Collapse the specified node in `TreeViewADV` in Essential Tools. | public void CollapseNode(string fullPath) | Void        |

## API Reference

### Methods
- **CollapseNode**:  
  - **Description**: Collapses the specified node in `TreeViewADV` in Essential Tools.  
  - **Parameters**:  
    - `string fullPath`: The path of the node to collapse.  
  - **Return Type**: Void  

## Code Examples

### Example: Using CollapseNode
```csharp
SwfWindow("QTPCheckBoxAdv").SwfObject("treeView").CollapseNode("/nodePath");
```

## Page-level Navigation/TOC (if applicable)
- Getting Started
- Methods
- Examples

### Cross References
- See also: `ExpandNode` method, `CheckBoxAdv` control, `TreeViewADV` control

## RAG Annotations
<!-- tags: [Features, checkbox, treeview, control, method, QTP, version 11.4.0.26] keywords: [GetCheckState, CollapseNode, ExpandNode, TreeViewADV, CheckBoxAdv] -->
```