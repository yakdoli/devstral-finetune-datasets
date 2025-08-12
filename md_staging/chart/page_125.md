```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_125.jpeg
document_name: chart
page_number: 125
page_id: chart#page_125
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:23:20Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

Though it's called a bubble chart, the data marker can be rendered as either a circle, image, or square using the **BubbleType** property.

The following image shows a multi-series Bubble Chart.

![Chart Displaying 3 Bubble Series](Chart Image)

### Chart Details

| Details                                      |
|---------------------------------------------|
| Number of Y values per point                | 2 (optional second value defines the size of the shape). |
| Number of Series                            | One or More |
| Cannot be Combined with                     | Pie, Bar, Stacked Bar charts, Polar, Radar. |

Bubble series can be added to the chart using the following code.

```csharp
// Create chart series and add data points into it.
ChartSeries series = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Bubble);
// The 2nd Y value represents the size of the shape
```

## Page-level Navigation/TOC (if applicable)
Not available in this section.

## Cross References
None.

## RAG Annotations
<!-- tags: [bubble chart, essential chart for windows forms, bubbletype property, winforms chart, chart series, multi-series bubble chart, chart details] keywords: [bubble chart, essential chart, winforms, bubbletype, chart series, multi-series, detail, number of series, cannot be combined, code example, chart control] -->
```