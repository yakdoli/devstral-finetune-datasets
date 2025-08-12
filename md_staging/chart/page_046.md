```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_046.jpeg
document_name: chart
page_number: 046
page_id: chart#page_046
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:18:06Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Content

#### Code Example

```vb
model.XName = "ID"
' The columns that contain the Y values.
model.YNames = New String() {"Population"}

Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Data Bound Series")
series.Text = series.Name
series.SeriesModelImpl = model

series.Style.TextColor = Color.White
series.Style.Font.Bold = True

Me.chartControl1.Series.Add(series)

Me.xAxisLabelModel = New ChartDataBindAxisLabelModel(Me.dataSet11, "Demographics")
' The columns that has the label values for the corresponding X values.
Me.xAxisLabelModel.LabelName = "City"

Me.chartControl1.PrimaryXAxis.LabelsImpl = Me.xAxisLabelModel
Me.chartControl1.PrimaryXAxis.ValueType = ChartValueType.Custom
```

#### Figure: Demographics DataSet bounded to the Chart

![Illustrates DataSet binding to Chart](https://i.imgur.com/ExampleImage.png)

**Figure 25: Demographics DataSet bounded to the Chart**

## API Reference

### Classes and Properties

- `ChartSeries`
- `ChartModel`
- `ChartControl`
  - `Series`
  - `PrimaryXAxis`
    - `LabelsImpl`
    - `ValueType`
- `ChartDataBindAxisLabelModel`

### Methods

- `NewSeries(name As String)`

### Events

- None explicitly mentioned in the code or image.

### See also

- Chapter on Chart Customization
- Documentation on Data Binding in Syncfusion WinForms

<!-- tags: [Syncfusion, WinForms, Chart, DataSet, DataBinding, C#] keywords: [ChartSeries, ChartModel, ChartControl, PrimaryXAxis, ChartDataBindAxisLabelModel, SeriesAdd, DataBinding, DemographicsDataSet] -->
```