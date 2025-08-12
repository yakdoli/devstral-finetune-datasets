```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_378.jpeg
document_name: chart
page_number: 378
page_id: chart#page_378
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:39:41Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- The page demonstrates how to handle empty data points in a chart by creating gaps in the chart when certain data points are set to empty values.

## Content

### Displaying Gaps for Empty Points
The chart in Figure 244 shows how setting specific data points as empty can create visual gaps in the chart.

#### Figure: 4th, 5th and 6th Data Points set as Empty Points
![](image.png)  
*Figure 244: 4th, 5th and 6th Data Points set as Empty Points*

This figure illustrates a bar chart where the 4th, 5th, and 6th data points are explicitly defined as empty, resulting in gaps in the chart series.

### Implementation in C#
To achieve this behavior in C#, the following code can be used:

```csharp
this.chartControl1.Indexed = true;
this.chartControl1.AllowGapForEmptyPoints = true;
```

### Implementation in VB.NET
For VB.NET, the equivalent code is as follows:

```vb
Me.chartControl1.Indexed = True
Me.chartControl1.AllowGapForEmptyPoints = True
```

## Notes
- The `Indexed` property ensures that the chart is indexed, which is necessary for displaying gaps where data points are empty.
- The `AllowGapForEmptyPoints` property is set to `true` to enable the chart to create gaps for empty data points.

## RAG Annotations
<!-- tags: [Syncfusion Winforms, Chart, Empty Points, Indexed, Allow Gap for Empty Points] keywords: [chart, empty data points, indexed, data gaps, visual representation, Syncfusion, Winforms] -->
```