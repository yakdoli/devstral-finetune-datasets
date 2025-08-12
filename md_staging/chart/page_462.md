```html
<!--    
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_462.jpeg
document_name: chart
page_number: 462
page_id: chart#page_462
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:45:19Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- This page explains how to enable panning in the zoomed chart using ChartControl's mouse and axis properties.
- Describes how to format axes labels for a zoomed chart using the SmartDateZoom property.

## Content

### Panning in Zoomed Chart
Panning allows users to pan across the zoomed chart area. The following settings enable the panning feature:

| Setting Controlled | Description |
|---------------------|-------------|
| Panning - Enables panning in the zoomed chart. | Details |
| None - Disables panning in the zoomed chart. | Details |

### Code Examples

#### C# Example
```csharp
// Enable panning in the chart.
this.chartControl1.MouseAction = ChartMouseAction.Panning;
this.chartControl1.PrimaryXAxis.ZoomActions = ChartZoomingAction.Panning;
this.chartControl1.PrimaryYAxis.ZoomActions = ChartZoomingAction.Panning;
```

#### VB.NET Example
```vb
' Enable panning in the chart.
Me.chartControl1.MouseAction = ChartMouseAction.Panning
Me.chartControl1.PrimaryXAxis.ZoomActions = ChartZoomingAction.Panning
Me.chartControl1.PrimaryYAxis.ZoomActions = ChartZoomingAction.Panning
```

### Note: Remember to enable zooming on both axes using EnableXZooming and EnableYZooming properties before trying out the above panning feature. You cannot pan a chart without zooming it.

#### Formatted Axes Labels
It is possible to show formatted axes labels for a zoomed chart. Essential Chart's SmartDateZoom property when set to `true` enables this feature. You can set any one of the following custom label formats to the chart axis.

- SmartDateZoomDayLevelLabelFormat
- SmartDateZoomYearLevelLabelFormat
- SmartDateZoomWeekLevelLabelFormat
- SmartDateZoomSecondLevelLabelFormat
- SmartDateZoomMonthLevelLabelFormat
- SmartDateZoomHourLevelLabelFormat
- SmartDateZoomMinuteLevelLabelFormat

#### C# Example
```csharp
// Enable formatted date labels for the zoomed chart.
this.chartControl1.PrimaryXAxis.SmartDateZoom = true;
this.chartControl1.PrimaryXAxis.SmartDateZoomDayLevelLabelFormat = "dd MM/yy HH.00";
```

#### VB.NET Example
```vb
' Enable formatted date labels for the zoomed chart.
Me.chartControl1.PrimaryXAxis.SmartDateZoom = True
Me.chartControl1.PrimaryXAxis.SmartDateZoomDayLevelLabelFormat = "dd MM/yy HH.00"
```

## API Reference

### SmartDateZoom Property
- **Type**: `Boolean`
- **Description**: Enables or disables the display of formatted date labels for a zoomed chart.
- **Default Value**: `false`

### SmartDateZoom*[Level]LabelFormat Properties
- **Type**: `String`
- **Description**: Specifies the format for displaying date labels at different levels of zoom.
- **Possible Values**:
  - `SmartDateZoomDayLevelLabelFormat`
  - `SmartDateZoomYearLevelLabelFormat`
  - `SmartDateZoomWeekLevelLabelFormat`
  - `SmartDateZoomSecondLevelLabelFormat`
  - `SmartDateZoomMonthLevelLabelFormat`
  - `SmartDateZoomHourLevelLabelFormat`
  - `SmartDateZoomMinuteLevelLabelFormat`

## Code Examples (Full)

### C# Example (Complete)
```csharp
using Syncfusion.Windows.Forms.Chart;

public class ChartExample
{
    public void ConfigurePanningAndFormatting()
    {
        // Enable panning
        this.chartControl1.MouseAction = ChartMouseAction.Panning;
        this.chartControl1.PrimaryXAxis.ZoomActions = ChartZoomingAction.Panning;
        this.chartControl1.PrimaryYAxis.ZoomActions = ChartZoomingAction.Panning;

        // Enable and format date labels
        this.chartControl1.PrimaryXAxis.SmartDateZoom = true;
        this.chartControl1.PrimaryXAxis.SmartDateZoomDayLevelLabelFormat = "dd MM/yy HH.00";
    }
}
```

### VB.NET Example (Complete)
```vb
Imports Syncfusion.Windows.Forms.Chart

Public Class ChartExample
    Public Sub ConfigurePanningAndFormatting()
        ' Enable panning
        Me.chartControl1.MouseAction = ChartMouseAction.Panning
        Me.chartControl1.PrimaryXAxis.ZoomActions = ChartZoomingAction.Panning
        Me.chartControl1.PrimaryYAxis.ZoomActions = ChartZoomingAction.Panning

        ' Enable and format date labels
        Me.chartControl1.PrimaryXAxis.SmartDateZoom = True
        Me.chartControl1.PrimaryXAxis.SmartDateZoomDayLevelLabelFormat = "dd MM/yy HH.00"
    End Sub
End Class
```

<!-- tags: [Syncfusion, WinForms, Chart, ChartControl, Zoom, Pan, AxesLabels, LabelFormatting, SmartDateZoom] keywords: [zoomed chart, panning, ChartMouseAction, ChartZoomingAction, formatted labels, date labels, axis formatting, control] -->
```