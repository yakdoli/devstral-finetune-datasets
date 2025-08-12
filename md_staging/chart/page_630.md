```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_630.jpeg
document_name: chart
page_number: 630
page_id: chart#page_630
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:57:04Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- This section discusses the appearance and customization of charts in Windows Forms, focusing on gradient effects and how to implement DrillDown charts.
- It covers providing DateTime type input data for chart series.

## Content

### Chart Appearance

![Figure 377: Chart with Gradient Look and Feel](#)
*Figure 377: Chart with Gradient Look and Feel*

**Note:**  
We can also use ChartControl.AllowGradientPalette property to enable or disable gradient effect for chart series. By default, it is set to false.

### 5.12 How to implement DrillDown charts

DrillDown charts can essentially be implemented by listening to the click events in the chart and either replacing the current visible chart with another chart that has drill-down information or reinitializing the chart with new drill-down information.

The ChartRegionClick event will let you listen to the user clicking on the data points in a chart.

The sample at "My Documents\\Syncfusion\\EssentialStudio\\Version Number\\Windows\\Chart.Windows\\Samples\\2.0\\User Interaction\\Chart Drill Down" illustrates the second approach.

### 5.13 How to provide input data of DateTime type

The Start Date and Time can be expressed using an instance of the **DateTime** class. If you want to add days, the **AddDays()** method can be used along with that instance. **AddHours()** and **AddMinutes()** can be used for adding any number of hours and minutes.

#### Code Example

```csharp
[C#]
```

## API Reference

- DateTime class
- AddDays()
- AddHours()
- AddMinutes()

## Code Examples

### DateTime Input Data Example

The example shows how to use DateTime for providing input data.

```csharp
DateTime startDate = new DateTime(2023, 1, 1);
DateTime endDate = startDate.AddDays(30);
```

## Page-level Navigation/TOC

- Chart Appearance
- How to implement DrillDown charts
- How to provide input data of DateTime type

## Cross References

See also:  
- Gradient effects in charts
- DrillDown functionality
- DateTime manipulation in chart input data

<!-- tags: [chart, datetime, drilldown, gradient, windows forms] keywords: [Synfusion, DateTime, DrillDown, gradient effect, Windows Forms] -->
```