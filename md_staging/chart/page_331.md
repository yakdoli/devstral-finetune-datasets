```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_331.jpeg
document_name: chart
page_number: 331
page_id: chart#page_331
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:34:13Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates how to create a stacked column chart with multiple stacking groups in Windows Forms using Syncfusion's chart component.
- Explains the concept of grouping chart series into distinct stacking groups to visually differentiate data clusters.
- Provides an example of implementing stacking groups in a column chart.

## Content

### Creating Stacked Column Charts with Stacking Groups

Storing the chart series as stacking columns can be used to group related data together. In this example, three series are created with distinct stacking groups, as shown in the code snippet below:

```csharp
Dim ser1 As New ChartSeries("Series 1")
ser1.Type = ChartSeriesType.StackingColumn
' specifying group name .
ser1.StackingGroup = "FirstGroup"

Dim ser2 As New ChartSeries("Series 2")
ser2.Type = ChartSeriesType.StackingColumn
' specifying group name .
ser2.StackingGroup = "SecondGroup"

Dim ser3 As New ChartSeries("Series 3")
ser3.Type = ChartSeriesType.StackingColumn
' specifying group name .
ser3.StackingGroup = "FirstGroup"
```

In the code above:
- `Series 1` and `Series 3` are placed in the same stacking group (`FirstGroup`).
- `Series 2` is placed in a different stacking group (`SecondGroup`).

### Visual Representation

The following image illustrates a column chart with stacking groups:

![Figure 209: Column chart with stacking group](media/image1.png)

**Figure 209: Column chart with stacking group.**

In the chart:
- Each stacking group is represented by distinct colors.
- Stacking groups visually separate the data, making it easier to differentiate between related data points.

## API Reference

### Chart Series Properties
- **StackingGroup**: A property of the `ChartSeries` type that specifies the name of the stacking group to which the series belongs. This is used to group related data stacks together.

```csharp
ser.StackingGroup = "GroupName"
```

### Chart Series Types
- **StackingColumn**: A type of column chart where each series is stacked. This type is used to visually represent the grouped data.

```csharp
ser.Type = ChartSeriesType.StackingColumn
```

## Code Examples

### Complete Code Implementation

Here is a complete example of implementing a stacked column chart with multiple stacking groups:

```csharp
Imports Syncfusion.Windows.Forms.Chart

' Create a new Chart control
Dim chart As New Chart()

' Initialize three series with distinct stacking groups
Dim ser1 As New ChartSeries("Series 1")
ser1.Type = ChartSeriesType.StackingColumn
ser1.StackingGroup = "FirstGroup"

Dim ser2 As New ChartSeries("Series 2")
ser2.Type = ChartSeriesType.StackingColumn
ser2.StackingGroup = "SecondGroup"

Dim ser3 As New ChartSeries("Series 3")
ser3.Type = ChartSeriesType.StackingColumn
ser3.StackingGroup = "FirstGroup"

' Add points to each series
' Add series to the chart

' Add the chart to the form
```

### Explanation
This example demonstrates defining multiple series with distinct stacking groups. By assigning each series to a specific stacking group, the data is visually grouped, making it easier to analyze and compare related data stacks.

## Cross References
- Refer to the [Chart Series Documentation](#chart-series-docs) for detailed information on chart series properties and types.
- For more examples of different chart types and customization options, see the [Chart Examples](#chart-examples) section.

<!-- tags: [chart, stacking, windows forms, Syncfusion, version 11.4.0.26] keywords: [StackingColumn, StackingGroup, ChartSeries, Series, Column chart, Stacked columns, Grouping, Chart] -->
```