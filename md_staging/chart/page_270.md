```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_270.jpeg
document_name: chart
page_number: 270
page_id: chart#page_270
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:31:45Z
fidelity: lossless
-->

## Chart Controls Overview

### Chart Types

- Column Charts
- Bar Charts
- Box and Whisker Chart
- Gantt Chart
- Histogram Chart
- Tornado Chart
- Polar and Radar Chart
- Candle Chart
- Hilo Chart (3D)
- HiloOpenClose (3D)

## Properties

### 4.5.1.46 LightColor

Specifies the color of light for all shading modes except ChartColumnShadingMode.FlatRectangle.

#### Details

| Feature                | Description                                      |
|------------------------|--------------------------------------------------|
| **Possible Values**    | A Color object                                   |
| **Default Value**      | Color.White                                      |
| **2D / 3D Limitations**| No                                              |
| **Applies to Chart Element** | Any Series                                  |
| **Applies to Chart Types** | Column Chart, Bar Chart, Box and Whisker Chart, Gantt Chart, Histogram Chart, Tornado Chart, Radar Chart |

### Sample Code

Here is a sample code snippet using `LightColor` in Column Chart.

#### C#

```csharp
this.chartControl1.Series[0].ConfigItems.ColumnItem.LightColor = Color.Blue;
this.chartControl1.Series[1].ConfigItems.ColumnItem.LightColor = Color.Green;
```

#### VB.NET

```vb
Private Me.chartControl1.Series(0).ConfigItems.ColumnItem.LightColor = Color.Blue
Private Me.chartControl1.Series(1).ConfigItems.ColumnItem.LightColor = Color.Green
```

## Copyright Information

© 2013 Syncfusion. All rights reserved.
```