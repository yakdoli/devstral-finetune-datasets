```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_434.jpeg
document_name: chart
page_number: 434
page_id: chart#page_434
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:43:41Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates how to customize the placement of Y-axis labels in a bar chart.
- Explains the use of `ChartFormatAxisLabel` event to position labels inside or outside an axis.
- Provides code examples to customize individual label positions based on specific conditions.

## Content

### Peak Average Network loads

#### Figure 279: Chart with Y-Axis Labels Placed Inside of Axis
- The chart displays peak average network loads, categorized into different groups.
- The Y-axis labels are positioned inside the axis for better readability.

```
```

### Positioning Individual Axis Labels

#### Overview
- Essential Chart supports customizing the position of individual axis labels based on specific conditions.
- Labels can be positioned to the right or left of the axis for horizontal axes, and to the top or bottom for vertical axes.

#### Customizing Individual Label Positions
- This feature is achieved using the `ChartFormatAxisLabel` event of the chart axis.
- The provided code example illustrates how to customize the label position based on the label value and data.

#### Code Example

```csharp
this.chartControl1.PrimaryYAxis.AxisLabelPlacement = ChartPlacement.Outside;

// Sets the AxisLabelPlacement property in the ChartFormatAxisLabel event.
private void chartControl1_ChartFormatAxisLabel(object sender, ChartFormatAxisLabelEventArgs e)
{
    if (e.AxisOrientation == ChartOrientation.Vertical)
    {
        if (e.Label == "1")
        {
            if ((series.Points[(int)e.Value - 1].YValues[0] > 0)
            {
                e.AxisLabelPlacement = ChartPlacement.Outside;
            }
        }
    }
}
```

### Notes
- The code snippet demonstrates how to dynamically change the placement of axis labels based on the data values.
- Use `ChartPlacement.Outside` to place labels outside the axis when their corresponding data values exceed a certain threshold.

## API Reference

- **Namespace:** `Syncfusion.Windows.Forms.Chart`
- **Class:** `Chart`
  - **Properties:**
    - `PrimaryYAxis`: Manages the primary Y-axis settings.
    - `AxisLabelPlacement`: Determines the placement of axis labels relative to the axis.
    - `ChartFormatAxisLabelEventArgs`: Contains data and event handling for customizing axis labels.

## Code Examples

The provided C# example showcases how to use the `ChartFormatAxisLabel` event to customize the placement of Y-axis labels dynamically based on conditions.

### Cross References
- Refer to the documentation for detailed examples of customizing axis labels and other chart features.

<!-- tags: [product, module, control, api, version?] keywords: [customizing axis labels, ChartFormatAxisLabel event, ChartPlacement, Essential Chart, Windows Forms] -->
```
```