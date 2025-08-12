```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_637.jpeg
document_name: chart
page_number: 637
page_id: chart#page_637
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:54:41Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates adjusting maximum and minimum values for charting.
- Provides instructions for Grayscale mode printing of charts.

## Content

### Modifying Maximum and Minimum Values
The following code snippet modifies the maximum and minimum values for charting in a `GraphicsContainer`. The `GraphicsContainer` is used to manage transformations while drawing the chart.

```csharp
// Modifying the maximum and minimum values
mi = mx;
mx = mx + Convert.ToDouble(textBox1.Text);
GraphicsContainer container = BeginTransform(e.Graphics);
e.Graphics.ResetTransform();
// Call the Draw method to draw the chart
this.chartControl1.Draw(e.Graphics, e.MarginBounds);
EndTransform(e.Graphics, container);
}
```

### Grayscale Mode of Print
The following section enables Grayscale mode for printing charts, adjusting style information and ensuring that the chart is rendered in black and white.

```csharp
// For Grayscale mode of print
else if (grayScale)
{
    ChartStyleInfo[] tempStyles = new ChartStyleInfo[this.chartControl1.Series.Count];
    Array ps = System.Enum.GetValues(typeof(PatternStyle));
    Array ds = System.Enum.GetValues(typeof(DashStyle));
    for (int i = 0; i < this.chartControl1.Series.Count; i++)
    {
        tempStyles[i] = new ChartStyleInfo();
        tempStyles[i].CopyFrom(this.chartControl1.Series[i].StylesImpl.Style);
        this.chartControl1.Series[i].Style.Interior = new BrushInfo((PatternStyle)ps.GetValue(i % ps.Length), Color.Black, Color.White);
        this.chartControl1.Series[i].Style.Border.MakeCopy(tempStyles[i], this.chartControl1.Series[i].Style.Border.Sip);
        this.chartControl1.Series[i].Style.Border.Color = Color.Black;
        this.chartControl1.Series[i].Style.Border.DashStyle = (DashStyle)ds.GetValue(i % ds.Length);

        // Checking the chart type
        if (this.chartControl1.Series[i].Type == ChartSeriesType.Line || 
            this.chartControl1.Series[i].Type == ChartSeriesType.Spline || 
            this.chartControl1.Series[i].Type == ChartSeriesType.StepLine || 
            this.chartControl1.Series[i].Type == ChartSeriesType.RotatedSpline)
        {
            this.chartControl1.Series[i].Style.Interior = new BrushInfo((PatternStyle)ps.GetValue(i % ps.Length), Color.White, Color.Black);
            if (this.chartControl1.Series3D || this.chartControl1.ChartInterior.BackColor
```

## API Reference
### Namespaces and Classes
- `System.Enum`
- `ChartStyleInfo`
- `BrushInfo`
- `ChartSeriesType`
- `PatternStyle`
- `DashStyle`

### Methods and Properties
- `BeginTransform(e.Graphics)`
- `EndTransform(e.Graphics, container)`
- `Draw(e.Graphics, e.MarginBounds)`
- `StylesImpl.Style`
- `Style.Interior`
- `Style.Border.Color`
- `Style.Border.DashStyle`
- `Series.Type`
- `ChartInterior.BackColor`

<!-- tags: [Syncfusion, Winforms, Chart, GraphicsContainer, Grayscale, Print, API, Version 11.4.0.26] keywords: [maximum, minimum, values, chartControl1, Draw, BeginTransform, EndTransform, Grayscale, black and white, PatternStyle, DashStyle, Series, Interior, Border, Color, ChartSeriesType] -->
```