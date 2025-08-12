```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_167.jpeg
document_name: chart
page_number: 167
page_id: chart#page_167
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:25:11Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
//To customize the marker color to low points
Me.sparkLine1.Markers.LowPointColor = new
BrushInfo(GradientStyle.BackwardDiagonal, Color.Blue, Color.Wheat)
```

![Figure 93: Markers for Column SparkLine](images/figure_93_markers_for_column_sparkline.png)

## Markers Support for WinLoss

**Markers Support for WinLoss**

This marker feature supports High Points, Low Points, Start Point, and Negative Point of WinLoss Sparkline. The markers feature of WinLoss is the same as Column markers. You can choose the marker color for data points.

Refer to the following code snippets to enable the marker in column sparkline.

### C#.NET

```csharp
//To enable marker to sparkline high,low,start,end,negative data points
this.sparkLine1.Markers.ShowHighPoint = true;
this.sparkLine1.Markers.ShowLowPoint = true;
this.sparkLine1.Markers.ShowStartPoint = true;
this.sparkLine1.Markers.ShowEndPoint = true;
this.sparkLine1.Markers.ShowNegativePoint = true;

//To customize the marker color to low points
this.sparkLine1.Markers.LowPointColor = new
BrushInfo(GradientStyle.BackwardDiagonal, Color.Blue, Color.Wheat);
```

### VB.NET

```vb
//To enable marker to sparkline high,low,start,end,negative data points
```

## Page-level Metadata
- **Source:** Image
- **Domain:** syncfusion-sdk
- **Task:** pdf-ocr-to-markdown
- **Language:** en
- **Source Filename:** page_167.jpeg
- **Document Name:** chart
- **Page Number:** 167
- **Page ID:** chart#page_167
- **Product:** Syncfusion Winforms
- **Version:** 11.4.0.26
- **Timestamp:** 2025-08-09T03:25:11Z
- **Fidelity:** lossless

<!-- tags: [chart, WinForms, Windows Forms, Sparkline, Markers, High Points, Low Points, Start Point, End Point, Negative Point, GradientBrush, Color, marker customization, WinLoss, Column Sparkline] keywords: [Winforms, Sparkline, Markers, High Points, Low Points, Start Point, End Point, Negative Point, GradientBrush, Color] -->
```