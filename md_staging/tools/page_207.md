<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_207.jpeg
document_name: tools
page_number: 207
page_id: tools#page_207
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:34:37Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## Event Data

The event handler receives an argument of type `DockActivationChangedEventArgs` containing data related to this event. The following `DockActivationChangedEventArgs` properties provide information specific to this event.

| Member     | Description                                                                 |
|------------|-----------------------------------------------------------------------------|
| Control    | The control which has been activated now.                                  |

### C#

```csharp
// The DockControlActivated event occurs when a dockable control gets activated.
private void dockingManager1_DockControlActivated(object sender, Syncfusion.Windows.Forms.Tools.DockActivationChangedEventArgs arg)
{
    // If we click on the Docked control or click on the Docked control title bar,
    // DockControlActivated event will be triggered
    // DockActivationChangedEventArgs has the property called Control which has the details of the
    // Activated control.
    Console.WriteLine("Dock Control Activated Event is Fired");
    // Here Display the name of the control that is being active currently.
    Console.WriteLine("Activated Control Name : " + arg.Control.Name);
}
```

### VB.NET

```vb
' The DockControlActivated event occurs when a dockable control gets activated.
Private Sub dockingManager1_DockControlActivated(ByVal sender As Object, ByVal arg As Syncfusion.Windows.Forms.Tools.DockActivationChangedEventArgs)
    ' If we click on the Docked control or click on the Docked control title bar,
    ' DockControlActivated event will be triggered
    ' DockActivationChangedEventArgs has the property called Control which has the details of the
    ' Activated control
    Console.WriteLine("Dock Control Activated Event is Fired")
    ' Here Display the name of the control that is being active currently.
    Console.WriteLine("Activated Control Name : " + arg.Control.Name)
End Sub
```

<!-- tags: [Syncfusion Winforms, DockControlActivated, DockActivationChangedEventArgs, C#, VB.NET] keywords: [event handler, dockable control, activated control, event, property, argument, example] -->