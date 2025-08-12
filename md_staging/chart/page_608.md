```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_608.jpeg
document_name: chart
page_number: 608
page_id: chart#page_608
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:52:40Z
fidelity: lossless
-->

### Handling Chart Region Events in Windows Forms

This section demonstrates how to handle the `ChartRegionDoubleClick` and `ChartRegionMouseDown` events for a `Syncfusion.Windows.Forms.Chart` control.

## ChartRegionDoubleClick Event

The `ChartRegionDoubleClick` event is triggered when the user double-clicks on a region of the chart. Below is an example implementation in C#:

```csharp
//ChartRegionDoubleClick Event
this.chartControl1.ChartRegionDoubleClick += new Syncfusion.Windows.Forms.Chart.ChartRegionMouseEventHandler(this.chartControl1_ChartRegionDoubleClick);

private void chartControl1_ChartRegionDoubleClick(object sender, ChartRegionMouseEventArgs e)
{
    if (this.chkRegionDoubleClick.Checked)
    {
        if (e.Region.SeriesIndex == 0)
        {
            OutputText(String.Format("Double Click over Series 1 Column {0} Point : {1}", e.Region.PointIndex, e.Point));
            ShowChartRegion("ChartSeries");
        }
        else
        {
            OutputText(String.Format("Double Click over {0}", e.Region.Description));
            ShowChartRegion(e.Region.Description);
        }
    }
}
```

### Explanation
- **Event Subscription**: The `ChartRegionDoubleClick` event is subscribed to the `chartControl1` object.
- **Condition Check**: The event handler checks if a checkbox (`chkRegionDoubleClick`) is checked.
- **Series Index Check**: If the double-click is on the first series (`SeriesIndex == 0`), the method outputs detailed information about the clicked point and highlights the chart series.
- **Region Check**: For other regions, the method outputs the region description and highlights that specific region.

## ChartRegionMouseDown Event

The `ChartRegionMouseDown` event is triggered when the user presses the mouse button down on a chart region. Below is an example implementation in C#:

```csharp
//Usage of Button property in ChartRegionMouseDown Event
void chartControl1_ChartRegionMouseDown(object sender, ChartRegionMouseEventArgs e)
{
    if (e.Button == MouseButtons.Right)
    {
        Console.WriteLine("Chart Region Mouse Down:=" + e.Point);
    }
}
```

### Explanation
- **Right Mouse Button Check**: The event handler checks if the right mouse button (`MouseButtons.Right`) was pressed.
- **Output**: If the right button is pressed, the method outputs the coordinates of the clicked point.

## VB.NET Implementation

The same functionality can also be implemented in VB.NET:

```vb.net
'ChartRegionDoubleClick Event
AddHandler Me.chartControl1.ChartRegionDoubleClick, AddressOf Me.chartControl1_ChartRegionDoubleClick

Private Sub chartControl1_ChartRegionDoubleClick(ByVal sender As Object, ByVal e As ChartRegionMouseEventArgs)
    If Me.chkRegionDoubleClick.Checked Then
        If e.Region.SeriesIndex = 0 Then
            ' Code to handle Series 1 Column
            ' OutputText(String.Format("Double Click over Series 1 Column {0} Point : {1}", e.Region.PointIndex, e.Point))
            ' ShowChartRegion("ChartSeries")
        Else
            ' Code to handle other regions
            ' OutputText(String.Format("Double Click over {0}", e.Region.Description))
            ' ShowChartRegion(e.Region.Description)
        End If
    End If
End Sub
```

### Explanation
- **Event Subscription**: Similar to the C# implementation, the `ChartRegionDoubleClick` event is subscribed in VB.NET using the `AddHandler` statement.
- **Condition Check**: The VB.NET implementation checks if the checkbox is checked and performs the appropriate actions based on the `SeriesIndex`.
- **Region Handling**: The event handler outputs information and highlights the region accordingly.

## Summary
- **Events Handled**: `ChartRegionDoubleClick` and `ChartRegionMouseDown`.
- **Conditional Logic**: Handles events based on user interactions and specific chart regions.
- **Multi-Language Support**: Implemented in both C# and VB.NET.

### RAG Annotations
<!-- tags: [Windows Forms, Chart, Event Handling, Syncfusion, ChartRegionDoubleClick, ChartRegionMouseDown] keywords: [chartcontrol1, chartregiondoubleclick, chartregionmousedown, mouseeventargs, doubleclick, mousedown, seriesindex, outputtext, regiondescription] -->
```