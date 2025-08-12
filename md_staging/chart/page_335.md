```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_335.jpeg
document_name: chart
page_number: 335
page_id: chart#page_335
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:34:36Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Chart Properties Summary

| **Property**                            | **Details**                                                                 |
|-----------------------------------------|-----------------------------------------------------------------------------|
| **Default Value**                       | - MaxX - 0 <br> - MaxY - 0 <br> - MinY - 0 <br> - MinX - 0 <br> - ModelImpl - Nil |
| **2D / 3D Limitations**                | No                                                                         |
| **Applies to Chart Element**           | Any Series                                                                 |
| **Applies to Chart Types**             | All chart types                                                            |

### Summary of Chart Features

Here is a sample code snippet using a Radar chart.

```csharp
// [C#]
string str = this.chartControl1.Series[0].Summary.MaxY.ToString();
string str1 = this.chartControl1.Series[0].Summary.MinY.ToString();
label1.Text = "Summary" + "\n" + " MaxY Value : " + str + "\n" + "MinY Value : " + str1;

// To get percentage value of series point in Pie chart
this.chartControl1.Series[0].Summary.GetYPercentage(1);
this.chartControl1.Series[0].Summary.GetYPercentage(1, 0);
```

```vbnet
' [VB.NET]
Dim str As String = Me.chartControl1.Series(0).Summary.MaxY.ToString()
Dim str1 As String = Me.chartControl1.Series(0).Summary.MinY.ToString()
label1.Text = "Summary" + "" & Chr(10) & "" + " MaxY Value : " + str + "" & Chr(10) & "" + "MinY Value : " + str1

' To get percentage value of series point in Pie chart
this.chartControl1.Series[0].Summary.GetYPercentage(1)
this.chartControl1.Series[0].Summary.GetYPercentage(1, 0)
```
```


<!-- tags: [winforms, radar chart, summary, percentage values, c#, vb.net] keywords: [syncfusion, windows forms, radar chart, maxy, miny, percentage, chartcontrol, series] -->
```