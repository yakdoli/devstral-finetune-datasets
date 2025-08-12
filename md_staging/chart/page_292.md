```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_292.jpeg
document_name: chart
page_number: 292
page_id: chart#page_292
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:33:43Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- This section describes the `PyramidMode` property, used to specify how y-values are interpreted in a pyramid chart.
- It explains the differences between Linear and Surface modes and provides details about possible values, default settings, and limitations.
- Includes sample code in both C# and VB.NET for setting the pyramid mode to Surface.

## Content

### PyramidMode
Specifies the mode in which the y values should be interpreted. In Linear mode, the y values are proportional to the length of the sides of the Pyramid. In Surface Mode, the y values are proportional to the surface area of the corresponding blocks.

#### Details

| **Possible Values**                               | - Linear - Draw pyramid chart in linear mode<br>- Surface - Draw pyramid chart in surface mode |
|----------------------------------------------------|-----------------------------------------------------------------------------------------------|
| **Default Value**                                 | Linear                                                                                         |
| **2D / 3D Limitations**                          | No                                                                                             |
| **Applies to Chart Element**                     | Any Series                                                                                     |
| **Applies to Chart Types**                       | Pyramid                                                                                       |

#### Sample Code

Here is some sample code.

**[C#]**
```csharp
this.chartControl1.Series[0].ConfigItems.PyramidItem.PyramidMode=ChartPyramidMode.Surface;
```

**[VB.NET]**
```vb
Private Me.chartControl1.Series(0).ConfigItems.PyramidItem.PyramidMode=ChartPyramidMode.Surface
```

## See Also
- Kagi Chart
- Point and Figure Chart
- Three Line Break Chart
- Renko Chart

## Note
- The `PyramidMode` property is particularly useful for visualizing and interpreting data in pyramid charts.
- The default setting is Linear, but Surface mode can be useful when the proportional representation is based on the surface area.

<!-- tags: [Windows Forms, PyramidChart, Charting, WinForms, Syncfusion] keywords: [PyramidMode, LinearMode, SurfaceMode, DataVisualization, ChartElements, PyramidChartTypes] -->
```