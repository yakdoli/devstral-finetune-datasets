```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_226.jpeg
document_name: tools
page_number: 226
page_id: tools#page_226
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:46:55Z
fidelity: lossless
-->

### Essential Tools for Windows Forms

#### Code Example

```csharp
[C#]

//this event triggers when the control's visibility has changed.
private void dockingManager1_DockVisibilityChanged(object sender,
Syncfusion.Windows.Forms.Tools.DockVisibilityChangedEventArgs arg)
{
    //GetDockVisibility method gives the detail of the docked control visibility
    if (this.dockingManager1.GetDockVisibility(arg.Control) == false)
    {
        //DockVisibilityChangedEventArgs instance arg holds the control being changed the visibility
        MessageBox.Show(this.dockingManager1.GetDockLabel(arg.Control)
+ " " + " window is closed.");
    }
}
```

```vb.net
[VB.NET]

'this event triggers when the control's visibility has changed.
Private Sub dockingManager1_DockVisibilityChanged(ByVal sender As Object, ByVal arg As Syncfusion.Windows.Forms.Tools.DockVisibilityChangedEventArgs) Handles dockingManager1.DockVisibilityChanged()

    'GetDockVisibility method gives the detail of the docked control visibility
    If Me.dockingManager1.GetDockVisibility(arg.Control) = False Then

        'DockVisibilityChangedEventArgs instance arg holds the control being changed the visibility
        MessageBox.Show(Me.dockingManager1.GetDockLabel(arg.Control) + " " + " window is closed.")

    End If

End Sub
```

#### DockVisibilityChanging Event

An use case demonstrating this event is available at [How to prevent closing of docked window?.](http://)

### Drag Events
```

<!-- tags: [Syncfusion Winforms, DockVisibilityChanging Event, Docking, Visibility, Control Events] keywords: [Windows Forms, DockControlEvents, DockVisibilityChangedEventArgs, DockingManager, Drag Events] -->
```