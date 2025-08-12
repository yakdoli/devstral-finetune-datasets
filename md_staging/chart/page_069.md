<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_069.jpeg
document_name: chart
page_number: 069
page_id: chart#page_069
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:19:55Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Describes properties and methods to improve performance for chart components.
- Focus on optimizing chart rendering and initialization speed.

## Content

### Chart Properties
| Property | Description |
| --- | --- |
| ChartArea.BackInterior | This property sets the back color for the chart area. If not set with gradient or pattern style, will help improve the performance of the chart. |
| ChartInterior | If this property which fills the chart interior, not set with gradient or pattern style, will improve the performance of the chart. |

### Method
| Method | Description |
| --- | --- |
| BeginUpdate and EndUpdate | Encapsulate your "data points adding code" within `BeginUpdate` and `EndUpdate` to improve Chart initialization speed. See the example below. |

## Code Examples
```csharp
[C#]
// Improves the performance of the chart when a large number of series are used.
this.chartControl1.ImprovePerformance = true;

this.chartControl1.CalcRegions = false;

this.chartControl1.Series[0].EnableStyles = false;

this.chartControl1.Series[0].Style.DisplayShadow = false;

this.chartControl1.Indexed = true;

// BeginUpdate and EndUpdate methods
private DataModel datamodel1;
ChartSeries series = this.chartControl1.Model.NewSeries("Line 1", ChartSeriesType.Line);

this.chartControl1.BeginUpdate();

// Add a whole bunch of points to the series like this:
series.Points.Add(1, 10), etc.
```

## Page-level Navigation/TOC (if applicable)
- Chart Properties
- Method
- Code Examples

## Cross References
- Refer to the official Syncfusion documentation for detailed usage and examples.

<!-- tags: [product, module, control, api, version?] keywords: [chart, chart area, chart interior, beginupdate, endupdate, performance optimization, winforms, syncfusion] -->