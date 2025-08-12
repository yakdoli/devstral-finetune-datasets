```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_424.jpeg
document_name: chart
page_number: 424
page_id: chart#page_424
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:40:47Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
this.chartControl1.PrimaryYAxis.GridLineType.PenType = 
System.Drawing.Drawing2D.PenType.LinearGradient;
this.chartControl1.PrimaryYAxis.GridLineType.Width = 2F;
```

### [VB.NET]

```vb.net
'' Customizing X-Axis Gridlines
Me.chartControl1.PrimaryXAxis.DrawGrid = True
Me.chartControl1.PrimaryXAxis.GridLineType.BackColor = 
System.Drawing.Color.Transparent
Me.chartControl1.PrimaryXAxis.GridLineType.DashStyle = 
System.Drawing.Drawing2D.DashStyle.DashDotDot
Me.chartControl1.PrimaryXAxis.GridLineType.ForeColor = 
System.Drawing.Color.DarkBlue
Me.chartControl1.PrimaryXAxis.GridLineType.Width = 2F

'' Customizing Y-Axis Gridlines
Me.chartControl1.PrimaryYAxis.DrawGrid = True
Me.chartControl1.PrimaryYAxis.GridLineType.BackColor = 
System.Drawing.Color.OliveDrab
Me.chartControl1.PrimaryYAxis.GridLineType.ForeColor = 
System.Drawing.Color.DarkOrange
Me.chartControl1.PrimaryYAxis.GridLineType.PenType = 
System.Drawing.Drawing2D.PenType.LinearGradient
Me.chartControl1.PrimaryYAxis.GridLineType.Width = 2F
```

## 4.6.13 Chart StripLines

Strip-lines are bands that are drawn at the background of the chart. They can be used to highlight areas of interest. They can be either vertical or horizontal and may be specified with a variety of options to precisely control where they are placed and how they are repeated. The strip-lines are stored in the `ChartAxis.StripLines` collection, which holds objects of class `ChartStripLine`.

A strip-line is configurable by setting its start, end, period and width in the same value type as the axis that holds it. The interior of the strip-lines support gradients, images and different text positions and orientations.

| Chart control Property | Description |
|-------------------------|-------------|
| BackImage              | Sets the background image for the stripline. |
| DateOffset             | Gets / sets the offset of the stripline if the chart's PrimaryX-axis is of type `Datetime` and `StartAtAxisPosition` is `true`. Also see `Offset`. |

## API Reference (if applicable)

### Namespaces and Classes

#### `System.Drawing.Drawing2D`
- `PenType`: Defines the type of pen used for drawing.

### Properties
- `DrawGrid`: A boolean property that determines whether grid lines are drawn on the axis.
- `GridLineType`: Specifies the type of grid line drawn on the axis.
- `DashStyle`: Defines the style of dashed lines.
- `PenType`: Specifies the type of pen used for grid lines.
- `Width`: Sets the width of the grid line.

### Methods
- `SetStripLineProperties`: Configures the properties of a strip-line.

## Code Examples (multi-language supported)

### C# Example

```csharp
// Configuring strip-lines on the chart
ChartStripLine stripLine = new ChartStripLine();
stripLine.Start = 0;
stripLine.End = 100;
stripLine.StripLineBackGradient.EndColor = Color.Red;
chartControl1.PrimaryXAxis.StripLines.Add(stripLine);
```

### VB.NET Example

```vb.net
' Configuring strip-lines on the chart
Dim stripLine As New ChartStripLine()
stripLine.Start = 0
stripLine.End = 100
stripLine.StripLineBackGradient.EndColor = Color.Red
Me.chartControl1.PrimaryXAxis.StripLines.Add(stripLine)
```

## RAG Annotations

<!-- tags: [chart, strip-line, axis, grid-line, windows-forms] keywords: [gridlines, axis, strip lines, gradient, chart, dashboard, syncfusion] -->
```