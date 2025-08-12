```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_204.jpeg
document_name: tools
page_number: 204
page_id: tools#page_204
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:30:06Z
fidelity: lossless
-->


## Docking Events

### Overview
- The Essential Tools DockingManager provides functionality for creating and working with enhanced docking windows.
- These docking windows can be attached to a host form's border, dragged around, docked to different edges, or floated as individual top-level windows.
- The framework allows any child control on a form to be made into a fully qualified docking window.
- The DockingManager offers programmatic access to interactions between dockable windows, including complex features like multiple docking levels, nested docking, tabbed docking, autohide mode, and state persistence.

### Content

#### 3.4.3.8 Docking Events
The Essential Tools DockingManager provides the functionality for creating and working with enhanced docking windows that support attaching to a host form's border, dragging around and docking to different edges within the form and also be dragged off the host form and floated as an individual top-level window.

The Essential Tools docking framework allows just about any child control on a form to be made into a fully qualified docking window. The Docking manager provides programmatic access to the interaction between these dockable windows and other complex features like multiple docking levels, nested docking, tabbed docking, tear-off tabs, autohide mode, state persistence etc., by raising several events.

The list of events and a detailed explanation about each of them is given in the following sections.

#### Table: Docking Events

| Docking Events               | Description                                                                                                                                     |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| AutoHideAnimationStart       | The AutoHideAnimationStart event occurs just before the start of an autohide animation.                                                       |
| AutoHideAnimationStop        | The AutoHideAnimationStop event occurs immediately after the end of an autohide animation.                                                  |
| AutoHideTabContextMenu       | This event occurs when the right mouse button is clicked over a AutoHideTabControl.                                                          |
| DockMenuClick                | This event occurs when the redock context menu item has been clicked.                                                                         |
| ControlMaximized             | This event occurs after the control is maximized.                                                                                           |
| ControlMaximizing            | This event occurs before the control is going to maximize.                                                                                  |
| ControlMinimized             | This event occurs after the control is minimized.                                                                                          |
| ControlRestored              | This event occurs after the control is restored.                                                                                           |
| DockAllow                    | The DockAllow event occurs when a docking window is dragged over a potential dock target.                                                   |
| DockContextMenu              | The DockContextMenu event occurs when the right mouse button is clicked over a docking|

### Cross References
See also: [unclear]

### RAG Annotations
<!-- tags: [DockingManager, docking windows, autohide, tabbed docking, state persistence, DockAllow, ControlMaximized, ControlMinimized, ControlRestored] keywords: [docking, windows, autohide animation, tabbed docking, nested docking, control properties, event descriptions] -->
```