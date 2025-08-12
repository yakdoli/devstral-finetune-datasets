```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_400.jpeg
document_name: chart
page_number: 400
page_id: chart#page_400
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:39:25Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Explains how to customize the label text for automatically generated intervals in the chart.
- Discusses the `ChartFormatAxisLabel` event and its properties used for customizing axis labels.
- Includes detailed descriptions of event-specific properties for handling axis label formatting.

## Content

### Customizing the label text for the automatically generated intervals

| ChartAxis Event           | Description                                                                                                                                                                                                                                                                            |
|---------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ChartFormatAxisLabel      | The event that gets raised for each label before getting rendered. This is a good place to customize the label text.                                                                                                                                                                     |

#### The following ChartFormatAxisLabelEventArgs properties provide information specific to this event.

| ChartFormatAxisLabel Property | Description                                                                                                                                                                                                                                                                                             |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AxisOrientation                | Returns the orientation of the axis for which the label is being generated.                                                                                                                                                                                                                               |
| Handled                        | Indicates whether this event was handled and no further processing is required from the chart.                                                                                                                                                                                                           |
| IsAxisPrimary                  | Indicates whether the axis for which the label is being generated is a primary axis.                                                                                                                                                                                                                     |
| Label                          | Gets / sets the label that is to be rendered.                                                                                                                                                                                                                                                          |
| Value                          | Returns the value associated with the position of the label.                                                                                                                                                                                                                                             |
| ValueAsDate                    | Returns the value associated with the position of the label as `DateTime`.                                                                                                                                                                                                                               |
| Tooltip                        | Specifies the content of the tooltip.                                                                                                                                                                                                                                                                   |
```