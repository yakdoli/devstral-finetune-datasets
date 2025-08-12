```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_444.jpeg
document_name: chart
page_number: 444
page_id: chart#page_444
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:42:16Z
fidelity: lossless
-->

## Chart Legend Items

Every ChartSeries in the chart control has a ChartLegendItem associated with it. This legend item gets automatically added to the default ChartLegend.

### Using a Custom ChartLegend

But, if you want to get that associated with a custom ChartLegend, use the LegendName to specify that chart legend as follows:

#### C#

```csharp
// Specifies the custom ChartLegend with which this series' legend item
// should be associated with
series1.LegendName = "MyLegend";
```

#### VB.NET

```vb
' Specifies the custom ChartLegend with which this series' legend item
' should be associated with
series1.LegendName = "MyLegend"
```

### Adding Custom Legend Items

To add your own custom legend items to a legend, use the `CustomItems` property in the ChartLegend as follows.

#### C#

```csharp
// Adding some custom items into the 2nd custom Legend

ChartLegendItem legendItem1 = new ChartLegendItem();
legendItem1.ItemStyle.ShowSymbol = true;
legendItem1.ItemStyle.Symbol.Shape = ChartSymbolShape.Circle;
legendItem1.ItemStyle.Symbol.Color = Color.Blue;
legendItem1.Text = "Legend Item";

this.chartControl1.Legends[1].CustomItems = new ChartLegendItem[] { legendItem1 };
```

#### VB.NET

```vb
' Adding some custom items into the 2nd custom Legend

Dim legendItem1 As New ChartLegendItem()
legendItem1.ItemStyle.ShowSymbol = True
legendItem1.ItemStyle.Symbol.Shape = ChartSymbolShape.Circle
legendItem1.ItemStyle.Symbol.Color = Color.Blue
```

#### <!-- tags: [chart, legend, legenditem, chartseries, customlegend, legendname, customitems, syncfusion winforms] keywords: [chart, legend, legenditem, chartseries, customlegend, legendname, customitems] -->
```