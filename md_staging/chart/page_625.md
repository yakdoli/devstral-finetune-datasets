```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_625.jpeg
document_name: chart
page_number: 625
page_id: chart#page_625
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:53:56Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Content

### WinForms Chart Data Binding

#### C#

```csharp
// Bind it to the model
Engine group = new Engine();
group.SetSourceList(list);
ExpressionFieldDescriptor exp = new ExpressionFieldDescriptor();
exp.Expression = "[Y] > " + this.textBox1.Text.ToString();
RecordFilterDescriptor rfd = new RecordFilterDescriptor(exp.Expression);
group.TableDescriptor.RecordFilters.Add(rfd);
System.Diagnostics.Trace.WriteLine("Filtered Record Count:" + group.Table.FilteredRecords.Count);
System.Diagnostics.Trace.WriteLine("Values greater than 30:");

// Filtering Data
this.chartControl1.Series[0].Points.Clear();
int j = 0;
foreach (Record rec in group.Table.FilteredRecords)
{
    string b = rec.GetData().ToString();
    System.Diagnostics.Trace.WriteLine(b);
    this.chartControl1.Series[0].Points.Add(j, Convert.ToDouble(b));
    j++;
}
this.label2.Text = "Number of Filtered points: " + group.Table.FilteredRecords.Count.ToString();
```

#### VB.NET

```vb
' Generating Series
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Filter Series", ChartSeriesType.Column)
series.Text = series.Name
list.Clear()
For i As Integer = 0 To 9
    a(i) = r.Next(300, 500)
    series.Points.Add(i, a(i))
    list.Add(New Data(i, a(i)))
Next i
Me.chartControl1.Series.Add(series)

' Bind it to the model
Dim group As Engine = New Engine()
group.SetSourceList(list)
Dim exp As ExpressionFieldDescriptor = New ExpressionFieldDescriptor()
exp.Expression = "[Y] > " & Me.textBox1.Text.ToString()
Dim rfd As RecordFilterDescriptor = New RecordFilterDescriptor(exp.Expression)
```

## Page-level Navigation/TOC (if applicable)

- This page describes how to bind data to a chart in the Syncfusion Winforms library using both C# and VB.NET. It demonstrates filtering the data based on a condition and visualizing it using the essential chart control.

## Cross References

- See also: DataSeries, ExpressionFieldDescriptor, RecordFilterDescriptor, Engine, chartControl1, TextBox, Label.

<!-- tags: chart, windows forms, data binding, filter, essential chart, Syncfusion, Winforms, C#, VB.NET keywords: essentialchart, windowsforms, databinding, filtering, syncfusionwinforms, csharp, vb.net -->
```