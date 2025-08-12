<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_264.jpeg
document_name: chart
page_number: 264
page_id: chart#page_264
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:32:14Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- This page demonstrates the use of `LabelPlacement` in a Funnel Chart for proper label alignment within the chart.

## Content

### Label Placement in Funnel Chart

#### Figure: ChartAccumulationLabelPlacement as Center

![](https://raw.githubusercontent.com/nesympathy/unclear-images/master/syncfusion-page_264-chart.png)
**Figure 155: ChartAccumulationLabelPlacement as Center**

Here is the code snippet using `LabelPlacement` in Funnel Chart.

#### [C#]

```csharp
this.chartControl1.Series[0].ConfigItems.FunnelItem.LabelPlacement = ChartAccumulationLabelPlacement.Center;
```

#### [VB.NET]

```vb
Me.chartControl1.Series(0).ConfigItems.FunnelItem.LabelPlacement = ChartAccumulationLabelPlacement.Center
```

## RAG Annotations
<!-- tags: [chart, funnel chart, label placement, windows forms, syncfusion winforms, version-11.4.0.26] keywords: [chartAccumulationLabelPlacement, center placement, funnels, series configuration, visual alignment] -->