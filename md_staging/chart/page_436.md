```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_436.jpeg
document_name: chart
page_number: 436
page_id: chart#page_436
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:41:50Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Chart Label Placement Customization

The following code snippet demonstrates how to customize the placement of individual labels on the y-axis of a chart:

```vb
If e.Label = "Canada" Then
    If series.Points(CInt(Fix(e.Value)) - 1).YValues(0) > 0 Then
        e.AxisLabelPlacement = ChartPlacement.Outside
    End If
ElseIf e.Label = "France" Then
    If series.Points(CInt(Fix(e.Value)) - 1).YValues(0) > 0 Then
        e.AxisLabelPlacement = ChartPlacement.Outside
    End If
ElseIf e.Label = "Japan" Then
    If series.Points(CInt(Fix(e.Value)) - 1).YValues(0) > 0 Then
        e.AxisLabelPlacement = ChartPlacement.Outside
    End If
ElseIf e.Label = "Britain" Then
    If series.Points(CInt(Fix(e.Value)) - 1).YValues(0) > 0 Then
        e.AxisLabelPlacement = ChartPlacement.Outside
    End If
ElseIf e.Label = "United States" Then
    If series.Points(CInt(Fix(e.Value)) - 1).YValues(0) > 0 Then
        e.AxisLabelPlacement = ChartPlacement.Outside
    End If
End If
e.Handled = True
End Sub
```

### Description

The following screenshot illustrates the customization options for individual label positions on the y-axis to the right or left side based on the y value of the data points. If the export value is positive, the label is rendered to the left side of the axis, and if it is negative, the label is rendered on the right side of the axis.

## Summary

This example shows how to dynamically adjust the placement of chart axis labels in a Windows Forms application using Syncfusion's charting component. The placement is determined based on a specific condition related to the y-value of the data points, allowing for customizable and context-sensitive visual representations.

## Footer
© 2013 Syncfusion. All rights reserved.
Page 436
```

<!-- tags: [chart, windows forms, label placement, customization, syncfusion] keywords: [LabelPlacement, ChartPlacement, Outside, Windows Forms, Charting, YValues, Conditional Placement] -->