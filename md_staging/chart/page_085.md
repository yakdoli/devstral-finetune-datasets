```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_085.jpeg
document_name: chart
page_number: 085
page_id: chart#page_085
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:20:43Z
fidelity: lossless
-->
# Essential Chart for Windows Forms

## Overview
- PointsToolTipFormat, SmartLabels, Summary, Text, TextColor, TextFormat, TextOffset, TextOrientation, Visible
- StackedBar100 Chart displaying cumulative proportions of each stacked element totaling 100%.

## Content

### PointsToolTipFormat, SmartLabels, Summary, Text, TextColor, TextFormat, TextOffset, TextOrientation, Visible

**See Also:**
- Stacking Area Chart
- Stacking Column Chart

#### 4.4.2.3 StackedBar100 Chart

**Description:**
This chart type displays multiple series of data as stacked Bars ensuring that the cumulative proportion of each stacked element always totals 100%. The y-axis will hence always be rendered with the range 0 - 100.

![Figure 48: A 100% StackedBar Chart](https://placehold.it/600x400?text=Eessential%20Chart-Stacked%20100%25%20Chart)

---

## Details

---

## API Reference (if applicable)

### Namespaces: 
- Members: PointsToolTipFormat, SmartLabels, Summary, Text, TextColor, TextFormat, TextOffset, TextOrientation, Visible

### Methods/Events:
- PointsToolTipFormat: Configures the tooltip format for data points.
- SmartLabels: Enables smart placement of labels to avoid overlaps.
- Summary: Provides aggregated summary information for the chart data.
- Text: Formats the textual labels associated with the chart elements.
- TextColor: Sets the color of the text labels.
- TextFormat: Defines the formatting style for text labels.
- TextOffset: Adjusts the position of text relative to its nominal location.
- TextOrientation: Sets the orientation of the text labels.
- Visible: Controls the visibility of chart elements.

---

## Code Examples (multi-language supported)

### Example 1: Setting up a StackedBar100 Chart

```csharp
// Example code for configuring a StackedBar100 Chart in C#

using Syncfusion.WinForms.Controls;

private void InitializeStackedBar100Chart()
{
    // Initialize the chart
    ChartControl chart = new ChartControl();

    // Configure stacked bar chart
    chart.Series.Add(new StackedBar100Series()
    {
        Name = "Series1",
        DataSource = data,
        XValue = "Category",
        YValue = "Value1"
    });

    // Add additional series
    chart.Series.Add(new StackedBar100Series()
    {
        Name = "Series2",
        DataSource = data,
        XValue = "Category",
        YValue = "Value2"
    });

    // Set chart properties
    chart.PrimaryXAxis.Range_Minimum = 0;
    chart.PrimaryYAxis.Range_Maximum = 100;

    // Add chart to the form
    this.Controls.Add(chart);
}
```

---

## Page-level Navigation/TOC (if applicable)

- [ ] StackedBar100 Chart
  - Description
  - Example Code
  - API Reference

---

## Cross References

**See also:**
- Stacking Area Chart
- Stacking Column Chart

---

## RAG Annotations
<!-- tags: [Syncfusion, WinForms, Essential Chart, StackedBar100, API, Version 11.4.0.26] keywords: [StackedBar100, Stacking Area Chart, Stacking Column Chart, PointsToolTipFormat, SmartLabels, Summary, Text, TextColor, TextFormat, TextOffset, TextOrientation, Visible] -->
```