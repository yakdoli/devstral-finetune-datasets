```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_088.jpeg
document_name: chart
page_number: 088
page_id: chart#page_088
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:21:09Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Cannot be Combined with

| Cannot be Combined with | Pie, Bar, Polar, Radar. |
| --- | --- |

#### Adding Gantt Series to the Chart

Gantt series can be added to the chart using the following code.

#### C# Code Example

```csharp
// Create chart series and add data points into it.
ChartSeries series = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Gantt);
series.Points.Add(0, 1, 5);
series.Points.Add(1, 3, 7);
series.Points.Add(2, 4, 8);

// Add the series to the chart series collection.
this.chartControl1.Series.Add(series);
```

#### VB.NET Code Example

```vb
// Create chart series and add data points into it.
Dim series As ChartSeries = Me.ChartControl1.Model.NewSeries("Series Name", ChartSeriesType.Gantt)
series.Points.Add(0, 1, 5)
series.Points.Add(1, 3, 7)
series.Points.Add(2, 4, 8)
Me.ChartControl1.Series.Add(series)
```

#### Customization Options

- Border
- ColumnDrawMode
- DisplayShadow
- DisplayText
- ElementBorders
- GanttDrawMode
- HighlightInterior
- ImageIndex
- Images
- LightAngle
- LightColor
- PhongAlpha
- PointWidth
- RelatedPoints
- Spacing
- Spacing Between Series
- ShadingMode
- ShadowInterior
- ShadowOffset
- ZOrder
- FancyToolTip
- Font
- Interior
- LegendItem
- Name
- PointsTooltipFormat
- SmartLabels
- Summary
- Text
- TextColor
- TextFormat
- TextOffset
- TextOrientation
- Visible

### 4.4.2.5 Histogram Chart

#### Overview

This section provides an overview of the Histogram Chart feature in Syncfusion WinForms. It details how to configure and utilize the Histogram Chart to effectively visualize data distributions in a graphical format.

### Content

The Histogram Chart is particularly useful for visualizing the distribution of numerical data, allowing users to observe patterns, trends, and anomalies in the data set. It can be customized using various properties to enhance its appearance and functionality.

Key Features:
- **Data Distribution Representation**: Histograms represent the frequency distribution of continuous or ordinal variables.
- **Customization Options**: Offers extensive customization options for appearance and functionality.

#### Example Scenario

To create and display a Histogram Chart, you can use the following steps:

1. **Create Chart Object**:
   ```csharp
   HistogramSeries histogramSeries = new HistogramSeries();
   ```

2. **Add Data**:
   ```csharp
   histogramSeries.DataSource = yourDataArray; // Replace with your data source
   ```

3. **Configure and Add to ChartControl**:
   ```csharp
   // Set properties like BarColor, BarWidth, etc.
   histogramSeries.BarColor = Color.Blue;
   histogramSeries.BarWidth = 5;

   chartControl1.Series.Add(histogramSeries);
   ```

4. **Display Chart**:
   ```csharp
   chartControl1.Refresh();
   ```

#### Why Histogram Charts?
- **Clear Data Visualization**: Histograms make it easier to understand complex data by breaking it down into visual elements.
- **Comparative Analysis**: They help in comparing different data sets within the same chart or across multiple charts.

## Page-level Navigation/TOC
- **Introduction to Histogram Charts**
- **Creating and Configuring Histogram Charts**
- **Customization Options for Histogram Charts**
- **Example Implementation**

### API Reference
- **HistogramSeries Class**
  - **Properties**
    - `DataSource`: Specifies the data source for the histogram.
    - `BarColor`: Sets the color of the histogram bars.
    - `BarWidth`: Determines the width of each bar.
  - **Methods**
    - `AddPoint()`: Adds individual data points to the series.
    - `Clear()`: Clears all data points from the series.

### Code Examples
```csharp
using Syncfusion.Windows.Forms.Chart;

ChartControl chartControl1 = new ChartControl();
HistogramSeries histogramSeries = new HistogramSeries();

histogramSeries.DataSource = yourDataArray; // Replace with your actual data array
histogramSeries.BarColor = Color.Green;

chartControl1.Series.Add(histogramSeries);
chartControl1.Refresh();
```

## RAG Annotations
- **Tags**: Chart, Histogram, Windows Forms, Syncfusion
- **Keywords**: Data Visualization, Histogram Chart, Customization, Windows Forms, Series, Data Representation
```