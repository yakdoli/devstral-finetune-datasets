```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_173.jpeg
document_name: chart
page_number: 173
page_id: chart#page_173
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:26:07Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- A comprehensive list of chart properties and their applicability to different chart types in Windows Forms.
- Details on chart series customization, like styling, highlighting, and advanced chart-specific features.
- Insights into configuring various chart types such as Polar, Radar, Bubble, Column, Line, HiLo, Pie, Doughnut, Funnel, Pyramid, Gantt, and more.

## Content

### Chart Series Properties

| Property | Applies To | Description |
|----------|------------|-------------|
| EnablePhongStyle | Series | Bubble Chart. |
| ErrorBarsSymbolShape | Series | Column Chart, Line Chart, and HiLo Chart. |
| ExplodedAll | Series | Pie Chart, Doughnut Chart. |
| ExplodedIndex | Series | Pie Chart. |
| ExplosionOffset | Series | Pie Chart. |
| FancyToolTip | Series | All Chart Types. |
| FigureBase | Series | Funnel and Pyramid Chart. |
| FillMode | Series | Pie Chart. |
| FunnelMode | Series | Funnel and Pyramid Chart. |
| Font | Series and points | All Chart types. |
| GanttDrawMode | Series | Gantt Chart. |
| GapRatio | Series | Funnel and Pyramid Chart. |
| Gradient | Series | Pie Chart. |
| HeightBox | Series | Point And Figure Chart. |
| HeightByAreaDepth | Series | Pie Chart. |
| HeightCoefficient | Series | Pie Chart. |
| HighlightInterior | Series | Bar Charts, Pie, Funnel, Pyramid, Bubble, Column, Area, Stacking Area, Stacking Area100, Line Charts, Box and Whisker, Gantt Chart, and Tornado Chart. |
| HitTestRadius | Series | Line Chart and Step Line Chart. |
| ImageIndex | Series and points | Area Charts, Bar Charts, Bubble Chart, Column Charts, Line Charts, Candle Chart, |

## API Reference

### Namespace: Syncfusion.Windows.Forms.Chart

#### Members:
- **EnablePhongStyle**: Controls the phong style for Bubble Chart.
- **ErrorBarsSymbolShape**: Define symbol shapes for Error Bars in Column, Line, and HiLo Chart.
- **ExplodedAll**: Set all slices in Pie Chart or Doughnut Chart to be exploded.
- **ExplodedIndex**: Specify an index for exploding a particular slice in Pie Chart.
- **ExplosionOffset**: Control the explosion offset for Pie Chart slices.
- **FancyToolTip**: Enable fancy tooltips for all chart types.
- **FigureBase**: Configure base settings for Funnel and Pyramid Chart.
- **FillMode**: Configure fill mode for Pie Chart.
- **FunnelMode**: Configure funnel and pyramid mode for Funnel and Pyramid Chart.
- **Font**: Set font for series and points across all chart types.
- **GanttDrawMode**: Configure drawing mode for Gantt Chart.
- **GapRatio**: Define gap ratio for Funnel and Pyramid Chart.
- **Gradient**: Set gradient for Pie Chart.
- **HeightBox**: Configure height ratio for Point And Figure Chart.
- **HeightByAreaDepth**: Configure height by area depth for Pie Chart.
- **HeightCoefficient**: Configure height coefficient for Pie Chart.
- **HighlightInterior**: Configure interior highlighting for various charts including Bar, Pie, Funnel, Pyramid, Bubble, Column, Area, Stacking Area, Stacking Area100, Line, Box and Whisker, Gantt Chart, and Tornado Chart.
- **HitTestRadius**: Configure hit test radius for Line and Step Line Chart.
- **ImageIndex**: Set image index for Area, Bar, Bubble, Column, Line, and Candle Chart.

## Code Examples

### Example: Using the FillMode Property
```csharp
// Configure FillMode for Pie Chart
chart.Series[0].FillMode = FillMode.None;
```

### Example: Highlighting the Interior of a Bar Chart
```csharp
// Configure HighlightInterior for Bar Chart
chart.Series[0].HighlightInterior = HighlightInterior.Middle;
```

### Example: Setting HitTestRadius for Line Chart
```csharp
// Configure HitTestRadius for Line Chart
chart.Series[0].HitTestRadius = 5;
```

## Cross References
- For more details on configuring specific chart types, refer to the individual chart type documentation sections.
- To understand advanced styling options, see the Chart Styling Guide.

<!-- tags: [syncfusion winforms, chart, series, styling, chart types] keywords: [chart properties, pie chart, doughnut chart, funnel chart, pyramid chart, gantt chart, stacking area chart, tornado chart] -->
```