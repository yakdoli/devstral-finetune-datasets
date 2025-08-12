```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_156.jpeg
document_name: diagram
page_number: 156
page_id: diagram#page_156
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:16:15Z
fidelity: lossless
-->

# Essential Diagram for Windows Forms

## Content

### 4.6 Advanced Features

This particular feature section covers the below topics.

#### 4.6.1 Node Selections

A node's behavior can be customized and modified using the `EditStyle` collection properties which can be used for the following:

- To prohibit selection, rotation, and deletion of nodes, by using `AllowSelect`, `AllowRotate`, and `AllowDelete` properties.
- To restrict a node's movement along the x or y axis, by using `AllowMoveX` and `AllowMoveY` properties.
- To prevent resizing the height and width of the node, by using `AllowChangeHeight`, `AllowChangeWidth`, and `AllowResize` properties.

| EditStyle Property       | Description                                                                                   |
|--------------------------|-----------------------------------------------------------------------------------------------|
| AllowChangeHeight        | Specifies whether or not to allow the height to be changed. Default value is `True`.         |
| AllowChangeWidth         | Specifies whether or not to allow the width to be changed. Default value is `True`.          |
| AllowDelete              | Specifies whether or not to allow the node to be deleted on clicking the DELETE key. Default value is `True`. |
| AllowMoveX               | Specifies whether or not to allow the node to be moved along the x-axis. Default value is `True`. |
| AllowMoveY               | Specifies whether or not to allow the node to be moved along the y-axis. Default value is `True`. |
| AllowRotate              | Specifies whether or not to rotate the node using the PinPoint. Default value is `True`.      |
| AllowSelect              | Specifies whether or not to select the node on mouse click. Default value is `True`.        |

Programmatically, the properties can be set as follows:

```csharp
```

## Page-level Navigation/TOC (if applicable)

- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown.
- Ignore global site TOC or breadcrumbs unless the page explicitly describes them.

## Cross References

- Add See also: bullet list of explicit links/texts present on the page. Do not fabricate.

<!-- tags: [Essential Diagram, node selection, customization, properties, AllowSelect, AllowRotate, AllowDelete, AllowMoveX, AllowMoveY, AllowChangeHeight, AllowChangeWidth, AllowResize, WinForms, Syncfusion, node customization, properties reference] keywords: [node behavior, editstyle, height, width, selection, rotation, deletion, movement, resize, true, properties description, programmatic setting] -->
```