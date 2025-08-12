```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_045.jpeg
document_name: chart
page_number: 045
page_id: chart#page_045
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:18:18Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Content

### Chart Data Binding Example

```csharp
ChartDataBindModel model = null;
ChartDataBindAxisLabelModel xAxisLabelModel = null;

// A custom DataSet bound to the Demographics table
private ChartAccessDataBind.DataSet1 dataSet1;

this.oleDbDataAdapter1.Fill(this.dataSet1.Demographics);

model = new ChartDataBindModel(this.dataSet1, "Demographics");
// The column that contains the X values.
model.XName = "ID";
// The columns that contain the Y values.
model.YNames = new string[] { "Population" };

ChartSeries series = this.chartControl1.Model.NewSeries("Data Bound Series");
series.Text = series.Name;
series.SeriesModelImpl = model;

series.Style.TextColor = Color.White;
series.Style.Font.Bold = true;

this.chartControl1.Series.Add(series);

this.xAxisLabelModel = new ChartDataBindAxisLabelModel(this.dataSet1, "Demographics");
// The columns that have the label values for the corresponding X values.
this.xAxisLabelModel.LabelName = "City";

this.chartControl1.PrimaryXAxis.LabelsImpl = this.xAxisLabelModel;
this.chartControl1.PrimaryXAxis.ValueType = ChartValueType.Custom;
```

```vb
[VB.NET]

Dim model As ChartDataBindModel = Nothing
Dim xAxisLabelModel As ChartDataBindAxisLabelModel = Nothing

' A custom DataSet bound to the Demographics table
Private dataSet1 As ChartAccessDataBind.DataSet1

Me.oleDbDataAdapter1.Fill(Me.dataSet1.Demographics)

model = New ChartDataBindModel(Me.dataSet1, "Demographics")
' The column that contains the X values.
```

## API Reference

### ChartDataBindModel

- **Properties**
  - `XName`: Indicates the X values.
  - `YNames`: Indicates the Y values.
  
### ChartDataBindAxisLabelModel

- **Properties**
  - `LabelName`: Indicates the label values for the corresponding X values.

## Code Examples

### C# Example

```csharp
ChartDataBindModel model = new ChartDataBindModel(dataSet1, "Demographics");
model.XName = "ID";
model.YNames = new string[] { "Population" };

ChartSeries series = new ChartSeries("Data Bound Series");
series.SeriesModelImpl = model;

this.chartControl1.Series.Add(series);
```

### VB.NET Example

```vb
Dim model As New ChartDataBindModel(Me.dataSet1, "Demographics")
model.XName = "ID"
model.YNames = New String() { "Population" }

Dim series As New ChartSeries("Data Bound Series")
series.SeriesModelImpl = model

Me.chartControl1.Series.Add(series)
```

## Related Topics

- Data binding in Syncfusion WinForms chart
- Customizing axis labels
- Adding series to the chart

<!-- tags: [Syncfusion WinForms, chart, data binding, axis labels, series] keywords: [ChartDataBindModel, ChartDataBindAxisLabelModel, ChartSeries, Data Binding, XAxis, YAxis, LabelsImpl, ValueType] -->
```