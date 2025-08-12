```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_211.jpeg
document_name: tools
page_number: 211
page_id: tools#page_211
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:37:15Z
fidelity: lossless
-->

## Overview
- Describes the functionality of the `AutoHideAnimationStop` event in Syncfusion Winforms.
- Includes example code snippets in C# and VB.NET to demonstrate the use of this event.
- Focuses on retrieving and displaying bounds, dock borders, and control properties related to autohide animations.

## Content

### Table: Event Properties
| Property      | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| Bounds        | The display bounds of the autohidden control.                            |
| DockBorder    | The HostForm border along which the AutoHide tab is aligned.            |

### Events and Properties in C#

```csharp
[C#]

//The AutoHideAnimationStop event occurs immediately after the end of an autohide animation
private void dockingManager1_AutoHideAnimationStop(object sender, Syncfusion.Windows.Forms.Tools.AutoHideAnimationEventArgs arg)
{
    Console.WriteLine("Animation has been stopped");
    //AutoHideAnimationEvent argument Contains the property "Control".
    //It has all kind of methods, events and properties of Control Class.
    Console.WriteLine("Control Name : " + arg.Control.Name);
    //The display bounds of the autohidden control. It will return the object of
    // Rectangle Class
    Console.WriteLine("Control Bounds Value : " + arg.Bounds.ToString());
    //The HostForm border along which the AutoHide tab is aligned.
    Console.WriteLine("Control Dock Border Value : ");
    Console.WriteLine(" " + arg.DockBorder.ToString() + "Type of the Dock Border is : " + arg.DockBorder.GetType());
}
```

### Events and Properties in VB.NET

```vb.net
[VB.NET]

'The AutoHideAnimationStop event occurs immediately after the end of an autohide animation
Private Sub dockingManager1_AutoHideAnimationStop(ByVal sender As object, ByVal arg As Syncfusion.Windows.Forms.Tools.AutoHideAnimationEventArgs)
    Console.WriteLine("Animation has been stopped")
    'AutoHideAnimationEvent argument Contains the property "Control".
    'It has all kind of methods, events and properties of Control Class.
    Console.WriteLine("Control Name : " + arg.Control.Name)
    'The display bounds of the autohidden control. It will return the object of
    ' Rectangle Class
    Console.WriteLine("Control Bounds Value : " + arg.Bounds.ToString())
    'The HostForm border along which the AutoHide tab is aligned.
    Console.WriteLine("Control Dock Border Value : ")
    Console.WriteLine(" " + arg.DockBorder.ToString() + "Type of the Dock Border is : " + arg.DockBorder.GetType())
End Sub
```

### Explanation
- The `AutoHideAnimationStop` event is triggered after the autohide animation completes.
- The event handler (`dockingManager1_AutoHideAnimationStop`) is provided with an `AutoHideAnimationEventArgs` object.
- The `Control` property of the event argument is used to access the control involved in the autohide animation.
- The `Bounds` property provides the display bounds of the autohidden control, and the `DockBorder` property indicates the host form border alignment.

### See also:
- `DockManager`
- `AutoHideAnimationEventArgs`
- `Control`
- `Bounds`
- `DockBorder`

## Page-level Navigation/TOC
- This section explains the `AutoHideAnimationStop` event in depth, showcasing code examples in both C# and VB.NET.

<!-- tags: [Syncfusion Winforms, AutoHideAnimationStop, DockManager, AutoHideAnimationEventArgs, Control] keywords: [autohide animation, bounds, dock border, event, event arguments, c#, vb.net] -->
```