```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_453.jpeg
document_name: chart
page_number: 453
page_id: chart#page_453
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:42:41Z
fidelity: lossless
-->

### Essential Chart for Windows Forms

```vb.net
[VB.NET]

'The general setting affecting all Legend items could be anything
Me.chartControl1.Legend.RepresentationType = 
ChartLegendRepresentationType.SeriesImage

'This will force a specific legend item to show a series icon
Me.chartControl1.Legend.Items(0).DrawSeriesIcon = True
```

### Series Symbol

You can also choose to show the exact same symbol that is shown in the data points in a series.

To do this for all the legend items:

```csharp
[C#]

//Set symbol for first series
this.chartControl1.Series[0].Style.Symbol.Shape = 
ChartSymbolShape.Diamond;
this.chartControl1.Series[0].Style.Symbol.Color = Color.Red;
this.chartControl1.Series[0].Style.Symbol.Size = new Size(7, 7);

//This will cause the legend to render with the same symbol defined above.
this.chartControl1.Legend.ShowSymbol = true;

//Setting RepresentationType to None to hide other representations
this.chartControl1.Legend.RepresentationType = 
ChartLegendRepresentationType.None;
```

```vb.net
[VB.NET]

'Set symbol for first series
Me.chartControl1.Series(0).Style.Symbol.Shape = 
ChartSymbolShape.Diamond
Me.chartControl1.Series(0).Style.Symbol.Color = Color.Red
Me.chartControl1.Series(10).Style.Symbol.Size = New Size(7, 7)

'This will cause the legend to render with the same symbol defined above.
Me.chartControl1.Legend.ShowSymbol = True

'Setting RepresentationType to None to hide other representations
Me.chartControl1.Legend.RepresentationType =
```

### Footer
© 2013 Syncfusion. All rights reserved. | 453
```