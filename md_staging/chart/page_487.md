```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_487.jpeg
document_name: chart
page_number: 487
page_id: chart#page_487
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:43:47Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Explains how to format tooltips for data points in a chart.
- Describes the placeholders for tooltip formatting.
- Demonstrates setting tooltip formats for individual data points.

## Content
### Tooltip Formatting For Data Points
The placeholders for tooltip formatting are as follows:

- `{0}` - Will be replaced by the corresponding `ChartSeries.Name`.
- `{1}` - Will be replaced by the corresponding `ChartSeries.Style.ToolTip`.
- `{2}` - Will be replaced by the corresponding data point's tooltip, for example to set the first point's tooltip, use "series1.Styled[0].ToolTip".
- `{3}` - Will be replaced by the corresponding X value of the point.
- `{4}` - Will be replaced by the corresponding Y value of the point. **Default setting.**
- `{5}` - Will be replaced by the 2nd Y value, if any.
- `{6}` - and so on.

#### Setting Tooltip Format in C#
```csharp
series1.PointsToolTipFormat = "Sales:{4}K";
```

#### Setting Tooltip Format in VB.NET
```vb
series1.PointsToolTipFormat = "Sales:{4}K"
```

### Example: Formatted Tooltips on the Series
![Illustrates Formatted Tooltips on the Series](https://i.imgur.com/example_graph.png)

**Figure 313: Tooltip Format set for Data Points**

### Customizing Tooltip for Individual Data Points
You can also customize the tooltip for individual data points by setting the `ToolTip` style for each data point. This is best accomplished by listening to the `ChartSeries.PrepareStyle` event as shown below.

## API Reference
- Properties:
  - `PointsToolTipFormat`: Gets or sets the format string for the tooltips of the data points.
  - `ToolTip`: Gets or sets the tooltip text for a data point.

## Code Examples

### C# Example
```csharp
// Set ToolTipFormat for the series
series1.PointsToolTipFormat = "Sales:{4}K";
```

### VB.NET Example
```vb
' Set ToolTipFormat for the series
series1.PointsToolTipFormat = "Sales:{4}K"
```

### Listening to ChartSeries.PrepareStyle Event
```csharp
chart.Series.PrepareStyle += (sender, args) =>
{
    if (args.Element is DataPoint point)
    {
        point.ToolTip = $"Custom Tooltip for {point.Y}";
    }
};
```

## Related Topics
- [Tooltip Customization in Syncfusion WinForms Chart](#tooltip-customization)
- [Events and Event Handling in Syncfusion WinForms](#events-handling)

<!-- tags: [winforms, chart, tooltip, data-point, formatting, preparestyle] keywords: [tooltip, data point, placeholders, custom tooltip, preparestyle event] -->
```