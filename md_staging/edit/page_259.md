```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_259.jpeg
document_name: edit
page_number: 259
page_id: edit#page_259
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:09:18Z
fidelity: lossless
-->

## 4.14.15.1 OutliningBeforeCollapse Event

This event is raised before a region is about to collapse.

The event handler receives an argument of type **OutliningEventArgs**. The following **OutliningEventArgs** members provide information specific to this event.

| Member         | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
| Cancel         | Gets / sets value indicating whether the user cancels the underlying event. |
| CollapsedText  | Gets / sets collapsed text.                                                |
| CollapseName   | Gets / sets collapse name.                                                 |
| Collapser      | Gets / sets collapser.                                                    |

### [C#]

```csharp
private void editControl_OutliningBeforeCollapse(object sender, Syncfusion.Windows.Forms.Edit.OutliningEventArgs e)
{
    Console.WriteLine(" OutliningBeforeCollapse event is raised ");
}
```

### [VB.NET]

```vb
Private Sub editControl_OutliningBeforeCollapse(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Edit.OutliningEventArgs)
    Console.WriteLine(" OutliningBeforeCollapse event is raised ")
End Sub
```

## 4.14.15.2 OutliningBeforeExpand Event

This event is raised before a region is about to expand.

The event handler receives an argument of type **OutliningEventArgs**. The following **OutliningEventArgs** members provide information specific to this event.

<!-- tags: [Syncfusion Winforms, OutliningEvent, OutliningEventArgs] keywords: [OutliningBeforeCollapse, OutliningBeforeExpand, event handler, region collapse, region expand] -->
```