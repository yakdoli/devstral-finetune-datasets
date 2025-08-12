```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_607.jpeg
document_name: chart
page_number: 607
page_id: chart#page_607
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:50:59Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Explains the properties and events related to `SeriesIndex`, `PointIndex`, `Region`, and `ToolTip` in Syncfusion Winforms where these regions represent specific points on a chart.
- Describes handling user interaction events such as `ChartRegionDoubleClick` and `ChartRegionMouseDown`.

## Content

| Property        | Description                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------|
| SeriesIndex     | The index into the `Series` array of the Chart in which this point occurs. If the Type is `SeriesPoint`. |
| PointIndex      | The index into the `Points` array of the ChartSeries in which this point occurs. If the Type is `SeriesPoint`. |
| Region          | The client region that represents this logical region.                                           |
| ToolTip         | Specifies the tooltip for this region.                                                         |

### ChartRegionDoubleClick and ChartRegionMouseDown Events

These events are used to handle different types of user interactions with regions on the chart.

## API Reference

### Properties

- `SeriesIndex`
- `PointIndex`
- `Region`
- `ToolTip`

### Events

- `ChartRegionDoubleClick`
- `ChartRegionMouseDown`

## Code Examples

### C# Example

```csharp
// Example of handling ChartRegionDoubleClick event
chart.ChartRegionDoubleClick += (sender, args) =>
{
    if (args.Type == ChartRegionClickEventArgs.RegionType.SeriesPoint)
    {
        MessageBox.Show($"Point: {args.PointIndex}");
    }
};
```

<!-- tags: [winforms, chart, series, point, tooltip, event] keywords: [syncfusion, chartregiondoubleclick, chartregionmousedown, seriesindex, pointindex, region, tooltip] -->
```