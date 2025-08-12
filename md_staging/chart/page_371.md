```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_371.jpeg
document_name: chart
page_number: 371
page_id: chart#page_371
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:36:34Z
fidelity: lossless
-->

## Creating and Customizing the Custom Point.

[C#]

```csharp
// Point that follows a series point:
ChartCustomPoint cp = new ChartCustomPoint();

// Gets the series index and point index if the Customtype is PointFollow.
cp.PointIndex = 1;
cp.SeriesIndex = 0;

// Specifies the text of the custom point.
cp.Text = "Custom Point";

// Specifies the custom type.
chartCustomPoint1.CustomType = Syncfusion.Windows.Forms.Chart.ChartCustomPointType.PointFollow;

// Specifies the shape of the custom point symbol.
cp.Symbol.Shape = ChartSymbolShape.Diamond;

// Specifies the color of the custom point.
chartCustomPoint1.Symbol.Color = Color.Khaki;

// Setting X-value and Y- value
chartCustomPoint1.XValue = 1;
chartCustomPoint1.YValue = 370;

// Setting the font properties
chartCustomPoint1.Color = System.Drawing.SystemColors.ButtonHighlight;
chartCustomPoint1.Font.Bold = true;
chartCustomPoint1.Font.Facename = "Verdana";
chartCustomPoint1.Font.Size = 10F;
```

[VB.NET]

```vb
' Point that follows a series point:
cp As ChartCustomPoint = New ChartCustomPoint()

' Gets the series index and point index if the Customtype is PointFollow.
cp.PointIndex = 1
cp.SeriesIndex = 0

' Specifies the text of the custom point.
```

<!-- tags: [syncfusion, winforms, chartcustompoint, custompointtype, pointfollow, chart, chartcustompointtype, seriesindex, pointindex, symbolshape, color, font, customtype] -->
```