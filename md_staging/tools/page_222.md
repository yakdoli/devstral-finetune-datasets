```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_222.jpeg
document_name: tools
page_number: 222
page_id: tools#page_222
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:44:13Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
Area.
Control[] ctrls = arg.Controls;
int i = 1;
// Here display all the controls in arg.Controls group.
foreach (Control ctrl in ctrls)
{
    Console.WriteLine("Control " + i + " Name : " + ctrl.Name);
    i++;
}
}
```

### [VB.NET]

#### Overview 
- The DockStateChanging event occurs just before a dock operation takes place.

```vbnet
Private Sub dockingManager1_DockStateChanging(ByVal sender As Object, _
    ByVal arg As Syncfusion.Windows.Forms.Tools.DockStateChangeEventArgs)
    Console.WriteLine("DockStateChanging Event has occurred")
    Console.WriteLine("Total Number of controls in a group : " + _
        arg.Controls.Length.ToString)
    ' arg.Controls gives the collection of controls which are in Docked Area.
    Dim ctrls As Control() = arg.Controls
    Dim i As Integer = 1
    ' Here display all the controls in arg.Controls group.
    For Each ctrl As Control In ctrls
        Console.WriteLine("Control" + i + " Name : " + ctrl.Name)
        System.Math.Min(System.Threading.Interlocked.Increment(i), i - 1)
    Next
End Sub
```

## 3.4.3.8.5.3 DockStateUnavailable Event

The DockStateUnavailable event occurs if serialized information is not available for a dockable control when loading a persisted dock state.

### Event Data

The event handler receives an argument of type DockStateUnavailableEventArgs containing data related to this event. The following DockStateUnavailableEventArgs property provides information specific to this event.

| Member   | Description            |
|----------|-------------------------|
| Control  | The name property of the control. |
<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
``` 
```