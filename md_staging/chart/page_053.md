```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_053.jpeg
document_name: chart
page_number: 053
page_id: chart#page_053
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:18:46Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Code Example: C#

```csharp
// Binding the ChartDataBindModel with the Series. This is the best
// practise for binding with the large amount of data since it will reduce
// the performance issue of Chart rendering and manipulating data.
series.SeriesModel = dataSeriesModel;

// Since we have specified YNames only for the DataBind model, it will
// take the data source is non indexed model and it will ignore the X
// axis values. We need to assign the X axis values what we need to show on X
// axis by ChartDataBindAxisLableModel separately.
ChartDataBindAxisLabelModel dataLabelsModel = new ChartDataBindAxisLabelModel(populations);

dataLabelsModel.LabelName = "City";

chartControl1.Series.Add(series);
chartControl1.PrimaryXAxis.LabelsImpl = dataLabelsModel;
```

### Code Example: VB.NET

```vb
[VB.NET]

Dim populations As New ArrayList()
populations.Add(New PopulationData("New York", 13))
populations.Add(New PopulationData("Houston", 6))
populations.Add(New PopulationData("Tokyo", 17))
populations.Add(New PopulationData("London", 15))
populations.Add(New PopulationData("Los Angeles", 11))

Dim series As New ChartSeries("Populations")
Dim dataSeriesModel As New ChartDataBindModel(populations)

' If ChartDataBindModel.XName is empty or null, X value is index of point.
' Here I have assigned the property name Population as Y axis name and
' ChartDataBindModel automatically detects the Population property and will
' bind the data from it.
dataSeriesModel.YNames = New String() {"Population"}

' Binding the ChartDataBindModel with the Series. This is the best
' practise for binding with the large amount of data since it will reduce
' the performance issue of Chart rendering and manipulating data.
series.SeriesModel = dataSeriesModel

' Since we have specified YNames only for the DataBind model, it will
' take the data source is non indexed model and it will ignore the X axis
' values. We need to assign the X axis values what we need to show on X
' axis by ChartDataBindAxisLableModel separately.
```

## API Reference

### ChartDataBindModel
- **Properties:**
  - `XName`: Specifies X-axis name.
  - `YNames`: Specifies Y-axis names.
- **Methods:**
  - Automatically detects the property based on the specified axis names.

### ChartDataBindAxisLabelModel
- **Properties:**
  - `LabelName`: Specifies the label name for the axis.

### ChartSeries
- **Properties:**
  - `SeriesModel`: Binds the data to the series.

### ChartControl
- **Methods:**
  - `Add(series)`: Adds a series to the chart.
  - `LabelsImpl`: Assigns the label model to the axis.

## Code Examples Explanation

The examples demonstrate how to bind a large amount of data to a Chart using the `ChartDataBindModel` and `ChartDataBindAxisLabelModel`. This approach optimizes performance by reducing the load on chart rendering and data manipulation.

### Key Points:
1. **Data Binding with ChartDataBindModel:**
   - The `YNames` property is set to `"Population"`, allowing the model to automatically detect and bind the `Population` property.

2. **Axis Label Binding:**
   - The `ChartDataBindAxisLabelModel` is used to specify the `LabelName` as `"City"`, ensuring the X-axis displays the city names correctly.

3. **Series Addition:**
   - The `ChartSeries` is added to the `chartControl1`, and its `SeriesModel` is assigned the `dataSeriesModel`.

4. **X-Axis Label Implementation:**
   - The `PrimaryXAxis.LabelsImpl` is set to the `dataLabelsModel` to display the correct labels on the X-axis.

### Note
- The `ChartDataBindModel.XName` is left empty, meaning the X value is derived from the index of the data points.

<!-- tags: [syncfusion, winforms, chart, databinding, performance, axislabels] keywords: [chartdatabindmodel, chartseries, chartcontrol, xaxis, yaxis, data labels, performance optimization, data binding, winforms chart] -->
```