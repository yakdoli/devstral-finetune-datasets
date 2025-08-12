```html
<!--  
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_153.jpeg
document_name: chart
page_number: 153
page_id: chart#page_153
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:24:48Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- A summary of the combined chart capabilities in `Essential Chart` for WinForms.
- Highlights the ability to combine multiple data series with different chart types.
- Provides details on creating combination charts and customizing chart elements.

### List of Chart Elements and Properties
- Border
- DisplayText
- DrawSeriesNameInDepth
- ElementBorders
- ImageIndex
- Images
- LightAngle
- LightColor
- PhongAlpha
- Radar Type
- RadarStyle
- Rotate
- ShadingMode
- ShadowInterior
- ShadowOffset
- FancyToolTip
- Font
- Interior
- LegendItem
- Name
- PointsToolTipFormat
- SmartLabels
- Summary
- Text
- TextColor
- TextFormat
- TextOffset
- TextOrientation
- Visible

#### 4.4.10 Combination Chart
##### Overview
- Enables the display of multiple data series in a single chart with varied chart types for each series.
- In `Essential Chart`, compatible chart types can be combined within the same Chart Area.
- Typically combines a Line chart and a Column chart, sharing an x-axis while using separate y-axes on either side.

##### Customization
- Altering an existing chart into a combination chart involves selecting the data series to modify and changing their chart type.

---

## Content
### 4.4.10 Combination Chart

#### Introduction
Combination Charts refer to the ability to display multiple data series in the same chart with each series visualized using different chart types. In **Essential Chart**, Chart types that are compatible with each other may be combined in the same **Chart Area**.

#### Description
Typically, it is a combination of a **Line chart** and a **Column chart**, sharing a common x-axis but with separate y-axes, one on either side of the chart.

#### Customization
One can change an existing chart to a combination chart by selecting the data series you want to change and then changing the chart type for that series.

---

## API Reference
This section details the properties and customization options available for creating and managing combination charts in `Essential Chart`.

### Key Properties for Combination Charts
- **DrawSeriesNameInDepth**: Allows deep customization of how series are drawn.
- **RadarStyle**: Specifies the style of radar charts.
- **Font**: Sets the font for text elements.
- **Color Styles**: Includes **LightColor**, **LightAngle**, and **PhongAlpha** for lighting effects.
- **LegendItem**: Manages items in the legend.
- **Text Formatting**: Includes **Text**, **TextColor**, **TextFormat**, and **TextOrientation** for text customization.

---

## Figures
#### Example of a Combination Chart
**Figure**: A **Combination Chart** displaying both a **Column chart** and a **Line chart** with separate y-axes.

- **Title**: Essential Chart Combination Chart
- **Y-Axis**: Range from -5 to 35
- **X-Axis**: Range from 0 to 10
- **Data Representation**: 
  - **Column (Blue Bars)**: Represents a major data series.
  - **Line (Orange Line)**: Represents an additional data series using a line chart type.

---

## Code Examples (C#)
```csharp
// Example of setting up a Combination Chart
using Syncfusion.Windows.Forms.Chart;

// Create chart and series
SfChart chart = new SfChart();

// Add column series
ChartSeries columnSeries = new ChartSeries("Column");
columnSeries.ChartType = ChartChartType.Column;
chart.Series.Add(columnSeries);

// Add line series
ChartSeries lineSeries = new ChartSeries("Line");
lineSeries.ChartType = ChartChartType.Line;
chart.Series.Add(lineSeries);

// Set data
columnSeries.DataSource = GetColumnData();
lineSeries.DataSource = GetLineData();

// Add to the form
this.Controls.Add(chart);
```

---

## RAG Annotations
<!-- tags: [Essential Chart, WinForms, Combination Chart, Chart Series, Column Chart, Line Chart, Data Visualization, Chart Types] keywords: [combination, multiple series, compatible chart types, custom elements, y-axis, radar style, font, text formatting, essential chart, syncfusion winforms] -->
```