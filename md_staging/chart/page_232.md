```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_232.jpeg
document_name: chart
page_number: 232
page_id: chart#page_232
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:30:22Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- This section provides detailed information about creating and customizing pie charts with the "AllPie" FillMode. It includes a reference to the FunnelMode for additional chart functionality.
- The provided pie chart illustrates a breakdown of project costs, categorized into various segments such as Labour, Production, Facilities, Insurance, Taxes, Legal, and Licenses.
- The FunnelMode section explains how to configure the funnel chart mode with possible values for YIsWidth and YIsHeight.

## Content

### Project Cost Breakdown
![Project Cost Breakdown](figure_134.png)
**Figure 134: Pie Chart with "AllPie" FillMode**

#### See Also
- [Pie Chart](Pie%20Chart)

#### FunnelMode
**4.5.1.28 FunnelMode**

This section describes how to get or set the chart funnel mode.

- **Details**
  
  | Possible Values                                       |                                                                                                 |
  |------------------------------------------------------|-------------------------------------------------------------------------------------------------|
  |                                                      | - **YIsWidth** - DataPoint y-value controls the radius of the funnel segment.                  |
  |                                                      | - **YIsHeight** - DataPoint y-value controls the height of the funnel segment.                 |

### Summary of Project Cost Breakdown
The pie chart in **Figure 134** presents a detailed breakdown of the project costs, with the following percentage allocations:
- **Labour**: 28%
- **Production**: 20%
- **Facilities**: 23%
- **Insurance**: 12%
- **Taxes**: 10%
- **Legal**: 2%
- **Licenses**: 3%

### About FunnelMode
The FunnelMode allows customization of funnel charts, with the following possible values:
- **YIsWidth**: Controls the radius of the funnel segment.
- **YIsHeight**: Controls the height of the funnel segment.

## API Reference

### FunnelMode
```csharp
public FunnelMode GetFunnelMode();
public void SetFunnelMode(FunnelMode value);
```

#### Parameters
- **YIsWidth**: Type of Control (e.g., `System.Double`)
  - **Description**: DataPoint y-value that controls the radius of the funnel segment.
- **YIsHeight**: Type of Control (e.g., `System.Double`)
  - **Description**: DataPoint y-value that controls the height of the funnel segment.

## Code Examples
```csharp
// Example of setting FunnelMode
chart.Series[0].FunnelMode = FunnelMode.YIsWidth;
```

## Page-level Navigation/TOC (if applicable)
- [Pie Chart with "AllPie" FillMode](#pie-chart-with-allpie-fillmode)
- [FunnelMode](#funnelmode)

## Cross References
- **See also**: [Pie Chart](Pie%20Chart)

<!-- tags: [project cost breakdown, funnel chart mode, YIsWidth, YIsHeight, pie chart, Windows Forms, Syncfusion] keywords: [chart, project cost, pie chart, allpie fillmode, funnelmode, yiswidth, yisheight, windows forms, syncfusion] -->
```