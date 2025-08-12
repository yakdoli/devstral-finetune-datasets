```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_186.jpeg
document_name: diagram
page_number: 186
page_id: diagram#page_186
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:20:10Z
fidelity: lossless
--> 

### Overview

- This section discusses the interactive features like scrolling, zooming, and panning support in Windows Forms.
- It explains how to manage the GroupNodePosition property and its functionality.
- Details on enabling or disabling horizontal and vertical scrollbars using HScroll and VScroll properties.

### Content

#### 4.6.7 Scrolling, Zooming And Panning Support

The interactive features like scrolling, zooming, and panning support are discussed in this section:

##### 4.6.7.1 Scroll Support

The horizontal and vertical scrollbars can be displayed or hidden by handling the HScroll and VScroll properties.

| Properties  | Description                                                                    |
|-------------|--------------------------------------------------------------------------------|
| HScroll     | Specifies whether to display the horizontal scrollbar.                          |
| VScroll     | Specifies whether to display the vertical scrollbar.                            |

**Programmatically, these properties can be set as follows.**

```csharp
this.diagram1.HScroll = true;
this.diagram1.VScroll = true;
```

```vb
Me.diagram1.HScroll = True
Me.diagram1.VScroll = True
```

#### Table: GroupNodePosition

| Name             | Description                                                                 | Type               | Default value | Value Accepted  | Reference         |
|------------------|-----------------------------------------------------------------------------|--------------------|---------------|-----------------|-------------------|
| GroupNodePosition | Specifies the mode in which the group node's child should be positioned. | GroupNodePositions | Relative      | Absolute, <br> Relative | GroupNodePosition |

<!-- tags: [Syncfusion, WinForms, control layout, GroupNodePosition, HScroll, VScroll, scrolling, zooming, panning, .NET, Windows Forms] keywords: [GroupNodePosition, HScroll, VScroll, scrolling, zooming, panning, interactive features, WinForms, Syncfusion] -->
```