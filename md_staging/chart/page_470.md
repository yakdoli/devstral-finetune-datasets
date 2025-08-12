```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_470.jpeg
document_name: chart
page_number: 470
page_id: chart#page_470
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:46:10Z
fidelity: lossless
--> 

## Overview
- The page explains how to configure the **Interior** style properties for a chart series using the **Chart Series Style** window in Windows Forms.
- It showcases the user interface for setting interior properties such as **Pattern**, **BackColor**, **ForeColor**, and **PatternStyle**.
- An example chart is provided to illustrate the appearance of a chart series with the specified interior properties applied.

## Content

### Chart Series Style Window

The **Chart Series Style** window is used to customize various aspects of a chart series in Windows Forms. Below is a detailed breakdown of the window:

#### Series Tab - Interior Properties
The **Interior** tab allows configuring the fill style of the chart series. The properties visible in the window include:

- **Pattern**: Specifies the type of pattern for the interior. In this example, it shows **Pattern; Percent20; WindowText**.
- **Style**: The style of the interior is set to **Pattern**.
- **BackColor**: The background color is set to **SteelBlue**.
- **ForeColor**: The foreground color is set to **WindowText**.
- **PatternStyle**: The pattern style is set to **Percent20**.
- **GradientColors**: The gradient colors are specified using **Syncfusion.Drawing.Br** (partially visible).

A **Reset Interior** button is available to revert the interior settings to their default values.

### Adjusting Interior Properties

The user can modify these properties to customize the appearance of the chart series. The changes can then be applied by clicking the **OK** button.

### Example Chart

The following chart demonstrates the effect of the customized interior properties:

#### Figure 300: Chart Series Style Window to set Interior Properties

![Bar Chart with Interior Style](https://example.com/bar-chart-interior-style.png)

- The chart displays a bar chart with sales volume data over the years 2000 to 2006.
- The bars have a patterned interior with a steel blue background color and a white text pattern as per the configured **Pattern** and **BackColor** properties.
- The chart clearly illustrates how the interior style settings affect the visual appearance of the chart series.

## Code Example

Here is an example of how to programmatically set the interior properties of a chart series:

```csharp
// Import necessary namespaces
using Syncfusion.Windows.Forms.Chart;
using Syncfusion.Drawing;

// Configure Interior properties for a chart series
ChartSeries series = chartControl.Series[0];

// Set the pattern style
series.Interior.Pattern = new PatternBrush(PatternType.Percent20, Color.SteelBlue, Color.WindowText);

// Apply the changes
chartControl.Refresh();
```

### API Reference

#### Interior Property Settings

- **Interior.Pattern**: Specifies a brush for the interior pattern.
- **BackColor**: Property to set the background color.
- **ForeColor**: Property to set the foreground color.
- **PatternStyle**: Property to set the pattern style.
- **GradientColors**: Property to set gradient colors.

## Page-level Navigation/TOC (if applicable)

- **Overview**
  - Chart Series Style Window
  - Example Chart
- **Content**
  - Chart Series Style Window
  - Adjusting Interior Properties
  - Example Chart
- **Code Example**
  - Interior Property Settings

## Cross References

See also:
- Other tabs in the **Chart Series Style** window (**Border**, **Text**, **Shadow**, **Symbol**, **FancyToolTip**).
- Related chart customization methods and properties in the Syncfusion WinForms documentation.

<!-- tags: [product, module, control, api, version?] keywords: [chart, series, style, interior, pattern, backcolor, forecolor, patternstyle, gradientcolors, example, windows forms, programmatically, badges] -->
```