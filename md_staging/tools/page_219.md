```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_219.jpeg
document_name: tools
page_number: 219
page_id: tools#page_219
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:42:44Z
fidelity: lossless
-->

## Essential Tools for Windows Forms

```vb
Private Sub dockingManagerl_ControlMinimized(ByVal sender As Object,
(ByVal arg As ControlMinimizedEventArgs)
    ' You can see the below line in output window during runtime.
    Console.WriteLine("Control Minimized event is raised")
    ' Displays the docked control name
    Console.WriteLine("Control Name : " + arg.Control.Name);
End Sub
```

### 3.4.3.8.4.4 ControlRestored Event

This event occurs after the control is restored to its original position. This event can give the previous state of the control using the PreviousSizeState property available for the handler.

#### Event Data

The event handler receives an argument of type ControlRestoredEventArgs containing data related to this event. The following ControlRestoredEventArgs properties provide information specific to this event.

| Member            | Description                                      |
|-------------------|--------------------------------------------------|
| PreviousSizeState | Returns previous size state of changing control. |

```csharp
private void dockingManagerl_ControlRestored(object sender, 
ControlRestoredEventArgs arg)
{
    // You can see the below line in output window during runtime.
    Console.WriteLine("Control Restored event is raised");
    // Displays the previous state
    Console.WriteLine("Control Name : " + arg.PreviousSizeState.ToString());
}
```

```vb
Private Sub dockingManagerl_ControlRestored(ByVal sender As Object,
(ByVal arg As ControlRestoredEventArgs)
    ' You can see the below line in output window during runtime.
    Console.WriteLine("Control Restored event is raised")
    ' Displays the previous state
    Console.WriteLine("Control Name : " + arg.PreviousSizeState.ToString());
End Sub
```

## Page-level Navigation/TOC (if applicable)
- ControlRestored Event
  - Overview
  - Event Data
  - Code Examples (C# and VB.NET)

## Cross References
- Related topics or reference materials can be noted here based on available content.

<!-- tags: [control, event, Windows Forms, Syncfusion] keywords: [ControlRestored, PreviousSizeState, event handler, Windows Forms, Syncfusion] -->
```