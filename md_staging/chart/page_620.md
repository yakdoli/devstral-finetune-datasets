```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_620.jpeg
document_name: chart
page_number: 620
page_id: chart#page_620
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:53:25Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Content

### Section: Custom Tooltips for Histogram Chart

#### Code Snippet
```vb
Dim text As String = Nothing
If e.Region.IsChartPoint Then
    e.Region.ToolTip = "Tooltip " & e.Region.PointIndex.ToString()
Else
    text = "Not a chart Point"
End If
End Sub
```

#### Figure: Custom Tooltip Displayed for Histogram Chart
![Figure 374: CustomTooltip Displayed for Histogram Chart](https://i.imgur.com/figure374.png)

*Figure 374: CustomTooltip Displayed for Histogram Chart*

### See Also

- [Chart Region Events](Chart Region Events)
- [Tooltips](Tooltips)
- [Histogram Chart](Histogram Chart)

### Section: Dragging Chart Series Points at Run Time

#### Subsection: Overview

You can drag the chart series points by calculating new x and y values while handling any of the ChartRegionMouse Events like MouseUp, MouseDown, MouseHover, MouseLeave, and so forth, on the chart. The new x and y values of the series are calculated from the mouse point, and GetValueByPoint which returns the x and y values of the mouse point calculated from the Chart Point.

#### Code Snippet for Mouse Event Handler
The following code snippet must be given under the mouse event handler of the ChartRegionMouse event.

---

<!-- tags: [windows forms, chart, tooltips, histograms, series, dragging, mouse events] keywords: [custom tooltips, histogram chart, drag points, mouse, event handler, GetValueByPoint] -->
```