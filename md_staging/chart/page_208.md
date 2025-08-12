```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_208.jpeg
document_name: chart
page_number: 208
page_id: chart#page_208
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:29:05Z
fidelity: lossless
-->

## ErrorBar Orientation

**Figure 117: Line Chart with ErrorBars and ErrorBarsSymbolShape="Diamond"**

### ErrorBar Orientation

Orientation of the ErrorBars can be specified in the `ErrorBars.Orientation` property. It can be `Vertical` or `Horizontal`.

#### Example Code in C#

```csharp
// Creates a New Series
ChartSeries s1 = new ChartSeries("series");

// Points for the Series
s1.Points.Add(10, new double[] { 20, 2, 2 });
s1.Points.Add(20, new double[] { 70, 2, 2 });
s1.Points.Add(30, new double[] { 10, 2, 2 });
s1.Points.Add(40, new double[] { 40, 2, 2 });
s1.Points.Add(40, new double[] { 40, 2, 2 });
s1.Text = s1.Name;

// Type of Series
s1.Type = ChartSeriesType.Line;
s1.ConfigItems.ErrorBars.Enabled = true;

// Set the orientation to horizontal
s1.ConfigItems.ErrorBars.Orientation = ChartOrientation.Horizontal;
s1.ConfigItems.ErrorBars.SymbolShape = ChartSymbolShape.None;

s1.Style.Interior = new Syncfusion.Drawing.BrushInfo(Color.Red);
this.chartControl1.PrimaryXAxis.DrawGrid = false;
this.chartControl1.PrimaryYAxis.DrawGrid = false;

this.chartControl1.Series.Add(s1);
```

#### Example Code in VB.NET

```vb
' Creates a New Series
Dim s1 As New ChartSeries("series")

' Points for the Series
s1.Points.Add(10, New Double() { 20, 2, 2 })
s1.Points.Add(20, New Double() { 70, 2, 2 })
s1.Points.Add(30, New Double() { 10, 2, 2 })
s1.Points.Add(40, New Double() { 40, 2, 2 })
s1.Points.Add(40, New Double() { 40, 2, 2 })
s1.Text = s1.Name
```

### Notes

- The `ErrorBars.SymbolShape` property is set to `None` in the example, but it can be set to other shapes as needed.
- The `ErrorBars.Orientation` property determines whether the error bars are displayed vertically or horizontally.

<!-- tags: [chart, errorbars, orientation, symbolshape, winforms, syncfusion] keywords: [error bars, vertical, horizontal, series, chart control, grid, chartorientation, chartsymbolshape] -->
```