```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_281.jpeg
document_name: chart
page_number: 281
page_id: chart#page_281
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:32:36Z
fidelity: lossless
-->

## Content

### 4.5.1.51 PhongAlpha

Specifies the Phong's alpha co-efficient used for calculating specular lighting.

| **Details**           |                                            |
|-----------------------|--------------------------------------------|
| **Possible Values**   | Any double value                          |
| **Default Value**     | 20                                         |
| **2D / 3D Limitations** | No                                           |
| **Applies to Chart Element** | Any Series                              |
| **Applies to Chart Types** | Column Chart, Bar Chart, Box and Whisker Chart, Gantt Chart, Histogram Chart, Tornado Chart, Polar and Radar Chart, HiLo Chart, HiLoOpenClose Chart, Candle Chart, Scatter Chart |

Here is code snippet using PhongAlpha in Column Chart.

#### C#
```csharp
this.chartControl1.Series[0].ConfigItems.ColumnItem.PhongAlpha = 2.0;
```

#### VB.NET
```vb
Private Me.chartControl1.Series(0).ConfigItems.ColumnItem.PhongAlpha = 2.0
```

## Page-level Navigation/TOC (if applicable)
- **4.5.1.51 PhongAlpha**

### Cross References
- **See also:** Essential Chart for Windows Forms

<!-- tags: [syncfusion-sdk, windows-forms, chart, phongalpha, specular-lighting, 2d-3d-limitations, essential-chart-for-windows-forms, series, chart-types, column-chart, bar-chart, box-and-whisker-chart, gantt-chart, histogram-chart, tornado-chart, polar-and-radar-chart, hi-lo-chart, hi-lo-open-close-chart, candle-chart, scatter-chart, csharp, visual-basic-net, syncfusion-windows-forms, version-11.4.0.26] -->
```