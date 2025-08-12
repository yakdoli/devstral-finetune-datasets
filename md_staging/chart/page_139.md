```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_139.jpeg
document_name: chart
page_number: 139
page_id: chart#page_139
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:23:18Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Describes how to add a Renko series to a chart in Windows Forms.
- Demonstrates using C# and VB.NET code snippets.
- Lists customization options for the Renko series.

## Content

### Cannot be Combined with
| Cannot be Combined with | Pie, Bar |
| --- | --- |

Renko series can be added to the chart using the following code.

### C#

```csharp
// Create chart series and add data points into it.
ChartSeries series = this.chartControl1.Model.NewSeries("SeriesName", ChartSeriesType.Renko);
series.Points.Add(0, 1);
series.Points.Add(1, 3);
series.Points.Add(2, 4);
series.ReversalAmount = 1.0;

// Add the series to the chart series collection.
this.chartControl1.Series.Add(series);
```

### VB.NET

```vbnet
' Create chart series and add data points into it.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("SeriesName", ChartSeriesType.Renko)
series.Points.Add(0, 1)
series.Points.Add(1, 3)
series.Points.Add(2, 4)
series.ReversalAmount = 1.0

' Add the series to the chart series collection.
Me.chartControl1.Series.Add(series)
```

### Customization Options
- Border
- ColorsMode
- DarkLightPower
- DisplayShadow
- DisplayText
- DrawSeriesNameInDepth
- ElementBorders
- ImageIndex
- Images
- PriceDownColor
- PriceUpColor
- ReversalAmount
- Spacing Between Series
- ShadowInterior
- ShadowOffset
- ShadowOffset
- FancyToolTip
- Font
- Interior
- LegendItem
- Name
- PointsToolTipFormatSmartLabels
- Summary
- Text
- TextColor
- TextFormat
- TextOffset
- TextOrientation
- Visible

## API Reference
- Methods/Properties used:
  - `NewSeries`: Creates a new chart series.
  - `Points.Add`: Adds data points to the series.
  - `ReversalAmount`: Sets the reversal amount for the Renko series.
  - `Add`: Adds the series to the chart series collection.

## Code Examples (C# and VB.NET)
The provided code examples demonstrate how to create a Renko series and add it to a chart. The examples include setting data points and adjusting the `ReversalAmount` property.

## Cross References
- See also: Documentation on other chart series and customization options for Windows Forms.

<!-- tags: [chart, renko, windows forms, syncfusion, c#, vb.net] keywords: [renko series, chart series, windows forms, customization, data points, reversal amount] -->
```