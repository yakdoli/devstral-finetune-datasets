```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_278.jpeg
document_name: diagram
page_number: 278
page_id: diagram#page_278
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T04:25:41Z
fidelity: lossless
-->

## Getting the Nearest Grid Point on a Diagram

### Overview
This section explains how to utilize the `GetNearestGridPoint` method to find the nearest grid point on a diagram based on a given point.

### Content

#### 5.19 How to Get the Nearest Grid Point on a Diagram

The `GetNearestGridPoint` method can be used to get the nearest grid point on a diagram based on a given point.

This method has the following two parameters:
- **Point** - specifies the location which calculates the nearest grid point.
- **Int** - specifies the ruler height.

The following code snippet illustrates the implementation of the `GetNearestGridPoint` method:

##### C#
```csharp
//Current mouse position
Point ptMouse = new Point(e.X, e.Y);
int rulerHeight = (diagram1.ShowRulers) ? diagram1.RulersHeight : 0;
//Nearest grid point
Point ptGridNearestPoint = diagram1.View.Grid.GetNearestGridPoint(ptMouse, rulerHeight);
```

##### VB.NET
```vb
'Current mouse position
Dim ptMouse As Point = New Point(e.X, e.Y)
Dim rulerHeight As Integer
rulerHeight = If(diagram1.ShowRulers, diagram1.RulersHeight, 0)
```

## Page-level Navigation/TOC
- [5.19 How to Get the Nearest Grid Point on a Diagram](#page_278#how-to-get-the-nearest-grid-point-on-a-diagram)

<!-- tags: [syncfusion, winforms, getnearestgridpoint, grid, point, diagram] keywords: [nearest grid point, diagram, ruler height, point, getnearestgridpoint method, c#, vb.net, grid, point] -->
```