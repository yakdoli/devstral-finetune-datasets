```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_210.jpeg
document_name: tools
page_number: 210
page_id: tools#page_210
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:36:13Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
// The HostForm border along which the AutoHide tab is aligned.
Console.WriteLine("Control Dock Border Value : "
                  + arg.DockBorder.ToString()
                  + "Type of the Dock Border is : " + arg.DockBorder.GetType());
}
```

### [VB.NET]

```vb
Private Sub dockingManager1_AutoHideAnimationStart(ByVal sender As Object, ByVal arg As Syncfusion.Windows.Forms.Tools.AutoHideAnimationEventArgs)
    ' You can see the below line in output window during runtime.
    Console.WriteLine("Auto Hide Animation starting now : " + i++)
    ' AutoHideAnimationEvent argument Contains the property "Control".
    ' It has all kind of methods, events and properties of Control Class.
    Console.WriteLine("Control Name : " & arg.Control.Name)
    ' The display bounds of the autohidden control. It will return the object of
    ' Rectangle Class
    Console.WriteLine("Control Bounds Value : " + arg.Bounds.ToString())
    ' The HostForm border along which the AutoHide tab is aligned.
    Console.WriteLine("Control Dock Border Value : "
                      + arg.DockBorder.ToString()
                      + "Type of the Dock Border is : " + arg.DockBorder.GetType())
End Sub
```

## 3.4.3.8.2.2 AutoHideAnimationStop Event

The AutoHideAnimationStop event occurs immediately after the end of an autohide animation. When the user clicks the auto hide button, the docked control will be hidden, and once this happens, the AutoHideAnimationStop event will be triggered.

### Event Data

The AutoHideAnimationEventHandler receives an argument of type AutoHideAnimationEventArgs containing data related to this event. The following AutoHideAnimationEventArgs properties provide information specific to this event.

| Members          | Description                                    |
|------------------|-----------------------------------------------|
|                  |                                                |

<!-- tags: [syncfusion-sdk, windows-forms, autohide-animation, event, dock, control] keywords: [autohide, animationstart, animationstop, event, args, dockborder, bounds, syncfusion, winforms] -->
```