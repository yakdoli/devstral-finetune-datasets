```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_268.jpeg
document_name: chart
page_number: 268
page_id: chart#page_268
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:32:24Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Content

### LightAngle

**Specifies the light angle in horizontal plane.**

| **Details**           |                            |
|-----------------------|----------------------------|
| **Possible Values**   | Any double value          |
| **Default Value**     | -0.785398163397448       |
| **2D / 3D Limitations** | No                       |
| **Applies to Chart Element** | Any Series           |
| **Applies to Chart Types** | Column Charts, Bar Charts, Box and Whisker Chart, Gantt Chart, Histogram Chart, Tornado Chart, Polar and Radar Chart, Candle Chart, Hilo Chart(3D), HiloOpenClose(3D) |

Here is code snippet using `LightAngle` in Column Chart.

```csharp
// Specifies light angle of both the series
this.chartControl1.Series[0].ConfigItems.ColumnItem.LightAngle = 45;
this.chartControl1.Series[1].ConfigItems.ColumnItem.LightAngle = 45;
```

```vb.net
' Specifies light angle of both the series
Private Me.chartControl1.Series(0).ConfigItems.ColumnItem.LightAngle = 45
Private Me.chartControl1.Series(1).ConfigItems.ColumnItem.LightAngle = 45
```

## Page-level Navigation/TOC (if applicable)
- **4.5.1.45 LightAngle**

## Cross References
- See also: [other related sections in the document]

<!-- tags: [Essential Chart, Windows Forms, LightAngle, Chart Elements, Syncfusion Winforms, 11.4.0.26] keywords: [LightAngle, default values, chart types, series, column charts, 2D/3D limitations, code snippet] -->
```