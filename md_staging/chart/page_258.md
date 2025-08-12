```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_258.jpeg
document_name: chart
page_number: 258
page_id: chart#page_258
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:31:00Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates how to set the InsideRadius property for a pie chart series in Syncfusion WinForms.
- Provides sample code in both C# and VB.NET to modify the InsideRadius of a pie chart series.
- Explains the chart element and chart type to which the property applies.

## Content

### Property Details
The following table provides details about the `InsideRadius` property:

| Default Value | None. |
| --- | --- |
| 2D / 3D Limitations | No. |
| Applies to Chart Element | All series. |
| Applies to Chart Types | Pie Chart. |

### Sample Code

#### C#
```csharp
ChartSeries series1 = this.chartControl1.Model.NewSeries("Market");
series1.InSideRadius = 0.5f;
```

#### VB.NET
```vb
Dim series1 As ChartSeries = Me.chartControl1.Model.NewSeries("Market")
series1.InSideRadius = 0.5f
```

### Visual Representation

The chart below visually demonstrates the `InsideRadius` property for a pie chart series.

![InSideRadius Pie Chart](https://i.imgur.com/03J7c7B.png)

**Figure 152: InSideRadius Pie Chart**

## See Also

- <!-- anchor: chart#page_258#see-also -->
```html
<!-- tags: [windows forms, essential chart, pie chart, inside radius, syncfusion, winforms] keywords: [inside radius, pie chart, essential chart, windows forms, chart series] -->
```
```