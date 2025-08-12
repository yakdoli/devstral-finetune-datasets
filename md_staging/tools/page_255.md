```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_255.jpeg
document_name: tools
page_number: 255
page_id: tools#page_255
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:01:59Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This section discusses how to work with docked controls in Windows Forms, focusing on accessing and modifying the collection of dock-enabled controls.
- Covers the use of the DockingManager and its Controls property to manage docked controls effectively.

## Content

### 3.4.4.3 Docked Group

This section covers the following topics:

#### 3.4.4.3.1 How to Access the Collection of Dock-Enabled Controls?

The DockingManager.Controls property returns an enumerator that may be used for accessing the controls that are currently associated with the DockingManager. To access and modify the DockingManager's control, the contents of the enumerator should first be copied to a temporary collection.

**Step 1: Create the respective controls and dock the control through design by setting EnableDocking on dockingManager property to true and follow the below given steps to enable, access and modify the docked controls.**

#### Figure 106: Docked Controls
![Docked Controls](https://i.imgur.com/AbbMqVJ.png)

**Step 2: Access and modify the dockable controls.**

The below given code snippet accesses the docked controls, disables docking, and then disposes the dockable controls.

## Code Examples
```csharp
// Example code to access and modify dockable controls
foreach (var control in dockingManager.Controls)
{
    control.Dock = DockStyle.None;
    control.Dispose();
}
```

### WinForms-specific conventions
- The example demonstrates how to iterate through the DockingManager.Controls collection, modify the Dock property, and dispose of the controls.

## API Reference
- **Namespace:** Syncfusion.Windows.Forms
- **Class:** DockingManager
- **Members:** Controls (property)

## RAG Annotations
<!-- tags: [DockingManager, DockedControls, WindowsForms] keywords: [DockStyle, enumerator, controls, dispose] -->
```