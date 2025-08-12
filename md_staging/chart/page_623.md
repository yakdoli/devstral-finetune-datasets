```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_623.jpeg
document_name: chart
page_number: 623
page_id: chart#page_623
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:51:57Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
int pointCount = series.Points.Count;
string seriesType = series.Type.ToString();

for (int p = 0; p < pointCount; p++)
{
    ChartPoint point = series.Points[p];

    string yvaluescsv = String.Empty;
    int count = point.YValues.Length;
    for (int i = 0; i < count; i++)
    {
        yvaluescsv += point.YValues[i];
        if (i != count - 1)
            yvaluescsv += comma;
    }
    csvLine = seriesName + "-" + seriesType + comma + point.X + comma + yvaluescsv;
    csvContent += csvLine + "\r\n";
}
}

// Using stream writer class the chart points are exported. Create an instance of the stream writer class.
System.IO.StreamWriter file = new System.IO.StreamWriter(fileName);

// Write the datapoints into the file.
file.WriteLine(csvContent);
file.Close();
```

## VB.NET

```vb
For Each series In Me.chartControl1.Series
    Dim seriesName As String = series.Name
    Dim pointCount As Integer = series.Points.Count
    Dim seriesType As String = series.Type.ToString()
    Dim p As Integer
    For p = 0 To pointCount - 1
        Dim point As ChartPoint = series.Points(p)
        Dim yvaluescsv As String = String.Empty
        Dim count As Integer = point.YValues.Length
        Dim i As Integer
        For i = 0 To count - 1
            yvaluescsv += point.YValues(i).ToString()
            If i <> count - 1 Then
                yvaluescsv += comma
            End If
```

```html
<!-- tags: [chart, windowsforms, syncfusion, export, csv, pointcount, streamwriter] keywords: [chart, windows forms, series, yvalues, csvexport, steamwriter, seriesname, seriesType, points] -->
``` 
