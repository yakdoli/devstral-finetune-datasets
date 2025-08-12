```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_435.jpeg
document_name: chart
page_number: 435
page_id: chart#page_435
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:40:33Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
e.Label = "Canada";
}
else if (e.Label == "2")
{
    if (series.Points[(int)e.Value - 1].YValues[0] > 0)
        e.AxisLabelPlacement = ChartPlacement.Outside;
    e.Label = "France";
}
else if (e.Label == "3")
{
    if (series.Points[(int)e.Value - 1].YValues[0] > 0)
        e.AxisLabelPlacement = ChartPlacement.Outside;
    e.Label = "Japan";
}
else if (e.Label == "4")
{
    if (series.Points[(int)e.Value - 1].YValues[0] > 0)
        e.AxisLabelPlacement = ChartPlacement.Outside;
    e.Label = "Britain";
}
else if (e.Label == "5")
{
    if (series.Points[(int)e.Value - 1].YValues[0] > 0)
        e.AxisLabelPlacement = ChartPlacement.Outside;
    e.Label = "United States";
}
e.Handled = true;
}
}
```

### [VB]
```vb
Me.chartControl1.PrimaryYAxis.AxisLabelPlacement = ChartPlacement.Indsode
'Sets the AxisLabelPlacement property in ChartFormatAxisLabel event. this.chartControl1.PrimaryYAxis.AxisLabelPlacement =
ChartPlacement.Indsode;
Private Sub chartControl1_ChartFormatAxisLabel(ByVal sender As Object, ByVal e As ChartFormatAxisLabelEventArgs)
    If e.AxisOrientation = ChartOrientation.Vertical Then
        If e.Label = "1" Then
            If series.Points(CInt(Fix(e.Value)) - 1).YValues(0)
                e.AxisLabelPlacement = ChartPlacement.Outside
            End If
```

## API Reference

### Control: chartControl1

- **Property**: `PrimaryYAxis.AxisLabelPlacement`
  - Type: `ChartPlacement`
  - Description: Specifies the placement of axis labels.
  - Possible Values:
    - `Inside`: Labels are placed inside the chart.
    - `Outside`: Labels are placed outside the chart.

### Event: `ChartFormatAxisLabel`

```csharp
private void chartControl1_ChartFormatAxisLabel(object sender, ChartFormatAxisLabelEventArgs e)
{
    if (e.AxisOrientation == ChartOrientation.Vertical)
    {
        if (e.Label == "1")
        {
            if (series.Points[(int)e.Value - 1].YValues[0] > 0)
            {
                e.AxisLabelPlacement = ChartPlacement.Outside;
            }
        }
    }
    e.Handled = true;
}
```

```vb
Private Sub chartControl1_ChartFormatAxisLabel(ByVal sender As Object, ByVal e As ChartFormatAxisLabelEventArgs)
    If e.AxisOrientation = ChartOrientation.Vertical Then
        If e.Label = "1" Then
            If series.Points(CInt(Fix(e.Value)) - 1).YValues(0)
                e.AxisLabelPlacement = ChartPlacement.Outside
            End If
    e.Handled = True
End Sub
```

## Code Examples

### Example: Dynamic Label Placement

```csharp
e.Label = "Canada";
}
else if (e.Label == "2")
{
    if (series.Points[(int)e.Value - 1].YValues[0] > 0)
        e.AxisLabelPlacement = ChartPlacement.Outside;
    e.Label = "France";
}
else if (e.Label == "3")
{
    if (series.Points[(int)e.Value - 1].YValues[0] > 0)
        e.AxisLabelPlacement = ChartPlacement.Outside;
    e.Label = "Japan";
}
else if (e.Label == "4")
{
    if (series.Points[(int)e.Value - 1].YValues[0] > 0)
        e.AxisLabelPlacement = ChartPlacement.Outside;
    e.Label = "Britain";
}
else if (e.Label == "5")
{
    if (series.Points[(int)e.Value - 1].YValues[0] > 0)
        e.AxisLabelPlacement = ChartPlacement.Outside;
    e.Label = "United States";
}
e.Handled = true;
}
}
```

```vb
Me.chartControl1.PrimaryYAxis.AxisLabelPlacement = ChartPlacement.Indsode
'Sets the AxisLabelPlacement property in ChartFormatAxisLabel event. this.chartControl1.PrimaryYAxis.AxisLabelPlacement =
ChartPlacement.Indsode
Private Sub chartControl1_ChartFormatAxisLabel(ByVal sender As Object, ByVal e As ChartFormatAxisLabelEventArgs)
    If e.AxisOrientation = ChartOrientation.Vertical Then
        If e.Label = "1" Then
            If series.Points(CInt(Fix(e.Value)) - 1).YValues(0)
                e.AxisLabelPlacement = ChartPlacement.Outside
            End If
```

<!-- tags: [syncfusion, windows forms, chart, axislabel placement, chart axis, chart control, dynamic label placement, chart format axis label event] keywords: [chart, axislabel, label placement, windows forms, dynamic, chart event, chart axis orientation] -->
```