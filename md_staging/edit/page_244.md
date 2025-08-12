```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_244.jpeg
document_name: edit
page_number: 244
page_id: edit#page_244
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:08:18Z
fidelity: lossless
-->

## Essential Edit for Windows Forms

This event is raised when the **CollapseAll** method is called. The event handler receives an argument of type **EventArgs**.

### Code Example: Handling CollapseAll Event

#### C#

```csharp
// Handle the CollapsedAll event.
this.editControl1.CollapsedAll += new EventHandler(editControl1_CollapsedAll);
// Call the CollapseAll method.
this.editControl1.CollapseAll();

private void editControl1_CollapsedAll(object sender, EventArgs e)
{
    // The below line will be displayed
    Console.WriteLine(" CollapsedAll event is raised ");
}
```

#### VB.NET

```vb
' Handle the CollapsedAll event.
Me.editControl1.CollapsedAll += New EventHandler(editControl1_CollapsedAll)
' Call the CollapseAll method.
Me.editControl1.CollapseAll()

Private Sub editControl1_CollapsedAll(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine(" CollapsedAll event is raised ")
End Sub
```

### 4.14.5.2 CollapsingAll Event

This event is raised when the **CollapseAll** method is called.

The event handler receives an argument of type **CancelEventArgs**. The following **CancelEventArgs** member provides information specific to this event.

#### Table of CancellableEventArgs Members

| Member   | Description                                                                 |
|----------|------------------------------------------------------------------------------|
| Cancel   | Gets / sets a value indicating whether the event should be cancelled. |
```

<!-- tags: [product, module, control, api, version?] keywords: [CollapseAll, EventArgs, CancelEventArgs, EventHandler, C#, VB.NET, console.log, Control} #edit#page_244 --> 
```