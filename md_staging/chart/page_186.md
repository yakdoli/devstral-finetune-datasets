```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_186.jpeg
document_name: chart
page_number: 186
page_id: chart#page_186
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:26:37Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates the `ColumnDrawMode` property for bar charts in Windows Forms.
- Compares the visual rendering between two modes: "PlaneMode" and "InDepthMode."
- Provides examples with bar charts showing data distribution.

## Content

### Figure 100: ColumnDrawMode set to "PlaneMode"

![](https://example.com/figure100.png)

The chart above illustrates how the `ColumnDrawMode` set to "PlaneMode" affects the visualization. The figure displays grouped bar charts with orange and blue blocks representing different datasets across categories. Error bars are also visible, indicating variability in the data points.

### Figure 101: ColumnDrawMode set to "InDepthMode"

![](https://example.com/figure101.png)

In contrast, the above figure shows the bar chart with `ColumnDrawMode` set to "InDepthMode." This mode provides a different visual representation, where the blocks appear more spread out and integrated into the depth of the chart, allowing for better visibility of the individual data points or categories.

## API Reference

### Properties
- `ColumnDrawMode`: A property of the chart control that determines the drawing style of the bars.

### Enumerations
- `PlaneMode`
- `InDepthMode`

## Code Examples (C#)

```csharp
// Setting ColumnDrawMode to PlaneMode
chart.Series[0].ColumnDrawMode = ChartColumnDrawMode.PlaneMode;

// Setting ColumnDrawMode to InDepthMode
chart.Series[0].ColumnDrawMode = ChartColumnDrawMode.InDepthMode;
```

## Cross References
- See also: Documentation on bar chart customization and error bars in the Syncfusion WinForms Charts User Guide.

<!-- tags: winforms, chart, column mode, plane mode, in depth mode, error bars, synchronization, customization keywords: plane mode, in depth mode, error bars, data visualization, user guide, chart series -->
```