```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_049.jpeg
document_name: chart
page_number: 049
page_id: chart#page_049
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:18:36Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
Public Function GetEmpty(ByVal index As Integer) As Boolean
    Return False
End Function

' Event that should be raised by any implementation of this
' interface if data that it holds changes. This will cause the chart to
' be updated accordingly. We don't raise this event in our implementation
' as our data will be static.
Public event ListChangedEventHandler Changed
End Class
```

**Bind the above model to the chart series.**

### C#
```csharp
//Creating series data and binding to the array model
ChartSeries series1 = this.chartControl1.Model.NewSeries("Series 1");
series1.SeriesIndexedModelImpl = new ArrayModel(new double[]{22,24,32,12,18});
series1.Type = ChartSeriesType.Bar;
this.chartControl1.Series.Add(series1);
```

### VB.NET
```vb
'Creating series data and binding to the array model
Dim series1 As ChartSeries = Me.chartControl1.Model.NewSeries("Series 1")
series1.SeriesIndexedModelImpl = New ArrayModel(New Double(){22,24,32,12,18})
series1.Type = ChartSeriesType.Bar
Me.chartControl1.Series.Add(series1)
```
```