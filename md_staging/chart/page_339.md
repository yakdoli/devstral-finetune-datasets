```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_339.jpeg
document_name: chart
page_number: 339
page_id: chart#page_339
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:34:49Z
fidelity: lossless
-->

### Essential Chart for Windows Forms

```csharp
this.chartControl1.Series[0].Styles[1].Symbol.Size = new Size(9, 9);
this.chartControl1.Series[0].Styles[1].Symbol.Offset = new Size(1, 20);

//Used to set the Color of the Symbol border.
this.chartControl1.Series[0].Styles[0].Symbol.Border.Color = Color.Blue;
//Used to set the Width of the Symbol border.
this.chartControl1.Series[0].Styles[0].Symbol.Border.Width = 3;
//Used to set the Alignment of the Symbol border.
this.chartControl1.Series[0].Styles[0].Symbol.Border.Alignment = PenAlignment.Outset;
//Used to set the Dash style of the Symbol Border.
this.chartControl1.Series[0].Styles[0].Symbol.Border.DashStyle = DashStyle.Solid;
```

### [VB.NET]

```vb
Private Me.chartControl1.Series(0).Styles(0).Symbol.Shape = ChartSymbolShape.Diamond
Private Me.chartControl1.Series(0).Styles(0).Symbol.Color = Color.Green
Private Me.chartControl1.Series(0).Styles(0).Symbol.Size = New Size(10, 10)
Private Me.chartControl1.Series(0).Styles(0).Symbol.Offset = New Size(1, 20)

Private Me.chartControl1.Series(0).Styles(1).Symbol.Shape = ChartSymbolShape.Hexagon
Private Me.chartControl1.Series(0).Styles(1).Symbol.Color = Color.Yellow
Private Me.chartControl1.Series(0).Styles(1).Symbol.Size = New Size(9, 9)
Private Me.chartControl1.Series(0).Styles(1).Symbol.Offset = New Size(1, 20)

'Used to set the Color of the Symbol border.
Private Me.chartControl1.Series(0).Styles[0].Symbol.Border.Color = Color.Blue
'Used to set the Width of the Symbol border.
Private Me.chartControl1.Series(0).Styles[0].Symbol.Border.Width = 3
'Used to set the Alignment of the Symbol border.
Private Me.chartControl1.Series(0).Styles[0].Symbol.Border.Alignment = PenAlignment.Outset
'Used to set the Dash style of the Symbol Border.
Private Me.chartControl1.Series(0).Styles[0].Symbol.Border.DashStyle = DashStyle.Solid
```

## See Also

---
```

<!-- tags: [Syncfusion Winforms, Essential Chart, Symbol Customization, VB.NET, C#] -->
```