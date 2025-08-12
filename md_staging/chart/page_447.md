```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_447.jpeg
document_name: chart
page_number: 447
page_id: chart#page_447
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:41:28Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Specifies shadow, size, text alignment, and spacing for legend items.
- Provides options for setting the title text and its appearance.
- Includes events for customizing legend rendering and size constraints.

## Content

### Chart Legend Properties

| Property            | Description                                                                                                                                                                                                                                             |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ItemsShadowOffset   | Specifies the breadth of the shadow. Default is `{2, 2}`.                                                                                                                               |
| ItemsSize          | Specifies the size of the legend item rectangle. If the specified size is smaller than necessary to render the text, then it's ignored.                                                         |
| ItemsTextAlignment | Specifies the vertical alignment of the legend item text within the item bounds. Possible Values: <br> • Bottom <br> • Center - Default value <br> • Top                                                                                         |
| Spacing            | Specifies the space between the legend borders and the legend items. Default is 4.                                                                                                          |
| Text               | Specifies the title text for the legend. You can set multiline text for the legend; Enter the text in the combobox and press ENTER key to begin a new line and CTRL+ENTER to set the entered multiline text. |
| TextColor          | Specifies the color of the title text.                                                                                                                                                     |
| TextAlignment      | Specifies the horizontal alignment of the title text. Possible Values: <br> • Center (Default value) <br> • Far <br> • Near                                                                                                        |

### ChartLegend Event

**Table 4: ChartLegend Event**

| Event       | Description                                           | Arguments                                  | Type | Reference links |
|-------------|-------------------------------------------------------|-------------------------------------------|------|-----------------|
| MinSize     | Used to specify a minimum rectangular size for the legend item. | object sender, <br> ChartLegendMinSizeEventArgs e | NA   | NA             |
| DrawlItem   | Used to customize the rendering of the legend.      | object sender, <br> ChartLegendDrawItemEventArgs e | NA   | NA             |

## Page-level Navigation/TOC (if applicable)
- If present, include local Table of Contents for this page as a bullet/numbered list of links and texts.

## Cross References
- Add See also: bullet list of explicit links/texts present on the page.

<!-- tags: [chart, legend, text alignment, spacing, title text, color, text alignment event, legend size, rendering customization, syncfusion winforms] keywords: [ItemsShadowOffset, ItemsSize, ItemsTextAlignment, Spacing, Text, TextColor, TextAlignment, ChartLegend Event, MinSize, DrawlItem, ChartLegendMinSizeEventArgs, ChartLegendDrawItemEventArgs] -->
```