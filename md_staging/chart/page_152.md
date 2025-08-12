```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_152.jpeg
document_name: chart
page_number: 152
page_id: chart#page_152
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:25:24Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Chart Details

| Details                        |                                     |
|---------------------------------|-------------------------------------|
| Number of Y values per point   | 1.                                 |
| Number of Series                | One.                               |
| Cannot be Combined with        | Any other chart types.            |

Radar series can be added to the chart using the following code.

### C#

```csharp
// Create chart series and add data points into it.
ChartSeries series = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Radar);
series.Points.Add(1, 83);
series.Points.Add(2, 79);
series.Points.Add(3, 48);
series.Points.Add(4, 46);
series.Points.Add(5, 42);

// Add the series to the chart series collection.
this.chartControl1.Series.Add(series);
```

### VB.NET

```vb
' Create chart series and add data points into it.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Radar)
series.Points.Add(1, 83)
series.Points.Add(2, 79)
series.Points.Add(3, 48)
series.Points.Add(4, 46)
series.Points.Add(5, 42)

' Add the series to the chart series collection.
Me.chartControl1.Series.Add(series)
```

### Customization Options
``` 
``` 
