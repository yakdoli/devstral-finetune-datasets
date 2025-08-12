```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Syncfusion WinForms Documentation</title>
</head>
<body>
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_320.jpeg
document_name: chart
page_number: 320
page_id: chart#page_320
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:35:19Z
fidelity: lossless
-->

<h3>Essential Chart for Windows Forms</h3>

<table>
    <thead>
        <tr>
            <th>2D / 3D Limitations</th>
            <th>No</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Applies to Chart Element</td>
            <td>Any Series</td>
        </tr>
        <tr>
            <td>Applies to Chart Types</td>
            <td>Histogram Chart</td>
        </tr>
    </tbody>
</table>

<p>Here is sample code snippet using <code>ShowHistogramDataPoints</code>.</p>

<h3>[C#]</h3>

```csharp
this.chartControl1.Series[0].ShowHistogramDataPoints = true;
```

<h3>[VB.NET]</h3>

```vbnet
Private Me.chartControl1.Series(0).ShowHistogramDataPoints = True
```

<div style="text-align: center;">
    <img src="chart_image.png" alt="Histogram Chart with ShowHistogramDataPoints set to True">
    <p>Figure 200: ShowHistogramDataPoints set to True</p>
</div>

</body>
</html>
<!-- tags: [Syncfusion Winforms, chart, histogram chart, ShowHistogramDataPoints] keywords: [chart control, histogram chart, data points, C#, VB.NET, sample code, essential chart, windows forms, Series[0], Series(0), chartControl1] -->
```