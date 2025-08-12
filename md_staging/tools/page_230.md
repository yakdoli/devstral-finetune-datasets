```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_230.jpeg
document_name: tools
page_number: 230
page_id: tools#page_230
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T09:49:39Z
fidelity: lossless
-->

# Essential Tools for Windows Forms

```csharp
[C#]

// The DragFeedbackStop event occurs immediately after the end of
// feedback of a drag operation.
private void dockingManager1_DragFeedbackStop(object sender, System.EventArgs e)
{
    Console.WriteLine("DragFeedbackStop Event is raised");
}
```

```vbnet
[VB.NET]

'The DragFeedbackStop event occurs immediately after the end of
'feedback of a drag operation.
Private Sub dockingManager1_DragFeedbackStop(ByVal sender As Object, ByVal e As System.EventArgs)
    Console.WriteLine("DragFeedbackStop Event is raised")
End Sub
```

## 3.4.3.8.8 Linked Managers

This section covers the following events:

### 3.4.3.8.8.1 TransferredToManager Event

The TransferredToManager event occurs after a dockable control that previously belonged to some other DockingManager has been transferred to the docking layout hosted by the current DockingManager.

#### Event Data

The event handler receives an argument of type TransferManagerEventArgs containing data related to this event. The following TransferManagerEventArgs properties provide information specific to this event.

| Member   | Description                                        |
|----------|----------------------------------------------------|
| Control  | Gets the control which is undergoing the transfer. |

## Page-level Navigation/TOC (if applicable)

### WinForms-specific conventions

- **Control and namespaces**: All control names, namespaces, and types are preserved as shown in the documentation, such as `Syncfusion.Windows.Forms.Tools.TabControlAdv`, `Syncfusion.Windows.Forms.Grid`.
- **Design-time vs runtime features**: The distinction between design-time and runtime features is preserved based on the context provided.
- **Code Examples**: Detailed examples in both C# and VB.NET are included as shown in the provided text.

<!-- tags: [Syncfusion Winforms, DockingManager, Events, TransferredToManager, TransferManagerEventArgs] keywords: [DockingManager, TransferManagerEventArgs, TransferredToManager, DragFeedbackStop, C#, VB.NET] -->
```