```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_399.jpeg
document_name: chart
page_number: 399
page_id: chart#page_399
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:38:12Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
this.chartControl1.PrimaryYAxis.Font = new System.Drawing.Font("Arial", 9F, System.Drawing.FontStyle.Bold);

//Label property settings for X-Axis
this.chartControl1.PrimaryXAxis.LabelAlignment = System.Drawing.ContentAlignment.Center;
this.chartControl1.PrimaryXAxis.LabelRotate = true;
this.chartControl1.PrimaryXAxis.LabelRotateAngle = 45;

//Label property settings for Y-Axis
this.chartControl1.PrimaryYAxis.LabelAlignment = System.Drawing.ContentAlignment.Far;
```

```vb
[VB]

'Settings datetime format to Xaxis
Me.chartControl1.PrimaryXAxis.DateTimeFormat = "MMM"

Settings format to Yaxis
Me.chartControl1.PrimaryYAxis.ValueType = ChartValueType.Double
Me.chartControl1.PrimaryYAxis.Format = "D"

'Setting ForeColor and Font to axes labels
Me.chartControl1.PrimaryXAxis.ForeColor = System.Drawing.Color.Navy
Me.chartControl1.PrimaryXAxis.Font = new System.Drawing.Font("Arial", 9F, System.Drawing.FontStyle.Bold)
Me.chartControl1.PrimaryYAxis.ForeColor = System.Drawing.Color.Navy
Me.chartControl1.PrimaryYAxis.Font = new System.Drawing.Font("Arial", 9F, System.Drawing.FontStyle.Bold)

'Label property settings for X-Axis
Me.chartControl1.PrimaryXAxis.LabelAlignment = System.Drawing.ContentAlignment.Center
Me.chartControl1.PrimaryXAxis.LabelRotate = True
Me.chartControl1.PrimaryXAxis.LabelRotateAngle = 45

'Label property settings for Y-Axis
Me.chartControl1.PrimaryYAxis.LabelAlignment = System.Drawing.ContentAlignment.Far
```

## 4.6.8.2 Customizing Label Text

The formatting options above will usually satisfy the label text requirements. However, there are many other scenarios where this might not be sufficient. Here are some ways to customize the text rendered in the label.

---
© 2013 Syncfusion. All rights reserved. 399 | Page
```