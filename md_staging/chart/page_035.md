```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_035.jpeg
document_name: chart
page_number: 035
page_id: chart#page_035
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:17:22Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### 4.1.4 Axes

Various settings like grid line, axis title, value type, formats, and other axes settings can be done using the wizard.

The below properties can be set separately for x-axis and y-axis.

- **Grid Lines** - Lets you show/hide the grid lines for this axis.
- **Axis Title** - The title text for the axis can be specified here.
- **Inversed, Opposed** - Specifies whether the axes are inversed, opposed.
- **Value Type** - If you know the type of data points you will be adding to this axis, specify it using the combo box. Possible value types are `double`, `datetime`, `custom`, and `logarithmic`.
- **Format** - Specifies the label format.
- **Edit Labels** - The labels at the axes can be varied by entering the values in the Collection Editor Dialog box, which pops up when the Edit Labels button is clicked.

## API Reference (if applicable)

### Code Examples

```csharp
// Example of setting axis properties
chart.Axes.XAxis.Title.Text = "X-Axis Title";
chart.Axes.YAxis.ValueType = ChartValueType.Double;
```

### Related Links and References
See also:
- [How to Customize Axis Labels in Charts](#)
- [Axes Configuration in Syncfusion WinForms](#)

<!-- tags: [axes, chart, synchronize, windows forms, axis customization] keywords: [grid lines, axis title, value type, axis settings, label formats, data points, chart properties, axis labels, widget settings] -->
```