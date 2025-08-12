```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_075.jpeg
document_name: chart
page_number: 075
page_id: chart#page_075
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:19:49Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Chart Series Overview

This section provides an overview of creating and customizing chart series, specifically focusing on Spline Series in Syncfusion Winforms.

### Spline Series Example

#### Chart Details

The following chart (Figure 43) illustrates a Spline Series for monitoring server load:

**Figure 43: Chart displaying a Spline Series**

![Daily Server Load Chart](image)

- **Legend Entries**: 
  - Server 1 (Blue)
  - Server 2 (Orange)

- **Axes**:
  - Y-axis: Server Load (MB) ranging from 0 to 500.
  - X-axis: Time intervals from 0 to 80.

### Chart Details

The table below outlines the details of the Spline Series:

| Details                   | Description                                   |
|---------------------------|-----------------------------------------------|
| Number of Y values per point | 1.                                         |
| Number of Series           | One or More.                                |
| Cannot be Combined with    | Pie, Bar, Stacked Bar, Polar, Radar.       |

### Adding Spline Series to the Chart

Spline series can be added to the chart using the following C# code:

```csharp
// Create chart series and add data points into it.
ChartSeries series = this.chartControl.Model.NewSeries("Series Name", ChartSeriesType.Spline);
series.Points.Add(0, 2);
series.Points.Add(1, 3);
series.Points.Add(2, 1);
series.Points.Add(3, 1.5);
series.Points.Add(4, 4);
```

### Summary
This documentation explains how to use Spline Series in a Windows Forms application with Syncfusion's chart control. By leveraging the provided code and details, users can effectively monitor and visualize trends in data series such as server loads.

## RAG Annotations
<!-- tags: [Syncfusion, Winforms, Chart, Spline Series] keywords: [Spline Series, Chart, Server Load, Daily, Windows Forms, Data Series] -->
```