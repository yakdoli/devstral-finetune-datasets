```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_123.jpeg
document_name: tools
page_number: 123
page_id: tools#page_123
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:37:01Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Drag and drop the DockingManager control onto a form to implement docking functionality.
- Configure the EnableDocking property for child controls to enable docking behavior.
- Turn on EnableDocking to transform controls into docking windows.

## Content

### Step-by-Step Guide

#### Step 2: Adding DockingManager and Enabling Docking

By dragging a DockingManager control from the toolbox onto the form, the docking manager is implemented as an extender provider. This will add the `EnableDocking` property to all child controls that are dropped onto the form. The effect is visualized in the image below.

![](DockingWindow.png)

**Figure 42: EnableDocking on dockingManager property added to the Properties Grid of the ListBox Control**

#### Step 3: Enabling Docking for Controls

Turn on the `EnableDocking` property for those controls that should be hosted as docking windows. Setting this property will immediately transform the control into a docking window by creating a dockable container and adding the control to it. The control is now a full-featured docking window that is docked to the form's left border, as shown in the image below.

## API Reference

### Properties
- **EnableDocking**: Controls whether the associated control can be docked.

## Code Examples

### Example: Enabling Docking for a ListBox

```csharp
// EnableDocking property for ListBox1
ListBox1.EnableDocking = true;
```

## Page-level Navigation/TOC
- Essential Tools for Windows Forms
  - Step-by-Step Guide
    - Step 2: Adding DockingManager and Enabling Docking
    - Step 3: Enabling Docking for Controls

## Cross References
- See also: "DockingManager Overview" for a deeper understanding of docking functionality.

<!-- tags: [syncfusion, winforms, dockingmanager, tools, extensionprovider] keywords: [enabledocking, propertiesgrid, listbox, dockablewindow, dockmanager] -->
```