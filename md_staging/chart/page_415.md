```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_415.jpeg
document_name: chart
page_number: 415
page_id: chart#page_415
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:39:10Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
this.secYAxis.TitleDrawMode = ChartTitleDrawMode.Wrap;
```

### [VB]

```vb
' Setting drawing mode of y-axis title
Me.chartControl1.PrimaryXAxis.TitleDrawMode = ChartTitleDrawMode.Ellipsis
' Setting drawing mode of secondary y-axis title
Me.secYAxis.TitleDrawMode = ChartTitleDrawMode.Wrap
```

![Figure 266: Y-Axis TitleDrawMode = "Ellipsis"; SecYAxis TitleDrawMode = "Wrap"](image.png)
**Figure 266: Y-Axis TitleDrawMode = "Ellipsis"; SecYAxis TitleDrawMode = "Wrap"**

### **4.6.10 Axis Ticks**

#### **Major Ticks**

Major Ticks are rendered automatically at the intersection of an axis with the interval grid lines. Here are some properties that will let you customize the look and feel, and behavior of the ticks.

| **ChartAxis Property** | **Description** |
| --- | --- |

---
© 2013 Syncfusion. All rights reserved. | Page 415
```