```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_158.jpeg
document_name: chart
page_number: 158
page_id: chart#page_158
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:24:39Z
fidelity: lossless
-->

## Overview
- Demonstrates configuration of a HeatMap using properties settings, such as displaying a color swatch and setting display titles.
- Explains stacking charts and their use in visualizing data that is segmented into parts.
- Introduces step charts and their continuous, step-by-step visualization of data.

## Content

```markdown
    ' Display color swatch.
    Me.chartControl1.Series(0).ConfigItems.HeatMapItem.DisplayColorSwatch = True
    ' Sets the display title.
    Me.chartControl1.Series(0).ConfigItems.HeatMapItem.DisplayTitle = True
    ' Sets the start and end text.
    series.ConfigItems.HeatMapItem.StartText = "US"
    series.ConfigItems.HeatMapItem.EndText = "Utah"
    ' Sets the lowest, highest and middle value color.
    series.ConfigItems.HeatMapItem LowestValueColor = Color.FromArgb(255, 23, 0)
    series.ConfigItems.HeatMapItem.HighestValueColor = Color.FromArgb(81, 168, 0)
    series.ConfigItems.HeatMapItem.MiddleValueColor = Color.Gold
    ' Sets the margin for the left and right labels.
    series.ConfigItems.HeatMapItem.LabelMargins = 15
```

### 4.4.12 Stacking Charts

Stacking Charts are similar to regular charts except that the y values stack on top of each other in the specified series order. Stacking charts help visualize data that is a sum of parts, each of which is in a series.

There are different types of stacking charts:

- Stacking Area Chart
- Stacking Bar Chart
- Stacking Column Chart
- StackedArea100 Chart
- StackedBar100 Chart
- StackedColumn100 Chart

### 4.4.13 Step Charts

Step Charts are similar to regular charts except that the values are drawn continuously, step-by-step without any gaps in-between.

There are two types of step charts.

## API Reference (if applicable)

## Code Examples (multi-language supported)

## Page-level Navigation/TOC (if applicable)

## Cross References

## RAG Annotations
<!-- tags: [Stacking Charts, Step Charts, HeatMap, StackingColumn100 Chart, StackingBar100 Chart, StackingArea Chart] keywords: [Stacking, Step, HeatMap, DisplayColorSwatch, DisplayTitle, StartText, EndText] -->
```