```md
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_427.jpeg
document_name: chart
page_number: 427
page_id: chart#page_427
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:39:52Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview

- Illustrates the use of StripLine in charts.
- Demonstrates how to render a StripLine in the Y-axis and X-axis.
- Explains how to use an image as a StripLine by setting it through the `StripLine.BackImage` property.

## Content

### Figure 274: Chart with StripLine rendered in Y-Axis

#### Description
The chart titled "Illustrates drawing Stripline at Particular Interval" displays a bar chart where the X-axis represents members (John, Matt, Jake, Julie, Beth, Andy) and the Y-axis represents monetary values in dollars (Dollars).

- The chart bars are colored in teal and show revenue values for each member.
- A horizontal StripLine is rendered in the Y-axis at the 150K mark, indicating a "100% of Quota" threshold.

#### Key Points
- The StripLine is a visual indicator marked with an orange bar at the 150K level, labeled "100% of Quota."
- It helps visualize performance relative to a target quota.

#### Implementation
Use an image as a StripLine by setting it through the `StripLine.BackImage` property.

---

### Figure 275: Chart with Image StripLine rendered in X-Axis

#### Description
The chart titled "Weather Chart" shows a line graph representing temperature changes over the course of a week (Monday through Sunday).

- The X-axis represents the days of the week.
- The Y-axis represents temperature values in degrees Fahrenheit (°F).
- A vertical StripLine is rendered in the X-axis at the "Thursday" mark, indicated by a thermometer image.

#### Key Points
- The StripLine is represented by an image of a thermometer, adding visual context to the Thursday data point.
- The temperature value for Thursday is highlighted as 82°F.

#### Implementation
To use an image as a StripLine, utilize the `StripLine.BackImage` property in the chart configuration.

---

## API Reference

### StripLine Properties
- **BackImage**: 
  - Type: Image
  - Description: Sets the background image for the StripLine.
  - Parameters:
    - Name: BackImage
    - Type: Image
    - Description: The image to be used as the background for the StripLine.
    - Required: No
    - Default: null

---

## Code Examples

### Example: Setting StripLine BackImage in a Y-Axis

```csharp
Chart.PrimaryYAxis.StripLines.Add(new StripLine
{
    BackImage = new Image(new Bitmap("quota.png")),
    IntervalOffset = 150000, // 150K
    IntervalType = ChartStripLineInterval.Each,
    Range = new Range { From = 150000, To = 250000 }
});
```

### Example: Setting StripLine BackImage in an X-Axis

```csharp
Chart.PrimaryXAxis.StripLines.Add(new StripLine
{
    BackImage = new Image(new Bitmap("thermometer.png")),
    IntervalOffset = 4, // Thursday (0-based indexing)
    IntervalType = ChartStripLineInterval.OnItemClickListener,
    Range = new Range { From = 4, To = 4 }
});
```

---

## Cross References

- [Chart StripLine Documentation](#chart-strip-line)
- [Customizing Chart Appearance](#customizing-chart-appearance)

<!-- tags: [windows forms, chart, stripline, image, x-axis, y-axis, visualization, quota, weather] keywords: [strip-line, back-image, chart, object, interval, target, performance] -->
```