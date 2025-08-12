```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_216.jpeg
document_name: tools
page_number: 216
page_id: tools#page_216
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:38:36Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

## C#

```csharp
private void dockingManager1_DocMenuClick(object sender, Syncfusion.Windows.Forms.Tools.DockMenuClickEventArgs arg)
{
    // You can see the below line in output window during runtime.
    Console.WriteLine("Dock Menu Click event is raised");
    // Display the Docking Style
    Console.WriteLine("DockingStyle : " + arg.DockingStyle.ToString());
}
```

## VB.NET

```vb
Private Sub dockingManager1_DocMenuClick(ByVal sender As Object, ByVal arg As Syncfusion.Windows.Forms.Tools.DockMenuClickEventArgs)
    ' You can see the below line in output window during runtime.
    Console.WriteLine("Dock Menu click event is raised")
    ' Display the Docking Style
    Console.WriteLine("DockingStyle : " + arg.DockingStyle.ToString())
End Sub
```

## Docked Control

This section covers the following events:

### ControlMaximized Event

The docked control gets maximized when the maximized button of the docked control is clicked. The `ControlMaximized` event will be triggered after the control is maximized.

#### Event Data

The event handler receives an argument of type `ControlMaximizedEventArgs` containing data related to this event. The following `ControlMaximizedEventArgs` properties provide information specific to this event.

| Members | Description |
| --- | --- |
| Cancel | Gets / sets value that indicates whether to cancel the operation or not. |

#### C#
- [C#]

```csharp
```

---

## API Reference (if applicable)

### WinForms-specific conventions
- Namespace: Required for reference.
- Members (Methods/Properties/Events/Enums).

---

## Code Examples (multi-language supported)
- Extract ALL code exactly.
- Using blocks and comments preserved as needed.

---

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
``` 
```