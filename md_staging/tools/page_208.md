```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_208.jpeg
document_name: tools
page_number: 208
page_id: tools#page_208
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:33:11Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
End Sub
```

## Overview
- The DockControlDeactivated event is triggered whenever a dockable control or a docked control loses focus.
- This event is useful for displaying the name of the control that is deactivated.
- The event handler receives an argument of type DockedActivationChangedEventArgs containing event-specific information.

## Content

### 3.4.3.8.1.3 DockControlDeactivated Event

Whenever a dockable control or the docked control loses focus, the DockControlDeactivated event will be raised. In other words, when a dockable control gets deactivated, this event will be fired. This event can display the control name that is deactivated.

#### Event Data

The event handler receives an argument of type DockedActivationChangedEventArgs containing data related to this event. The following DockActivationChangedEventArgs property provides information specific to this event.

| Member   | Description                                      |
|----------|--------------------------------------------------|
| Control  | The control which has been activated now.      |

#### C#

```csharp
// The DockControlDeactivated event occurs when a dockable control gets deactivated.
private void dockingManager1_DockControlDeactivated(object sender, Syncfusion.Windows.Forms.Tools.DockActivationChangedEventArgs arg)
{
    // Deactivation Event will be triggered when the control has lost the focus.
    Console.WriteLine("Dock Control Deactivated Event is Fired");
    // Here Display the name of the control that is being active currently.
    Console.WriteLine("Deactivated Control Name : " + arg.Control.Name);
}
```

#### VB.NET

```vb
'The DockControlDeactivated event occurs when a dockable control gets deactivated.
Private Sub dockingManager1_DockControlDeactivated(ByVal sender As Object, ByVal arg As Syncfusion.Windows.Forms.Tools.DockActivationChangedEventArgs)
    ' Deactivation Event will be triggered when the control has lost the
End Sub
```

---

<!-- tags: [DockControlDeactivated, DockableControl, DockedControl, Syncfusion, WindowsForms, Events, C#, VB.NET] keywords: [DockControlDeactivatedEvent, DockableControl, DockedControl, DeactivatedControl, DockingManager] -->
```