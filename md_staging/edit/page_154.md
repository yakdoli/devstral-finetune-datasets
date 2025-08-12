```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_154.jpeg
document_name: edit
page_number: 154
page_id: edit#page_154
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:03:30Z
fidelity: lossless
-->


# Essential Edit for Windows Forms

## Overview
- Demonstrates how to interact with the context menu in the `EditControl` of Syncfusion WinForms.
- Shows methods to call in-built dialogs such as `Find`, `Replace`, and `GoTo`.
- Includes examples in both C# and VB.NET for handling menu events and creating custom context menu items.

## Content

### Accessing the Underlying Menu Provider and Calling Dialogs

```csharp
// If you need to get access to the underlying menu provider you can access it using the below given code.
Syncfusion.Windows.Forms.IContextMenuProvider contextMenuProvider = this.editControl1.ContextMenuManager.ContextMenuProvider;
}

// Calling the in-built dialogs.

void ShowFindDialog(object sender, EventArgs e)
{
    this.editControl1.ShowFindDialog();
}

void ShowReplaceDialog(object sender, EventArgs e)
{
    this.editControl1.ShowReplaceDialog();
}

void ShowGoToDialog(object sender, EventArgs e)
{
    this.editControl1.ShowGoToDialog();
}
```

### Handling Context Menu in VB.NET

```vb
' Handle the MenuFill event which is called each time the context menu is displayed.
AddHandler Me.editControl1.MenuFill, AddressOf cm_FillMenu

Private Sub cm_FillMenu(ByVal sender As Object, ByVal e As EventArgs)
    Dim cm As ContextMenuManager = DirectCast(sender, ContextMenuManager)

    ' To clear default context menu items.
    cm.ClearMenu()

    ' Add a separator.
    cm.AddSeparator()

    ' Add custom context menu items and their Click eventhandlers.
    cm.AddMenuItem("&Find", New EventHandler(AddressOf ShowFindDialog))
    cm.AddMenuItem("&Replace", New EventHandler(AddressOf ShowReplaceDialog))
    cm.AddMenuItem("&Goto", New EventHandler(AddressOf ShowGoToDialog))

    ' If you need to get access to the underlying menu provider you can access it using the below given code.
    Dim contextMenuProvider As Syncfusion.Windows.Forms.IContextMenuProvider = 
```

## API Reference (if applicable)
- **Namespace**: `Syncfusion.Windows.Forms`
- **Class**: `EditControl`
  - **Methods**:
    - `ShowFindDialog()`
    - `ShowReplaceDialog()`
    - `ShowGoToDialog()`
  - **Events**:
    - `MenuFill`

## Code Examples (multi-language supported)
### C#
```csharp
// Example of showing a Find dialog
void ShowFindDialog(object sender, EventArgs e)
{
    this.editControl1.ShowFindDialog();
}
```

### VB.NET
```vb
' Example of handling the MenuFill event
Private Sub cm_FillMenu(ByVal sender As Object, ByVal e As EventArgs)
    Dim cm As ContextMenuManager = DirectCast(sender, ContextMenuManager)
    cm.ClearMenu()
    cm.AddSeparator()
    cm.AddMenuItem("&Find", New EventHandler(AddressOf ShowFindDialog))
    cm.AddMenuItem("&Replace", New EventHandler(AddressOf ShowReplaceDialog))
    cm.AddMenuItem("&Goto", New EventHandler(AddressOf ShowGoToDialog))
End Sub
```

## Cross References
- See also: [Syncfusion WinForms API Reference](https://www.syncfusion.com/products/windowsforms/api)

<!-- tags: [product, module, control, api, version?] keywords: [Syncfusion, WinForms, EditControl, Menu, ContextMenu, Find, Replace, GoTo, C#, VB.NET] -->
```