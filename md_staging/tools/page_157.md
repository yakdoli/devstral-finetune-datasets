```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_157.jpeg
document_name: tools
page_number: 157
page_id: tools#page_157
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:59:41Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- The page discusses customization of the CaptionButton Collection Editor and the implementation of context menus in Syncfusion Winforms.
- Features like SuperToolTip customization are explained using the CaptionButton Collection Editor.
- Context menus are discussed for right-clicking the caption bar and for the menu button in the caption bar.

## Content

### WinForms-specific features

#### CaptionButton Collection Editor
**Figure 72: SuperToolTip customized by using the CaptionButton Collection Editor**

The CaptionButton Collection Editor allows for customizing the properties of various buttons such as CloseButton, PinButton, MenuButton, MaximizeButton, and RestoreButton. The screenshot shows the editor interface where users can modify properties such as BackColor, BorderColor, and ToolTip for each button.

#### 3.4.3.4.3 Context Menu

A context menu is displayed whenever the user right-clicks the caption bar or clicks the menu button in the caption bar. The `EnableContextMenu` property should be set to `true` to display the context menu, which is true by default.

**When Docked Control is in Autohide Mode**
When the docked control is in autohide mode, clicking the auto hide tab right-clicks will display a unique context menu, similar to Visual Studio. The `EnableAutoHideTabContextMenu` property should be set to `true` for this functionality, which is also true by default.

#### Code Examples

##### [C#]
```csharp
this.dockingManager1.EnableContextMenu = true;
this.dockingManager1.EnableAutoHideTabContextMenu = true;
```

##### [VB.NET]
```vbnet
Me.dockingManager1.EnableContextMenu = True
Me.dockingManager1.EnableAutoHideTabContextMenu = True
```

## API Reference

### Properties
- **EnableContextMenu**: Boolean property that determines whether the context menu is displayed when the caption bar is right-clicked. Default value is `true`.
- **EnableAutoHideTabContextMenu**: Boolean property that determines whether a unique context menu is displayed when the auto hide tab is right-clicked. Default value is `true`.

## Cross References
- Related features such as button customization and docking management are part of Syncfusion Winforms controls.

<!-- tags: [Syncfusion Winforms, CaptionButtons, ContextMenu, AutoHide, DockingControl] keywords: [CaptionButton Collection Editor, SuperToolTip, EnableContextMenu, EnableAutoHideTabContextMenu, ContextMenu] -->
```