```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_214.jpeg
document_name: tools
page_number: 214
page_id: tools#page_214
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:38:47Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates how to initialize and set properties for a `ParentBarItem` and `BarItem` using Syncfusion.Windows.Forms.Tools.XPMenus.
- Adds the `File` menu with an `Exit` option to the DockContextMenu.
- Includes both C# and VB.NET code examples.

## Content

### C# Code Example

```csharp
private Syncfusion.Windows.Forms.Tools.XPMenus.ParentBarItem pbiFile;

// Initialize and set the properties.
this.pbiFile = new Syncfusion.Windows.Forms.Tools.XPMenus.ParentBarItem();
this.bar1 = new Syncfusion.Windows.Forms.Tools.XPMenus.BarItem();
this.pbiFile.Text = "File";
this.bar1.Text = "Exit";
this.pbiFile.Items.AddRange(new Syncfusion.Windows.Forms.Tools.XPMenus.BarItem[] { this.bar1 });
// Call the event
this.dockingManager1.DockContextMenu += new Syncfusion.Windows.Forms.Tools.DockContextMenuEventHandler(this.dockingManager1_DockContextMenu);

private void dockingManager1_DockContextMenu(object sender,
Syncfusion.Windows.Forms.Tools.DockContextMenuEventArgs arg)
{
    arg.ContextMenu.ParentBarItem.Items.Add(this.pbiFile);
}
```

### VB.NET Code Example

```vb
' Adding Namespace
Imports Syncfusion.Windows.Forms.Tools.XPMenus

' Declaration
Private pbiFile As Syncfusion.Windows.Forms.Tools.XPMenus.ParentBarItem
Private WithEvents bar1 As Syncfusion.Windows.Forms.Tools.XPMenus.BarItem

' Initialize and set the properties
Me.pbiFile = New Syncfusion.Windows.Forms.Tools.XPMenus.ParentBarItem()
Me.bar1 = New Syncfusion.Windows.Forms.Tools.XPMenus.BarItem()
Me.pbiFile.Text = "File"
Me.bar1.Text = "Exit"
Me.pbiFile.Items.AddRange(New Syncfusion.Windows.Forms.Tools.XPMenus.BarItem() { Me.bar1})

'handling the event
Private Sub dockingManager1_DockContextMenu(ByVal sender As Object, ByVal arg As Syncfusion.Windows.Forms.Tools.DockContextMenuEventArgs)
    arg.ContextMenu.ParentBarItem.Items.Add(Me.pbiFile)
End Sub
```

## API Reference

### Classes and Members
- **Syncfusion.Windows.Forms.Tools.XPMenus.ParentBarItem**
  - `Text`: Property to set the display text of the parent bar item.
  - `Items`: Property to manage the collection of child bar items.
- **Syncfusion.Windows.Forms.Tools.XPMenus.BarItem**
  - `Text`: Property to set the display text of the bar item.
- **Syncfusion.Windows.Forms.Tools.DockContextMenuEventHandler**
  - Event handler for handling the DockContextMenu event.

## Code Examples (Multi-Language Supported)
- **C#**: Demonstrates creating a `ParentBarItem` with a child `BarItem` and handling the DockContextMenu event.
- **VB.NET**: Equivalent functionality using VB.NET syntax.

## RAG Annotations
<!-- tags: [Syncfusion, WinForms, Tools, ParentBarItem, BarItem, DockContextMenu] keywords: [ParentBarItem, BarItem, DockContextMenu, Syncfusion, Windows Forms, XP Menus, C#, VB.NET, initialization, properties, event handling] -->
```