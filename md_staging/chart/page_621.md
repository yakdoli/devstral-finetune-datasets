```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_621.jpeg
document_name: chart
page_number: 621
page_id: chart#page_621
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:53:37Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
private void chartControl1_ChartRegionMouseUp(object sender, Syncfusion.Windows.Forms.Chart.ChartRegionMouseEventArgs e)
{
    Cursor = Cursors.SizeAll;
    if (this.isDragging)
    {
        double newY = Math.Floor(this.chartControl1.ChartArea.GetValueByPoint(e.Point).YValues[0]);
        double newX = this.chartControl1.ChartArea.GetValueByPoint(e.Point).X;
        if (newY < 0 || newY >= 50 || newX < 0 || newX > 7)
            MessageBox.Show("Cannot drag outside chart bounds");
        else
        {
            this.NewYValue(newY);
            this.NewXValue(newX);
        }
        this.isDragging = false;
        this.currentRegion = null;
        this.selectedDataPoint.Y = 0;
        this.selectedDataPoint.X = 0;
        this.chartControl1.Redraw(true);
    }
    this.chartControl1.Series[0].Style.TextFormat = "{0}";
    this.chartControl1.Refresh();
}
```

```vb
Private Sub chartControl1_ChartRegionMouseUp(ByVal sender As Object, ByVal e As Syncfusion.Windows.Forms.Chart.ChartRegionMouseEventArgs) Handles chartControl1.ChartRegionMouseUp
    Cursor = Cursors.SizeAll
    If Me.isDragging Then
        Dim newY As Double = Math.Floor(Me.chartControl1.ChartArea.GetValueByPoint(e.Point).YValues(0))
        Dim newX As Double = Me.chartControl1.ChartArea.GetValueByPoint(e.Point).X
        If newY < 0 OrElse newY >= 50 OrElse newX < 0 OrElse newX > 7 Then
            MessageBox.Show("Cannot drag outside chart bounds")
        Else
            Me.NewYValue(newY)
        End If
    End If
End Sub
```

## API Reference

### `chartControl1_ChartRegionMouseUp`

#### Parameters
- `sender`: Object
- `e`: Syncfusion.Windows.Forms.Chart.ChartRegionMouseEventArgs

#### Description
This event handler is triggered when the mouse is released over a chart region. It checks whether the dragging action is in progress (`this.isDragging`), calculates the new Y and X values based on the mouse position, and ensures that the new values do not exceed the chart's boundaries. If the new values are within bounds, it updates the chart with the new values. If not, it displays a message box indicating that dragging outside the chart bounds is not allowed. It also refreshes the chart display.

## Code Examples

The provided C# and VB.NET code examples demonstrate how to handle the `ChartRegionMouseUp` event for a `Syncfusion.Windows.Forms.Chart` control. These examples include:
- Setting the cursor to a resizing style when dragging ends.
- Checking if dragging has occurred and calculating new data point positions.
- Validating the new position within chart boundaries.
- Updating the chart with the new values and refreshing the display.

## Page-level Navigation/TOC (if applicable)
This section aligns with the functionalities involved in handling mouse events on a `Syncfusion.Windows.Forms.Chart` control, specifically focusing on the `ChartRegionMouseUp` event.

### Cross References
- For further details on chart controls and their event handling, refer to the Syncfusion Windows Forms documentation for the `Syncfusion.Windows.Forms.Chart` namespace.

### RAG Annotations
<!-- tags: Syncfusion, Windows Forms, Chart, ChartRegionMouseUp, Mouse Events, Dragging, Chart Boundaries, Refresh, Cursor, API Reference -->
<!-- keywords: ChartRegionMouseUp, Mouse Release, Data Point, Bounds, Redraw, Cursor, Windows Forms, Syncfusion -->
```