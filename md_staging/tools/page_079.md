```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_079.jpeg
document_name: tools
page_number: 079
page_id: tools#page_079
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:18:59Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

[VB.NET]

```vb
Private commandBarController1 As Syncfusion.Windows.Forms.Tools.CommandBarController
Private commandBar1 As Syncfusion.Windows.Forms.Tools.CommandBar
Private popupMenu1 As Syncfusion.Windows.Forms.XPMenu.PopupMenu
Private parentBarItem1 As Syncfusion.Windows.Forms.Tools.XPMenu.ParentBarItem
Private barItem1 As Syncfusion.Windows.Forms.Tools.XPMenu.BarItem
Private barItem2 As Syncfusion.Windows.Forms.Tools.XPMenu.BarItem
Private barItem3 As Syncfusion.Windows.Forms.Tools.XPMenu.BarItem

Me.commandBarController1 = New Syncfusion.Windows.Forms.Tools.CommandBarController(Me.components)
Me.commandBar1 = New Syncfusion.Windows.Forms.Tools.CommandBar()
Me.popupMenu1 = New Syncfusion.Windows.Forms.XPMenu.PopupMenu(Me.components)
Me.parentBarItem1 = New Syncfusion.Windows.Forms.Tools.XPMenu.ParentBarItem()
Me.barItem1 = New Syncfusion.Windows.Forms.Tools.XPMenu.BarItem()
Me.barItem2 = New Syncfusion.Windows.Forms.Tools.XPMenu.BarItem()
Me.barItem3 = New Syncfusion.Windows.Forms.Tools.XPMenu.BarItem()

' commandBarController1
Me.commandBarController1.CommandBars.Add(Me.commandBar1)
Me.commandBarController1.HostForm = Me

' commandBar1
Me.commandBar1.Text = "commandBar1"
Me.commandBar1.PopupMenu = Me.popupMenu1

' popupMenu1
Me.popupMenu1.ParentBarItem = Me.parentBarItem1

' parentBarItem1
Me.parentBarItem1.Items.AddRange(New Syncfusion.Windows.Forms.Tools.XPMenu.BarItem() {Me.barItem1, Me.barItem2, Me.barItem3})
Me.parentBarItem1.Style = Syncfusion.Windows.Forms.VisualStyle.OfficeXP

' barItem1
Me.barItem1.Text = "Syncfusion Home"

' barItem2
Me.barItem2.Text = "Windows Forms FAQ"

' barItem3
```

## API Reference

### Syncfusion.Windows.Forms.Tools.CommandBarController
- **CommandBars.Add(CommandBar commandBar)**: Adds the specified command bar to the collection.

### Syncfusion.Windows.Forms.Tools.CommandBar
- **Text**: Gets or sets the text associated with the command bar.
- **PopupMenu**: Gets or sets the popup menu associated with the command bar.

### Syncfusion.Windows.Forms.XPMenu.PopupMenu
- **ParentBarItem**: Gets or sets the parent bar item that displays the popup menu.

### Syncfusion.Windows.Forms.Tools.XPMenu.ParentBarItem
- **Items.AddRange(BarItem() barItems)**: Adds the specified collection of bar items to the collection.
- **Style**: Gets or sets the visual style of the parent bar item.

### Syncfusion.Windows.Forms.Tools.XPMenu.BarItem
- **Text**: Gets or sets the text associated with the bar item.

## Code Examples

### Creating a Command Bar with a Pop-up Menu

This example demonstrates how to create a `CommandBar` with a pop-up menu containing three bar items:

```vb
Private commandBarController1 As Syncfusion.Windows.Forms.Tools.CommandBarController
Private commandBar1 As Syncfusion.Windows.Forms.Tools.CommandBar
Private popupMenu1 As Syncfusion.Windows.Forms.XPMenu.PopupMenu
Private parentBarItem1 As Syncfusion.Windows.Forms.Tools.XPMenu.ParentBarItem
Private barItem1 As Syncfusion.Windows.Forms.Tools.XPMenu.BarItem
Private barItem2 As Syncfusion.Windows.Forms.Tools.XPMenu.BarItem
Private barItem3 As Syncfusion.Windows.Forms.Tools.XPMenu.BarItem

Me.commandBarController1 = New Syncfusion.Windows.Forms.Tools.CommandBarController(Me.components)
Me.commandBar1 = New Syncfusion.Windows.Forms.Tools.CommandBar()
Me.popupMenu1 = New Syncfusion.Windows.Forms.XPMenu.PopupMenu(Me.components)
Me.parentBarItem1 = New Syncfusion.Windows.Forms.Tools.XPMenu.ParentBarItem()
Me.barItem1 = New Syncfusion.Windows.Forms.Tools.XPMenu.BarItem()
Me.barItem2 = New Syncfusion.Windows.Forms.Tools.XPMenu.BarItem()
Me.barItem3 = New Syncfusion.Windows.Forms.Tools.XPMenu.BarItem()

' Add the command bar to the controller
Me.commandBarController1.CommandBars.Add(Me.commandBar1)
Me.commandBarController1.HostForm = Me

' Configure the command bar
Me.commandBar1.Text = "commandBar1"
Me.commandBar1.PopupMenu = Me.popupMenu1

' Configure the pop-up menu
Me.popupMenu1.ParentBarItem = Me.parentBarItem1

' Add bar items to the parent bar item
Me.parentBarItem1.Items.AddRange(New Syncfusion.Windows.Forms.Tools.XPMenu.BarItem() {Me.barItem1, Me.barItem2, Me.barItem3})
Me.parentBarItem1.Style = Syncfusion.Windows.Forms.VisualStyle.OfficeXP

' Set text for the bar items
Me.barItem1.Text = "Syncfusion Home"
Me.barItem2.Text = "Windows Forms FAQ"
```

<!-- tags: [Syncfusion Winforms, CommandBar, Pop-up Menu, BarItem] keywords: [commandBarController, commandBar, popupMenu, parentBarItem, barItem] -->
```