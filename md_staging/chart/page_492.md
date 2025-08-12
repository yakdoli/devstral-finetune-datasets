```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_492.jpeg
document_name: chart
page_number: 492
page_id: chart#page_492
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:45:41Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
this.chartControl1.BackInterior = new
Syncfusion.Drawing.BrushInfo(System.Drawing.Color.LightBlue);
```

```vbnet
Me.chartControl1.BackInterior = New
Syncfusion.Drawing.BrushInfo(System.Drawing.Color.LightBlue)
```

![Illustrates Back Interior of ChartControl](https://user-content.githubusercontent.com/492/assets/chart-back-interior.png)

**Figure 316: BackInterior = "LightBlue"**

## Inside the Plot Area

Use the `ChartArea.BackInterior` to customize the background of the rectangular region where the points are plotted.

```csharp
this.chartControl1.ChartArea.BackInterior = new
Syncfusion.Drawing.BrushInfo(System.Drawing.Color.SkyBlue);
```

```vbnet
Me.chartControl1.ChartArea.BackInterior = New
Syncfusion.Drawing.BrushInfo(System.Drawing.Color.SkyBlue)
```
```