```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_353.jpeg
document_name: chart
page_number: 353
page_id: chart#page_353
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:36:37Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Chart Element Properties

The following table outlines the possible properties and their details for a variety of chart types:

| Possible Values | Any string value |
|------------------|------------------|
| Default Value    | Nil              |
| 2D / 3D Limitations | No             |
| Applies to Chart Element | Any Series |
| Applies to Chart Types | Scatter Chart, Hilo Open Close Chart(3D), Column Charts, BarCharts, Bubble Chart, Line Charts, BoxandWhisker Chart, Tornado Chart, Combination Chart, Gantt Chart, Candle Chart, HiLo Chart(3D), PolarAndRadar, PieChart, Accumulation Charts, Area Charts |

### Property Details

Table: Property Table

| Property        | Description                                         | Type        | Data Type | Reference links |
|------------------|-----------------------------------------------------|-------------|-----------|-----------------|
| ShowToolTips     | Specifies whether tooltip has to be displayed.    | Server side | Boolean   | NA              |

### Code Examples

Here is sample code snippet using ToolTip in the Column Chart.

#### Series Wide Setting

[C#]

```csharp
this.chartControl1.ShowToolTips = true;
series1.PointsToolTipFormat = "{1}";
series1.Style.ToolTip = "Tooltip of Series1";
```

[VB.NET]

```vb
Me.chartControl1.ShowToolTips = True
series1.PointsToolTipFormat = "{1}"
series1.Style.ToolTip = "Tooltip of Series1"
```

## API Reference

### Chart Tooltips

**Property**: ShowToolTips  
- **Description**: Specifies whether tooltips have to be displayed.  
- **Type**: Server side  
- **Data Type**: Boolean  
- **Default Value**: NA  

---

<!-- tags: [chart, tooltips, windows forms, syncfusion] keywords: [chart, tooltips, series, staggered, 2d, 3d, scatters, hi-lo, column, bar, bubble, line, box and whisker, tornado, combination, gantt, candle, hi-lo 3d, polar, radar, pie, accumulation, area, series] -->
``` 
