```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_285.jpeg
document_name: chart
page_number: 285
page_id: chart#page_285
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:32:48Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Displays examples of different types of pie charts, including outside and round pie charts.
- Explains the `PieChart` control and its properties, specifically `PieWithSameRadius`.

## Content

### Pie Chart Examples

#### Figure 174: Pie Outside Chart
- A pie chart with segments rendered outside the main chart area.
- Legend is displayed to the right of the chart.

#### Figure 175: Pie Round Chart
- A pie chart with segments rendered in a rounded manner.
- Legend is displayed to the right of the chart.

### See Also
- [PieChart](PieChart)

### 4.5.1.53 PieWithSameRadius

#### Description
- Gets or sets whether the pie chart is rendered in the same radius when the `LabelStyle` is set to `Outside` or `OutsideInColumn`.

#### Details
- Additional details about the property are expected to be filled in this section.

## API Reference

### Property: PieWithSameRadius

#### Functionality
- This property determines if the pie chart segments maintain the same radius when labels are placed outside the chart.

#### Parameters
- **LabelStyle**: 
  - Type: `LabelStyle`
  - Description: Specifies the style of labels used in the chart.
  - Default: Not explicitly stated.

## Code Examples

### C#

```csharp
PieChart pieChart = new PieChart();
pieChart.PieWithSameRadius = true;
```

### VB.NET

```vb
Dim pieChart As New PieChart()
pieChart.PieWithSameRadius = True
```

## Page-level Navigation/TOC (if applicable)
- Introduction
- Overview
- Content
  - Pie Chart Examples
  - See Also
  - 4.5.1.53 PieWithSameRadius
  - Property: PieWithSameRadius
  - Code Examples

### Cross References
- [PieChart](PieChart)

<!-- tags: [syncfusion, winforms, chart, piechart, pie, labelstyle, radius, essentialchart, windowsforms] keywords: [pie chart, pie with same radius, label style, outside, outside column, legend, round chart, pie with same radius property] -->
```