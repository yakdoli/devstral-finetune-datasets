```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_253.jpeg
document_name: chart
page_number: 253
page_id: chart#page_253
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:30:58Z
fidelity: lossless
-->

## 4.5.1.38 `ImageIndex`

### Overview

- A detailed description of the `ImageIndex` property, including how it gets or sets the image index from the associated `ImageList` property.
- Supports various chart types and elements, applicable to both series and points without any 2D/3D limitations.

### Content

#### Details

| **Possible Values**                | A numeric value indicating an index of the image list. |
|-------------------------------------|---------------------------------------------------------|
| **Default Value**                  | None                                                   |
| **2D / 3D Limitations**           | No                                                     |
| **Applies to Chart Element**       | All series and points                                  |
| **Applies to Chart Types**         | - Area Charts<br>- Bar Charts<br>- Bubble Chart<br>- Column Charts<br>- Line Charts<br>- Candle Chart<br>- Renko chart<br>- Three Line Break Chart<br>- Box and Whisker Chart<br>- Gantt Chart<br>- Tornado Chart<br>- Polar and Radial Chart                                   |

#### Sample Code

Here is some sample code demonstrating how to use the `ImageIndex` property.

##### Series Wide Setting

**C#**

```csharp
// Setting Images For the Series1
series1.Style.Images = new ChartImageCollection(this.imageList1.Images);
series1.Style.Symbol.ImageIndex = 0;
series1.Style.Symbol.Size = new Size(20, 20);
series1.Style.Symbol.Shape = ChartSymbolShape.Image;
```

**VB.NET**

```vb.net
' Setting Images For the Series1
series1.Style.Images = New ChartImageCollection(Me.imageList1.Images)
series1.Style.Symbol.ImageIndex = 0
series1.Style.Symbol.Size = New Size(20, 20)
series1.Style.Symbol.Shape = ChartSymbolShape.Image
```

### Page-level Navigation/TOC (if applicable)
#### Navigation
- [**Main Content**](#4.5.1.38-imageindex)
- [**Sample Code**](#series-wide-setting)

### RAG Annotations
<!-- tags: [syncfusion, winforms, chart, imagelist, imagindex, series, points] keywords: [imagindex, imageindex, imagelist, series, points, charttypes] -->
```