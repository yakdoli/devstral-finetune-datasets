```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_156.jpeg
document_name: chart
page_number: 156
page_id: chart#page_156
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:25:35Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Explains the configuration and usage of combination charts in Windows Forms.
- Details adding series to the chart, specifically using the C# and VB.NET code snippets.
- Outlines the properties and features of heat map charts in Syncfusion Winforms.

## Content

### Description of Combination Charts

The following table defines the essential properties of combination charts:

| Number of Y values per point | 2 |
| --- | --- |
| Number of Series | One. |
| Cannot be Combined with | Any other chart types. |

### Adding Combination Series

Combination series can be added to the chart using the following code.

#### C#
```csharp
ChartSeries Stocks = new ChartSeries("Stocks", 
    ChartSeriesType.HeatMap);
Stocks.Points.Add(7, 4, 10000);
Stocks.Points.Add(6, 3, 5541);
Stocks.Points.Add(5, 2, 6007);
Stocks.Points.Add(4, 2, 5022);
Stocks.Points.Add(3, 2.5, 6882);
Stocks.Points.Add(2, 1.5, 6584);
Stocks.Points.Add(1, 1, 2799);
this.chartControl1.Series.Add(Stocks);
```

#### VB.NET
```vb
Dim Stocks As ChartSeries = Me.chartControl1.Model.NewSeries("Stocks", 
    ChartSeriesType.Line)
Stocks.Points.Add(7, 4, 10000)
Stocks.Points.Add(6, 3, 5541)
Stocks.Points.Add(5, 2, 6007)
Stocks.Points.Add(4, 2, 5022)
Stocks.Points.Add(3, 2.5, 6882)
Stocks.Points.Add(2, 1.5, 6584)
Stocks.Points.Add(1, 1, 2799)

' Add the series to the chart series collection.
Me.chartControl1.Series.Add(Stocks)
```

### Features

The following table lists the properties of heat map chart with descriptions.

#### Properties and Descriptions of Heat Map Charts
| Property          | Description |
| ---               | ---         |
| HeatMapStyle      | Specifies styles of heat maps. The types are Rectangular, Vertical and Horizontal styles. |

## API Reference

### HeatMapStyle Property
- Specifies styles of heat maps.
- Types: Rectangular, Vertical, and Horizontal styles.

## Code Examples

### C#
```csharp
this.chartControl1.Series.Add(Stocks);
```

### VB.NET
```vb
Me.chartControl1.Series.Add(Stocks)
```

## Cross References
- See also: "Features of Chart Types in Windows Forms," "Interactive Elements in Charts."

<!-- tags: [Syncfusion Winforms, Chart, HeatMapStyle, CombinationSeries, EssentialChart] keywords: [C#, VB.NET, series, chartControl, properties, HeatMapStyle, chart series] -->
```