```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_252.jpeg
document_name: edit
page_number: 252
page_id: edit#page_252
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:08:44Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
// Call the ExpandAll method.
this.editControl.ExpandAll();

private void editControl_ExpandingAll(object sender, CancelEventArgs e)
{
    // The below given line will be displayed in the output window at runtime.
    Console.WriteLine(" ExpandingAll event is raised ");

    // Cancels the event.
    e.Cancel = true;
}
```

### [VB.NET]

```vb
' Handle the ExpandingAll event.
Me.editControl.ExpandingAll += New EventHandler(editControl_ExpandingAll)

' Call the ExpandAll method.
Me.editControl.ExpandAll()

Private Sub editControl_ExpandingAll(ByVal sender As Object, ByVal e As CancelEventArgs)
    ' The below given line will be displayed in the output window at runtime.
    Console.WriteLine(" CollapsingAll event is raised ")

    ' Cancels the event.
    e.Cancel = True
End Sub
```

## 4.14.10 Indicator Margin Events

This section discusses the below given indicator margin events.

### 4.14.10.1 IndicatorMarginClick Event

This event is raised when the user clicks on the indicator margin area.

The event handler receives an argument of type `IndicatorClickEventArgs`. The following `IndicatorClickEventArgs` members provide information specific to this event.
```html
<!-- tags: [syncfusion, windowsforms, edit, indicatormargin, events] keywords: [ExpandingAll, IndicatorMarginClick, WinForms, ExpandAll, IndicatorMarginEvent, EventHandling, C#, VB, EventArgs, IndicatorClickEventArgs] -->
```
```