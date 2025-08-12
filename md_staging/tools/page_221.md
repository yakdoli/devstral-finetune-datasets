```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_221.jpeg
document_name: tools
page_number: 221
page_id: tools#page_221
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:42:55Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Overview
- The `DockStateChanged` and `DockStateChanging` events are key components of dock operations in Windows Forms.
- These events help manage and track changes in control docking states.

## Content

### VB.NET Example

The `DockStateChanged` event occurs immediately after a dock operation.

```vb
' The DockStateChanged event occurs immediately after a dock operation.
Private Sub dockingManager1_DockStateChanged(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Tools.DockStateChangeEventArgs)
    Console.WriteLine("DockStateChanged Event has occurred")
    Console.WriteLine("Total Number of controls in a group : " + e.Controls.Length.ToString())
    ' e.Controls Gets the collection of controls undergoing the dockstate transfer.
    Dim ctrls As Control() = e.Controls
    Dim i As Integer = 1
    ' Here display all the controls in e.Controls group.
    For Each ctrl As Control In ctrls
        Console.WriteLine("Control" + i + " Name : " + ctrl.Name)
        System.Math.Min(System.Threading.Interlocked.Increment(i), i - 1)
    Next
End Sub
```

### 3.4.3.8.5.2 DockStateChanging Event

The `DockStateChanging` event will be triggered just before a dock operation takes place.

#### Event Data

The event handler receives an argument of type `DockStateChangeEventArgs` containing data related to this event. The following `DockStateChangeEventArgs` property provides information specific to this event.

| Member     | Description                                                |
|------------|------------------------------------------------------------|
| Control    | Gets the collection of controls undergoing the dockstate transfer. |

### C# Example

The `DockStateChanging` event occurs just before a dock operation takes place.

```csharp
// The DockStateChanging event occurs just before a dock operation takes place.
private void dockingManager1_DockStateChanging(object sender, Syncfusion.Windows.Forms.Tools.DockStateChangeEventArgs e)
{
    Console.WriteLine("DockStateChanging Event has occurred");
    Console.WriteLine("Total Number of controls in a group : " + e.Controls.Length.ToString());
    // e.Controls gives the collection of controls which are in Docked
}
```

## API Reference

### Members

- `DockStateChangeEventArgs`
  - **Control**: Gets the collection of controls undergoing the dockstate transfer.

## Code Examples

### VB.NET

```vb
Private Sub dockingManager1_DockStateChanged(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Tools.DockStateChangeEventArgs)
    ' ... (code from above example)
End Sub
```

### C#

```csharp
private void dockingManager1_DockStateChanging(object sender, Syncfusion.Windows.Forms.Tools.DockStateChangeEventArgs e)
{
    // ... (code from above example)
}
```

## Cross References

- See also: [DockManager](#dockmanager), [DockStateChangeEventArgs](#dockstatechangeeventargs)

<!-- tags: [Syncfusion Winforms, Windows Forms, Docking, DockStateChanged, DockStateChanging, DockStateChangeEventArgs, Event handling, Control collection] keywords: [Docking, DockState, Control collection, DockStateChanged, DockStateChanging] -->
```