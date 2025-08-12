```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_081.jpeg
document_name: tools
page_number: 081
page_id: tools#page_081
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T08:20:20Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

This can be done through code as follows.

## Code Example

```csharp
[C#]

private Syncfusion.Windows.Forms.Tools.CommandBarController commandBarController1;
private Syncfusion.Windows.Forms.Tools.CommandBar commandBar1;
private Syncfusion.Windows.Forms.Tools.XPMenus.PopupMenu popupMenu1;
private Syncfusion.Windows.Forms.Tools.XPMenus.ParentBarItem parentBarItems;
private Syncfusion.Windows.Forms.Tools.XPMenus.BarItem barItem1;
private Syncfusion.Windows.Forms.Tools.XPMenus.BarItem barItem2;
private Syncfusion.Windows.Forms.Tools.XPMenus.BarItem barItem3;
private Syncfusion.Windows.Forms.Tools.XPMenus.PopupMenusManager popupMenusManager1;

this.commandBarController1 = new Syncfusion.Windows.Forms.Tools.CommandBarController(this.components);
this.commandBar1 = new Syncfusion.Windows.Forms.Tools.CommandBar();
this.popupMenu1 = new Syncfusion.Windows.Forms.Tools.XPMenus.PopupMenu(this.components);
this.parentBarItems1 = new Syncfusion.Windows.Forms.Tools.XPMenus.ParentBarItem();
this.barItem1 = new Syncfusion.Windows.Forms.Tools.XPMenus.BarItem();
this.barItem2 = new Syncfusion.Windows.Forms.Tools.XPMenus.BarItem();
this.barItem3 = new Syncfusion.Windows.Forms.Tools.XPMenus.BarItem();
this.popupMenusManager1.SetXPContextMenu(this.commandBar1, this.popupMenu1);

// commandBarController1
this.commandBarController1.CommandBars.Add(this.commandBar1);
this.commandBarController1.HostForm = this;

// commandBar1
this.commandBar1.Text = "commandBar1";
this.commandBar1.PopupMenu = this.popupMenu1;
this.popupMenusManager1 = new Syncfusion.Windows.Forms.Tools.XPMenus.PopupMenusManager(this.component);

// popupMenu1
this.popupMenu1.ParentBarItem = this.parentBarItems1;

// parentBarItems1
this.parentBarItems1.Items.AddRange(new Syncfusion.Windows.Forms.Tools.XPMenus.BarItem[] {
```

## Footer

© 2013 Syncfusion. All rights reserved.  
```