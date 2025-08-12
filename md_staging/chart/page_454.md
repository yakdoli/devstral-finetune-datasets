```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_454.jpeg
document_name: chart
page_number: 454
page_id: chart#page_454
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:44:59Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### ChartLegendRepresentationType.None

![Illustrates Symbol Settings](https://via.placeholder.com/150x150)

> **Figure 288:** Legend Items rendered with the Same Symbol

#### Custom Representation Icon

You can also choose to use one of the built-in representation icons in the legend items.

To do this for all the legend items:

#### Code Example in C#

```csharp
this.chartControl1.Legend.RepresentationType =
    ChartLegendRepresentationType.Diamond;

// To specify a custom color for the interior of the icon
this.chartControl1.Legend.Items[0].Interior = new
    BrushInfo(Color.Violet);
```

#### Code Example in VB.NET

```vbnet
Me.chartControl1.Legend.RepresentationType =
    ChartLegendRepresentationType.Diamond

'To specify a custom color for the interior of the icon
Me.chartControl1.Legend.Items(0).Interior = New
    BrushInfo(Color.Violet)
```

### Footer
© 2013 Syncfusion. All rights reserved.

<!-- tags: [syncfusion, winforms, chart, chartlegendrepresentationtype, legend, customrepresentationicon, built-inicon, symbols, legenditems, diamond] keywords: [chartlegendrepresentationtype, legend, custom icon, built-in, diamond, color, interior, brushinfo, syncfusion, winforms] -->
```
