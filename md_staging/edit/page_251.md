```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_251.jpeg
document_name: edit
page_number: 251
page_id: edit#page_251
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:08:52Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

## Content

### Expansion of Controls

#### Example in C#

```csharp
// Handle the ExpandedAll event.
this.editControl.ExpandedAll += new EventHandler(editControl_ExpandedAll);

// Call the ExpandAll method.
this.editControl.ExpandAll();

private void editControl_ExpandedAll(object sender, EventArgs e)
{
    // The below line will be displayed in the output window at runtime.
    Console.WriteLine("ExpandedAll event is raised ");
}
```

#### Example in VB.NET

```vbnet
' Handle the ExpandedAll event.
Me.editControl.ExpandedAll += New EventHandler(editControl_ExpandedAll)

' Call the ExpandAll method.
Me.editControl.ExpandAll()

Private Sub editControl_ExpandedAll(ByVal sender As Object, ByVal e As EventArgs)
    ' The below line will be displayed in the output window at runtime
    Console.WriteLine("ExpandedAll event is raised ")
End Sub
```

### 4.14.9.2 ExpandingAll Event

#### Overview
This event is raised when the `ExpandAll` method is called.

The event handler receives an argument of type `CancelEventArgs`. The following `CancelEventArgs` member provides information specific to this event.

| Member    | Description                                                                 |
|-----------|------------------------------------------------------------------------------|
| `Cancel`  | Gets / sets a value indicating whether the event should be cancelled.     |

#### Code Example in C#

```csharp
// Handle the ExpandingAll event.
this.editControl.ExpandingAll += new EventHandler(editControl_ExpandingAll);
```

## Page-level Navigation/TOC (if applicable)

- **Handle the `ExpandedAll` event**: Event handling details and example usage.
- **ExpandingAll Event Documentation**: Comprehensive explanation of the event and its behavior.
- **Code Examples**: Illustrations in both C# and VB.NET.

## Cross References

See also: 
- Documentation on event handling in WinForms.
- Examples of using `ExpandAll` method in practical scenarios.

## RAG Annotations

<!--
tags: [Syncfusion, WinForms, EssentialEdit, ExpandingAllEvent, ExpandAllMethod, CancelEventArgs]
keywords: [ExpandedAll, event handler, event, ExpandAll, C#, VB.NET, output window, runtime, EventHandler, event handling, essential edit]
-->

```