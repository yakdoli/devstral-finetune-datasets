```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_209.jpeg
document_name: tools
page_number: 209
page_id: tools#page_209
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:34:24Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
Console.WriteLine("Deactivated Control Name : " + arg.Control.Name)
End Sub
```

## AutoHide Animation

This section discusses the below events that are raised at the start and end of autohide animation.

### AutoHideAnimationStart Event

**The AutoHideAnimationStart event occurs just before the start of an autohide animation. When the user tries to click the auto hide button to hide the docked control, this event will be triggered.**

#### Event Data

The AutoHideAnimationEventHandler receives an argument of type AutoHideAnimationEventArgs containing data related to this event. The following AutoHideAnimationEventArgs properties provide information specific to this event.

| Members       | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| Bounds        | The display bounds of the autohidden control.                              |
| DockBorder    | The HostForm border along which the AutoHide tab is aligned.              |

### C#

```csharp
private void dockingManager1_AutoHideAnimationStart(object sender, Syncfusion.Windows.Forms.Tools.AutoHideAnimationEventArgs arg)
{
    // You can see the below line in output window during runtime.
    Console.WriteLine("Auto Hide Animation starting now : " + i++);
    // AutoHideAnimationEvent argument Contains the property "Control".
    // It has all kind of methods, events and properties of Control Class.
    Console.WriteLine("Control Name : " + arg.Control.Name);
    // The display bounds of the autohidden control. It will return the object of
    // Rectangle Class
    Console.WriteLine("Control Bounds Value : " + arg.Bounds.ToString());
}
```

## Code Examples (if applicable)

```csharp
// Example usage of AutoHideAnimationStart event handler.
private void dockingManager1_AutoHideAnimationStart(object sender, Syncfusion.Windows.Forms.Tools.AutoHideAnimationEventArgs arg)
{
    Console.WriteLine("AutoHideAnimationStart event triggered.");
    Console.WriteLine("Control Name: " + arg.Control.Name);
    Console.WriteLine("Control Bounds: " + arg.Bounds.ToString());
}
```

## RAG Annotations

<!-- tags: WinForms, AutoHideAnimation, AutoHideAnimationStart, Syncfusion Winforms 11.4.0.26 keywords: AutoHideAnimation, AutoHideAnimationStart, Docked Control, AutoHide Button, AutoHideAnimationEventArgs -->
```