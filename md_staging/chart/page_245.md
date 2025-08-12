```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_245.jpeg
document_name: chart
page_number: 245
page_id: chart#page_245
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:30:28Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview

- Description and characteristics of the PointAndFigure Chart.
- Explanation of the Box Size parameter and its effect on visualization.
- Reference to the ChartArea.Depth property and its functionality.

## Content

### StockPrice Summary

![PointAndFigure Chart with Box Size of 2](#)

*Figure 144: PointAndFigure Chart with Box Size of 2*

The PointAndFigure Chart shown in Figure 144 demonstrates stock price trends over time, using "X" and "O" symbols to represent price movements. The chart is divided into days, with the Box Size set to 2. This allows for a visual summary of price fluctuations.

#### See Also

- **PointAndFigure Chart**: Linked reference for more detailed information on the PointAndFigure Chart.

### 4.5.1.34 HeightByAreaDepth

#### Overview

Indicates whether to draw series using the `ChartArea.Depth` property.

#### Details

| Details        |               |
|-----------------|---------------|
| Possible Values | True or False |
| Default Value   | False         |
| 2D / 3D Limitations | 3D Only     |
| Applies to Chart Element | All series |

## API Reference

#### Properties

- **HeightByAreaDepth**

  - **Namespace**: Syncfusion.Windows.Forms.Chart
  - **Type**: Boolean

  Indicates whether to draw series using the `ChartArea.Depth` property.
  
  - **Options**:
    - `True`: Draws series based on the `Depth` property.
    - `False`: Draws series without using the `Depth` property.

  - **Default Value**: `False`
  - **2D / 3D Limitations**: Only applicable in 3D charts.
  - **Applies to**: All series in the chart.

### Implementation Example

The `HeightByAreaDepth` property can be set in code as follows:

```csharp
chart.Series[0].HeightByAreaDepth = true;
```

This configuration will enable the series to be drawn with depth, enhancing the 3D visualization.

## Cross References

### See Also

- **PointAndFigure Chart**: Further details and customization options for the PointAndFigure Chart.

<!-- tags: [chart, windowsforms, syncfusion, essentialchart, pointandfigurechart, heightbyareadepth, chartareadepth, stockprice, visualization] keywords: [chart, boxsize, pointandfigure, stocksummary, 3dchart, depthproperty] -->
```