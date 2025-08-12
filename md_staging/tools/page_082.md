```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_082.jpeg
document_name: tools
page_number: 082
page_id: tools#page_082
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:20:13Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- This section demonstrates the use of Syncfusion's Windows Forms Tools for creating a command bar with menu items.
- It provides examples in both C# and VB.NET for configuring and setting up a `CommandBar` with multiple menu items.

## Content

### CommandBar Configuration in C#

```csharp
this.barItem1,
this.barItem2,
this.barItem3});
this.parentBarItem1.Style =
Syncfusion.Windows.Forms.VisualStyle.OfficeXP;

// barItem1
this.barItem1.Text = "Syncfusion Home";

// barItem2
this.barItem2.Text = "Windows Forms FAQ";

// barItem3
this.barItem3.Text = "Syncfusion Sales";
```

### CommandBar Configuration in VB.NET

```vb
Private commandBarController1 As
Syncfusion.Windows.Forms.Tools.CommandBarController
Private commandBar1 As
Syncfusion.Windows.Forms.Tools.CommandBar
Private popupMenu1 As
Syncfusion.Windows.Forms.Tools.XPMenus.PopupMenu
Private parentBarItem1 As
Syncfusion.Windows.Forms.Tools.XPMenus.ParentBarItem
Private barItem1 As
Syncfusion.Windows.Forms.Tools.XPMenus.BarItem
Private barItem2 As
Syncfusion.Windows.Forms.Tools.XPMenus.BarItem
Private barItem3 As
Syncfusion.Windows.Forms.Tools.XPMenus.BarItem
Private popupMenusManager1 As
Syncfusion.Windows.Forms.Tools.XPMenus.PopupMenusManager

Me.commandBarController1 = New
Syncfusion.Windows.Forms.Tools.CommandBarController(Me.components)
Me.commandBar1 = New
Syncfusion.Windows.Forms.Tools.CommandBar()
Me.popupMenu1 = New
Syncfusion.Windows.Forms.Tools.XPMenus.PopupMenu(Me.components)
Me.parentBarItem1 = New
Syncfusion.Windows.Forms.Tools.XPMenus.ParentBarItem()
Me.barItem1 = New
Syncfusion.Windows.Forms.Tools.XPMenus.BarItem()
Me.barItem2 = New
Syncfusion.Windows.Forms.Tools.XPMenus.BarItem()
Me.barItem3 = New
Syncfusion.Windows.Forms.Tools.XPMenus.BarItem()
Me.popupMenusManager1 = New
Syncfusion.Windows.Forms.Tools.XPMenus.PopupMenusManager(Me.components)

' commandBarController1
Me.commandBarController1.CommandBars.Add(Me.commandBar1)
Me.commandBarController1.HostForm = Me

' commandBar1
```

## API Reference

### Namespaces and Classes
- `Syncfusion.Windows.Forms.Tools.CommandBarController`
- `Syncfusion.Windows.Forms.Tools.CommandBar`
- `Syncfusion.Windows.Forms.Tools.XPMenus.PopupMenu`
- `Syncfusion.Windows.Forms.Tools.XPMenus.ParentBarItem`
- `Syncfusion.Windows.Forms.Tools.XPMenus.BarItem`
- `Syncfusion.Windows.Forms.Tools.XPMenus.PopupMenusManager`

### Methods and Properties
- `CommandBarController.CommandBars.Add(CommandBar bar)`
- `CommandBarController.HostForm`
- `ParentBarItem.Style`

## Code Examples

### C# Example
The provided C# example demonstrates how to configure and add `barItems` to a `ParentBarItem` within a `CommandBar`.

### VB.NET Example
The VB.NET example showcases the creation and initialization of a `CommandBar` along with its associated `barItems` and `popupMenu`.

<!-- tags: [Windows Forms, CommandBar, SyncGrid, VisualStyle, OfficeXP] keywords: [ToolBar, ParentBarItem, BarItem, PopupMenu, HostForm] -->
```