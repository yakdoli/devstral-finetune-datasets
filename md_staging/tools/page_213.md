```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_213.jpeg
document_name: tools
page_number: 213
page_id: tools#page_213
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:37:19Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Content

### DockContextMenu Event

The DockContextMenu event is fired when the mouse is right-clicked over a docking window's caption.

#### Event Data

The event handler receives an argument of type DockContextMenuEventArgs containing data related to this event. The following DockContextMenuEventArgs properties provide information specific to this event.

| Members       | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| ContextMenu   | Gets or sets the context menu to be displayed.                             |
| Owner         | Gets the control that is displaying the context menu.                     |

#### Editing the context menu of a Docked Control

The DockContextMenuEventArgs allows us to,

- Edit the context menu that appears when right clicked on the caption bar (Using DockContextMenuEventArgs.ContextMenu).
- Retrieve the control that is displaying the context menu (Using DockContextMenuEventArgs.Owner).

Create a simple docking window. Add the required name spaces. Declare and initialize the bar items to be placed in the context menu as shown in the code below.

```csharp
// Adding namespaces
using Syncfusion.Windows.Forms.Tools.XPMenu;

// Declaring the bar items
private Syncfusion.Windows.Forms.Tools.XPMenu.BarItem bar1;
```

## API Reference

### ContextMenu
```csharp
// Gets or sets the context menu to be displayed.
public ContextMenu { get; set; }
```

### Owner
```csharp
// Gets the control that is displaying the context menu.
public Control Owner { get; }
```

## Code Examples

```csharp
// Example usage of DockContextMenuEventArgs
private void DockContextMenuEvent(DockContextMenuEventArgs e)
{
    // Access the context menu being displayed
    ContextMenu currentMenu = e.ContextMenu;

    // Access the control displaying the context menu
    Control owningControl = e.Owner;

    // Customize the context menu as needed
    // Example: Add items or modify existing items
}
```

```vb
' Example usage of DockContextMenuEventArgs
Private Sub DockContextMenuEvent(ByVal e As DockContextMenuEventArgs)
    ' Access the context menu being displayed
    Dim currentMenu As ContextMenu = e.ContextMenu

    ' Access the control displaying the context menu
    Dim owningControl As Control = e.Owner

    ' Customize the context menu as needed
    ' Example: Add items or modify existing items
End Sub
```

<!-- tags: [Syncfusion, Windows Forms, Dock, ContextMenu, Event] keywords: [DockContextMenuEvent, DockContextMenuEventArgs, context menu, control, caption bar, right click, synchronization, Syncfusion Windows Forms, Event Handler, Event Data] -->
```