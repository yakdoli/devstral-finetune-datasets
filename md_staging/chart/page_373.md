```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_373.jpeg
document_name: chart
page_number: 373
page_id: chart#page_373
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:37:39Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Detailed explanation of various point types in a chart.
- Different coordinate systems (`ChartCoordinates`, `Percent`, `Pixel`) for custom point placement.
- Illustration of custom point types and their meanings.

## Content

### Coordinate Systems for Chart Points

| Term                | Description                                                                                     |
|---------------------|-------------------------------------------------------------------------------------------------|
| ChartCoordinates    | This lets you render a point type at any location in the chart.                             |
| Percent             | The coordinates are specified as the percentage of the chart area.                           |
| Pixel               | The coordinates are specified to be in pixels of the chart area.                              |

### Custom Points Illustrated

#### Figure 240: Custom Point Types Illustrated

The custom point symbols in the above image represent the following Custom Types respectively:

1. **Yellow "Circle" – PointFollow**
2. **Orange "Star" - Pixel**
3. **Pink "Pentagon" - Percent**
4. **OrangeRed "Diamond" - ChartCoordinates**

![](Illustrates Custom Points)

#### Explanation of the Chart

The chart illustrates sales volume from 1994 to 2006. It uses various custom point symbols to denote different custom point types as described above.

### Sample Demonstration

A sample demonstrating all the custom point types is available in our installation at the following location:

- `..\\My Documents\\Syncfusion\\EssentialStudio\\VersionNumber\\Windows\\Chart.Windows\\Samples\\2.0\\Chart Series\\Chart Custom Points`

## API Reference (if applicable)
- **Namespace:** Syncfusion.Windows.Forms.Chart
- **Class:** Chart

### Code Examples (multi-language supported)

#### C# Example
```csharp
using Syncfusion.Windows.Forms.Chart;

// Example of adding a custom point in the chart
Chart chart = new Chart();

// Adding a custom point using ChartCoordinates
chart.CustomPoints.Add(new ChartCustomPoint(0.5, 0.7, ChartElementPosition.ChartArea));

// Adding a custom point using Pixel coordinates
chart.CustomPoints.Add(new ChartCustomPoint(100, 200, ChartElementPosition.ChartArea));

// Adding a custom point using Percent coordinates
chart.CustomPoints.Add(new ChartCustomPoint(50, 70, ChartElementPosition.ChartArea));
```

## Cross References
- See also: [Syncfusion Winforms Documentation](https://help.syncfusion.com/windowsforms/chart)

<!-- tags: [syncfusion, windowsforms, chart, custompoints, coordinates] keywords: [chart coordinates, percent, pixel, custom points, custom point types, windows forms, sales volume, point follow, star, pentagon, diamond, point placement] -->
```