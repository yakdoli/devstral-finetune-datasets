```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_083.jpeg
document_name: tools
page_number: 083
page_id: tools#page_083
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:19:26Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to configure Keyboard navigation for the SyncfusionCommandBar.
- Shows the use of the MenuItemManager to configure properties such as the Style, and AlternateStyle in popup menus and toolbar items.
- Illustrates the design-time feature of associating Property window with the SyncfusionCommandBar controls.

## Content

### Configuring CommandBar Properties

The following code snippet illustrates how to configure various properties of the CommandBar control along with its associated menu items. This includes setting the text, style, and associating bar items with the parent bar.

```vb
Me.commandBar1.Text = "commandBar1"
Me.commandBar1.PopupMenu = Me.popupMenu1
Me.popupMenusManager1.SetXPContextMenu(Me.commandBar1, Me.popupMenu1)

' popupMenu1
Me.popupMenu1.ParentBarItem = Me.parentBarItem1

' parentBarItem1
Me.parentBarItem1.Items.AddRange(New Syncfusion.Windows.Forms.Tools.XPMenuS.BarItem() {Me.barItem1, Me.barItem2, Me.barItem3})
Me.parentBarItem1.Style = Syncfusion.Windows.Forms.VisualStyle.OfficeXP

' barItem1
Me.barItem1.Text = "Syncfusion Home"

' barItem2
Me.barItem2.Text = "Windows Forms FAQ"

' barItem3
Me.barItem3.Text = "Syncfusion Sales"
```

#### Figure: "XPContextMenu on popupMenusManager" property in the Properties Window of CommandBar Control

![](attachment://image.png)

### Figure 28: "XPContextMenu on popupMenusManager" property in the Properties Window of CommandBar Control

This figure illustrates the property grid displaying the SyncfusionCommandBar control and its associated properties, especially focusing on the `XPContextMenu` property that is configured on the `popupMenusManager`.

### Key Features Highlighted
- **Keyboard Navigation**: Configures command keys for seamless navigation.
- **MenuItemManager**: Utilizes the `MenuItemManager` for advanced customization.
- **Design-Time Features**: Shows how to associate custom styles and properties in the design-time environment.

### RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [Windows Forms, CommandBar, Keyboard Navigation, MenuItemManager, Syncfusion, toolbar items, popup menus, style, design-time, property window] -->
```