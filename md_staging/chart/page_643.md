```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_643.jpeg
document_name: chart
page_number: 643
page_id: chart#page_643
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:53:18Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates the usage of `Syncfusion.Windows.Forms.Chart` control for exporting charts to an Image.
- Highlights the properties and methods used for managing how the chart's axes and series are rendered.
- Includes handling for print functionality and chart re-draw.

## Content

### Example of Exporting and Configuring Chart Control

The following code snippet demonstrates how to manage the export and configuration of a chart control in a Windows Forms application. It specifically shows how to handle the chart's printing options, series styles, and axis properties.

```vb
Rectangle(Point.Empty, img.Size)
g.ReleaseHdc(hdc)
g.Dispose()
mf.Dispose()
End Using
End Using
EndTransform(e.Graphics, container)

For i As Integer = 0 To Me.chartControl1.Series.Count - 1
    Me.chartControl1.Series(i).StylesImpl.Style.ResetInterior()
    Me.chartControl1.Series(i).StylesImpl.Style.ResetBorder()
    Me.chartControl1.Series(i).StylesImpl.Style.CopyFrom(tempStyles(i))
Next

End If
```
/// Checking Toolbar functionality of print

```vb
If Not Me.chartControl1.PrintDocument.PrintToolBar Then
    Me.chartControl1.ShowToolBar = toolBatVisibility
End If
```

```vb
///Redraws the chart
Me.chartControl1.Redraw(True)
```

```vb
/ Reset the HasMorePages property to false when it exceeds the charts default maximum.
If mx > [end] Then
    e.HasMorePages = False
End If
```

```vb
//Finally resets the maximum and minimum value for default chartcontrol

Me.chartControl1.ChartArea.PrimaryXAxis.Range.Min = start
Me.chartControl1.ChartArea.PrimaryXAxis.Range.Max = [end]
Me.chartControl1.ChartArea.PrimaryXAxis.Range.Interval = Intervel
End Sub
```

### Explanation of Key Concepts
- **`ResetInterior()` and `ResetBorder()`**: These methods are used to reset the interior and border styles of each series in the chart, ensuring consistent rendering.
- **`CopyFrom(tempStyles(i))`**: This method copies the style properties from a predefined template, allowing for unified visual design across series.
- **`ShowToolBar`**: Controls the visibility of the print toolbar when printing functionality is enabled.
- **`Redraw(True)`**: Forces the chart to redraw, ensuring any changes are rendered visible.
- **`HasMorePages`**: A property that determines whether additional pages are required for the chart when printed.
- **`ChartArea.PrimaryXAxis.Range`**: Used to set the minimum, maximum, and interval values for the primary X-axis of the chart.

### Summary
This section provides a detailed guide on managing different aspects of the `Syncfusion.Windows.Forms.Chart` control, focusing on export, print, and rendering functionalities. It highlights the use of various properties and methods to configure the chart control effectively for different scenarios.

## Cross References
- Refer to the `Syncfusion.Windows.Forms.Chart` documentation for additional information on other properties and methods available for chart configuration.
- See also: Chapter on Exporting Charts, Print Configuration, and Adjusting Axis Properties.

<!-- tags: [Syncfusion, Windows Forms, Chart Control, Exporting, Printing, Axis Configuration, Series Style] keywords: [Syncfusion.Windows.Forms.Chart, ResetInterior, ResetBorder, PrintToolBar, Redraw, HasMorePages, PrimaryXAxis] -->
```