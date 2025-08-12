```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_559.jpeg
document_name: tools
page_number: 559
page_id: tools#page_559
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:21:08Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview

- The ComboDropDown control allows users to interact with tree nodes by editing or double-clicking on them.
- The control provides functionality to select nodes in the drop-down either by double-clicking or editing the text.
- Interactive features include suppressing dropdown events and associating with GridList controls.

## Content

### Node Interaction

At run time:

1. When the user double-clicks on a node, the node text will appear in the ComboDropDown.
2. When the user edits the text, the corresponding node will be selected in the tree in the drop-down.

### Figure: Selecting the Edited Node

![Figure 344: Selecting the Edited Node](attachment_or_image_path_here)

#### Note

We can also suppress the dropdown event from firing by setting the `SuppressDropDownEvent` property to `true`.

### Interactive GridList Control

We can associate a GridList control with the ComboDropDown to make it interactive. A sample demonstrating this feature is available in the following sample installation location:

```
..\My Documents\Syncfusion\EssentialStudio\Version Number\Windows\Tools.Windows\Samples\2.0\Editors Package\ComboDropDown
```

### Make the Drop-Down Respond to Mouse Move

**Overview**

By default, the drop-down control does not have the focus when it is displayed, so it will not respond to mouse move messages. To address this, you can force the control hosted in the drop-down to take focus when the drop-down is shown.

#### Steps

1. Drag the ComboDropDown and TreeView control onto the Form.
2. Add a TreeView with nodes to the drop-down portion of the ComboDropDown.
3. Listen to the ComboDropDown's `PopupContainer's Popup` event. This event will be fired after the drop-down is shown.
4. In this event, call the drop-down control's `Focus` method.

#### Code Example

```csharp
[C#]
```

## Page-level Navigation/TOC (if applicable)

- Essential Tools for Windows Forms
  - Node Interaction
  - Selecting the Edited Node
  - Interactive GridList Control
  - Make the Drop-Down Respond to Mouse Move

## RAG Annotations

<!-- tags: [ComboDropDown, TreeView, GridListControl, WinForms, Syncfusion, version 11.4.0.26] keywords: [ComboDropDown, Node, Double-Click, Edit, TreeView, GridList, SuppressDropDownEvent, MouseMove, Focus, Popup] -->
```