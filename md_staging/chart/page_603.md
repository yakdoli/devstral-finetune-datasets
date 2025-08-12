```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_603.jpeg
document_name: chart
page_number: 603
page_id: chart#page_603
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:50:49Z
fidelity: lossless
-->



## Essential Chart for Windows Forms

### Chart Area Bounds

#### Full Chart Area Bounds

Use the **Bounds** property to get the rectangular area comprising the chart area that includes the axis, axis titles, and other sections.

#### C#

```csharp
this.chartControl1.ChartAreaPaint += new
System.Windows.Forms.PaintEventHandler(chartControl1_ChartAreaPaint);

void chartControl1_ChartAreaPaint(object sender, System.Windows.Forms.PaintEventArgs e)
{
    Rectangle axisBounds = this.chartControl1.ChartArea.Bounds;
    // Render a rectangle around this bounds
    e.Graphics.DrawRectangle(Pens.Red, axisBounds);
}
```

### Caption and Figref

**Figure 366: Legend Item Identified using GetItemBy Method**

### Copyright Notice

© 2013 Syncfusion. All rights reserved.  
603 | Page
``` 

<!-- tags: [chart, windows forms, chart area, bounds, legend, controls, winforms, syncfusion 11.4.0.26] keywords: [chart area bounds, getitemby method, legend item, full chart area, paint event, rectangle bounds, axis titles, chart controls] -->
```