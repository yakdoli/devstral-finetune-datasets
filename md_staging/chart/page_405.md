```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_405.jpeg
document_name: chart
page_number: 405
page_id: chart#page_405
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:39:42Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Adding DateTime formatted labels to axes.
- Handling label intersections with built-in properties.

## Content

### Adding Labels with DateTime Values
The following code snippet demonstrates how to add a label with a formatted DateTime value to the primary X-axis of a chart control.

```vbnet
Me.chartControl1.PrimaryXAxis.Labels.Add(New ChartAxisLabel("",
    Color.Maroon, New Font("Arial", 9F, System.Drawing.FontStyle.Bold),
    New DateTime(2007, 05, 15), "", "M", ChartValueType.DateTime))
```

**Figure 260: DateTime formatted labels at the specified Intervals**

![Illustrates Adding Labels with formatted DateTime values](image.png)

The chart in the figure shows the X-axis with DateTime labels formatted as 'M' (month). The DateTime values are set at specified intervals, ensuring clarity and precision in the visual representation.

### 4.6.8.3 Intersecting Labels

Sometimes the chart dimensions can cause the labels to intersect. The chart will, by default, render those texts one over the other. However, it also has some built-in capabilities to work around this overlap and lets you dictate the technique to follow. Refer to the properties below.

#### ChartAxis Property Descriptions

| ChartAxis Property            | Description                                                                                                                                                                                                 |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **LabelIntersectAction**      | Specifies the action to take when labels texts intersect.                                                                                                                                               |
|                               | - **MultipleRows** - Will render the labels in multiple rows.                                                                                                                                            |
|                               | - **None** - Do nothing (default value).                                                                                                                                                                 |
|                               | - **Rotate** - Rotates text so as to avoid overlap.                                                                                                                                                      |
|                               | - **Wrap** - wraps text.                                                                                                                                                                               |
| **EdgeLabelsDrawingMode**    | Affects the labels that get rendered at the edges of the axis. Possible values:                                                                                                                           |
|                               | - **Center** - Centers the label at the interval. Default setting.                                                                                                                                       |
|                               | - **Shift** - Shifts the labels so that it's within the interval boundaries.                                                                                                                             |

## Page-level Navigation/TOC (if applicable)
- **Adding Labels with DateTime Values**
- **Intersecting Labels**
- **Properties: LabelIntersectAction and EdgeLabelsDrawingMode**

## Cross References
- Related topics on handling axis labels and date-time formatting in charts.

<!-- tags: [Syncfusion Winforms, chart, labels, DateTime, intersecting labels, properties, LabelIntersectAction, EdgeLabelsDrawingMode] keywords: [charting, DateTime formatting, label intersections, UI customization] -->
```