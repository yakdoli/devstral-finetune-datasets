```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_617.jpeg
document_name: chart
page_number: 617
page_id: chart#page_617
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:53:25Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## 5 Frequently Asked Questions

This section guides you with the features of the Chart control based on specific tasks.

### 5.1 How to add custom TrendLine in Chart

TrendLines are used to draw lines in the ChartArea. They can be added to the chart using the TrendLineAdder class.

TrendLines can also be drawn using the Mouse Events. In this case, you will have to make use of the Utility class to listen to mouse events and convert them into trendlines. You can draw any number of trendlines, and can set different colors to differentiate them.

#### C#

```csharp
// Creating Custom Points
ChartPoint ptStart = this.chart.ChartArea.GetValueByPoint(start);
ChartPoint ptEnd = this.chart.ChartArea.GetValueByPoint(end);
ChartSeries tseries = this.chart.Model.NewSeries("TrendLine", ChartSeriesType.Line);
tseries.Points.Add(ptStart);
tseries.Points.Add(ptEnd);
this.chart.Series.Add(tseries);
tseries.LegendItem.Visible = false;

// Specify the color for the lines.
tseries.Style.Interior = new Syncfusion.Drawing.BrushInfo(ptStart.YValues[0] < ptEnd.YValues[0] ? Color.DarkGreen : Color.Red);
```

#### VB.NET

```vb
' Creating Custom Points
Dim tlineAdder As TrendLineAdder
Dim ptStart As ChartPoint = Me.chart.ChartArea.GetValueByPoint(start)
Dim ptEnd As ChartPoint = Me.Chart.ChartArea.GetValueByPoint(end_Renamed)
Dim tseries As ChartSeries = Me.chart.Model.NewSeries("TrendLine", ChartSeriesType.Line)
tseries.Points.Add(ptStart)
```
```