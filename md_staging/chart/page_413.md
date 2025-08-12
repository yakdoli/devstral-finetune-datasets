```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_413.jpeg
document_name: chart
page_number: 413
page_id: chart#page_413
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:40:22Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- This page demonstrates how to set a multiline axis title through the Properties window in Syncfusion Windows Forms.
- It shows a screenshot of a chart control with customizable axis titles.

## Content

### Setting Multiline Axis Title Through Properties Window

The screenshot below illustrates the properties window for a chart control in Syncfusion Windows Forms.

```plaintext
Figure 264: Setting Multiline Axis Title Through Properties Window

The following screenshot shows the chart control's properties window where various properties related to the chart axis can be adjusted. Specifically, the "Title" property allows setting a multiline axis title.

- **SmartDateZoomWeekLevel**: MMM, ddd, yyyy
- **SmartDateZoomYearLevel**: y
- **TickColor**: ControlText
- **TickDrawingMode**: NumberOfIntervalsFixed
- **TickLabelGridPadding**: 5
- **TickLabelsDrawingMode**: AutomaticMode
- **TickSize**: 1, 1
- **Title**: 
    - **Multiline**
    - **Chart Axis Title**

Note: The properties window allows you to customize various aspects of the chart axis, including setting a multiline title for better readability and styling adjustments.
```

### Screenshot Description
The below screenshot illustrates a chart with multiline axes titles.

```markdown
The screenshot demonstrates a chart with axes titles that span multiple lines. This feature is particularly useful when the axis title is descriptive or requires additional text to convey information effectively. The property window shown in the screenshot highlights the ability to customize the chart's visual attributes, including multiline titles, to enhance the chart's readability and aesthetic appeal.
```

## API Reference
### Namespace: Syncfusion.Windows.Forms.Chart
- **Class**: ChartControl
- **Property**: Title
  - Description: Allows setting a multiline title for the chart axis.
  - Type: String
  - Example: 
    ```csharp
    chartControl1.Title = "Multiline Chart Axis Title";
    ```

## Code Examples
```csharp
// Example of setting a multiline axis title
chartControl1.Title = "Multiline Chart Axis Title";
chartControl1.TickColor = System.Drawing.Color.Black;
chartControl1.TickSize = new System.Drawing.SizeF(1, 1);
chartControl1.TickLabelsDrawingMode = DrawingMode.AutomaticMode;
```

## Cross References
- See also:
  - Documentation on chart styling and customizations
  - Reference on using the Properties window for chart controls

<!-- tags: Syncfusion, Winforms, ChartControl, AxisTitle, PropertiesWindow, MultilineAxisTitle keywords: chart, chart control, axis title, multiline title, properties window -->
```