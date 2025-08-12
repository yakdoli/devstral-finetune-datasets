```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_312.jpeg
document_name: chart
page_number: 312
page_id: chart#page_312
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:34:43Z
fidelity: lossless
-->  

## Chart Shadow Interior Configuration

### Overview

- Specifies the interior color of the shadow in a chart.
- Allows customization of shadow appearance for various chart elements and types.
- Supports multiple chart types and series.

---

## Content

### Details

| **Aspect**               | **Description**                   |
|--------------------------|------------------------------------|
| Possible Values          | Any valid Color format            |
| Default Value            | Black                             |
| 2D / 3D Limitations     | 2D only                           |
| Applies to Chart Element | Any Series                        |
| Applies to Chart Types   | Column Charts, Bubble Chart, Line Charts, BarCharts, Candle Chart, Kagi Chart, Point and Figure Chart, Renko Chart, Three Line Break Chart, Box and Whisker Chart, Gantt Chart, Histogram Chart, Tornado Chart, Pie Chart, Polar and Radar Chart, Area Chart, Step Area Chart |

### Sample Code Snippet Using ShadowInterior in Column Chart

#### Series Wide Setting

[C#]

```csharp
// Specifying Shadow Interior for 2 series
this.chartControl1.Series[0].Style.DisplayShadow = true;
this.chartControl1.Series[0].Style.ShadowInterior = new
BrushInfo(GradientStyle.None, Color.SteelBlue, Color.SteelBlue);
```

[VB.NET]

```vbnet
' Specifying Shadow Interior for 2 series
Private Me.chartControl1.Series(0).Style.DisplayShadow = True
Private Me.chartControl1.Series(0).Style.ShadowInterior = New
BrushInfo(GradientStyle.None, Color.SteelBlue, Color.SteelBlue)
```

---

## API Reference

### Members

- **DisplayShadow**: Property to control the visibility of the shadow.
- **ShadowInterior**: Property to set the interior color of the shadow, accepting a `BrushInfo` object.

### Parameters

| Name           | Type         | Description                                                                 | Default  |
|----------------|--------------|-----------------------------------------------------------------------------|----------|
| GradientStyle  | GradientStyle | Specifies the gradient style for the shadow.                             | None     |
| StartColor     | Color        | Specifies the starting color for the gradient.                           | SteelBlue |
| EndColor       | Color        | Specifies the ending color for the gradient.                             | SteelBlue |

---

## Code Examples

#### C# Example

```csharp
using Syncfusion.Windows.Forms.Chart;

// Create a new chart
ChartControl chart = new ChartControl();
chart.Dock = DockStyle.Fill;

// Add a series
Series series = new Series();
series.Name = "Sample Series";
series.ChartType = ChartType.Column;
series.Points.Add(new PointData(1, 20));
series.Points.Add(new PointData(2, 30));
series.Points.Add(new PointData(3, 40));

// Configure shadow interior
series.Style.DisplayShadow = true;
series.Style.ShadowInterior = new BrushInfo(GradientStyle.None, Color.SteelBlue, Color.SteelBlue);

// Add the series to the chart
chart.PrimaryXAxis.Minimum = 0;
chart.PrimaryXAxis.Maximum = 4;
chart.Series.Add(series);
```

#### VB.NET Example

```vbnet
Imports Syncfusion.Windows.Forms.Chart

' Create a new chart
Dim chart As New ChartControl()
chart.Dock = DockStyle.Fill

' Add a series
Dim series As New Series()
series.Name = "Sample Series"
series.ChartType = ChartType.Column
series.Points.Add(New PointData(1, 20))
series.Points.Add(New PointData(2, 30))
series.Points.Add(New PointData(3, 40))

' Configure shadow interior
series.Style.DisplayShadow = True
series.Style.ShadowInterior = New BrushInfo(GradientStyle.None, Color.SteelBlue, Color.SteelBlue)

' Add the series to the chart
chart.PrimaryXAxis.Minimum = 0
chart.PrimaryXAxis.Maximum = 4
chart.Series.Add(series)
```

---

## RAG Annotations

<!-- tags: [Chart, ShadowInterior, DisplayShadow, BrushInfo] keywords: [Essential Chart for Windows Forms, Shadow, Interior Color, Gradient Style, Chart Types, Series] -->
```