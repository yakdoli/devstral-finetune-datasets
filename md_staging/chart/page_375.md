```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_375.jpeg
document_name: chart
page_number: 375
page_id: chart#page_375
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:36:46Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- This page demonstrates the use of custom points with multiple axes in a chart.
- It explains the concept of "Empty Points" in charts and how to implement them in code.

## Content

### Custom Points in Multiple Axes

#### Figure 241: Custom Points in Multiple Axes
The figure illustrates a chart with multiple axes, showing three different data series:
- **Population (in millions)**: Represented by blue bars.
- **Growth [%]**: Represented by green bars.
- **Life Expectancy**: Represented by a green line with circular markers.

Each axis is plotted on different scales, allowing the visualization of various data types in a single chart. The chart includes labeled points for clarity.

#### 4.5.4 Empty Points
**Essential Chart** allows you to prevent certain points from being plotted in the resultant chart. Such points are termed **Empty Points**.

#### Implementation of Empty Points
Empty Points can be implemented by setting the `IsEmpty` property of the `ChartPoint` class to `true`.

#### C# Code Example
```csharp
// This sets the specified point as empty point.
this.chartControl1.Series[1].Points[0].IsEmpty = true;
```

## API Reference
- **Namespace**: EssentialChart
- **Class**: ChartPoint
- **Property**: `IsEmpty`
  - **Type**: `bool`
  - **Description**: Determines whether the point is plotted or not.

## Code Examples
The C# code snippet provided above demonstrates how to set a point as an empty point by setting the `IsEmpty` property to `true`.

## Page-level Navigation/TOC (if applicable)
- **4.5.4 Empty Points**
  - Description of Empty Points
  - Implementation details
  - Code example

## Cross References
- See also: the sections on custom chart configurations and multiple axes utilization.

<!-- tags: [chart, empty points, multiple axes, essential chart, syncfusion winforms] keywords: [custom points, life expectancy, population, growth percentage, empty points, IsEmpty property, chart point, chartControl, C# code example] -->
```