```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_260.jpeg
document_name: chart
page_number: 260
page_id: chart#page_260
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:32:02Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Content
- This page explains how to use gradient control and specific data point settings in charts for Windows Forms.

### Specific Data Point Setting
You can also set the interior color for individual data points using the `Series.Styles[0].Interior` property.

[C#]

```csharp
this. chartControl1.Series[0].Styles[0].Interior = new
BrushInfo(GradientStyle.Horizontal ,Color.AliceBlue, Color.Green);
this. chartControl1.Series[0].Styles[1].Interior = new
BrushInfo(GradientStyle.Horizontal ,Color.Blue, Color.AliceBlue);
```

[VB.NET]

```vb
Me. chartControl1.Series(0).Styles[0].Interior = New
BrushInfo(GradientStyle.Horizontal,Color.AliceBlue, Color.Green)
Me. chartControl1.Series(0).Styles[1].Interior = New
BrushInfo(GradientStyle.Horizontal,Color.Blue, Color.AliceBlue)
```

### PieChart Specific

When rendering pie charts, it's sometimes very helpful to render a patterned background for each slice, while printing the pie on a gray scale printer. You can do so easily as shown below. The code here is for a Pie Chart series with 4 points.

[C#]

```csharp
// Code will be added here
```

## Page-level Navigation/TOC (if applicable)
- If there's a local Table of Contents, it should appear here. Evaluate and include if present.

## Cross References
- See also: [unclear] (include relevant cross-references if present).

<!-- tags: [chart, windows forms, gradient control, pie chart, data point setting] keywords: [Work Load, Series 1, Series 2, GradientStyle.Horizontal, AliceBlue, Green, Blue, Patterned background, Pie Chart series, gray scale printer] -->
```
