```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_611.jpeg
document_name: chart
page_number: 611
page_id: chart#page_611
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:51:11Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- This section discusses customizing the appearance of data points in a chart to highlight members who have met or exceeded their sales quota.
- It introduces the concept of using the `PrepareStyle` event to conditionally apply styles to specific data points.

## Content

### Conditional Styling for Sales Quota Achievement

The following code snippet demonstrates how to use the `PrepareStyle` event to apply a green fill to the columns of销售人员 who have achieved or exceeded a 100% sales quota.

```csharp
' Condition to select members (data points) who made 100 % quota in sales
If ((series.Points(args.Index).YValues(0) / 150) * 100) >= 100
    Then
        args.Style.Interior = New Syncfusion.Drawing.BrushInfo(Syncfusion.Drawing.GradientStyle.Horizontal, System.Drawing.Color.DarkGreen, System.Drawing.Color.LightYellow)
    End If
End If
End Sub
```

#### Figure: Series Customization using PrepareStyle Event

![Figure 369: Green columns indicate employees who met 100 percent of their Quota](attachment:figure369.png)

*Figure 369: Green columns indicate employees who met 100 percent of their Quota.*

### 4.19.5 SeriesInCompatible Event

#### Overview
- This section explains the `SeriesInCompatible` event, which is triggered when the Chart detects that the series in the chart are incompatible after updating.

#### Description
When the Chart has completed updating the series and determines that the series are incompatible, the `SeriesInCompatible` event is raised.

#### Code Example

```csharp
[C#]
private static void chartControl1_SeriesInCompatible(object sender, EventArgs e)
{
    Console.WriteLine("SeriesInCompatible event is raised");
}
```

## API Reference

### Events
- **SeriesInCompatible**: Triggered when the Chart detects that the series are incompatible after updating.

## Code Examples

### SeriesInCompatible Event Example

The `SeriesInCompatible` event is used to handle situations where the series in the chart are deemed incompatible. Below is an example of how to handle this event:

```csharp
// C# Example
private static void chartControl1_SeriesInCompatible(object sender, EventArgs e)
{
    Console.WriteLine("SeriesInCompatible event is raised");
}
```

## Page-level Navigation/TOC
- Essential Chart for Windows Forms
- Conditional Styling for Sales Quota Achievement
- SeriesInCompatible Event

## Cross References
- See also: "Handling Chart Events" for more information on other chart events.

## RAG Annotations
<!-- tags: [Essential Chart, Windows Forms, Syncfusion, SeriesInCompatible Event, PrepareStyle Event] keywords: [Customization, Data Points, Sales Quota, Green Fill, Incompatible Series, C#] -->
```