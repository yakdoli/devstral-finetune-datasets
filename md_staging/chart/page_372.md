```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_372.jpeg
document_name: chart
page_number: 372
page_id: chart#page_372
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:37:58Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
cp.Text = "Custom Point"
```

```csharp
'Specifies the custom type.
chartCustomPoint1.CustomType =
Syncfusion.Windows.Forms.Chart.ChartCustomPointType.PointFollow

'Specifies the shape of the custom point symbol.
cp.Symbol.Shape = ChartSymbolShape.Diamond

'Specifies the color of the custom point.
cp.Symbol.Color = Color.Khaki

//Setting X-value and Y- value
chartCustomPoint1.XValue = 1
chartCustomPoint1.YValue = 370

'Setting the font properties
chartCustomPoint1.Color = System.Drawing.SystemColors.ButtonHighlight
chartCustomPoint1.Font.Bold = true
chartCustomPoint1.Font.Name = "Verdana"
chartCustomPoint1.Font.Size = 10F
```

**Note:** You can also customize a custom point symbol using the `Symbol` property.

- Adding Custom Point to the Chart.

```csharp
[C#]
// Adds the custom point to the collection.
this.chartControl1.CustomPoints.Add(cp);
```

```vb
[VB.NET]
' Adds the custom point to the collection.
Me.chartControl1.CustomPoints.Add(cp)
```

## Custom point types

| CustomPoint types       | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| PointFollow             | This custom point will follow the regular points of any series, to which it is assigned. |

---

© 2013 Syncfusion. All rights reserved. Page 372

<!-- tags: [product, Syncfusion Winforms, chart, custom points, types, Windows Forms] keywords: [custom point symbols, ChartCustomPointType, CustomPoint, SymbolShape, Font,シリーズフォローポイント] -->
```