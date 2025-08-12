```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_604.jpeg
document_name: chart
page_number: 604
page_id: chart#page_604
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:52:28Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Content

### Chart Area Bounds

```vb
[VB.NET]

AddHandler Me.chartControl1.ChartAreaPaint, AddressOf
chartControl1_ChartAreaPaint

Private Sub chartControl1_ChartAreaPaint(ByVal sender As Object, ByVal e As System.Windows.Forms.PaintEventArgs)
    Dim axisBounds As Rectangle = Me.chartControl1.ChartArea.Bounds
    ' Render a rectangle around this bounds
    e.Graphics.DrawRectangle(Pens.Red, axisBounds)
End Sub
```

**Figure 367: Chart Area Bounds in Red**

![Illustrates Full Chart Area Bounds](https://i.imgur.com/5mCfH.webp)

### Chart Plot Area Bounds

Use the `RenderBounds` property to get the rectangular area comprising just the plot-area, bound by the axes.

## Chart Plot Area Bounds

**Use the `RenderBounds` property to get the rectangular area comprising just the plot-area, bound by the axes.**

```csharp
[C#]

this.chartControl1.ChartAreaPaint += new
System.Windows.Forms.PaintEventHandler(chartControl1_ChartAreaPaint);

void chartControl1_ChartAreaPaint(object sender,
System.Windows.Forms.PaintEventArgs e)
{
```

## Page-level Navigation/TOC (if applicable)

- [Chart Area Bounds]
- [Chart Plot Area Bounds]

## Cross References

See also: [Syncfusion WinForms Documentation](https://www.syncfusion.com)

<!-- tags: [syncfusion-sdk, chart, windowsforms, .net], keywords: [chart area, bounds, plot area, render bounds, vb.net, csharp, windows forms, chart control, syncfusion, 11.4.0.26] -->
```