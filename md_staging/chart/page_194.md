```<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_194.jpeg
document_name: chart
page_number: 194
page_id: chart#page_194
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:27:07Z
fidelity: lossless
--># Essential Chart for Windows Forms

## Overview
- Describes how to customize column types in various chart types.
- Includes code samples for configuring column types in C# and VB.NET.
- Provides an example of a Column Chart with different column types.

## Content

### Applies to Chart Types

| Chart Types                          | Column Chart, Column Range Chart, Stacking Column Chart, Candle Chart, Bar Chart, Stacking Bar Chart |
|--------------------------------------|-----------------------------------------------------------------------------------------------|

Here is some sample.

#### C# Code Example

```csharp
this.chartControl1.Series[0].ConfigItems.ColumnHeader.ColumnType = ChartColumnType.Cylinder;
this.chartControl1.Series[1].ConfigItems.ColumnHeader.ColumnType = ChartColumnType.Box;
```

#### VB.NET Code Example

```vbnet
Me.chartControl1.Series(0).ConfigItems.ColumnHeader.ColumnType = ChartColumnType.Cylinder
Me.chartControl1.Series(1).ConfigItems.ColumnHeader.ColumnType = ChartColumnType.Box
```

### Column Chart Example

![Sales Volume Comparison](https://example.com/sales-volume-comparison.png)

**Figure 107: Column Chart**

This figure shows a comparison of sales volumes over several years, using different column types for visualization.

## See Also
- Column Chart
- Column Range Chart
- Stacking Column Chart
- Candle Chart
- Bar Chart
- Stacking Bar Chart

## Page-level Metadata
- All content is © 2013 Syncfusion. All rights reserved.

<!-- tags: [Syncfusion Winforms, Chart, ColumnChart, StackingColumnChart, CandleChart, BarChart, StackingBarChart, ChartTypes] keywords: [Customizing Column Types, C#, VB.NET, Column Range Chart, Stack Chart, Candle Chart, Bar Chart, Stacking Bar Chart] -->
```