```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_486.jpeg
document_name: chart
page_number: 486
page_id: chart#page_486
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:47:09Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Product sales per month are visualized with interactive tooltips.
- Customizable tooltips support multiple areas of the chart.
- The ShowToolTips property controls tooltip visibility.

## Content

### Product Sales per Month

The chart illustrates product sales per month with interactive tooltips.

#### Data Points
Months 2 through 18 are represented, showing fluctuating sales data.

#### Figure 312: Symbols shown at intersection between series point and interactive cursor

![](./image_0.png)

**Figure 312:** Symbols shown at intersection between series point and interactive cursor.

#### 4.9.5 ToolTips

**Overview of ToolTips**
- Essential Chart supports ToolTips in various areas of the chart with multiple customization options.
- ToolTips in the chart can be turned off using the control's ShowToolTips property.

**Usage Note**
- The ShowToolTips property is false by default, so it should be turned on before setting tooltips in different chart areas.

#### DataPoint ToolTips
- ToolTips can display on each data point when the mouse hovers.
- The format of the tooltip is specified in ChartSeries using PointsToolTipFormat.

#### ChartSeries Property Description

| ChartSeries Property        | Description                                                                                                                                                                 |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PointsToolTipFormat         | Specifies the format for the datapoint tooltips. The following placeholders can be used in the value.                                                                      |

### Summary

- ToolTips enhance chart interactivity by providing extra information at specific points.
- Users can customize tooltips using the Essential Chart's interface and properties.
- Proper configuration ensures tooltips are displayed effectively.

### WinForms-specific conventions
- Tooltip property usage integrates seamlessly with Syncfusion.Windows.Forms controls.
- Ensure proper configuration to maintain usability and consistency within the application.

### Summary of ToolTips in Essential Chart
- Customization options allow for tailored user experiences.
- Interactivity through tooltips improves data comprehension and usability.

### Cross References
- Refer to previous sections for additional information on configuring chart properties.
- Check related documentation for advanced tooltip customization options.

### RAG Annotations
<!-- tags: [chart, windows forms, tooltips, essential chart, synchronization, customization, toolTips, interactive cursors] keywords: [ShowToolTips, PointsToolTipFormat, DataPoint ToolTips, interactive tooltips, multiple customization options, product sales per month] -->
```