```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_510.jpeg
document_name: chart
page_number: 510
page_id: chart#page_510
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:48:32Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Content

### Code Example in VB.NET

```vb
Private Sub chartControl1_ChartAreaPaint(ByVal sender As Object, ByVal e As PaintEventArgs)
    ' Get the right end of the X axis
    Dim ptX As Point = Me.chartControl1.ChartArea.GetPointByValue(New ChartPoint(Me.chartControl1.PrimaryXAxis.Range.Max, Me.chartControl1.PrimaryYAxis.Range.Min))

    Dim ptX1 As New PointF(ptX.X - 7, ptX.Y - 4)
    Dim ptX2 As New PointF(ptX.X, ptX.Y)
    Dim ptX3 As New PointF(ptX.X - 7, ptX.Y + 4)

    ' Draws an arrow at the end of the X axis
    e.Graphics.FillPolygon(Brushes.Black, New PointF() {ptX1, ptX2, ptX3})

    ' Get the top end of the Y axis
    Dim ptY As Point = Me.chartControl1.ChartArea.GetPointByValue(New ChartPoint(Me.chartControl1.PrimaryXAxis.Range.Min, Me.chartControl1.PrimaryYAxis.Range.Max))

    Dim ptY1 As New PointF(ptY.X - 4, ptY.Y + 7)
    Dim ptY2 As New PointF(ptY.X, ptY.Y)
    Dim ptY3 As New PointF(ptY.X + 4, ptY.Y + 7)

    ' Draws an arrow at the top of the Y Axis.
    e.Graphics.FillPolygon(Brushes.Black, New PointF() {ptY1, ptY2, ptY3})

    ' Draws a line through the center of the chart.
    e.Graphics.DrawLine(Pens.Gray, ptY.X, ptX.Y, ptX.X, ptY.Y)
End Sub
```

## Page-level Navigation/TOC (if applicable)

### Related Topics
- Chart customization
- Graphical annotations
- Chart area rendering

## Cross References

### See also:
- `ChartArea.GetPointByValue` method
- `FillPolygon` method
- `DrawLine` method

## RAG Annotations
<!-- tags: [Syncfusion Winforms, Chart, ChartArea, Customization] keywords: [chart, axis, annotation, paint event, FillPolygon, DrawLine, Graphical] -->
```