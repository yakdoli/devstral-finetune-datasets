```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_297.jpeg
document_name: chart
page_number: 297
page_id: chart#page_297
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:33:30Z
fidelity: lossless
-->


# Essential Chart for Windows Forms

## Overview

- This page discusses the advanced charting capabilities of the Syncfusion Windows Forms library.
- Focus on polygon radar styles and the `RelatedPoints` feature for Gantt charts.
- Includes detailed descriptions of properties and their functions.

## Content

### Figure 183: Radar Chart with Polygon RadarStyle

![Radar Chart with Polygon RadarStyle](./image_url)

**Figure 183: Radar Chart with Polygon RadarStyle**

#### See Also
- **Radar Charts**

---

### 4.5.1.61 RelatedPoints

This section explains how to specify the relationship between two points in the Gantt chart type, which will render a line connecting the specified points.

#### Details

| **Property**      | **Description**                                                                 |
|-------------------|---------------------------------------------------------------------------------|
| **Possible Values** | A `ChartRelatedPointInfo` object, which has the following properties:       |
|                   | - **Color** - Any Color Object                                                |
|                   | - **Alignment** - Any PenAlignment Property                                     |
|                   | - **Points** - Integer Array containing the points which are to be connected. |

## API Reference (if applicable)

### Namespaces and Classes
- **Namespace**: Syncfusion.Windows.Forms.Chart
- **Class**: ChartRelatedPointInfo

#### Properties
- **Color**:
  - **Type**: Any Color Object
  - **Description**: Specifies the color for the connection line.
- **Alignment**:
  - **Type**: Any PenAlignment Property
  - **Description**: Determines the alignment property of the connecting line.
- **Points**:
  - **Type**: Integer Array
  - **Description**: Contains the points to be connected.

## Code Examples (multi-language supported)

### C# Example
```csharp
using Syncfusion.Windows.Forms.Chart;

// Create a ChartRelatedPointInfo object
ChartRelatedPointInfo connectionInfo = new ChartRelatedPointInfo();

// Set properties
connectionInfo.Color = System.Drawing.Color.Blue;
connectionInfo.Alignment = PenAlignment.Center;
connectionInfo.Points = new int[] { 1, 2, 3 };

// Add the related points to the chart series
chart.Series[0].RelatedPoints.Add(connectionInfo);
```

```vb
Imports Syncfusion.Windows.Forms.Chart

' Create a ChartRelatedPointInfo object
Dim connectionInfo As New ChartRelatedPointInfo()

' Set properties
connectionInfo.Color = System.Drawing.Color.Blue
connectionInfo.Alignment = PenAlignment.Center
connectionInfo.Points = New Integer() { 1, 2, 3 }

' Add the related points to the chart series
chart.Series(0).RelatedPoints.Add(connectionInfo)
```

## Page-level Navigation/TOC (if applicable)

- **Radar Charts**
- **RelatedPoints**
  - Description
  - Properties
  - Code Examples

## Cross References

- **RelatedPoints**: A feature in Gantt charts to display connections between specified points.
- **Radar Charts**: A chart type showcasing the comparison of multiple variables on a two-dimensional surface.

## RAG Annotations

<!-- tags: [syncfusion, winforms, chart, radar, relatedpoints, gantt, essentialchart] keywords: [polygon radarstyle, chartrelatedpointinfo, penalignment, color, points, connection line] -->
```