```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_147.jpeg
document_name: tools
page_number: 147
page_id: tools#page_147
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:53:37Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Features detailed customization options for captions in docked controls.
- Explains the properties controlling the visibility of various buttons associated with docked controls.
- Provides details on the configuration and functionality of menu, maximize, and other buttons.

## Content

### 3.4.3.2.2 Caption Buttons

#### Note:
- **Background** and **foreground** appearance of the captions can be customized.

**See Also**
- Caption Buttons, Custom Caption Buttons

The buttons available for the docked control and the properties which control the visibility of the button are discussed in this section.

#### Figure 63: Buttons for the Docked Control

![Buttons for the Docked Control](#)

The docked control has several buttons that can be customized:
- **Maximize Button**: Enables or disables the maximize functionality.
- **Menu Button**: Displays context menu items when clicked.
- **Close Button**: Closes the docked window.
- **AutoHide Button**: Toggles the autohide feature.
- **Tabbed Docking, AutoHiding, Floating**: Optional modes for docking behavior.

#### Menu Button
The menu button in a docked control can be made visible or hidden by setting the `MenuButtonEnabled` property to `true`. Clicking this button will display the context menu items.

#### Maximize Button
Maximize button can be enabled by using the `MaximizeButtonEnabled` property. This maximize button allows users to maximize / restore a docking window, so that a clear view of the contents can be made visible.

## API Reference

### Properties
- `MaximizeButtonEnabled`: Boolean property to enable or disable the maximize button.
- `MenuButtonEnabled`: Boolean property to enable or disable the menu button.

#### Example Usage in C#
```csharp
dockingControl.MaximizeButtonEnabled = true;
dockingControl.MenuButtonEnabled = true;
```

### Code Examples
#### C#
```csharp
using Syncfusion.Windows.Forms.Tools;

// Example usage:
DockingControl dockingControl = new DockingControl();
dockingControl.MaximizeButtonEnabled = true;
dockingControl.MenuButtonEnabled = true;
```

## RAG Annotations
<!-- tags: [Syncfusion Winforms, docked controls, caption buttons, maximize, menu, autohide, tabbed docking, autohiding, floating] keywords: [customization, captions, visibility, maximize, menu, close, autohide, tabbed docking, autohiding, floating, buttons, properties] -->
```