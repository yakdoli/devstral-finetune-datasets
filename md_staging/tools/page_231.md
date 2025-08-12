```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_231.jpeg
document_name: tools
page_number: 231
page_id: tools#page_231
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:50:54Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Demonstrates the functionality of transferring docking windows between different docking layouts.
- Explains the event handling mechanism for docking manager transfers.
- Includes C# and VB.NET code samples for managing dockable controls and docking managers.

## Content

### C#

```csharp
// A docking window is being transferred from one docking layout to another.
// Update the control's DockingManager reference.
protected void DockingManager_TransferredToManager(object sender, TransferManagerEventArgs args)
{
    Console.WriteLine("Transferred to Manager Event has been Raised");
    DockableControlBase dockablecontrol = args.Control as DockableControlBase;
    dockablecontrol.CurrentDockingManager = sender as DockingManager;
    Console.WriteLine("HostControl Name (Target Page Name) : " + dockablecontrol.CurrentDockingManager.HostControl.Name);
}
```

### VB.NET

```vb
Protected Sub DockingManager_TransferredToManager(ByVal sender As Object, ByVal args As TransferManagerEventArgs)
    Console.WriteLine("Transferred to Manager Event has been Raised")
    Dim dockablecontrol As DockableControlBase = CType(ConversionHelpers.AsWorkaround(args.Control, GetType(DockableControlBase)), DockableControlBase)
    dockablecontrol.CurrentDockingManager = CType(ConversionHelpers.AsWorkaround(sender, GetType(DockingManager)), DockingManager)
    Console.WriteLine("HostControl Name (Target Page Name) : " + dockablecontrol.CurrentDockingManager.HostControl.Name)
End Sub
```

### Sample

A sample that demonstrates the Linked Managers concept is available in the following sample installation path:

```
..My Documents\Syncfusion\EssentialStudio\<Version Number>\Windows\Tools.Windows\Samples\2.0\Docking Package\LinkedManagers
```

### 3.4.3.8.8.2 TransferringFromManager Event

The TransferringFromManager event occurs when a dockable control hosted by a DockingManager is about to be transferred to the docking layout hosted by some other DockingManager.

#### Event Data

## Page-Level Navigation/TOC

- Essential Tools for Windows Forms
- C# Example
- VB.NET Example
- Sample Installation Path
- TransferringFromManager Event
- Event Data

### Cross References

See also:
- DockableControlBase
- DockingManager
- TransferManagerEventArgs

<!-- tags: [Syncfusion, Winforms, DockingManager, Event, C#, VB.NET, Sample] keywords: [docking, transfer, event, linked managers, TransferringFromManager] -->
```
