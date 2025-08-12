```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_438.jpeg
document_name: chart
page_number: 438
page_id: chart#page_438
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:43:57Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates how to configure and use the `ShowSeriesTitle` property for pie, funnel, and pyramid charts.
- Explains how to access the `GetSeriesBounds` method for a series.

## Content

### Accessing Series Bounds

In both C# and VB.NET, you can access the bounds of a series in the ChartArea as follows:

#### C#

```csharp
this.chartControl1.ChartArea.GetSeriesBounds(series);
```

#### VB.NET

```vb.net
Me.chartControl1.ChartArea.GetSeriesBounds(series)
```

### Displaying Series Titles

The `ShowSeriesTitle` property is used to display the series name as a title for each section of pie, funnel, and pyramid charts in the divided area.

#### C#

```csharp
ChartSeries.ConfigItems.PieItem.ShowSeriesTitle = true;
ChartSeries.ConfigItems.FunnelItem.ShowSeriesTitle = true;
ChartSeries.ConfigItems.PyramidItem.ShowSeriesTitle = true;
```

#### VB.NET

```vb.net
ChartSeries.ConfigItems.PieItem.ShowSeriesTitle = True
ChartSeries.ConfigItems.FunnelItem.ShowSeriesTitle = True
ChartSeries.ConfigItems.PyramidItem.ShowSeriesTitle = True
```

### Sample Installation Location

A sample demonstrating the chart divide area support is available at the following location:

```plaintext
<sample installed location>\Syncfusion\EssentialStudio\<Version Number>\Windows\Chart.Windows\Samples\2.0\Chart Appearance\Chart Divide Area
```

### See Also
- [PieWithSameRadius](PieWithSameRadius)

## 4.8 Chart Legend and Legend Items

### Overview of Chart Legend

Essential Chart by default displays a legend with information on each series that has been plotted on the chart.

#### Key Points
- **Legend Visibility:** The legend provides an overview of all plotted series.
- **Customization Options:** Allows for adjusting the placement, style, and content of the legend.

### Example

```csharp
// Example of configuring the chart legend
Chart legendChart = new Chart();
Legend legend = new Legend();
legend.Position = new RectangleF(20, 20, 100, 100);
legend.Chart = legendChart;
legend.ShowSeriesLabels = true;
legend.ShowSeriesShape = true;
legendChart.Legends.Add(legend);
```

### Usage Context
- When integrating legends in your chart, ensure they are appropriately placed to avoid overlapping with data series.

## API Reference

### ChartArea Class
- **Method:** `GetSeriesBounds(Series series)`
  - **Description:** Retrieves the bounds of a specified series within the chart area.

### ChartSeries Class
- **Property:** `ConfigItems.PieItem.ShowSeriesTitle`
  - **Type:** `bool`
  - **Description:** Controls whether the pie series title is displayed.

### Legend Class
- **Property:** `ShowSeriesLabels`
  - **Type:** `bool`
  - **Description:** Determines if the labels for all series items are visible in the legend.

## Code Examples

### C# Example - Setting ShowSeriesTitle

```csharp
ChartSeries.ConfigItems.PieItem.ShowSeriesTitle = true;
ChartSeries.ConfigItems.FunnelItem.ShowSeriesTitle = true;
ChartSeries.ConfigItems.PyramidItem.ShowSeriesTitle = true;
```

### VB.NET Example - Setting ShowSeriesTitle

```vb.net
ChartSeries.ConfigItems.PieItem.ShowSeriesTitle = True
ChartSeries.ConfigItems.FunnelItem.ShowSeriesTitle = True
ChartSeries.ConfigItems.PyramidItem.ShowSeriesTitle = True
```

### Example - Configuring Chart Legend

```csharp
Legend legend = new Legend();
legend.Position = new RectangleF(20, 20, 100, 100);
legend.ShowSeriesLabels = true;
legendChart.Legends.Add(legend);
```

## RAG Annotations
<!-- tags: [syncfusion, winforms, chart, essential chart, legend, series, pie, funnel, pyramid, version] keywords: [chartcontrol1, getseriesbounds, showseriestitle, legendchart, showseriesshape, showserieslabels, showserieslabels, seriesconfiguration, dividedarea, pie item, funnel item, pyramid item, chart studio, winforms samples] -->
```