```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_408.jpeg
document_name: chart
page_number: 408
page_id: chart#page_408
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:39:51Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Illustrates grouping labels with grid in X-Axis and how to configure tooltips for ChartAxisLabels.
- Explains cases where tooltips can display full text in place of truncated ChartAxisLabels.
- Demonstrates adding customized tooltips for ChartAxisLabels using code examples.

## Content

### Figure 262: Q1 and Q2 Grouping Labels with Grids

![](Illustrates Grouping Lables with Grid in X-Axis)

#### 4.6.8.5 Tooltip Support for ChartAxisLabels

Essential Chart provides tooltip support for ChartAxisLabel. By default, ChartAxisLabel will be displayed as a tooltip. You can also customize the tooltip to show any content you want.

#### Use Case Scenarios

- If a ChartAxisLabel is too long and truncated, the tooltip for the label will show the full text.
- You can also show additional information about the ChartAxisLabel.

#### Adding Tooltip for ChartAxisLabel

To add a tooltip for a chart, set the `ShowToolTips` property to `true`. By default, ChartAxisLabel content will be taken as tooltip content. You can also customize the tooltip content using the `ChartFormatAxisLabel` event.

The following code illustrates how to add a customized tooltip for ChartAxisLabel:

```csharp
this.chartControl1.ChartFormatAxisLabel += new ChartFormatAxisLabelEventHandler(chartControl1_ChartFormatAxisLabel);
```

## API Reference

- `ChartFormatAxisLabel` event: Allows customization of tooltip content for ChartAxisLabels.

## Code Examples

- Example of adding a customized tooltip for ChartAxisLabel in C#.

<!-- tags: [chart, chartaxislabels, tooltips, grid, essential chart, windows forms] -->
<!-- keywords: [chartaxislabel, showtooltips, ChartFormatAxisLabelEventHandler, ChartAxisLabels, grouping labels, tooltip support, additional information, truncated labels] -->
```