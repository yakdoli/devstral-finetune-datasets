```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_252.jpeg
document_name: chart
page_number: 252
page_id: chart#page_252
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:31:33Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

```vb
[VB.NET]

' Specifies the circle radius around the point for HitTest
Me.chartControl1.Series(0).Style.HitTestRadius = 20

' ChartClick Event will be fired if clicked within the above circle
Private Sub chartControl1_ChartRegionClick(ByVal sender As Object, 
                         ByVal e As Syncfusion.Windows.Forms.Chart.Chart.ChartRegionMouseEventArgs)
    ' Message appears when User hits the test radius region
    If e.Region.IsChartPoint Then
        MessageBox.Show("Point is Hit")
    End If
End Sub
```

![HitTestRadius example](https://via.placeholder.com/500x300.png?text=Figure+149%3A+Chart+with+HitTestRadius+%3D+%2220%22)

### Figure 149: Chart with HitTestRadius = "20"

## See Also
- Line Chart, StepLineChart, ChartRegionClick Events
```


<!-- tags: [Windows Forms, Chart, HitTestRadius, ChartRegionClick, Syncfusion] keywords: [Windows Forms, Chart, HitTestRadius, ChartRegionClick, VB.NET, Syncfusion, ChartPoint, Mouse Events, Visual Basic, Syncfusion.Windows.Forms.Chart, HitTest, MessageBox, Product Comparison Chart, Graph Interaction, Data Visualization] -->
```