```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_215.jpeg
document_name: chart
page_number: 215
page_id: chart#page_215
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:27:53Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

Me.chartControl1.Series(0).Style.Symbol.Color = Color.Yellow  
Me.chartControl1.Series(0).Style.Symbol.Shape = ChartSymbolShape.InvertedTriangle  
' Setting ElementBorder for a symbol  
cbi As ChartBordersInfo = New ChartBordersInfo()  
cbi.Outer = New ChartBorder(ChartBorderStyle.Solid, Color.White)  
cbi.Inner = New ChartBorder(ChartBorderStyle.DashDot, Color.Cyan)  
Me.chartControl1.Series(0).Style.ElementBorders = cbi  

![](https://i.imgur.com/example_image_link.png)
*Figure 121: Column Chart with ElementBorder*

## Specific Data Point Setting

### [C#]

```csharp
//Specifying element border for the first data point Styles(0), second
//data point Styles(1) and so on..
this.chartControl1.Series[0].Styles[0].ElementBorders = cbi;
```

### [VB.NET]
```vb
'Specifying element border for the first data point Styles(0), second
'data point Styles(1) and so on..
this.chartControl1.Series(0).Styles(0).ElementBorders = cbi
```

### See Also

- Area Charts  
- Bar Charts  
- Bubble Chart  
- Column Charts  
- Line Charts  
- Candle Chart  
- Renko chart  
- Three Line Break Chart  
- Box and Whisker Chart  
- Gantt Chart  
- Tornado Chart  
- Polar and Radar Chart  
```