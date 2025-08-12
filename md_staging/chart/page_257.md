```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_257.jpeg
document_name: chart
page_number: 257
page_id: chart#page_257
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:31:12Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Content

```csharp
series1.Styles[0].Images = new ChartImageCollection(this.imageList1.Images);
series1.Styles[0].Symbol.ImageIndex = 1;
series1.Styles[0].Symbol.Size = new Size(20, 20);
series1.Styles[0].Symbol.Shape = ChartSymbolShape.Image;

series1.Styles[1].Images = new ChartImageCollection(this.imageList2.Images);
series1.Styles[1].Symbol.ImageIndex = 2;
series1.Styles[1].Symbol.Size = new Size(20, 20);
series1.Styles[1].Symbol.Shape = ChartSymbolShape.Image;
```

```vb
series1.Styles(0).Images = New ChartImageCollection(Me.imageList1.Images)
series1.Styles(0).Symbol.ImageIndex = 1
series1.Styles(0).Symbol.Size = New Size(20, 20)
series1.Styles(0).Symbol.Shape = ChartSymbolShape.Image

series1.Styles(1).Images = New ChartImageCollection(Me.imageList2.Images)
series1.Styles(1).Symbol.ImageIndex = 2
series1.Styles(1).Symbol.Size = New Size(20, 20)
series1.Styles(1).Symbol.Shape = ChartSymbolShape.Image
```

### See Also

- Area Charts
- Bar Charts
- Bubble Chart
- Column Charts
- Line Charts
- Candle Chart
- Renko chart
- Three Line Break Chart
- Box and Whisker Chart
- Gantt Chart
- Tornado Chart
- Polar and Radar Chart

## API Reference

### 4.5.1.40 InSideRadius

**Description**: Sets / Gets the radius of the doughnut hole of Pie chart as a fraction of the radius of the pie.

| Details         |
|-----------------|
| Possible Values | Ranges from 0.0f to 1.0f. |

<!-- tags: [chart, windows forms, syncfusion,罔的形式格式可视化, winforms,图表类型,图像索引,图形形状选项,图表样式,图像集合,面积图表,柱状图,柱形图表,折线图,浊水图,雷诺内径之图,三线突破图,箱形 whisker图表,甘特图,漏形图表,极座和雷达图,duong内半径] keywords: [chart series, image collection, symbol image index, symbol shape, doughnut hole, radius, fraction, syncfusion winforms, pie chart, line charts, candle chart, renko chart, gantt chart, tornado chart, polar and radar chart] -->
```