```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_489.jpeg
document_name: chart
page_number: 489
page_id: chart#page_489
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:45:03Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Illustrates formatted tooltips on the series.
- Explores different types of tooltip formats for individual data points, chart area, and empty areas.
- Describes the functionality of the "fancy tooltip" feature and customization options.

## Content

### Chart Area Tooltip
Tooltips can also be set for the whole chart area (does not include legends and the space around legends) through the **ChartAreaToolTip**. The data points tooltips will of course override this setting.

#### Chart Empty Area Tooltip
The chart also lets you show a tooltip when the mouse hovers over empty areas in the chart (usually around the legend) via the **ChartToolTip** property.

#### DataPoint FancyToolTip
Chart Windows includes a "fancy tooltip" feature. As the name implies, this tooltip, which occurs when hovering over a data point looks like a balloon and includes information regarding the series name and the X, Y points. This feature can be turned on by setting the **ChartSeries.FancyToolTip.Visible** property to `true`.

The FancyToolTip can also be customized with more of the following properties:

| FancyToolTip Property | Description |
|------------------------|-------------|
| Alignment             | Indicates the alignment of the marker to that of the tooltip balloon. |

### WinForms-specific conventions
- Preserves control names, namespaces, and types from the Syncfusion.Windows.Forms.Tools and Syncfusion.Windows.Forms.Grid.

### Figure: ToolTip Format set for Individual Data Points
![Illustration of Formatted Tooltips](https://i.imgur.com/789456.png)

- **Figure 314: ToolTip Format set for Individual Data Points**

## API Reference (if applicable)
- **Namespace**: Syncfusion.Windows.Forms.Chart
- **Class**: Chart
- **Members**:
  - **ChartToolTip**: Property for setting tooltips in empty areas.
  - **ChartAreaToolTip**: Property for setting tooltips in the chart area.
  - **ChartSeries.FancyToolTip.Visible**: Property for enabling the "fancy tooltip" feature.
  - **FancyToolTip.Alignment**: Property for aligning the marker to the tooltip balloon.

## Code Examples (multi-language supported)

```csharp
// Enabling FancyToolTip
ChartSeries.Series = new ChartSeries();
ChartSeries.FancyToolTip.Visible = true;
```

## Page-level Navigation/TOC (if applicable)
- Chart Area Tooltip
- Chart Empty Area Tooltip
- DataPoint FancyToolTip
- API Reference
- Code Examples

## Cross References
- See also: Related features and documentation sections for tooltips and data visualization.

<!-- tags: [syncfusion, winforms, chart, tooltip, fancytooltip, data visualization] keywords: [chart, windows forms, tooltips, data points, alignment, properties] -->
```