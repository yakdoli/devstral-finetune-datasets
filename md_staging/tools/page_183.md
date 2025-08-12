```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_183.jpeg
document_name: tools
page_number: 183
page_id: tools#page_183
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:17:47Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes how to use the DockingClientPanel control in forms without the MDIContainer style set.
- Provides a step-by-step guide to setting up a docking layout on a non-MDIContainer form using DockingClientPanel.
- Explains properties and behavior of DockingClientPanel in managing docking windows and static relative bounds for non-dockable controls.

## Using the DockingClientPanel Control

### Key Points
- The DockingClientPanel is used to manage docking windows and non-dockable controls requiring static relative bounds.
- It acts as a container to implement positioning and layout management for non-dockable controls.

### Step-by-Step Guide

1. Add the DockingManager to the form and apply the EnableDocking on dockingManager1 property for those controls that need to be set as docking windows.
2. Select the DockingClientPanel control from the designer toolbox and drop it onto the form hosting the DockingManager. Size the control so that its bounds are sufficient to accommodate any non-dockable child controls that may already be present on the form.
3. [unclear]
4. If any non-dockable controls are present on the form, then drag-and-drop these controls onto the DockingClientPanel instance.
5. [unclear]
6. Set the DockingClientPanel.SizeToFit property to be true. Turning on the SizeToFit property will force the DockingClientPanel to start interacting with the Essential Tools docking architecture and the control will automatically be resized / repositioned to occupy the form's client bounds, left unoccupied by the docking windows.
7. [unclear]
8. Set the BorderStyle property to get the 3D or fixed single effect to the dockingclientpanel control.
9. [unclear]
10. The DockingClientPanel will now function as a proxy for the form's client surface and all controls originally intended to be placed on the form should henceforth be located on the DockingClientPanel; any anchoring / layout features for the child controls should be set relative to the DockingClientPanel.
11. [unclear]
12. To add controls directly to the form, the SizeToFit property can temporarily be turned off within the designer and the form resized to expose its surface. At run-time, the SizeToFit property is always enabled.

### DockingClientPanel Properties

| DockingClientPanel Property | Description |
|-----------------------------|-------------|
| SizeToFit                  | Gets or sets a value indicating whether the control is sized to fill the form's area. |
| BorderStyle                | Indicates the border Style of the Control. |

13. DockingClientPanel control can be added to the Non-MDI forms using the below code snippet for example.

### API Reference
- **Namespace**: Syncfusion.Windows.Forms.Tools
- **Class**: DockingClientPanel
- **Properties**:
  - **SizeToFit**: Boolean
  - **BorderStyle**: BorderStyle
- **Behavior**:
  - SizeToFit automatically adjusts the DockingClientPanel size to fit the form's client area, leaving space for docking windows.
  - BorderStyle determines the appearance style of the DockingClientPanel.

### Code Examples
```csharp
// Example of using DockingClientPanel
DockingClientPanel dockingClientPanel = new DockingClientPanel();
dockingClientPanel.SizeToFit = true;
dockingClientPanel.BorderStyle = BorderStyle.Fixed3D;
dockingClientPanel.Dock = DockStyle.Fill;

this.Controls.Add(dockingClientPanel);
```

### See also:
- DockingManager
- Docking Architecture
- MDIContainer Style
- SizeToFit Property
- BorderStyle Property

<!-- tags: [syncfusion, winforms, dockingclientpanel, essential tools, non-mdicontainer, dundockingmanager, sizefit] keywords: [docking, client panel, layout management, non-dockable controls, essentialtools, winforms controls] -->
```