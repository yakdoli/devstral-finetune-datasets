```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_157.jpeg
document_name: diagram
page_number: 157
page_id: diagram#page_157
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:18:32Z
fidelity: lossless
-->

## Essential Diagram for Windows Forms

### Code Snippets

```csharp
rect.EditStyle.AllowChangeHeight = true;
rect.EditStyle.AllowChangeWidth = true;
rect.EditStyle.AllowDelete = false;
rect.EditStyle.AllowMoveX = true;
rect.EditStyle.AllowMoveY = false;
rect.EditStyle.AllowRotate = true;
rect.EditStyle.AllowSelect = true;
```

```vb
[VB]

rect.EditStyle.AllowUserHeight = True
rect.EditStyle.AllowUserWidth = True
rect.EditStyle.AllowUserDelete = False
rect.EditStyle.AllowUserMoveX = True
rect.EditStyle.AllowUserMoveY = False
rect.EditStyle.AllowUserRotate = True
rect.EditStyle.AllowUserSelect = True
```

**In the above code snippets, the properties are set to the Rectangular node (rect) created through the code.**

### Behavior Settings

| Property               | Description                                                                                   |
|------------------------|-----------------------------------------------------------------------------------------------|
| AspectRatio            | Specifies whether to maintain the height and width ratio when the node is resized.           |
| DefaultHandleEditMode  | Specifies the mode in which the node should be handled. The default value for links and lines is Vertex and for all other nodes and polyline the default value is Resize. To move the nodes, DefaultHandleEditMode should be set to Resize. <br> The options provided are as follows. <br> • None <br> • Resize <br> • Vertex |
| Enabled                | Specifies whether the node is enabled. Default value is `True`.                            |

---

<div style="text-align: right;">© 2013 Syncfusion. All rights reserved.</div>
---

<!-- tags: [syncfusion, winforms, diagram, essential diagram, behavior settings, properties, aspect ratio, default handle edit mode, enabled] keywords: [behavior settings, essential diagram, properties, aspect ratio, default handle edit mode, enabled, node, rect, allow change height, allow change width, allow delete, allow move x, allow move y, allow rotate, allow select, syncfusion windows forms] -->
```