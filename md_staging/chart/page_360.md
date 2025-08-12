```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_360.jpeg
document_name: chart
page_number: 360
page_id: chart#page_360
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:37:26Z
fidelity: lossless
-->

## 4.5.1.90 VisibleAllPies

**Specifies whether the legend is to be displayed with one legend item for each slice in the pie.**

| Details                          |                                                                                           |
|----------------------------------|-------------------------------------------------------------------------------------------|
| **Possible Values**             | - `True` - Indicates only one legend item for all slices of pie.                        |
|                                  | - `False` - Indicates one legend item for each slice of pie.                           |
| **Default Value**               | `False`                                                                                   |
| **2D / 3D Limitations**        | No                                                                                        |
| **Applies to Chart Element**    | Any Series                                                                                |
| **Applies to Chart Types**      | Pie Chart                                                                                 |

Here is the sample code snippet using `VisibleAllPies` in `PieChart`.

### Sample Code

#### [C#]
```csharp
this.chartControl1.ChartArea.VisibleAllPies = false;
chartControl1.Legend.RowsCount = 3;
```

#### [VB.NET]
```vbnet
Me.chartControl1.ChartArea.VisibleAllPies = False
chartControl1.Legend.RowsCount = 3
```

<!-- tags: [syncfusion, winforms, chart, legend, piechart, visibleallpies, userguide] keywords: [visibleallpies, legend, piechart, chartcontrol, syncfusion, winforms, api reference, code examples, c#, vb.net, user guide, 11.4.0.26] -->
```