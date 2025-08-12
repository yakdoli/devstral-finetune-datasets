```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_217.jpeg
document_name: tools
page_number: 217
page_id: tools#page_217
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:40:18Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Event: dockingManager1_ControlMaximized

### C#

```csharp
private void dockingManager1_ControlMaximized(object sender, Syncfusion.Windows.Forms.Tools.ControlMaximizedEventArgs arg)
{
    // You can see the below line in output window during runtime.
    Console.WriteLine("Control Maximized event is raised");
    //Displays the docked control name
    Console.WriteLine("Control Name : " + arg.Control.Name);
    //Cancel is the boolean property which can prevent docking event when it is true.
    arg.Cancel = true;
}
```

### VB.NET

```vb
Private Sub dockingManager1_ControlMaximized(ByVal sender As Object, ByVal arg As Syncfusion.Windows.Forms.Tools.ControlMaximizedEventArgs)
    ' You can see the below line in output window during runtime.
    Console.WriteLine("Control Maximized event is raised")
    'Displays the docked control name
    Console.WriteLine("Control Name : " + arg.Control.Name)
    'Cancel is the boolean property which can prevent docking event when it is true.
    arg.Cancel = True
End Sub
```

## 3.4.3.8.4.2 ControlMaximizing Event

When the user clicks on the maximize button, and when the control is going to be maximized, the `ControlMaximizing` event will be raised.

### Event Data

The event handler receives an argument of type `ControlMaximizeEventArgs` containing data related to this event. The following `ControlMaximizeEventArgs` properties provide information specific to this event.

| Members | Description |
|---------|-------------|
| Cancel | Gets / sets value that indicates whether to cancel the operation or not. |

### C#

```csharp
private void dockingManager1_ControlMaximizing(object sender, Syncfusion.Windows.Forms.Tools.ControlMaximizeEventArgs arg)
```

<!-- tags: [Syncfusion Winforms, ControlMaximizing Event, ControlMaximizeEventArgs] keywords: [dockingManager1_ControlMaximized, ControlMaximizedEventArgs, ControlMaximizing, ControlMaximizeEventArgs, event handler, maximize button, Event Data] -->
```