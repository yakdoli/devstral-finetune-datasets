```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_203.jpeg
document_name: chart
page_number: 203
page_id: chart#page_203
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:27:11Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
this.chartControl1.Series[0].Styles[0].DisplayText = true;
this.chartControl1.Series[0].Styles[0].TextColor = Color.LightSlateGray;
```

#### VB.NET

```vb
' Enabling DisplayText for the first data point
Me.chartControl1.Series(0).Styles(0).DisplayText = True
Me.chartControl1.Series(0).Styles(0).TextColor = Color.LightSlateGray
```

### See Also
- Chart Types

## 4.5.1.12 DoughnutCoefficient

Specifies the percentage of the overall radius of the chart that will be used for the Doughnut center hole. For example, if it is set to 0, the doughnut hole will not exist, therefore, the chart will look like a Pie chart.

| Details          |
|-----------------|
| Possible Values  | Ranges from 0.0 to 0.9 |
| Default Value    | 0                      |
| 2D / 3D Limitations | No.                 |
| Applies to Chart Element | All series.     |
| Applies to Chart Types | Doughnut Chart, Pie Chart. |

PieCharts with a DoughnutCoefficient specified will be rendered as doughnuts. By default, this value is set to 0.0 and hence the chart will be rendered as a full pie.

The DoughnutCoefficient property specifies the fraction of the radius occupied by the doughnut whole. Hence the value can range from 0.0 to 0.9.

<!-- tags: [Essential Chart, DoughnutCoefficient, Doughnut Chart, Pie Chart, Windows Forms, Syncfusion] keywords: [DoughnutCoefficient, Doughnut Chart, Pie Chart, radius, hole, chart visualization] -->
```