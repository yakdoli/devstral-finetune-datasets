```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_298.jpeg
document_name: chart
page_number: 298
page_id: chart#page_298
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:33:19Z
fidelity: lossless
--> 

## Overview
- Specifies the number of points and the line style including DashStyle, DashPattern, and Width for related points in the chart.
- Default values include Control Text Color, Center alignment, Solid DashStyle, and Width set to 5.0f.
- Applies to any series and points in a Gantt Chart.

## Content

Here is the detailed table of specifications and default values:

|                  | Specified Properties                                                                 |
|------------------|---------------------------------------------------------------------------------------|
|                  | - Count - Specifies the Number of points                                              |
|                  | - DashStyle - Any System.Drawing.Drawing2D.DashStyle                                  |
|                  | - DashPattern - A Float array with two values                                        |
|                  | - Width - Any Float value                                                            |
| Default Value    | - Color - Control Text Color                                                         |
|                  | - Alignment - Center                                                                  |
|                  | - Points - Null                                                                      |
|                  | - Count - 0                                                                          |
|                  | - DashStyle - Solid                                                                  |
|                  | - DashPattern - Null                                                                 |
|                  | - Width - 5.0f                                                                       |
| 2D / 3D Limitations | No                                                                               |
| Applies to Chart Element        | Any Series and Points                                                 |
| Applies to Chart Types          | Gantt Chart                                                           |

### Related Points Configuration Sample Code

Here is a sample code snippet demonstrating the use of RelatedPoints in a Gantt Chart.

```csharp
// Related Points for first series
int[] ptIndices = new int[] { 2, 4 };
this.chartControl1.Series[0].Styles[3].RelatedPoints.Points = ptIndices;
this.chartControl1.Series[0].Styles[3].RelatedPoints.Color = Color.Red;
this.chartControl1.Series[0].Styles[3].RelatedPoints.Alignment = System.Drawing.Drawing2D.PenAlignment.Right;
this.chartControl1.Series[0].Styles[3].RelatedPoints.DashStyle = System.Drawing.Drawing2D.DashStyle.Custom;
this.chartControl1.Series[0].Styles[3].RelatedPoints.Width = 3f;
float[] dash = new float[] { 1.5f, 2.4f };
this.chartControl1.Series[0].Styles[3].RelatedPoints.DashPattern = dash;

// Related Points for second series
int[] ptIndices = new int[] { 1 };
this.chartControl1.Series[1].Styles[5].RelatedPoints.Points =
```

## RAG Annotations

<!-- tags: [chart, gantt chart, related points, winforms, syncfusion] keywords: [chart, gantt, points, related points, winforms, ChartControl, series, styles, dash style, dash pattern, width] -->
```