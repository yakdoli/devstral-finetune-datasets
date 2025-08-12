```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_491.jpeg
document_name: chart
page_number: 491
page_id: chart#page_491
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:44:03Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- This page explains how to customize the appearance of charts in Syncfusion Winforms, focusing on the background colors and other properties to enhance the chart's visual appeal.

## Content

### Figure 315: Fancy ToolTip set for Data Point

The figure illustrates the use of `FancyTooltip` on data points, providing detailed tool tips for each data point in a chart.

#### Chart Appearance

The following topics under this section discuss various properties used to customize the appearance of the chart:

#### 4.10.1 Background Colors

**Essential Chart** allows customization of the background colors of different portions of the chart.

##### Outside the Chart Area

Use the `BackInterior` property of the chart to customize the background of the chart area that is outside the actual chart area. This is where the legend and the chart title are typically rendered. By default, it is set to the **White** color.

### See Also
- [How to display tooltip over Histogram Chart columns](https://example.com/tooltip-over-histogram-chart-columns)

## Page-level Navigation/TOC (if applicable)

## Cross References

## API Reference (if applicable)
- **Properties**:
  - `BackInterior`: Used to set the background color of the chart area outside the actual chart data.

## Code Examples (multi-language supported)
- Example of setting the `BackInterior` property in C#:
  ```csharp
  // Set the background color outside the chart area
  chartControl1.BackInterior = System.Drawing.Color.Blue;
  ```

<!-- tags: [syncfusion winforms, essential chart, background colors, chart appearance, fancy tooltip, backinterior property] keywords: [chart customization, data point tooltip, color management, histogram chart, chart background] -->
```