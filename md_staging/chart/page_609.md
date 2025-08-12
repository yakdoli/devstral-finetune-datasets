```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_609.jpeg
document_name: chart
page_number: 609
page_id: chart#page_609
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:53:01Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Content

### ChartRegionMouseDown Event Example in VB.NET

```vb
If e.Button = MouseButtons.Right Then
    Console.WriteLine("Chart Region Mouse Down:=" + e.Point.ToString())
End If
```

### VisibleRangeChanged Event

ChartControl provides various zooming options for the user while interacting with the Chart. The `VisibleRangeChanged` event will be raised when the visible range changes during the zooming operation.

#### Code Example in C#

```csharp
private static void chartControl1_VisibleRangeChanged(object sender, EventArgs e)
{
    Console.WriteLine("Visible Range Changed event is raised");
}
```

#### Code Example in VB.NET

```vb
Private Sub chartControl1_VisibleRangeChanged(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("Visible Range Changed event is raised")
End Sub
```

## Page-level Navigation/TOC (if applicable)

- ChartRegionMouseDown Event Example in VB.NET
- VisibleRangeChanged Event

### RAG Annotations

<!-- tags: [Syncfusion, Winforms, ChartControl, Zooming, VisibleRangeChanged] keywords: [ChartControl, zooming, visible range, event handling, C#, VB.NET] -->
```