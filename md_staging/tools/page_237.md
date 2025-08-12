```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_237.jpeg
document_name: tools
page_number: 237
page_id: tools#page_237
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:53:41Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
"Width=" + arg.CaptionBounds.Width);
//IsActive Caption property gives the docked control is in Active or else. It will return
// bool value
if (arg.IsActiveCaption)
    Console.WriteLine("Control Name=" + arg.Control.Name);
}
```

### [VB.NET]

```vb
Private Sub dockingManager1_ProvideGraphicsItems(ByVal sender As Object, ByVal arg AsSyncfusion.Windows.Forms.Tools.ProvideGraphicsItemsEventArgs)
    Console.WriteLine("ProvideGraphicsItems Event Raised" + System.Math.Min(System.Threading.Interlocked.Increment(i), i - 1))
    'Caption Background uses the Brush for Drawing on the caption bar
    arg.CaptionBackground = New LinearGradientBrush(arg.CaptionBounds, Color.Transparent, Color.White, CType(0, Single))
    'Caption Fore ground color property will be used to specify the Font color of the caption
    arg.CaptionForeground = Color.Black
    'Caption Bounds property gives the values of Caption Height, width, Top ,Bottom and
    'More like rectangle control.
    Console.WriteLine("Caption Bounds, Height=" + arg.CaptionBounds.Height + "Width=" + arg.CaptionBounds.Width)
    'IsActive Caption property gives the docked control is in Active or else. It will return
    ' bool value
    If arg.IsActiveCaption Then
        Console.WriteLine("Control Name=" + arg.Control.Name)
    End If
End Sub
```

## 3.4.3.8.12 ProvidePersistenceID Event

This event lets you specify a unique ID to distinguish the persistence information of different instances of the Form type.

### Event Data

The event handler receives an argument of type ProvidePersistenceIDEventArgs containing data related to this event. The following ProvidePersistenceIDEventArgs property provides information specific to this event.

<!-- tags: [windows forms, event, providepersistenceid, persistinfo] keywords: [persistentid, form instances, uniqueid, event handler, providegraphicsitems, captionforegound, captionbackground] -->
```
