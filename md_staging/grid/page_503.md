```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_503.jpeg
document_name: grid
page_number: 503
page_id: grid#page_503
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T06:20:50Z
fidelity: lossless
-->

# Essential Grid for Windows Forms

## Content

### 4.1.4.22 Drag Column Header

In Grid control, a column header can be dragged to a new position by clicking on it, similar to how the fields in Microsoft Outlook are dragged without selecting the columns. This feature can be enabled in Grid control by adding the `DragColumnHeader` option under the `ControllerOptions` property. The event `QueryAllowDragColumnHeader` can be handled, while performing the drag operation.

> The following code examples illustrate this feature.

#### 1. Using C#

[C#]

```csharp
this.gridControl1.ControllerOptions |= GridControllerOptions.DragColumnHeader;
void gridControl1_QueryAllowDragColumnHeader(object sender, GridQueryDragColumnHeaderEventArgs e)
{
    if (e.Reason != GridQueryDragColumnHeaderReason.HitTest)
        System.Diagnostics.Debug.WriteLine("gridControl1_QueryAllowDragColum nHeader: " + e.ToString());
}
```

#### 2. Using VB.NET

[VB.NET]

```vb
Me.gridControl1.ControllerOptions = Me.gridControl1.ControllerOptions Or GridControllerOptions.DragColumnHeader
Private Sub gridControl1_QueryAllowDragColumnHeader(ByVal sender As Object, ByVal e As GridQueryDragColumnHeaderEventArgs)
    If e.Reason <> GridQueryDragColumnHeaderReason.HitTest Then
        System.Diagnostics.Debug.WriteLine("gridControl1_QueryAllowDragColumnHeader: " & e.ToString())
    End If
End Sub
```

> The following screen shot illustrates how to drag the column header.
```