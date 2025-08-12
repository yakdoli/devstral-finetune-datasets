```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_256.jpeg
document_name: chart
page_number: 256
page_id: chart#page_256
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:31:43Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Configures a `BubbleChart` with custom images for data points.
- Demonstrates setting image shapes and sizes for series data points.
- Shows how to disable PhongStyle for better visual clarity.

## Content

### Configuring Bubble Chart with Images

`C#`

```csharp
series1.Style.Images = new ChartImageCollection(this.imageList1.Images);
series1.Style.Symbol.ImageIndex = 0;
series1.Style.Symbol.Size = new Size(20, 20);
series1.Style.Symbol.Shape = ChartSymbolShape.Image;

// Disabling PhongStyle
this.chartControl1.Series[0].ConfigItems.BubbleItem.EnablePhongStyle = false;
```

`VB.NET`

```vb
' Setting Images For the Series1
series1.Style.Images = New ChartImageCollection(Me.imageList1.Images)
series1.Style.Symbol.ImageIndex = 0
series1.Style.Symbol.Size = New Size(20, 20)
series1.Style.Symbol.Shape = ChartSymbolShape.Image

' Disabling PhongStyle
Me.chartControl1.Series(0).ConfigItems.BubbleItem.EnablePhongStyle = False
```

### Visual Representation

```html
<figure>
  <img src="bubble_chart_with_image.png" alt="Bubble Chart with Image" />
  <figcaption>Figure 151: Bubble Chart with Image</figcaption>
</figure>
```

### Specific Data Point Setting

You can also specify different image collections for different data points using the following code.

## Code Examples

### Defining Different Images for Data Points
```csharp
// Example of setting up different images for data points
series1.Points[0].ImageIndex = 0;
series1.Points[1].ImageIndex = 1;
series1.Points[2].ImageIndex = 2;

// Additional customization for size and shape
series1.Style.Symbol.Size = new Size(25, 25);
series1.Style.Symbol.Shape = ChartSymbolShape.Image;
```

### Disabling PhongStyle for Improved Visual Clarity
```csharp
this.chartControl1.Series[0].ConfigItems.BubbleItem.EnablePhongStyle = false;
```

## Page-level Navigation/TOC (if applicable)

- Chart with Custom Images
- Disabling PhongStyle
- Setting Different Images for Data Points

### Cross References
- Refer to the related sections on customizing chart series and styles.
- See also: Chart Styling Guidelines for detailed styling options.

<!-- tags: [syncfusion, winforms, chart, bubblechart, image, customize, disable phongstyle] keywords: [series, symbol, shape, imageindex, size, phongstyle, enable, disable, customimage, datapoimg, setting] -->
```