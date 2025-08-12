```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_316.jpeg
document_name: chart
page_number: 316
page_id: chart#page_316
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:35:04Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## 4.5.1.70 ShowDataBindLabels

Indicates whether data bound labels are displayed in the chart.

| Details                      |                                                                                                       |
|------------------------------|-------------------------------------------------------------------------------------------------------|
| Possible Values              | • True - Displays the databind labels.<br> • False - Hides the databind labels.                     |
| Default Value                | False                                                                                                 |
| 2D / 3D Limitations         | No                                                                                                    |
| Applies to Chart Element     | All Series                                                                                            |
| Applies to Chart Types       | Pie Chart, Doughnut Chart, Funnel Chart and Pyramid chart.                                       |

Here is sample code snippet using ShowDataPointLabels.

### C#

```csharp
// For Pie Chart
this.chartControl.Series[0].ConfigItems.PieItem.ShowDataBindLabels = true;
// For Funnel Chart
this.chartControl.Series[0].ConfigItems.FunnelItem.ShowDataBindLabels = true;
// For Pyramid Chart
this.chartControl.Series[0].ConfigItems.PyramidItem.ShowDataBindLabels = true;
```

### VB.NET

```vb
' For Pie Chart
Me.chartControl.Series(0).ConfigItems.PieItem.ShowDataBindLabels = True
' For Funnel Chart
Me.chartControl.Series(0).ConfigItems.FunnelItem.ShowDataBindLabels = True
' For Pyramid Chart
Me.chartControl.Series(0).ConfigItems.PyramidItem.ShowDataBindLabels = True
```

<!-- tags: [Syncfusion Winforms, Chart, ShowDataBindLabels, Pie Chart, Doughnut Chart, Funnel Chart, Pyramid chart] keywords: [data bound labels, chart control, chart elements, chart types, 2D/3D limitations] -->
``` 
