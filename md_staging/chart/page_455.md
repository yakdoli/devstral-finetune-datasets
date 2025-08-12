```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_455.jpeg
document_name: chart
page_number: 455
page_id: chart#page_455
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:41:56Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

![Figure: Legend Item with a Custom Representation Icon](image.png)

*Figure 289: Legend Item with a Custom Representation Icon*

To do the above only on specific legend items, use the `ChartLegendItem.Type` property.

## More Symbol Shapes

ChartLegendItem has the `Symbol` property, using which we can customize the symbols for particular legend items. This setting overrides the `Series[0].Style.Symbol` settings.

### Code Examples

#### C#

```csharp
//Series symbol settings
chartControl1.Legend.ShowSymbol = true;
chartControl1.Series[0].Style.Symbol.Shape = ChartSymbolShape.Diamond;
chartControl1.Series[0].Style.Symbol.Color = Color.AliceBlue;

//the above symbol settings is overridden by the following settings
chartControl1.Legend.Items[0].Symbol.Shape = ChartSymbolShape.Triangle;
chartControl1.Legend.Items[0].Symbol.Color = Color.Yellow;
```

#### VB.NET

```vb
'Series symbol settings
chartControl1.Legend.ShowSymbol = True
chartControl1.Series(0).Style.Symbol.Shape = ChartSymbolShape.Diamond
chartControl1.Series(0).Style.Symbol.Color = Color.AliceBlue

'the above symbol settings is overridden by the following settings
chartControl1.Legend.Items[0].Symbol.Shape = ChartSymbolShape.Triangle
chartControl1.Legend.Items[0].Symbol.Color = Color.Yellow
```
```html
<!-- tags: [chart, legend, symbol, shape, customization, override, winforms, syncfusion, series, properties] keywords: [chart legend, symbol shape, custom representation, legend item, override settings, Syncfusion Winforms, series properties, ChartSymbolShape, ShowSymbol] -->
```