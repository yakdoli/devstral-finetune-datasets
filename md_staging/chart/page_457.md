```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_457.jpeg
document_name: chart
page_number: 457
page_id: chart#page_457
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:42:54Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```text
' The image will be picked up from this collection
series1.Style.Images = New ChartImageCollection(Me.imageList1.Images)

' Or from this collection, if available
Me.chartControl1.Legend.Items(0).ImageList = New ChartImageCollection(this.imageList1.Images)
```

![Figure 291: Chart Legend Items with Custom Images](./assets/chart_image_custom.jpg "Figure 291: Chart Legend Items with Custom Images")

## Hiding Icons

Icons for legend items can be hidden in any of the following ways:

```csharp
this.chartControl1.Legend.RepresentationType = ChartLegendRepresentationType.None;

// To do this for a specific legend item:

// This will not even allocate any space for the icons
this.chartControl1.Legend.Items[0].ShowIcon = false;

// Or, set this. This will not render the icons, but will allocate some empty space for it
this.chartControl1.Legend.Items[0].Type = ChartLegendItemType.None;
```

```vbnet
Me.chartControl1.Legend.RepresentationType = ChartLegendRepresentationType.None

' To do this for a specific legend item

' This will not even allocate any space for the icons
Me.chartControl1.Legend.Items(0).ShowIcon = False

' Or, set this. This will not render the icons, but will allocate some empty space for it
Me.chartControl1.Legend.Items(0).Type = ChartLegendItemType.None
```

## Page-Level Navigation/TOC (if applicable)
- Essential Chart for Windows Forms
  - Setting Custom Images
  - Hiding Icons

### Cross References
See also: Legend Item Customization, Chart Customization, WinForms Chart Control.

<!-- tags: [WinForms, Chart, Legend, Custom Images, Hiding Icons] keywords: [Essential Chart, Windows Forms, Custom Images, Legend Items, Chart Control] -->
```
