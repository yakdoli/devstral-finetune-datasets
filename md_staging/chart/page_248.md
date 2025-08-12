```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_248.jpeg
document_name: chart
page_number: 248
page_id: chart#page_248
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:31:20Z
fidelity: lossless
-->

### WinForms Pie Chart Configuration with Height Coefficient

- This section demonstrates how to configure a Pie Chart in Windows Forms to adjust the height of pie slices using the `HeightCoefficient` property.
- Sample code in both C# and VB.NET is provided to illustrate the configuration of the chart.

## Content

### Code Examples

#### C#
```csharp
this.chartControl1.Series[0].ConfigItems.PieItem.HeightByAreaDepth = false;
this.chartControl1.Series[0].ConfigItems.PieItem.HeightCoefficient = 0.1f;
```

#### VB.NET
```vb
Me.chartControl1.Series(0).ConfigItems.PieItem.HeightByAreaDepth = False
Me.chartControl1.Series(0).ConfigItems.PieItem.HeightCoefficient = 0.1f
```

### Diagram

![Pie Chart with HeightCoefficient](https://assets.synfusion.com/docs/samples/chart_s17.png)

**Figure 147: Pie Chart with HeightCoefficient**

### Related Documentation

- [Pie Chart](Pie%20Chart)

### HighlightInterior (Auto Highlight Color)

#### Overview

- The auto highlight color for any series can be customized by setting the color at the `HighlightInterior` property of the `ChartStyleInfo` class.

## API Reference

### Methods/Properties

- `HighlightInterior`: Property of the `ChartStyleInfo` class used to set the auto highlight color for a series.

### Code Examples

#### C#
```csharp
chart.Series[0].Style.HighLightInterior = Color.Yellow;
```

## See Also

- [Pie Chart](Pie%20Chart)

## Observations and Notes

- This section provides a detailed guide on configuring Pie Charts in Windows Forms, focusing on the adjustment of slice heights and highlighting styles.
- Both C# and VB.NET examples are provided for ease of implementation across different development environments.

<!-- tags: Windows Forms, Pie Chart, Height Coefficient, HighlightInterior property keywords: pie chart configuration, height coefficient, highlight interior, windows forms -->
```