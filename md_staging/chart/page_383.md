```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_383.jpeg
document_name: chart
page_number: 383
page_id: chart#page_383
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:37:12Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

![Changes in Network Load from Average Load](https://example.com/image-url)  
*Figure 248: Chart with both Axes Reversed*

### 4.6.3 Opposed Axis

For every chart type, there is an implied x-axis and y-axis position, and by default, all the x-axes and y-axes are rendered in their corresponding positions. You can override this default behavior by setting the `OpposedPosition` property to `true` for an axis, which will cause it to be rendered in a side opposite to that of the implied position.

#### Code Examples

##### C#

```csharp
// Will cause the X axis to be rendered on top instead of the default bottom position
this.chartControl1.PrimaryXAxis.OpposedPosition = true;
// Will cause the Y axis to be rendered on the right instead of the default left position
this.chartControl1.PrimaryYAxis.OpposedPosition = true;
```

##### VB.NET

```vbnet
' Will cause the X axis to be rendered on top instead of the default bottom position
Me.chartControl1.PrimaryXAxis.OpposedPosition = True
' Will cause the Y axis to be rendered on the right instead of the 
```
```html
<!-- tags: [chart, axis, opposedposition, windowsforms] keywords: [chartcontrol, primaryxaxis, primaryyaxis, opposedposition, csharp, vb.net] -->
```