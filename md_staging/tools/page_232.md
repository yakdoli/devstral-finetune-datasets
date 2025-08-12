```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_232.jpeg
document_name: tools
page_number: 232
page_id: tools#page_232
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:49:24Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- The event handler receives an argument of type `TransferManagerEventArgs` containing data related to the event.
- `TransferManagerEventArgs` provides information specific to the event.

## Content

| Member       | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| Control      | Gets the control which is undergoing the transfer.                        |

### C#
```csharp
// The TransferringFromManager event occurs when a dockable control hosted by this DockingManager is
// about to be transferred to the docking layout hosted by some other DockingManager.
protected void DockingManager_TransferringFromManager(object sender, TransferManagerEventArgs args)
{
    Console.WriteLine("Transferring From Manager Event has been raised");
    DockableControlBase dockablecontrol = args.Control as DockableControlBase;
    dockablecontrol.CurrentDockingManager = sender as DockingManager;
    Console.WriteLine("HostControl name : " + dockablecontrol.CurrentDockingManager.HostControl.Name);
}
```

### VB.NET
```vb
' The TransferringFromManager event occurs when a dockable control hosted by this DockingManager is
' about to be transferred to the docking layout hosted by some other DockingManager.
Protected Sub DockingManager_TransferringFromManager(ByVal sender As Object, ByVal args As TransferManagerEventArgs)
    Console.WriteLine("Transferring From Manager Event has been raised")
    Dim dockablecontrol As DockableControlBase = CType(ConversionHelpers.AsWorkaround(args.Control, GetType(DockableControlBase)), DockableControlBase)
    dockablecontrol.CurrentDockingManager = CType(ConversionHelpers.AsWorkaround(sender, GetType(DockingManager)), DockingManager)
    Console.WriteLine("HostControl name : " + dockablecontrol.CurrentDockingManager.HostControl.Name)
End Sub
```

### API Reference
#### Namespace
- Syncfusion.Windows.Forms.Tools
#### Class
- DockingManager
#### Event
- `TransferringFromManager`

### Code Examples

#### C#
```csharp
// TransferringFromManager event handler in C#
protected void DockingManager_TransferringFromManager(object sender, TransferManagerEventArgs args)
{
    // Logic to handle event
}
```

#### VB.NET
```vb
' TransferringFromManager event handler in VB.NET
Protected Sub DockingManager_TransferringFromManager(ByVal sender As Object, ByVal args As TransferManagerEventArgs)
    ' Logic to handle event
End Sub
```

### See also
- [DockingManager Documentation](#unclear)

<!-- tags: [syncfusion, windows forms, tools, event handler, dockable control, transfer manager, version 11.4.0.26] -->
```