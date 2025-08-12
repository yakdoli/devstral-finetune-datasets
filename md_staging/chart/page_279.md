```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_279.jpeg
document_name: chart
page_number: 279
page_id: chart#page_279
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:31:23Z
fidelity: lossless
-->


## Chart Control Features

### Chart Property Details

The following table provides details about the chart property.

| Property            | Description                            |
|---------------------|----------------------------------------|
| **Default Value**   | True                                   |
| **2D/3D Limitations** | No.                                   |
| **Applies to Chart Element** | Any Series.                    |
| **Applies to Chart Types** | Pie Chart.                      |

### Using OptimizePiePointPositions

Here is the code snippet using `OptimizePiePointPositions`.

#### C#

```csharp
ChartSeries series = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Pie);
series.Points.Add(0, 20);
series.Points.Add(1, 28);
series.Points.Add(2, 23);
series.Points.Add(3, 10);
series.Points.Add(4, 12);
series.Points.Add(5, 3);
series.Points.Add(6, 2);
series.ExplodedIndex = 2;
series.OptimizePiePointPositions = false;
this.chartControl1.Series.Add(series);
```

#### VB.NET

```vb
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Pie)
series.Points.Add(0, 20)
series.Points.Add(1, 28)
series.Points.Add(2, 23)
series.Points.Add(3, 10)
series.Points.Add(4, 12)
series.Points.Add(5, 3)
series.Points.Add(6, 2)
series.ExplodedIndex = 2
series.OptimizePiePointPositions = False
```

<!-- tags: [Syncfusion Winforms, Chart Control, Pie Chart, OptimizePiePointPositions] keywords: [chart, pie chart, OptimizePiePointPositions, C#, VB.NET, properties, 2D/3D, limitations, default value, series] -->
```