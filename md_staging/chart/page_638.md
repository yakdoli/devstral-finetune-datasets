```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_638.jpeg
document_name: chart
page_number: 638
page_id: chart#page_638
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:57:35Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
foreach (Series sl in this.chartControl1.Series)
{
    if (sl.Style.Interior.GetGradientStops()[1] == Color.Black)
    {
        this.chartControl1.Series[i].Style.Interior = new BrushInfo((PatternStyle)ps.GetValue(i % ps.Length), Color.Black, Color.White);
        this.chartControl1.Series[i].Style.Border.Color = Color.Black;
    }
}

GraphicsContainer container = BeginTransform(e.Graphics);
e.Graphics.ResetTransform();

using (Image img = new Bitmap(e.MarginBounds.Width, e.MarginBounds.Height))
{
    using (Graphics g = Graphics.FromImage(img))
    {
        // Assigning the initial values of max and min to chartcontrol maximum and minimum values

        this.chartControl1.ChartArea.PrimaryXAxis.Range.Min = mi;
        this.chartControl1.ChartArea.PrimaryXAxis.Range.Max = mx;
        this.chartControl1.ChartArea.PrimaryXAxis.Range.Interval = (this.chartControl1.ChartArea.PrimaryXAxis.Range.Max - this.chartControl1.ChartArea.PrimaryXAxis.Range.Min) / this.chartControl1.ChartArea.PrimaryXAxis.Range.NumberOfIntervals;

        // Modifying the maximum and minimum values
        mi = mx;
        mx = mx + Convert.ToDouble(textBox1.Text);

        IntPtr hdc = g.GetHdc();
        Stream stream = new MemoryStream();
        Metafile mf = new Metafile(stream, hdc);

        // Call the Draw method to draw the chart
        this.chartControl1.Draw(mf, img.Size);
        DrawingUtils.DrawGrayedImage(e.Graphics, mf, e.MarginBounds, new Rectangle(Point.Empty, img.Size));
        g.ReleaseHdc(hdc);
        g.Dispose();
    }
}
```

## Overview
- The code snippet demonstrates the customization and rendering of a `ChartControl` in a Windows Forms application using Syncfusion's charting library.
- It involves setting interior and border styles for series, controlling axis properties such as range and interval, and handling image and graphics contexts for visualization.

## Content

### Chart Styling and Axis Configuration
- **Interior Style Customization**:
  - The `BrushInfo` is used to apply pattern styles, backgrounds, and gradients to the chart series.
  - The condition checks the interior gradient stop and applies a new `BrushInfo` if necessary.

- **Axis Range Adjustment**:
  - The `PrimaryXAxis.Range.Min` and `PrimaryXAxis.Range.Max` properties are set to define the axis range.
  - The interval is calculated dynamically based on the minimum and maximum values and the number of intervals.

### Image and Graphics Handling
- **Bitmap Creation**:
  - A `Bitmap` is created with the dimensions specified by `e.MarginBounds.Width` and `e.MarginBounds.Height`.
- **Graphics Context Management**:
  - `GraphicsContainer` is used to manage transformations and reset the graphics state.
  - The `GetHdc` and `ReleaseHdc` methods ensure proper handling of device contexts.
- **Chart Rendering**:
  - The `Draw` method of `ChartControl` is called to render the chart onto a `Metafile`.
  - The `DrawGrayedImage` method is used to render the chart onto the main graphics context with a gray effect.

## API Reference

### Classes and Methods
- **Syncfusion.Windows.Forms.Chart.ChartControl**
  - Methods:
    - `Draw(Metafile, Size)`
    - `SetStyle(SeriesStyle)`
    - `ChartArea.Property.Settings` (e.g., `PrimaryXAxis.Range`)

- **System.Drawing**
  - Classes:
    - `Graphics`
    - `Bitmap`
    - `Metafile`
    - `Stream`
  - Methods:
    - `Graphics.GetHdc()`
    - `Graphics.ReleaseHdc(IntPtr)`
    - `Bitmap.FromImage(Image)`
  
## Code Examples
The provided code snippet is an example of setting up a chart in a Windows Forms application, managing axis ranges, and rendering the chart with appropriate styles and effects.

## Page-level Navigation/TOC
- [Overview](#overview)
- [Content](#content)
  - [Chart Styling and Axis Configuration](#chart-styling-and-axis-configuration)
  - [Image and Graphics Handling](#image-and-graphics-handling)

## Cross References
- See also: [Syncfusion Documentation for ChartControl](https://help.syncfusion.com/windowsforms/chart),

<!-- tags: [chartcontrol, windowsforms, axisconfiguration, graphics, metafile, syncfusion] keywords: [chart customization, axis range, image handling, device context, drawing, winforms charting] -->
```