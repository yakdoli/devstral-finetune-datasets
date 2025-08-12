```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_382.jpeg
document_name: chart
page_number: 382
page_id: chart#page_382
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:39:53Z
fidelity: lossless
--> 

# Essential Chart for Windows Forms

You can also optionally customize the labels of the points in such an indexed series as explained in **Chart Labels Customization**.

## 4.6.2 Inverted Axis

Essential Chart provides support for inverting the values in an axis. Data on an inverted axis is plotted in the opposite direction - top to bottom for y-axis and right to left for x-axis. To enable this behavior, set the **ChartAxis.Inversed** to **true**.

| Chart Axis Property | Description                         |
|----------------------|-------------------------------------|
| **Inversed**        | Indicates whether the axis should be reversed. |

### C# Example

```csharp
// This inverts the specified chart axis.
this.chartControl1.PrimaryXAxis.Inversed = true;
this.chartControl1.PrimaryYAxis.Inversed = true;
```

### VB.NET Example

```vb
' This inverts the specified chart axis.
Me.chartControl1.PrimaryXAxis.Inversed = True
Me.chartControl1.PrimaryYAxis.Inversed = True
```

The following image shows a chart whose x and y axes have been reversed.

<!-- tags: [chart, inverted axis, Essential Chart, Windows Forms, ChartAxis.Inversed, C#, VB.NET] keywords: [chart customization, axis inversion, data plotting, reverse axis, essential chart properties, winforms chart, axis direction, x-axis, y-axis, API reference, code examples] -->
```