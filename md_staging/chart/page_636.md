```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_636.jpeg
document_name: chart
page_number: 636
page_id: chart#page_636
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:54:16Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Chart Configuration and Printing

### Setting Chart Properties

The following section demonstrates how to configure a chart for multi-page printing and adjust the chart's axis range dynamically based on user input.

```csharp
// Initialize the chart's multi-page property and set label action
// Set the HasMorePages property to true for dividing the chart into Multiple pages
e.HasMorePages = true;

this.chartControl1.PrimaryXAxis.LabelIntersectAction = ChartLabelIntersectAction.Wrap;

// Set initial ranges for the chart's axis
if (mx == 0.0 && mi == 0.0)
{
    mx = Convert.ToDouble(textBox1.Text);  // Initializing max and min range
    mi = 0;
}
```

### Handling Color Modes and Toolbars

The code snippet below handles the color modes and toolbar visibility based on the printing settings and user actions.

```csharp
// Get the Color mode
bool grayScale = this.chartControl1.PrintDocument.ColorMode == ChartPrintColorMode.GrayScale;
bool toolBatVisibility = this.chartControl1.ShowToolbar;

// Check whether to hide the toolbar
if (!this.chartControl1.PrintDocument.PrintToolBar)
{
    this.chartControl1.ShowToolbar = false;
}

// Handle the color mode check for specific actions
if (m_currentAction.Value == PrintAction.PrintToPrinter
    && this.chartControl1.PrintDocument.ColorMode == ChartPrintColorMode.CheckPrinter)
{
    grayScale = this.chartControl1.PrintDocument.PrinterSettings.SupportsColor;
}
```

### Assigning Axis Ranges Dynamically

The following code assigns the maximum and minimum values for the chart's axis based on the values set in the TextBox control (`textBox1.Text`). It also dynamically calculates the intervals based on the maximum, minimum, and number of intervals specified.

```csharp
// Assigning the initial values of max and min to chartcontrol's maximum and minimum values
this.chartControl1.ChartArea.PrimaryXAxis.Range.Min = mi;
this.chartControl1.ChartArea.PrimaryXAxis.Range.Max = mx;

// Calculating the interval for the axis range
this.chartControl1.ChartArea.PrimaryXAxis.Range.Interval = 
    (this.chartControl1.ChartArea.PrimaryXAxis.Range.Max - 
     this.chartControl1.ChartArea.PrimaryXAxis.Range.Min) / 
     this.chartControl1.ChartArea.PrimaryXAxis.Range.NumberOfIntervals;
```

## API Reference

### Properties Used

- **HasMorePages**: Property to enable multi-page charts.
- **LabelIntersectAction**: Property to handle label intersections, specifically used for wrapping labels.
- **PrimaryXAxis.Range.Min**: Specifies the minimum value for the primary x-axis range.
- **PrimaryXAxis.Range.Max**: Specifies the maximum value for the primary x-axis range.
- **PrimaryXAxis.Range.Interval**: Specifies the interval of values for the axis range.
- **ShowToolbar**: Property to control the visibility of the chart's toolbar.
- **PrintDocument.ColorMode**: Property to manage the color mode (color or grayscale) for printing.
- **PrinterSettings.SupportsColor**: Property to check whether the printer supports color printing.

### Methods Used

- **Convert.ToDouble**: Converts a string value to a double, used to parse the `TextBox` input.

## Code Examples

The provided code examples demonstrate how to:

1. Enable and configure multi-page charts and handle label wrapping.
2. Dynamically set the axis ranges based on user input.
3. Adjust the display and printing settings (color modes, toolbar visibility) depending on the printer and action type.

## See also

- [Configuring Axis Ranges in Syncfusion Chart Control](#configuring-axis-ranges)
- [Printing and Color Management in Syncfusion Document Printing](#printing-and-color-management)

<!-- tags: [chart, winforms, printing, axis, range, colorMode, multi-page] keywords: [labelIntersectAction, ChartLabelIntersectAction.Wrap, ShowToolbar, PrintDocument.ColorMode, PrintDocument.PrintToolBar, ChartPrintColorMode] -->
```
