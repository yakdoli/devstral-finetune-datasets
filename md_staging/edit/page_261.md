<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_261.jpeg
document_name: edit
page_number: 261
page_id: edit#page_261
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T05:10:19Z
fidelity: lossless
-->

# Essential Edit for Windows Forms

```csharp
Syncfusion.Windows.Forms.Edit.CollapseEventArgs e)
{
    Console.WriteLine(" OutliningCollapse event is raised ");
}
```

### [VB.NET]

```vb
Private Sub editControl1_OutliningCollapse(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Edit.CollapseEventArgs)
    Console.WriteLine(" OutliningBeforeCollapse event is raised ")
End Sub
```

## 4.14.15.4 OutliningExpand Event

This event is raised when a region expands.

The event handler receives an argument of type `CollapseEventArgs`. The following `CollapseEventArgs` members provide information specific to this event.

| Member         | Description                          |
|----------------|--------------------------------------|
| CollapsedText | Gets / sets collapsed text.         |
| CollapseName  | Gets / sets collapse name.          |
| Collapser     | Gets / sets collapser.             |

### [C#]

```csharp
private void editControl1_OutliningExpand(object sender, Syncfusion.Windows.Forms.Edit.CollapseEventArgs e)
{
    Console.WriteLine(" OutliningExpand event is raised ");
}
```

### [VB.NET]

```vb
Private Sub editControl1_OutliningExpand(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Edit.CollapseEventArgs)
    Console.WriteLine(" OutliningExpand event is raised ")
End Sub
```

<!-- tags: [product, module, control, api, version?] keywords: [outlining, collapse, expand, event, region, collapseeventargs, syncfusion windows forms edit, outliningexpand, event handler] -->