```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_602.jpeg
document_name: chart
page_number: 602
page_id: chart#page_602
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:55:21Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Code Examples (C#)
This section demonstrates how to implement a tooltip for chart legends in Windows Forms using C#.

```csharp
private ToolTip toolTip2;
this.chartControl1.Legend.MouseHover += new
MouseEventHandler(lgnd_MouseHover);

void lgnd_MouseHover(object sender, EventArgs e)
{
    Point pl = this.chartControl1.Legend.PointToClient(new
    Point(Control.MousePosition.X, Control.MousePosition.Y));
    ChartLegendItem item = chartControl1.Legend.GetItemBy(pl);
    if (item != null)
        this.toolTip2.Show(item.Text, this.chartControl1.Legend, pl.X + 
10, pl.Y + 20, 3000);
}
```

### Code Examples (VB.NET)
This section provides the equivalent implementation in VB.NET for the same functionality.

```vb
[VB.NET]

private toolTip2 As ToolTip
AddHandler Me.chartControl1.Legend.MouseHover, AddressOf
lgnd_MouseHover

Private Sub lgnd_MouseHover(ByVal sender As Object, ByVal e As
EventArgs)
    ' Get the item at the specified location..
    Dim pl As Point = Me.chartControl1.Legend.PointToClient(New
    Point(Control.MousePosition.X, Control.MousePosition.Y))
    Dim item As ChartLegendItem = chartControl1.Legend.GetItemBy(pl)
    If item IsNot Nothing Then
        Me.toolTip2.Show(item.Text, this.chartControl1.Legend, pl.X + 
10, pl.Y + 20, 3000)
    End If
End Sub
```

### Summary
This example shows how to display a tooltip when hovering over a legend item in a chart control within a Windows Forms application. The tooltip is positioned slightly offset from the legend item and remains visible for a duration of 3 seconds. This functionality enhances user interaction and provides valuable information about the chart data.

### Notes
- Ensure that the `toolTip2` instance is properly initialized and that the `chartControl1` control is correctly set up in the form's design.
- The `MousePosition` properties provide the current position of the mouse in screen coordinates, which are converted to client coordinates using the `PointToClient` method.
- The `GetItemBy` method retrieves the legend item under the specified point.

### Cross References
- See also: [Tooltip Properties](#tooltip-properties), [Chart Control Events](#chart-control-events)

### API Reference
- **ToolTips**: ToolTips are used to display additional information to the user when they hover over certain controls. In this case, it is used to display information about the chart legend.
- **MouseEventHandler**: Handles the event that is raised when the mouse pointer is over the control.
- **PointToClient**: Converts a point from screen coordinates to client coordinates.
- **ChartLegendItem**: Represents an item in the chart legend.

### Visualization
- The tooltip provides a user-friendly way to display detailed information about specific legend items without cluttering the chart itself.
- By hovering over each legend item, users can gain insights into the data represented by each series.

<!-- tags: [Syncfusion, ToolTips, Chart Control, Windows Forms, Mouse Hover, Chart Legend] keywords: [tooltip, legend, mouse hover, chart control, windows forms, synchronization, user interaction, information display] -->
```