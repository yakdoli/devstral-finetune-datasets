```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_276.jpeg
document_name: chart
page_number: 276
page_id: chart#page_276
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:32:47Z
fidelity: lossless
-->

## Visualizing OpenCloseDrawMode in Charts

### Overview
This page demonstrates how to configure and visualize the `OpenCloseDrawMode` property for a series in a chart, specifically in a Windows Forms application. The key features include:
- Adding a series to a chart control.
- Setting the `OpenCloseDrawMode` property to display data in "Open" mode.
- Visual representation of the "Open" mode in a bar chart for different days of the week.

### Content

#### Setting the OpenCloseDrawMode

You can configure the `OpenCloseDrawMode` for a series in the chart control using the following code snippet:

```vb
Me.chartControl1.Series.Add(CS1)
Me.chartControl1.Series(0).OpenCloseDrawMode = ChartOpenCloseDrawMode.Open
```

This Code snippet sets the `OpenCloseDrawMode` property of the first series in the chart control (`chartControl1`) to `Open`. The `Open` mode highlights the starting value of each data point (the "open" value) in the chart.

#### Visual Representation

The chart below illustrates the effect of setting the `OpenCloseDrawMode` to "Open". Each bar in the chart represents a day of the week, with the height indicating the "open" value for that day.

![Illustrates OpenCloseDrawMode](chart_image.png)

**Figure 164: Chart with "Open" Mode**

The chart displays the "open" values for different days of the week, showing how the `OpenCloseDrawMode` affects the visualization.

### API Reference

#### Properties
- **OpenCloseDrawMode**
  - **Type**: `ChartOpenCloseDrawMode`
  - **Default**: `ChartOpenCloseDrawMode.OpenClose`
  - **Description**: Determines how the open and close values are drawn for a series in the chart control.

### Code Examples

#### VB.NET Example

```vb
Dim chart As New Chart
Dim series As New Series

' Add the series to the chart control
chart.Series.Add(series)

' Set the OpenCloseDrawMode to Open
series.OpenCloseDrawMode = ChartOpenCloseDrawMode.Open

' Populate the series with data (example)
series.Points.AddNew(New DateTime(2023, 1, 1), 300D, 400D, 250D, 350D)
series.Points.AddNew(New DateTime(2023, 1, 2), 350D, 450D, 300D, 400D)
' ... continue adding points as needed

' Add the chart to the form
Me.Controls.Add(chart)
```

### Cross References
- For more information on configuring different modes in charts, refer to the "Chart Series Customization" section.
- Refer to the "Chart Control Overview" for general setup and customization options.

### Tags and Keywords
<!-- tags: [chartcontrol, openclosedrawmode, windowsforms, syncfusion winforms] keywords: [openclose, series, chart customization, visual representation] -->
```