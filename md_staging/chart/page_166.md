```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_166.jpeg
document_name: chart
page_number: 166
page_id: chart#page_166
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:25:14Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Content
### Markers Support for Column

This marker feature supports High Points, Low Points, Start Point and Negative Point of column sparkline. You can choose the marker color for data points.

Refer to the following code snippets to enable the marker in column sparkline.

#### [C#.NET]

```csharp
//To enable marker to sparkline high, low, start, end, negative data points
this.sparkLin1.Markers.ShowHighPoint = true;
this.sparkLin1.Markers.ShowLowPoint = true;
this.sparkLin1.Markers.ShowStartPoint = true;
this.sparkLin1.Markers.ShowEndPoint = true;
this.sparkLin1.Markers.ShowNegativePoint = true;

//To customize the marker color to low points
this.sparkLin1.Markers.LowPointColor = new
BrushInfo(GradientStyle.BackwardDiagonal, Color.Blue, Color.Wheat);
```

#### [VB.NET]

```vb
//To enable marker to sparkline high, low, start, end, negative data points
Me.sparkLin1.Markers.ShowHighPoint = True
Me.sparkLin1.Markers.ShowLowPoint = True
Me.sparkLin1.Markers.ShowStartPoint = True
Me.sparkLin1.Markers.ShowEndPoint = True
Me.sparkLin1.Markers.ShowNegativePoint = True
```

## Images
**Figure 92: Marker for Line SparkLine**
![Marker for Line SparkLine](attachment://image.png)

## Footer
© 2013 Syncfusion. All rights reserved.  
**166 | Page**

<!-- tags: [product, chart, Windows Forms, markers, column sparkline, Syncfusion Winforms, version] keywords: [marker feature, high points, low points, start point, negative point, marker color, code snippets, customization, gradient style, blue, wheat] -->
```