```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_262.jpeg
document_name: tools
page_number: 262
page_id: tools#page_262
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T10:03:27Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

### Overview
- Demonstrates how to attach a `TabbedMDIManager` to an MDI container.
- Explains how to enable docking for user controls.
- Details setting user controls as MDI children in a docking manager.

### Content

```vb
Me.tabbedMDIManager.AttachToMdiContainer(Me)

' Dock the User Controls
Me.dockingManager1.SetEnableDocking(Me.userControl1, True)
Me.dockingManager1.SetEnableDocking(Me.userControl2, True)
Me.dockingManager1.SetEnableDocking(Me.userControl3, True)

' Set the user controls to MDI mode
Me.dockingManager1.SetAsMDIChild(Me.userControl1, True)
Me.dockingManager1.SetAsMDIChild(Me.userControl2, True)
Me.dockingManager1.SetAsMDIChild(Me.userControl3, True)
```

![Form1 showing UserControls used as TabbedMDIManager's children by using the Docking Manager](image.png)

**Figure 109: UserControls used as TabbedMDIManager's Children by using the Docking Manager**

### See Also
- [MDI Child Transition](#)

#### 3.4.4.5 Context Menu

This section covers the following topics:

##### 3.4.4.5.1 How to customize the dock context menu of a docked control?

This can be done in the `DockContextMenu` event.

<!-- tags: [Syncfusion, Winforms, DockingManager, MDIChild, TabbedMDIManager, ContextMenu, Docking, MDIChildTransition, DockedControl, ContextMenuCustomization] keywords: [DockingManager, MDIChild, MDIChildTransition, TabbedMDIManager, DockContextMenu, DockedControl, ContextMenu, Customization, Windows Forms] -->
```