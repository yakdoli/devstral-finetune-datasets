```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_395.jpeg
document_name: chart
page_number: 395
page_id: chart#page_395
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:38:02Z
fidelity: lossless
-->

## Rect

| Rect | Specifies the rectangle that includes the axis and it's labels. This provides great flexibility in letting you customize the position and size of the axes. |
| --- | --- |

## Illustrating Custom Axis Location

![Setting Location for Y-Axis](https://i.imgur.com/ANORMAL.png)

**Figure 254: Chart Axis with Location Properties Set**

### C#

```csharp
this.chartControl1.PrimaryYAxis.LocationType = Syncfusion.Windows.Forms.Chart.ChartAxisLocationType.Set;
this.chartControl1.PrimaryYAxis.Location = new PointF(15, 200);
```

### VB

```vb
Me.ChartControl1.PrimaryYAxis.LocationType = Syncfusion.Windows.Forms.Chart.ChartAxisLocationType.Set
Me.ChartControl1.PrimaryYAxis.Location = New PointF(15, 200)
```

## Illustrating Custom Axis Size
```


<!-- tags: [Syncfusion Winforms, Custom Axis Location, Chart, Axis Size, ChartAxisLocationType, Rectangle, C#, VB] keywords: [Axis, Location, Size, Chart, Rect, Synchronization, Windows Forms, Syncfusion, Flexibility, Customization, ChartAxisLocationType, PrimaryYAxis, C#, VB] -->
```