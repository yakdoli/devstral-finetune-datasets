```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_314.jpeg
document_name: chart
page_number: 314
page_id: chart#page_314
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:34:16Z
fidelity: lossless
--> 

## Essential Chart for Windows Forms

### 4.5.1.69 ShadowOffset

Specifies the width of the shadow of the series.

| Details            |                                                                                                                     |
|--------------------|---------------------------------------------------------------------------------------------------------------------|
| Possible Values    | Any possible numeric values for x, y                                                                               |
| Default Value      | 3, 2                                                                                                               |
| 2D / 3D Limitations | 2D only                                                                                                           |
| Applies to Chart Element | Any Series                                                                                                    |
| Applies to Chart Types | Column Charts, Bubble Chart, Line Charts, BarCharts, Candle Chart, Kagi Chart, Point and Figure Chart, Renko Chart, Three Line Break Chart, <br> Box and Whisker Chart, Gantt Chart, Histogram Chart, Tornado Chart, Pie Chart, <br> Polar and Radar Chart, Area Chart, Step Area Chart |

Here is sample code snippet using `ShadowOffset` in Column Chart.

#### Series Wide Setting

```csharp
series.Style.DisplayShadow = true;
series.Style.ShadowOffset = new Size(7, 7);

// For specific points
series.Styles[0].ShadowOffset = new Size(7, 7);
series.Styles[1].ShadowOffset = new Size(8, 8);
series.Styles[2].ShadowOffset = new Size(6, 6);
```

```vb.net
Private series.Style.DisplayShadow = True
Private series.Style.ShadowOffset = New Size(7, 7)

' For specific points
Private series.Styles(0).ShadowOffset = New Size(7, 7)
```

---
© 2013 Syncfusion. All rights reserved.
<!-- tags: [chart, essentialchart, windowsforms, shadowoffset, shadowwidth, sdk, version11.4.0.26] keywords: [chart, essentialchart, windowsforms, shadowoffset, shadowwidth, series, samplecode, displayshadow, size, charttypes, 2dchart, columnchart, samplecode, csharp, vb.net] -->
``` 
