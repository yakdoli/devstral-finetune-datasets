```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_218.jpeg
document_name: tools
page_number: 218
page_id: tools#page_218
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:41:30Z
fidelity: lossless
-->

### Control Events

#### ControlMaximizing Event

The `ControlMaximizing` event is triggered when the control is maximized using the maximize option available for the docked control. This event allows you to display information about the control, such as its name, and provides the ability to prevent the docking event by setting the `Cancel` property to `true`.

##### Example Code: C#

```csharp
{
    // You can see the below line in output window during runtime.
    Console.WriteLine("Control Maximizing event is raised");
    //Displays the docked control name
    Console.WriteLine("Control Name : " + arg.Control.Name);
    //Cancel is the boolean property which can prevent docking event when it is true.
    arg.Cancel = true;
}
```

##### Example Code: VB.NET

```vb
Private Sub dockingManager1_ControlMaximizing(ByVal sender As Object, ByVal arg As Syncfusion.Windows.Forms.Tools.ControlMaximizeEventArgs)
    ' You can see the below line in output window during runtime.
    Console.WriteLine("Control Maximizing event is raised")
    'Displays the docked control name
    Console.WriteLine("Control Name : " + arg.Control.Name)
    'Cancel is the boolean property which can prevent docking event when it is true.
    arg.Cancel = True
End Sub
```

#### `ControlMinimized` Event

This event is fired after the control is minimized using the minimize option available for the docked control. This event can display the control name using the `Control` parameter available for the `ControlMinimizedEventHandler`.

##### Example Code: C#

```csharp
private void dockingManager1_ControlMinimized(object sender, ControlMinimizedEventArgs arg)
{
    // You can see the below line in output window during runtime.
    Console.WriteLine("Control Minimized event is raised");
    //Displays the docked control name
    Console.WriteLine("Control Name : " + arg.Control.Name);
}
```

##### Example Code: VB.NET

```vb
Private Sub dockingManager1_ControlMinimized(ByVal sender As Object, ByVal arg As ControlMinimizedEventArgs)
    ' You can see the below line in output window during runtime.
    Console.WriteLine("Control Minimized event is raised")
    'Displays the docked control name
    Console.WriteLine("Control Name : " + arg.Control.Name)
End Sub
```

#### Event Summary: ControlMinimized Event

| Members   | Description                                               |
|-----------|-----------------------------------------------------------|
| Control   | Specifies the docked control which is minimized.          |

<!-- tags: [WinForms, Control Events, ControlMaximizing, ControlMinimized] keywords: [ControlMaximizing event, ControlMinimized event, docked control, maximize, minimize, event handler] -->
```