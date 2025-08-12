```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_631.jpeg
document_name: chart
page_number: 631
page_id: chart#page_631
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:52:23Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Content
### Adding Data to a Chart
```csharp
DateTime start = new DateTime(2006, 11, 1);
ChartSeries series = this.chartControl1.Model.NewSeries("");
series.Points.Add(start.AddDays(7), 363);
series.Points.Add(start.AddDays(14), 417);
```

```vb.net
Dim start As DateTime = New DateTime(2006, 11, 1)
ChartSeries series = Me.chartControl1.Model.NewSeries("")
series.Points.Add(start.AddDays(7), 363)
series.Points.Add(start.AddDays(14), 417)
```

### 5.14 How to set the Color Palette for a Chart

**ChartColorPalette.Color** property can be used to specify the color palettes for the **Chart.ColorPalette** class. Apart from specifying predefined palettes, you can specify your own palette colors using the **Custom** style in the ChartColorPalette.

#### Specifying a Custom Color Palette in C#
```csharp
// Specify a custom color.
this.chartControl1.CustomPalette = new System.Drawing.Color []
{ 
    System.Drawing.Color.FromArgb(((int)((byte)(255)))),
    ((int)((byte)(203))),
    ((int)((byte)(216))), System.Drawing.Color.FromArgb(((int)((byte)(22
2))),
    ((int)((byte)(209))),
    ((int)((byte)(248))), System.Drawing.Color.FromArgb(((int)((byte)(25
0))),
    ((int)((byte)(155))), ((int)((byte)(155))))
};
this.chartControl1.Palette = ChartColorPalette.Custom;
```

#### Specifying a Custom Color Palette in VB.NET
```vb.net
' Specify a custom color.
Me.chartControl1.CustomPalette = New System.Drawing.Color()
{ 
    System.Drawing.Color.FromArgb((CInt(Fix((CByte(255)))),
    (CInt(Fix((CByte(203)))),
    (CInt(Fix((CByte(216))))))), System.Drawing.Color.FromArgb((CInt(Fix((CBy
te(222)))),
    (CInt(Fix((CByte(209))),
    (CInt(Fix((CByte(248))))))),
    System.Drawing.Color.FromArgb((CInt(Fix((CByte(250)))))
    (CInt(Fix((CByte(155)))),
    (CInt(Fix((CByte(155))))))
}
Me.chartControl1.Palette = ChartColorPalette.Custom
```

---

## Page-level Navigation/TOC
- [4.14 How to set the Color Palette for a Chart](#5.14-how-to-set-the-color-palette-for-a-chart)

## Cross References
- See also: Chart, ChartColorPalette, ChartColorPalette.Custom, ColorPalette

## RAG Annotations
<!-- tags: [chart, colorpalette, customcolors, winforms] keywords: [ChartColorPalette, Custom, ColorPalette, Chart, Palette, addDays] -->
```