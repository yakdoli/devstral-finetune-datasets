```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_411.jpeg
document_name: chart
page_number: 411
page_id: chart#page_411
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:38:58Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Code Example

```vb
Private Sub chartControl1_ChartFormatAxisLabel(ByVal sender As Object, ByVal e As ChartFormatAxisLabelEventArgs)
    Dim index As Integer = CInt(Fix(e.Value))
    If e.AxisOrientation = ChartOrientation.Horizontal Then
        If index >= 0 AndAlso index < arrLabel.Count Then
            e.Label = arrLabel(index).ToString()
        ' Specify arrTooltip content as chartAxisLabel Tooltip
            e.ToolTip = arrTooltip(index).ToString()
        End If
    End If
    e.Handled = True
End Sub
```

### Figure

![Product Sales](https://example.com/product_sales_image)

**Figure 263: Customized Tooltip**

### Refer Also

- [Customizing Label Text](#)
- [ToolTip](#)

### Page Footer

© 2013 Syncfusion. All rights reserved.
```

<!-- tags: [chart, label text, tooltip, windows forms, syncfusion, winforms, control, api reference, example, code, figure, product sales, customized tooltip] keywords: [chartcontrol1_chartformataxislabel, arrlabel, arrtooltip, chartformataxislabeleventargs, chartorientation.horizontal, e.handled, e.label, e.tooltip, customize, labels, tooltips, axis orientation, million, product sales, country, india, pakistan, sri lanka, japan, charting, visualization, data display, syncing, chart properties, axis formatting, event handling, api reference, essentials, windows forms, 2013, product, syncfusion, control, documentation, reference, sample code, figure, example, guide, tutorial, customizing, operations, millions, product, chart, axislabel] -->
```