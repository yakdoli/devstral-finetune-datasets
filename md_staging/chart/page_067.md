```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_067.jpeg
document_name: chart
page_number: 067
page_id: chart#page_067
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:19:19Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates how to bind a data source to a chart using the Chart Wizard.
- Focuses on improving chart performance by utilizing specific properties and methods.

## Content

### 4.3 Improving Performance

#### Properties and Methods used to improve chart performance

| **Chart control**                  | **Description**                                                                                     |
|------------------------------------|-----------------------------------------------------------------------------------------------------|
| **Property**                       | **ChartControl.ImprovePerformance**                                                                 |
|                                    | Instructions the chart to calculate the axes ranges only before painting and not at every series adding or moving. Performance of a Chart with a large number of series will be improved significantly, if this property is enabled. By default, this property is false. |

### Figure 41: Data Source bound to the Chart by using the Chart Wizard

![Data Source bound to the Chart by using the Chart Wizard](https://placehold.it/600x400)

## API Reference (if applicable)
- Namespace: `Syncfusion.Windows.Forms.Chart`
- Class: `ChartControl`

### Properties
- `ImprovePerformance`: A Boolean property that optimizes chart performance by calculating axis ranges only once during rendering.

## Code Examples (multi-language supported)

### C# Example
```csharp
using Syncfusion.Windows.Forms.Chart;

// Create ChartControl instance
ChartControl chart = new ChartControl();

// Enable performance improvement
chart.ImprovePerformance = true;
```

### VB.NET Example
```vbnet
Imports Syncfusion.Windows.Forms.Chart

' Create ChartControl instance
Dim chart As New ChartControl()

' Enable performance improvement
chart.ImprovePerformance = True
```

## Cross References
- See also: Chapter 4.2 on "Data Binding with Chart Wizard" for details on setting up data sources for charts.

<!-- tags: [Syncfusion, WinForms, ChartControl, Performance, ImprovePerformance, DataBinding] keywords: [chart, performance, data source, series, axes, rendering, C#, VB.NET] -->
```