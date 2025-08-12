```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_612.jpeg
document_name: chart
page_number: 612
page_id: chart#page_612
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:53:04Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## 4.19.6 LayoutCompleted Event

This event is handled every time a resizing of the chart is caused and when the chart re-renders itself. Listening to this event helps in cases where you render custom images over the chart or position custom controls over the chart.

### Code Example: C#

```csharp
[C#]

private static void chartControl1_LayoutCompleted(object sender, EventArgs e)
{
    Console.WriteLine("Layout Completed event is raised");
}
```

### Code Example: VB.NET

```vbnet
[VB.NET]

Private Sub chartControl1_LayoutCompleted(ByVal sender As Object, ByVal e As EventArgs)
    Console.WriteLine("Layout Completed event is raised")
End Sub
```

## 4.19.7 ChartAreaPaint Event

ChartAreaPaint event is discussed in **Custom Drawing**.

### See Also

- Chart Area Bounds

---

© 2013 Syncfusion. All rights reserved. 612 | Page
```