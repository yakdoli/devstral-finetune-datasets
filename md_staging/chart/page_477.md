```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_477.jpeg
document_name: chart
page_number: 477
page_id: chart#page_477
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:44:10Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Chart Series Highlighting

You can also highlight a particular chart series alone while mouse hovering, and make the other series transparent. For this, you need to set **SeriesHighlight** property to **true**. The series can also be highlighted by hovering the mouse over a legend item corresponding to a particular series.

The following table describes properties related to this feature.

| Property                | Description                                                                                   |
|-------------------------|-----------------------------------------------------------------------------------------------|
| HighlightInterior       | Sets the highlight color for the series.                                                     |
| HiddenInterior          | Controls the transparency of the non-highlighted series. While mouse hovering on a particular series, all other series will be set with the color specified in this property. |
| SeriesHighlightIndex   | If you want to highlight only a particular series alone, you need to set the index value for this property. The default value is **-1**. |

**Note**: The AutoHighlight property should be disabled to enable this chart series highlighting feature.

### Code Examples

#### C#

```csharp
this.chartControl1.SeriesHighlight = true;
this.chartControl1.Series[0].Style.HighlightInterior = new BrushInfo(Color.Gold);
BrushInfo bi = new BrushInfo(GradientStyle.Vertical, Color.Red, Color.Red);
this.chartControl1.Series[0].Style.HiddenInterior = new BrushInfo(0, bi);
```

#### VB.NET

```vb
Me.chartControl1.SeriesHighlight = True
Me.chartControl1.Series(0).Style.HighlightInterior = New BrushInfo(Color.Gold)
Dim bi As New BrushInfo(GradientStyle.Vertical, Color.Red, Color.Red)
Me.chartControl1.Series(0).Style.HiddenInterior = New BrushInfo(0, bi)
```

## Page-level Metadata
© 2013 Syncfusion. All rights reserved.

<!-- tags: [chart, series, highlight, hover, transparency, legend, autohighlight, syncfusion. winforms, version 11.4.0.26] keywords: [chart series, mouse hover, highlight, transparency, legend, autohighlight, syncfusion] -->
```