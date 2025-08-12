```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_244.jpeg
document_name: chart
page_number: 244
page_id: chart#page_244
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:31:06Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

Here is some sample code.

## Adjusting Box Size in Chart Series

### C#

```csharp
this.chartControl1.Series[0].HeightBox = 2f;
```

### VB.NET

```vb.net
Me.chartControl1.Series(0).HeightBox = 2f
```

### Chart Visualization

The following chart demonstrates the effect of setting the box size to 1 (default).

#### Figure 143: PointAndFigure Chart with Box Size of 1 (Default)

![Stock Price Summary](https://via.placeholder.com/600x400?text=Stock+Price+Summary)

The chart shows daily stock price data for a month, with the price range and fluctuations illustrated using box plot markers. This example highlights how adjusting the box size can impact the visual representation of data trends.

## API Reference

The `HeightBox` property of the `Series` class in `Syncfusion.Windows.Forms.DataVisualization.Charting` is used to define the height of the box plot markers. This property is particularly useful in adjusting the visual representation for charts like PointAndFigure.

### Key Methods and Properties

- **HeightBox**: Sets the height of the box plot markers in the chart series.

## Code Examples

### Example 1: Setting Box Height in C#
```csharp
this.chartControl1.Series[0].HeightBox = 3f;
```

### Example 2: Setting Box Height in VB.NET
```vb.net
Me.chartControl1.Series(0).HeightBox = 3f
```

## Page-level Navigation/TOC

- [Sample Code Examples](#chart#page_244#sample-code-examples)
- [Chart Visualization](#chart#page_244#chart-visualization)
- [API Reference](#chart#page_244#api-reference)
- [Code Examples](#chart#page_244#code-examples)

<!-- tags: [chart, pointandfigure, boxsize, windowsforms, syncfusion] keywords: [chart control, box plot, stock price, visualization, api reference, sample code] -->
```