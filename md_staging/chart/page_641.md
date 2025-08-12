```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_641.jpeg
document_name: chart
page_number: 641
page_id: chart#page_641
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:55:00Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- This section demonstrates configuration and customization of chart controls in Windows Forms, focusing on axis ranges, transformations, and grayscale mode printing.
- Includes code examples for modifying axis ranges, enabling transformations, and configuring styles for grayscale printing.

## Content

### Configuring Axis Ranges
The following code snippet shows how to set the minimum, maximum, and interval values for the X-Axis of a chart control:

```vb
Me.chartControl1.ChartArea.PrimaryXAxis.Range.Min = mi
Me.chartControl1.ChartArea.PrimaryXAxis.Range.Max = mx
Me.chartControl1.ChartArea.PrimaryXAxis.Range.Interval = (Me.chartControl1.ChartArea.PrimaryXAxis.Range.Max - Me.chartControl1.ChartArea.PrimaryXAxis.Range.Min) / Me.chartControl1.ChartArea.PrimaryXAxis.Range.NumberOfIntervals
```

#### Modifying Maximum and Minimum Values
The code dynamically adjusts the maximum value (`mx`) and the minimum value (`mi`) based on user input:

```vb
mi = mx
mx = mx + Convert.ToDouble(textBox1.Text)
```

### Graphics Transformation for Chart Drawing
This section demonstrates the use of `BeginTransform`, `EndTransform`, and `transform` methods to ensure proper rendering:

```vb
Dim container As GraphicsContainer = BeginTransform(e.Graphics)
e.Graphics.ResetTransform()
Me.chartControl1.Draw(e.Graphics, e.MarginBounds)
EndTransform(e.Graphics, container)
```

#### Call the Draw Method to Draw the Chart
The `Draw` method is called with the current graphics object and margin bounds to render the chart.

### Grayscale Mode of Print
The code snippet below sets up grayscale mode for printing by modifying the chart series styles:

```vb
Dim tempStyles As ChartStyleInfo() = New ChartStyleInfo(Me.chartControl1.Series.Count - 1) {}
Dim ps As Array = System.[Enum].GetValues(GetType(PatternStyle))
Dim ds As Array = System.[Enum].GetValues(GetType(DashStyle))
For i As Integer = 0 To Me.chartControl1.Series.Count - 1
    tempStyles(i) = New ChartStyleInfo()
    tempStyles(i).CopyFrom(Me.chartControl1.Series(i).StylesImpl.Style)
    Me.chartControl1.Series(i).Style.Interior = New BrushInfo(DirectCast(ps.GetValue(i Mod ps.Length), PatternStyle), Color.Black, Color.White)
    Me.chartControl1.Series(i).Style.Border.MakeCopy(tempStyles(i), Me.chartControl1.Series(i).Style.Border.Sip)
    Me.chartControl1.Series(i).Style.Border.Color = Color.Black
    Me.chartControl1.Series(i).Style.Border.DashStyle = DirectCast(ds.GetValue(i Mod ds.Length), DashStyle)
```

### Checking the Chart Type
The code checks and applies specific styling based on the type of the chart series (e.g., Line, Spline, StepLine, RotatedSpline):

```vb
If Me.chartControl1.Series(i).Type = ChartSeriesType.Line OrElse
   Me.chartControl1.Series(i).Type = ChartSeriesType.Spline OrElse
   Me.chartControl1.Series(i).Type = ChartSeriesType.StepLine OrElse
   Me.chartControl1.Series(i).Type = ChartSeriesType.RotatedSpline Then
```

## API Reference

### Properties
- **Range.Min**: Sets the minimum value for the X-Axis.
- **Range.Max**: Sets the maximum value for the X-Axis.
- **Range.Interval**: Sets the interval between axis markings.
- **Series.Interior**: Configures the fill style for chart series.
- **Series.Border.Color**: Sets the color of the border for chart series.
- **Series.Border.DashStyle**: Configures the dash pattern for chart series borders.

### Methods
- **BeginTransform(Graphics)**: Begins a graphics transformation.
- **EndTransform(Graphics, GraphicsContainer)**: Ends a graphics transformation.
- **Draw(Graphics, Rectangle)**: Renders the chart in the specified graphics with the given rectangle bounds.

## Code Examples
#### Example 1: Setting Axis Ranges
```vb
Me.chartControl1.ChartArea.PrimaryXAxis.Range.Min = mi
Me.chartControl1.ChartArea.PrimaryXAxis.Range.Max = mx
Me.chartControl1.ChartArea.PrimaryXAxis.Range.Interval = (Me.chartControl1.ChartArea.PrimaryXAxis.Range.Max - Me.chartControl1.ChartArea.PrimaryXAxis.Range.Min) / Me.chartControl1.ChartArea.PrimaryXAxis.Range.NumberOfIntervals
```

#### Example 2: Grayscale Printing
```vb
Dim tempStyles As ChartStyleInfo() = New ChartStyleInfo(Me.chartControl1.Series.Count - 1) {}
Dim ps As Array = System.[Enum].GetValues(GetType(PatternStyle))
Dim ds As Array = System.[Enum].GetValues(GetType(DashStyle))
For i As Integer = 0 To Me.chartControl1.Series.Count - 1
    tempStyles(i) = New ChartStyleInfo()
    tempStyles(i).CopyFrom(Me.chartControl1.Series(i).StylesImpl.Style)
    Me.chartControl1.Series(i).Style.Interior = New BrushInfo(DirectCast(ps.GetValue(i Mod ps.Length), PatternStyle), Color.Black, Color.White)
    Me.chartControl1.Series(i).Style.Border.MakeCopy(tempStyles(i), Me.chartControl1.Series(i).Style.Border.Sip)
    Me.chartControl1.Series(i).Style.Border.Color = Color.Black
    Me.chartControl1.Series(i).Style.Border.DashStyle = DirectCast(ds.GetValue(i Mod ds.Length), DashStyle)
End If
```

<!-- tags: [chart, windows forms, range, transform, grayscale, graphics, series, stroke, fill] keywords: [range, interval, transform, grayscale, graphics, series, style] -->
```