```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_086.jpeg
document_name: chart
page_number: 086
page_id: chart#page_086
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:20:22Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview

- This page describes the properties and usage of the StackingBar100 chart type in Windows Forms.
- Highlights include defining a single series with multiple data points, adding custom points, and utilizing various customization options.

## Content

| Feature                       | Description                                                                           |
|------------------------------|---------------------------------------------------------------------------------------|
| Number of Y values per point | 1                                                                                       |
| Number of Series             | Two or more.                                                                           |
| SupportMarker                | No                                                                                     |
| Cannot be Combined with      | Any other chart types.                                                               |

### Code Examples

#### C#

```csharp
ChartSeries series1 = this.chartControl1.Model.NewSeries("chart",
    ChartSeriesType.StackingBar100);
series1.Points.Add(0, 25.3);
series1.Points.Add(1, 45.7);
series1.Points.Add(2, 97.3);
series1.Points.Add(3, 20.6);
series1.Points.Add(4, 125.8);
series1.Points.Add(5, 216.1);
this.chartControl1.Series.Add(series1);
```

#### VB.NET

```vb
Dim series1 As ChartSeries = Me.chartControl1.Model.NewSeries("chart",
    ChartSeriesType.StackingBar100)
series1.Points.Add(0, 25.3)
series1.Points.Add(1, 45.7)
series1.Points.Add(2, 97.3)
series1.Points.Add(3, 20.6)
series1.Points.Add(4, 125.8)
series1.Points.Add(5, 216.1)
Me.chartControl1.Series.Add(series1)
```

### Customization Options

The following are some of the customization options available for the StackingBar100 chart type:

- **Border**
- **ColumnDrawMode**
- **DisplayText**
- **DrawSeriesNameInDepth**
- **ElementBorders**
- **HighlightInterior**
- **ImageIndex**
- **Images**
- **LightAngle**
- **LightColor**
- **Rotate**
- **Spacing**
- **Spacing Between Series**
- **ShadingMode**
- **ShadowInterior**
- **ShadowOffset**
- **ZOrder**
- **FancyToolTip**
- **Font**
- **Interior**
- **LegendItem**
- **Name**
- **PointsToolTipFormat**
- **SmartLabels**
- **Summary**
- **Text**
- **TextColor**
- **TextFormat**
- **TextOffset**
- **TextOrientation**
- **Visible**

## See Also

- Refer to related documentation or examples for more details on chart customization and features.

<!-- tags: [syncfusion, windows forms, chart, stacking bar, winforms, chart control] keywords: [stackingbar100, chart series, data points, customization options, point addition, csharp, vb.net, essential chart for windows forms, light angle, shading mode, shadow interior, summary text, visible elements] -->
```