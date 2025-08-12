```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_624.jpeg
document_name: chart
page_number: 624
page_id: chart#page_624
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:53:36Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
Next i 
    csvLine = seriesName + "-" + seriesType + comma + 
              point.X.ToString() + comma + yvaluescsv 
    csvContent += csvLine + vbCr + vbLf 
Next p 
Next series 

' Using stream write class the chart points are exported. Create an instance of the stream writer class. 
Dim file As New System.IO.StreamWriter(fileName) 

' Write the datapoints into the file. 
file.WriteLine(csvContent) 
file.Close()
```

## 5.7 How to filter particular set of data points in the Chart Series

Data is filtered on a series-by-series basis. When series data points are filtered, they can be either removed from the Series Points collection or marked as **Empty**.

Also, you can reflect changes in data by filtering a particular set of data points using the **Grouping Engine**. While using the grouping engine, the main data source for the whole engine can be set. The TableDescriptor will pick up the ItemProperties from the SourceList, and table will be initialized at run time with records from the list. Using the **RecordFilterDescriptor** class, you can filter the chart point values by comparing it against a given constant value. The filtered points will be added to the series.

### Code Example

```csharp
[C#]

// Generating Series 
ChartSeries series = this.chartControl1.Model.NewSeries("Filter Series", ChartSeriesType.Column);
series.Text = series.Name;
list.Clear();
for (int i = 0; i < 10; i++)
{
    a[i] = r.Next(300, 500);
    series.Points.Add(i, a[i]);
    list.Add(new Data(i, a[i]));
}
this.chartControl1.Series.Add(series);
```

## Page-level Navigation/TOC (if applicable)
- Use the Grouping Engine to filter data points.
- Reflect changes in data using the Grouping Engine.
- Use RecordFilterDescriptor to filter chart point values.

## API Reference (if applicable)
- **Namespace**: Syncfusion.WinForms.Chart
- **Class**: ChartControl, ChartSeries
- **Members**: NewSeries, Points, Add, RecordFilterDescriptor

## Code Examples (multi-language supported)
- Sample usage of filtering data points in a chart series.

<!-- tags: [product, winforms, chart, filtering, data points, grouping engine, recordfilterdescriptor] keywords: [series, data points, filtering, grouping engine, recordfilterdescriptor] -->
```