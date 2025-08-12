```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_174.jpeg
document_name: chart
page_number: 174
page_id: chart#page_174
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:25:43Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview

- An overview of various chart types supported in Syncfusion WinForms.
- Details about chart series and points attributes for different chart types.
- Attributes applicable to specific chart types, such as `InsideRadius`, `Interior`, `LabelPlacement`, etc.

## Content

### Chart Attributes and Their Applicability

The following table outlines the attributes and their applicability across different chart types:

| Attribute            | Applicable to                    | Applicable Chart Types                                                                                                                                                                                                 |
|----------------------|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                       |                                 | Renko chart, Three Line Break Chart, Box and Whisker Chart, Gantt Chart, Tornado Chart, Polar and Radar Chart.                                                                                                       |
| **Images**           | Series and points               | Area Charts, Bar Charts, Bubble Chart, Column Charts, Line Charts, Candle Chart, Renko chart, Three Line Break Chart, Box and Whisker Chart, Gantt Chart, Tornado Chart, Polar and Radar Chart.                                                                 |
| **InsideRadius**     | Series                          | Pie Chart.                                                                                                                                                                                                          |
| **Interior**         | Series and points               | All Chart Types.                                                                                                                                                                                                    |
| **LabelPlacement**   | Series                          | Funnel and Pyramid Charts.                                                                                                                                                                                          |
| **LabelStyle**       | Series                          | Funnel and Pyramid, Pie                                                                                                                                                                                             |
| **LegendItem**       | Series                          | All Chart Types.                                                                                                                                                                                                    |
| **LightAngle**       | Series                          | Scatter Chart, Column Charts, Bar Charts, Box and Whisker Chart, Gantt Chart, Histogram Chart, Tornado Chart, Polar and Radar Chart.                                                                                 |
| **LightColor**       | Series                          | Scatter Chart, Column Charts, Bar Charts, Box and Whisker Chart, Gantt Chart, Histogram Chart, Tornado Chart, Polar and Radar Chart.                                                                                 |
| **Name**             | Series                          | All chart types.                                                                                                                                                                                                    |
| **NumberOfHistogramIntervals** | Series                | Histogram Chart.                                                                                                                                                                                                    |
| **OpenCloseDrawMode** | Series                          | HiLo OpenClose chart.                                                                                                                                                                                              |
| **OptimizePiePointPositions** | Series                 | Pie chart                                                                                                                                                                                                           |
| **PhongAlpha**       | Series                          | Column Chart.                                                                                                                                                                                                       |
| **PieType**          | Series                          | Pie chart                                                                                                                                                                                                           |

### Note on Applicability

Each attribute has its specific use and applicability based on the type of chart used. Developers can customize charts by setting these attributes to suit their needs.

## API Reference (if applicable)

This section would typically detail the API for configuring chart attributes, but it is not explicitly shown in the provided content.

## Code Examples (multi-language supported)

The section for code examples is not provided in the content. However, it would include samples demonstrating how to configure chart attributes programmatically.

## Cross References

For more detailed information on chart customization and attributes, refer to the Syncfusion WinForms documentation.

<!-- tags: [chart, windows forms, attributes, types, syncfusion] keywords: [renko chart, three line break chart, box and whisker chart, gantt chart, tornado chart, polar chart, radar chart, area charts, bar charts, bubble chart, column charts, line charts, candle chart, pie chart, funnel chart, pyramid chart, scatter chart, histogram chart] -->
```