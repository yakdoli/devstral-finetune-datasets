```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_430.jpeg
document_name: chart
page_number: 430
page_id: chart#page_430
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:43:06Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview

- Demonstrates how to create breaks in a chart's primary Y-axis using C# and VB.NET.
- Configures break lines, styles, and spacing for the Y-axis in a chart control.

## Content

### Configuring Chart Breaks in C#

The following C# code snippet shows how to configure break lines and ranges for the primary Y-axis in a chart control.

```csharp
this.chartControl1.PrimaryYAxis.BreakInfo.LineColor = Color.Black;
this.chartControl1.PrimaryYAxis.BreakInfo.LineWidth = 1;
this.chartControl1.PrimaryYAxis.BreakInfo.LineStyle = DashStyle.Dot;
this.chartControl1.PrimaryYAxis.BreakInfo.SpacingColor = Color.White;
this.chartControl1.PrimaryYAxis.BreakRanges.BreakAmount = 0.5;
```

### Configuring Chart Breaks in VB.NET

The following VB.NET code snippet demonstrates how to configure break lines and ranges for the primary Y-axis in a chart control.

```vb
Me.chartControl1.PrimaryYAxis.MakeBreaks = True

Me.chartControl1.PrimaryYAxis.BreakRanges.BreaksMode = ChartBreaksMode.Manual
Me.chartControl1.PrimaryYAxis.BreakRanges.Union(New DoubleRange(500, 600))
Me.chartControl1.PrimaryYAxis.BreakRanges.Union(New DoubleRange(950, 3000))

Me.chartControl1.PrimaryYAxis.BreakInfo.LineType = ChartBreakLineType.Wave
Me.chartControl1.PrimaryYAxis.BreakInfo.LineSpacing = 5
Me.chartControl1.PrimaryYAxis.BreakInfo.LineColor = Color.Black
Me.chartControl1.PrimaryYAxis.BreakInfo.LineWidth = 1
Me.chartControl1.PrimaryYAxis.BreakInfo.LineStyle = DashStyle.Dot
Me.chartControl1.PrimaryYAxis.BreakInfo.SpacingColor = Color.White
Me.chartControl1.PrimaryYAxis.BreakRanges.BreakAmount = 0.5
```

### Explanation of Break Configurations

- **`MakeBreaks = True`**: Enables the creation of breaks in the chart.
- **`BreaksMode = Manual`**: Specifies that the breaks are manually defined.
- **`Union(DoubleRange(...))`**: Adds specific ranges where breaks should occur.
- **`BreakInfo.LineType = ChartBreakLineType.Wave`**: Sets the style of the break lines to a wave pattern.
- **`BreakInfo.LineSpacing = 5`**: Defines the spacing between the break lines.
- **`BreakInfo.LineColor = Color.Black`**: Sets the color of the break lines.
- **`BreakInfo.LineWidth = 1`**: Sets the width of the break lines.
- **`BreakInfo.LineStyle = DashStyle.Dot`**: Sets the style of the break lines to dotted.
- **`BreakInfo.SpacingColor = Color.White`**: Sets the color of the spacing area for breaks.
- **`BreakAmount = 0.5`**: Defines the amount of breaking, where 0.5 represents a 50% break.

### Example Chart with Breaks

The following image illustrates a chart with break lines:

![Chart with Breaks](chart_with_breaks.png)

In the chart above:

- The primary Y-axis contains break lines to indicate gaps in the data range.
- Break lines are styled with a dotted pattern and set to a specific spacing and color.
- The breaks are manually defined to cover specific ranges (500 to 600 and 950 to 3000).

## API Reference

### BreakInfo Properties
- **LineColor**: Specifies the color of the break lines.
- **LineWidth**: Specifies the width of the break lines.
- **LineStyle**: Specifies the style of the break lines (e.g., DashStyle.Dot).
- **SpacingColor**: Specifies the color of the spacing area for breaks.

### BreakRanges Properties
- **BreaksMode**: Specifies the method of defining breaks (e.g., Manual).
- **BreakAmount**: Specifies the amount of breaking applied to the axis.

## Code Examples

### Complete C# Example

```csharp
this.chartControl1.PrimaryYAxis.MakeBreaks = true;
this.chartControl1.PrimaryYAxis.BreakRanges.BreaksMode = ChartBreaksMode.Manual;
this.chartControl1.PrimaryYAxis.BreakRanges.Union(new DoubleRange(500, 600));
this.chartControl1.PrimaryYAxis.BreakRanges.Union(new DoubleRange(950, 3000));

this.chartControl1.PrimaryYAxis.BreakInfo.LineType = ChartBreakLineType.Wave;
this.chartControl1.PrimaryYAxis.BreakInfo.LineSpacing = 5;
this.chartControl1.PrimaryYAxis.BreakInfo.LineColor = Color.Black;
this.chartControl1.PrimaryYAxis.BreakInfo.LineWidth = 1;
this.chartControl1.PrimaryYAxis.BreakInfo.LineStyle = DashStyle.Dot;
this.chartControl1.PrimaryYAxis.BreakInfo.SpacingColor = Color.White;
this.chartControl1.PrimaryYAxis.BreakRanges.BreakAmount = 0.5;
```

### Complete VB.NET Example

```vb
Me.chartControl1.PrimaryYAxis.MakeBreaks = True
Me.chartControl1.PrimaryYAxis.BreakRanges.BreaksMode = ChartBreaksMode.Manual
Me.chartControl1.PrimaryYAxis.BreakRanges.Union(New DoubleRange(500, 600))
Me.chartControl1.PrimaryYAxis.BreakRanges.Union(New DoubleRange(950, 3000))

Me.chartControl1.PrimaryYAxis.BreakInfo.LineType = ChartBreakLineType.Wave
Me.chartControl1.PrimaryYAxis.BreakInfo.LineSpacing = 5
Me.chartControl1.PrimaryYAxis.BreakInfo.LineColor = Color.Black
Me.chartControl1.PrimaryYAxis.BreakInfo.LineWidth = 1
Me.chartControl1.PrimaryYAxis.BreakInfo.LineStyle = DashStyle.Dot
Me.chartControl1.PrimaryYAxis.BreakInfo.SpacingColor = Color.White
Me.chartControl1.PrimaryYAxis.BreakRanges.BreakAmount = 0.5
```

## Cross References

- See also:
  - [Customizing Chart Axes](#customizing-chart-axes)
  - [Chart Series Breaks](#chart-series-breaks)

<!-- tags: [Syncfusion Windows Forms, Chart Control, Break Configuration, Break Lines, Manual Breaks] keywords: [BreakInfo, BreakRanges, ChartBreakLineType, DashStyle.Dot, Wave, BreakAmount] -->
```
