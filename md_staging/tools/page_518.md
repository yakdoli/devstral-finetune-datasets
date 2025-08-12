```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_518.jpeg
document_name: tools
page_number: 518
page_id: tools#page_518
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:18:29Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This page explains how to work with `ParentBarItem` and `DropDownBarItem` in a `PopupMenu` context.
- It provides steps to configure the `PopupControlContainer` related to `DropDownBarItem`.

---

## Content

### Configuring Bar Items in a PopupMenu

#### Step 4: Adding and Configuring Bar Items
1. In the property grid of `PopupMenu`, expand `ParentBarItem`, then add a `DropDownBarItem` to the `ParentBarItem` using the **BarItem Collection Editor**.
2. Set the `PopupControlContainer` as the `DropDownBarItem`'s `PopupControlContainer`, as shown in the image below.

**Figure 303: Adding Default ParentBarItem**
![](image1.png)

**Explanation:**
- Upon expanding `ParentBarItem` in the `BarManager` properties, the `MenuBar` and `Item` controls will appear. Add a `Default ParentBarItem` using the **BarManager's context menu**.

**Figure 304: Assigning PopupControlContainer to DropDownBarItem**
![](image2.png)

**Explanation:**
- Open the **BarItem Collection Editor** when editing a `ParentBarItem` in the property grid.
- Locate the `DropDownBarItem` in the properties editor and set the `PopupControlContainer` property to the desired container.

#### Step 5: Handling the MouseUp Event
- In the `MouseUp` event of the `Panel` control, call the `PopupMenu.Show` method to display the configured menu.

---

## RAG Annotations
<!-- tags: [PopupMenu, ParentBarItem, DropDownBarItem, PopupControlContainer, Windows Forms, BarItem Collection Editor] keywords: [PopupMenu, ParentBarItem, DropDownBarItem, BarItem, Property Grid, BarManager, MouseUp, Show, Syncfusion] -->
```