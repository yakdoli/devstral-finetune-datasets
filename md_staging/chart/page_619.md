<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_619.jpeg
document_name: chart
page_number: 619
page_id: chart#page_619
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:51:43Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

Using the `SeriesModelImpl` property, you can set an instance of the `IChartSeriesModel`, underlying the series. Use this property to replace the instance with our own implementation.

## Customizing Data Points using IChartSeriesModel Interface

### C#

```csharp
// Customize data points using IChartSeriesModel interface.
series1.SeriesModelImpl = new NonIndexedModel(new double[] { 2, 5, 3, 4, 6 }, new double[] { 10, 33, 20, 43, 12 });
```

### VB.NET

```vb
' Customize data points using IChartSeriesModel interface.
series1.SeriesModelImpl = New NonIndexedModel(New Double() { 2, 5, 3, 4, 6 }, New Double() { 10, 33, 20, 43, 12 })
```

## 5.3 How to display custom tooltip over Histogram Chart columns

On Setting `ShowTooltip` property to `true`, the series name will be displayed as tooltip on the histogram chart columns by default. You can also set custom tooltip by handling `ChartRegionMouseMove` event as follows.

### C#

```csharp
private void chartControl1_ChartRegionMouseMove(object sender, ChartRegionMouseEventArgs e)
{
    string text = null;
    if (e.Region.IsChartPoint)
    {
        e.Region.ToolTip = "Tooltip " + e.Region.PointIndex.ToString();
    }
    else
    {
        text = "Not a chart Point";
    }
}
```

### VB.NET

```vb
Private Sub chartControl1_ChartRegionMouseMove(ByVal sender As Object, ByVal e As ChartRegionMouseEventArgs)
```

## Page-level Navigation/TOC (if applicable)

- Essential Chart for Windows Forms
  - 5.3 How to display custom tooltip over Histogram Chart columns

## Cross References

- See also: [IChartSeriesModel](#reference-link), [NonIndexedModel](#reference-link), [ChartRegionMouseMove](#reference-link)

<!-- tags: [chart, series, tooltip, histogram, events, windows forms, syncfusion] keywords: [seriesmodelimpl, icchartsersmodel, nonindexedmodel, chartregionmousemove, custom tooltip, histogram chart] -->