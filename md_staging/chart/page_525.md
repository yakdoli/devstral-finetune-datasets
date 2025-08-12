```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_525.jpeg
document_name: chart
page_number: 525
page_id: chart#page_525
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:47:12Z
fidelity: lossless
--> 

## Content

### Essential Chart for Windows Forms

```csharp
ser3.Type = ChartSeriesType.StackingColumn;
// specifying group name.
ser3.StackingGroup = "FirstGroup";
```

#### [VB]

```vb
Dim ser1 As New ChartSeries("Series 1")
ser1.Type = ChartSeriesType.StackingColumn
' specifying group name.
ser1.StackingGroup = "FirstGroup"
Dim ser2 As New ChartSeries("Series 2")
ser2.Type = ChartSeriesType.StackingColumn
' specifying group name.
ser2.StackingGroup = "SecondGroup"
Dim ser3 As New ChartSeries("Series 3")
ser3.Type = ChartSeriesType.StackingColumn
' specifying group name.
ser3.StackingGroup = "FirstGroup"
```

### 4.11 Realtime

Essential Chart is optimized to deal with real time data. It can work with both huge and real time data and render a smooth and dynamic chart using any of the several available chart types.

Essentially, this involves updating the chart's data points list and optionally updating the chart axis ranges if the default ranges are not user-friendly.

While you can use the `ChartSeries.Points` to add new data points to the existing list, for best performance, it's recommended to implement your own "model" to store the data points in real-time scenarios.

A sample application that illustrates this is distributed along with the Essential Chart installation and can be found at:

Sample Location: `<sample installation location>\Syncfusion\EssentialStudio\Version Number\Windows\Chart.Windows\Samples\2.0\Real Time\Chart Recorder`
```


<!-- tags: [Essential Chart, Windows Forms, Realtime Data, Stacking Column Series, Chart Series Type, ChartSeries.Points, Model Implementation, Performance Optimization, Data Points List, Chart Axis Ranges, Sample Application, Installation Location, Chart Recorder] keywords: [Essential Chart, Realtime, Data Points, Performance, Interaction, Dynamic Charts, ChartSeries Type, Group Name, Stacking Group, Model Data points list, Axis range update, Sample application, Chart Recorder] -->
```