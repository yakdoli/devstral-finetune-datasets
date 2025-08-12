```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_263.jpeg
document_name: chart
page_number: 263
page_id: chart#page_263
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:30:31Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- **Setting DataPoint label alignment in Funnel and Pyramid Charts.**
- **Code examples in both C# and VB.NET for configuring `LabelPlacement`.**
- **Functional details** about how DataPoint labels are aligned within Pyramid segments.

## Content

### LabelPlacement Configuration for Pyramid Charts

| **Attribute**               | **Description**                                                                                                   |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------|
|                               | - **Bottom** – DataPoint labels are aligned to the bottom of the Pyramid segment.                                |
|                               | - **Left** - DataPoint labels are aligned to the Left of the Pyramid segment.                                   |
|                               | - **Right** - DataPoint labels are aligned to the Right of the Pyramid segment.                                 |
| Default Value                | Right                                                                                                           |
| 2D / 3D Limitations         | No                                                                                                              |
| Applies to Chart Element    | Any Series                                                                                                      |
| Applies to Chart Types      | Funnel and Pyramid Charts                                                                                       |

### Code Snippet for LabelPlacement in Pyramid Chart

#### [C#]
```csharp
this.chartControl1.Series[0].ConfigItems.PyramidItem.LabelPlacement = ChartAccumulationLabelPlacement.Center;
```

#### [VB.NET]
```vb
Me.chartControl1.Series(0).ConfigItems.PyramidItem.LabelPlacement = ChartAccumulationLabelPlacement.Center
```

<!-- tags: [windows-forms, charts, label-placement, pyramid-chart, funnel-chart, label-alignment, essential-charts, syncfusion] keywords: [chartcontrol, datapoint, labelplacement, alignment, center, bottom, left, right, series, funnel, pyramid, code-examples, csharp, vb.net] -->
```