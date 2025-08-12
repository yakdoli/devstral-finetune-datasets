```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_183.jpeg
document_name: chart
page_number: 183
page_id: chart#page_183
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:26:06Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Core Features

| Feature                                       | Description                                        |
|----------------------------------------------|----------------------------------------------------|
| **Symbol Type**                              | Image - Symbol is rendered as an image             |
| **Default Value**                            | Circle                                              |
| **2D / 3D Limitations**                     | No                                                  |
| **Applies to Chart Element**                 | All Series                                          |
| **Applies to Chart Types**                   | Bubble                                              |

### Setting the Image BubbleType

Here is some sample code to specify an Image BubbleType.

#### Series wide setting

**C#**

```csharp
this.chartControl1.Series[0].ConfigItems.BubbleItem.BubbleType = ChartBubbleType.Image;
this.chartControl1.Series[0].Style.Images = new ChartImageCollection(this.imageList1.Images);
this.chartControl1.Series[0].Style.ImageIndex = 0;
```

**VB.NET**

```vb.net
Me.chartControl1.Series[0].ConfigItems.BubbleItem.BubbleType = ChartBubbleType.Image
Me.chartControl1.Series[0].Style.Images = New ChartImageCollection(Me.imageList1.Images)
Me.chartControl1.Series[0].Style.ImageIndex = 0
```

#### Specific Data Point Setting

**Specify image for specific data points.**

**C#**

```csharp
this.chartControl1.Series[0].Styles[0].Images = new ChartImageCollection(this.imageList1.Images);
this.chartControl1.Series[0].Styles[0].ImageIndex = 0;
this.chartControl1.Series[0].Styles[1].Images = new ChartImageCollection(this.imageList1.Images);
this.chartControl1.Series[0].Styles[1].ImageIndex = 1;
```

---

## Page-level Navigation/TOC (if applicable)
- [Essential Chart for Windows Forms]
  - Series wide setting
  - Specific Data Point Setting

### Cross References
- See also: [Image BubbleType], [Chart Bubble Type]

#### RAG Annotations
<!-- tags: [chart, windows forms, image bubbletype, series settings, vb.net, c#, syncfusion winforms] keywords: [chartcontrol, imagelist, datapaoint, series, imageindex, chartimagecollection] -->
```