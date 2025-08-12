```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_610.jpeg
document_name: chart
page_number: 610
page_id: chart#page_610
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:55:58Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Discusses the ChartFormatAxisLabel Event in detail.
- Explains the PrepareStyle Event and its usage in customizing styles for series points.

## Content

### 4.19.3 ChartFormatAxisLabel Event
This event is discussed in detail in this topic: [Customizing Label Text](#customizing-label-text).

### 4.19.4 PrepareStyle Event

When a series point is about to be rendered by the chart, it will raise this event and allow event subscribers to change the style used.

#### C#
```csharp
// Listen to the prepare style event for the series.
series.PrepareStyle += new 
ChartPrepareStyleInfoHandler(series_PrepareStyle);

private void series_PrepareStyle(object sender, 
ChartPrepareStyleInfoEventArgs args)
{
    ChartSeries series = sender as ChartSeries;
    if (series != null)
    {
        // Condition to select members (data points) who made 100 % quota in sales
        if (((series.Points[args.Index].YValues[0] / 150) * 100) >= 100)
        {
            args.Style.Interior = new
            Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.Horizontal,
            System.Drawing.Color.DarkGreen, 
            System.Drawing.Color.LightYellow);
        }
    }
}
```

#### VB.NET
```vbnet
' Listen to the prepare style event for the series.
AddHandler series.PrepareStyle, AddressOf 
Me.ChartControlSeries_PrepareStyle

Private Sub series_PrepareStyle(ByVal sender As Object, ByVal args As 
ChartPrepareStyleInfoEventArgs)
    Dim series As ChartSeries = TryCast(sender, ChartSeries)
    If series IsNot Nothing Then
```

## API Reference

- Namespace: `Syncfusion.Drawing`
- Class: `BrushInfo`
- Methods/Properties:
  - `GradientStyle.Horizontal`
  - `Color.DarkGreen`, `Color.LightYellow`

## Code Examples

### C#
The example demonstrates setting a gradient style for points that meet a certain sales quota.

### VB.NET
The example demonstrates listening to the `PrepareStyle` event and customizing the interior style of series points based on conditions.

## Cross References
- See also: [Customizing Label Text](#customizing-label-text) for related topics.

<!-- tags: [syncfusion, winforms, chart, preparestyle, event, series, style] keywords: [chart, formataxislabel, preparestyle, event, data points, rendering, gradientstyle, VB.NET, C#, interior style] -->
```