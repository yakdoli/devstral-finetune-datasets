```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_509.jpeg
document_name: chart
page_number: 509
page_id: chart#page_509
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:46:10Z
fidelity: lossless
 -->

# Essential Chart for Windows Forms

## Overview
- Explains how to perform custom drawing on a chart using the ChartAreaPaint event.
- Demonstrates rendering geometric shapes such as arrows at the ends of the X and Y axes, and a horizontal line through the center of the chart.

## Content

### 4.10.6 Custom Drawing

Essential Chart allows you to render any data on the chart area. If the built-in features and functionality are not sufficient, you can simply draw whatever you want on the chart surface.

You can do so by listening to the `ChartAreaPaint` event. This event is raised both when a chart is painted as well as when the chart is exported to other image formats, such as SVG, etc. Remember to do your custom drawing in this event instead of in the `Paint` event (which will not be called during chart export).

#### Code Example

```csharp
[C#]

private void chartControl1_ChartAreaPaint(object sender, PaintEventArgs e)
{
    // Get the right end of the X axis
    Point ptX = this.chartControl1.ChartArea.GetPointByValue(new ChartPoint(this.chartControl1.PrimaryXAxis.Range.Max, this.chartControl1.PrimaryYAxis.Range.Min));

    PointF ptX1 = new PointF(ptX.X - 7, ptX.Y - 4);
    PointF ptX2 = new PointF(ptX.X, ptX.Y);
    PointF ptX3 = new PointF(ptX.X - 7, ptX.Y + 4);

    // Draws an arrow at the end of the X axis
    e.Graphics.FillPolygon(Brushes.Black, new PointF[] { ptX1, ptX2, ptX3 });

    // Get the top end of the Y axis
    Point ptY = this.chartControl1.ChartArea.GetPointByValue(new ChartPoint(this.chartControl1.PrimaryXAxis.Range.Min, this.chartControl1.PrimaryYAxis.Range.Max));

    PointF ptY1 = new PointF(ptY.X - 4, ptY.Y + 7);
    PointF ptY2 = new PointF(ptY.X, ptY.Y);
    PointF ptY3 = new PointF(ptY.X + 4, ptY.Y + 7);

    // Draws an arrow at the top of the Y Axis.
    e.Graphics.FillPolygon(Brushes.Black, new PointF[] { ptY1, ptY2, ptY3 });

    // Draws a line through the center of the chart.
    e.Graphics.DrawLine(Pens.Gray, ptY.X, ptX.Y, ptX.X, ptY.Y);
}
```

## API Reference
- `ChartAreaPaint` event: Triggered when a chart is painted or exported.
- `ChartArea.GetPointByValue`: Method to obtain the screen coordinates corresponding to a point on the chart area.

## Code Examples
The provided C# code demonstrates how to draw custom shapes on a chart using the `ChartAreaPaint` event. The example:
- Determines the right end of the X axis and the top end of the Y axis.
- Draws arrows at these ends using `FillPolygon`.
- Draws a line through the center of the chart using `DrawLine`.

## Cross References
- For more detailed information, refer to the Essential Chart documentation for Windows Forms.

<!-- tags: [winforms, essential chart, custom drawing, chartareapaint] keywords: [custom drawing, chart area, ChartAreaPaint, WinForms, Syncfusion] -->
```