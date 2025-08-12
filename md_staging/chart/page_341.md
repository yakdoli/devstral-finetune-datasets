```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_341.jpeg
document_name: chart
page_number: 341
page_id: chart#page_341
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:36:01Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- The chart control in Windows Forms allows for customizable series text.
- Demonstrates setting series text both implicitly and explicitly.
- Includes methods for displaying and comparing sales volume data for different months.

## Content

### Setting Series Text

```csharp
' Here the series text will be taken from series name
Dim series1 As ChartSeries = 
Me.chartControl1.Model.NewSeries("August", ChartSeriesType.Column)

' Add points to series1.
'....
'
' Here, the text is given explicitly.
'
Dim series2 As ChartSeries = 
Me.chartControl1.Model.NewSeries("June", ChartSeriesType.Column)
series2.Text = "JuneSales"
```

#### Figure: Sales Volume Comparison

![Sales Volume Comparison](image.png)

**Figure 215: Text set for the Series**

### Key Features
- Automatically generates series text from the series name.
- Allows explicit text assignment for clarity and customization.

## See Also
- Chart Types

## API Reference

- **Namespace**: Syncfusion.Windows.Forms.Chart
- **Class**: ChartSeries
  - **Property**: Text
    - Type: `String`
    - Description: Sets or gets the label text for the series.
    - Default: Series name
    - Example: `series2.Text = "JuneSales"`

## Code Examples

The above code snippet demonstrates how to set series text for a chart in Windows Forms.

## Cross References
- For more details, refer to the "Chart Types" section.

<!-- tags: [chart, series, text, windows forms, sales volume, comparison] keywords: [chart series, windows forms, text setter, sales volume visualization, explicit and implicit text, chart controls, text properties] -->
```