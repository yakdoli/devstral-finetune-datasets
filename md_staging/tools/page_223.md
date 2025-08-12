```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_223.jpeg
document_name: tools
page_number: 223
page_id: tools#page_223
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:45:06Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- Describes the DockStateUnavailable and NewDockStateBeginLoad events in Syncfusion Winforms.
- Explains the behavior of dockable controls when loading persisted dock states.
- Provides code examples in both C# and VB.NET for handling the DockStateUnavailable event.

## Content

### DockStateUnavailable Event

#### C#
```csharp
// The DockStateUnavailable event occurs if serialized information is not available
// for a dockable control when loading a persisted dock state.
private void dockingManager1_DockStateUnavailable(object sender, Syncfusion.Windows.Forms.Tools.DockStateUnavailableEventArgs arg)
{
    Console.WriteLine("DockStateUnavailable Event has been fired");
    Console.WriteLine("Dock state unavailable for the Control is : " + arg.Control.Name);
}
```

#### VB.NET
```vb.net
' The DockStateUnavailable event occurs if serialized information is not available
' for a dockable control when loading a persisted dock state.
Private Sub dockingManager1_DockStateUnavailable(ByVal sender As Object, ByVal arg As Syncfusion.Windows.Forms.Tools.DockStateUnavailableEventArgs)
    Console.WriteLine("DockStateUnavailable Event has been fired")
    Console.WriteLine("Dock state unavailable for the Control is : " + arg.Control.Name)
End Sub
```

### NewDockStateBeginLoad Event

The NewDockStateBeginLoad event occurs just before a new dock state is loaded. Whenever an application with one or more docked controls is going to be loaded, this event will be triggered.

#### Members
| Member      | Description                                                               |
|-------------|---------------------------------------------------------------------------|
| Control     | Gets the docked control for which a new dock state is going to be loaded. |

## Page-level Navigation/TOC
- **3.4.3.8.5.4 NewDockStateBeginLoad Event** details the event that occurs just before a new dock state is loaded.

## Cross References
- Refer to the Syncfusion Winforms documentation for additional details on dockable controls and event handling.

## RAG Annotations
<!-- tags: [syncfusion, winforms, dockstate, event handling, dockable controls] keywords: [DockStateUnavailable, NewDockStateBeginLoad, serialized information, persisted dock state, docked controls] -->
```