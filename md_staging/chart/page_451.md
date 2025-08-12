```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_451.jpeg
document_name: chart
page_number: 451
page_id: chart#page_451
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:41:44Z
fidelity: lossless
-->

## Overview
- Essential Chart for Windows Forms properties related to legend items.
- Details on how to configure legend items for charts using properties like `DrawSeriesIcon`, `ImageList`, `Symbol`, and others.

## Content

### ChartLegendItem Properties

| ChartLegendItem Property | Description |
|--------------------------|-------------|
| **DrawSeriesIcon** | Specifies if an icon representing the series type should be rendered for this legend item. |
| **ImageList** | Contains a collection of images and will be referred to, by the ImageList property. |
| **ImageIndex** | Specifies the index into the `ImageList` array which contains the image for this item. |
| **Interior** | Specifies the `BrushInfo` used to render the interior of a Chart Symbol. |
| **RepresentationSize** | Specifies the size of the rectangle inside which the associated image or symbol will get rendered. |
| **ShowSymbol** | If `true`, the exact symbol rendered in the corresponding series data points will be used to render the icon in this legend as well. This overrides most of the other settings. |
| **Symbol** | Symbols rendered in the Legend item can be customized using this property. |
| **Type** | If `ShowSymbol` is `false`, you can customize the type of icon that gets rendered in the legend item. The default value will reflect the `ChartLegend.RepresentationType` setting. <br><br>Possible Values: <br>- Area <br>- Circle <br>- Cross <br>- Diamond <br>- Hexagon <br>- Image <br>- InvertedTriangle <br>- Line <br>- None <br>- Pentagon <br>- PieSlice <br>- Rectangle |

<!-- tags: [chart, windowsforms, legend, sackandlegenditem, syncfusion, 11.4.0.26] keywords: [chartlegenditem, drawseriesicon, imagelist, imageindex, interior, representationsize, showsymbol, symbol, type] -->
```