```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_272.jpeg
document_name: chart
page_number: 272
page_id: chart#page_272
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:32:37Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Code Snippets for Adding and Customizing a Series

#### C#

```csharp
// This Code Snippet gives the name of the series as Product1
ChartSeries s1 = this.chartControl1.Model.NewSeries();
s1.Type = Syncfusion.Windows.Forms.Chart.ChartSeriesType.Column;
s1.Name = "Product1";
// Points to be added
this.chartControl1.Series.Add(s1);

// Series retrieved using Name
this.chartControl1.Series["Product1"].Style.Symbol.Shape = ChartSymbolShape.Diamond;
this.chartControl1.Series["Product1"].Style.Symbol.Color = Color.Red;
```

#### VB.NET

```vb.net
' This Code Snippet gives the name of the series as Product1
s1 As ChartSeries = Me.chartControl1.Model.NewSeries()
s1.Type = Syncfusion.Windows.Forms.Chart.ChartSeriesType.Column
s1.Name = "Product1"
' Points to be added
Me.chartControl1.Series.Add(s1)

' Series retrieved using Name
Me.chartControl1.Series["Product1"].Style.Symbol.Shape = ChartSymbolShape.Diamond
Me.chartControl1.Series["Product1"].Style.Symbol.Color = Color.Red
```

<!-- tags: [syncfusion, winforms, chart, series, customisation] keywords: [chart series, product1, column chart, symbol shape, color] -->
```