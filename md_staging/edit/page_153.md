```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_153.jpeg
document_name: edit
page_number: 153
page_id: edit#page_153
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:04:03Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Overview
- Demonstrates how to show different styles of context menus (Office 2003 and Standard) using Syncfusion's XP Menus and Standard Menus Provider.
- Explains how to customize the context menu by handling the `MenuFill` event.

## Content

### Setting Different Context Menu Styles

The following snippets show how to configure the `contextMenuManager` to display context menus in different styles.

```csharp
// Show Office2003 style context menu.
this.editControl.ContextMenuManager.ContextMenuProvider = new Syncfusion.Windows.Forms.Tools.XPMenus.XPMenusProvider();

// Show Standard style context menu.
this.editControl.ContextMenuManager.ContextMenuProvider = new Syncfusion.Windows.Forms.StandardMenusProvider();
```

```vb.net
' Show Office2003 style context menu
Me.editControl.ContextMenuManager.ContextMenuProvider = New Syncfusion.Windows.Forms.Tools.XPMenus.XPMenusProvider()

' Show Standard style context menu
Me.editControl.ContextMenuManager.ContextMenuProvider = New Syncfusion.Windows.Forms.StandardMenusProvider()
```

### Adding Customized Menu Items

#### Handling the `MenuFill` Event

You can customize the context menu by handling the `MenuFill` event, which is triggered each time the context menu is displayed. This allows you to add, remove, or modify menu items dynamically.

```csharp
// C#

// Handle the MenuFill event which is called each time the context menu is displayed.
this.editControl.MenuFill += new EventHandler(cm_FillMenu);

private void cm_FillMenu(object sender, EventArgs e)
{
    ContextMenuManager cm = (ContextMenuManager) sender;

    // To clear default context menu items.
    cm.ClearMenu();

    // Add a separator.
    cm.AddSeparator();

    // Add custom context menu items and their Click event handlers.
    cm.AddMenuItem("&Find", new EventHandler(ShowFindDialog));
    cm.AddMenuItem("&Replace", new EventHandler(ShowReplaceDialog));
    cm.AddMenuItem("&Goto", new EventHandler(ShowGoToDialog));
}
```

## API Reference

### Syncfusion.Windows.Forms.Tools.ContextMenuManager

- **Methods:**
  - `ClearMenu()`: Clears all items from the context menu.
  - `AddSeparator()`: Adds a separator to the context menu.
  - `AddMenuItem(string text, EventHandler handler)`: Adds a menu item with the given text and event handler.

## Code Examples

### Example of Customizing Context Menu Using `MenuFill` Event

Refer to the previous code snippet under **Adding Customized Menu Items** for an example of how to customize the context menu by handling the `MenuFill` event.

## RAG Annotations

<!-- tags: [Syncfusion Winforms, context menu, customization, XPMenusProvider, StandardMenusProvider, MenuFill event] keywords: [context menu styles, default context menu items, custom menu items, event handling, separator, event handlers] -->
```