```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_622.jpeg
document_name: chart
page_number: 622
page_id: chart#page_622
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:56:35Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
Me.NewXValue(newX)
End If
Me.selectedDataPoint.Y = 0
Me.selectedDataPoint.X = 0
Me.isDragging = False
Me.currentRegion = Nothing
Me.ChartControl1.Redraw(True)
End If
Me.ChartControl1.Series(0).Style.TextFormat = "{0}"
Me.ChartControl1.Refresh()
End Sub
```

## 5.5 How to draw the Y-axis at the center of the X-axis

The y-axis can be drawn at any custom position using the `ChartAxisLocationType` class. This can be achieved by setting the value of the `LocationType` property of the `PrimaryYAxis` to `Set`.

### C#

```csharp
// Drawing Y-axis at the center of the X-axis.
this.chartControl1.PrimaryYAxis.LocationType = ChartAxisLocationType.Set;
this.chartControl1.PrimaryYAxis.Location = new PointF(300, 352);
```

### VB.NET

```vb
' Drawing Y-axis at the center of the X-axis.
Me.chartControl1.PrimaryYAxis.LocationType = ChartAxisLocationType.Set
Me.chartControl1.PrimaryYAxis.Location = New PointF(300, 352)
```

## 5.6 How to export the Chart Points into a CSV file

Creating a CSV (comma separated values) of the chart points simply involves parsing through the chart series and writing out the chart points into the FileStream. The code for this is provided below for your convenience.

### C#

```csharp
foreach (ChartSeries series in this.chartControl1.Series)
{
    string seriesName = series.Name;
```

## API Reference (if applicable)

## Code Examples (multi-language supported)

## Page-level Navigation/TOC (if applicable)

## Cross References

## RAG Annotations
<!-- tags: [Syncfusion, Winforms, chart, ChartAxisLocationType, CSV export, axis customization] keywords: [ChartAxisLocationType, PrimaryYAxis, LocationType, CSV, chart points, export] -->
```