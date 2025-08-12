```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_456.jpeg
document_name: chart
page_number: 456
page_id: chart#page_456
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:43:05Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Custom Images

You can also choose to show custom images in the legend items as follows:

#### Figure 290: LegendItem customized with "Triangle" Symbol in "Yellow" Color

![Figure: LegendItem customized with "Triangle" Symbol in "Yellow" Color](image.png)

#### Code Examples

- **C#**
```csharp
// Setting the representation type for the Legend items
this.chartControl1.Legend.RepresentationType = 
    ChartLegendRepresentationType.SeriesImage;
// Setting the image index
this.chartControl1.Legend.Items[0].ImageIndex = 0;
// The image will be picked up from this collection
series1.Style.Images = new
    ChartImageCollection(this.imageList1.Images);

// Or from this collection, if available
this.chartControl1.Legend.Items[0].ImageList = new
    ChartImageCollection(this.imageList1.Images);
```

- **VB.NET**
```vb
' Setting the representation type for the Legend items
Me.chartControl1.Legend.RepresentationType = 
    ChartLegendRepresentationType.SeriesImage
' Setting the image index
Me.chartControl1.Legend.Items(0).ImageIndex = 0
```

---

## Page-level Navigation/TOC (if applicable)
- Custom Images

## Cross References
- See also: Legend, LegendItem, SeriesImage, ImageIndex, ImageList

## RAG Annotations
<!-- tags: windowsforms, essentialchart, legend, legenditem, images, triangles, customizations keywords: windowsforms, essentialchart, legend, legenditem, SeriesImage, ImageIndex, ImageList -->
```