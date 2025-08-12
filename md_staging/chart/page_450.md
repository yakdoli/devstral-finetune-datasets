```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_450.jpeg
document_name: chart
page_number: 450
page_id: chart#page_450
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:44:48Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### See Also
- [ChartLegend](#chartlegend)
- [Customizing LegendItem Image](#customizing-legenditem-image)

## 4.8.3 Customizing LegendItem Image

There are several options to customize the image rendered in the Legend. The following properties let you do so:

| ChartLegend Property | Description |
|----------------------|-------------|
| **ShowSymbol**      | If `true`, the exact symbol rendered in the series data points will be used to render the icon in the legend as well. This overrides most of the other settings. |
| **RepresentationType** | Specifies how each legend item should be represented, as the name implies: <br> <br> None (default setting) <br> - SeriesType - An icon representing the series type. <br> - SeriesImage - Will use the ImageList associated with the Series style. <br> <br> • Rectangle <br> • Line <br> • StraightLine <br> • Circle <br> • Diamond <br> • Hexagon <br> • Pentagon <br> • Triangle <br> • InvertedTriangle <br> • Cross |

The following ChartLegendItem properties that can be accessed via the `Legend.Items` list typically override the above settings set in the Legend.

<!-- tags: [chart, legend, customizing legenditem, syncfusion windows forms] keywords: [chartlegend, customizing legenditem image, representationtype, showsymbol, legend items, overriding settings] -->
```