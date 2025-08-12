```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_070.jpeg
document_name: chart
page_number: 070
page_id: chart#page_070
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:19:26Z
fidelity: lossless
-->

## Overview
- Discusses performance optimization techniques for charts in Windows Forms.
- Provides code examples for improving chart performance and managing large series.
- Explains the use of `BeginUpdate` and `EndUpdate` methods for efficient chart updates.
- Introduces various chart types supported by Essential Chart and their configurability.

## Content

### Performance Optimization for Multiple Series

#### Code Example: Performance Optimization
```csharp
this.chartControl1.EndUpdate();
```

#### Code Example: VB.NET for Performance Optimization
```vb
' Improves the performance of the chart when a large number of series are used.
Me.chartControl1.ImprovePerformance = True

Me.chartControl1.CalcRegions = False

Me.chartControl1.Series[0].EnableStyles = False

Me.chartControl1.Series[0].Style.DisplayShadow = False

Me.chartControl1.Indexed = True

' BeginUpdate and EndUpdate methods
Private datamodel As DataModel
Private series As ChartSeries = Me.chartControl1.Model.NewSeries("Line 1", ChartSeriesType.Line)

Me.chartControl1.BeginUpdate()

' Add a whole bunch of points to the series like this:
series.Points.Add(1, 10), etc.

Me.chartControl1.EndUpdate()
```

### 4.4 Chart Types

Essential Chart includes a comprehensive set of more than 35 Chart types for all your business needs. Each one is highly and easily configurable with built-in support for creating stunning visual effects.

#### Chart Types Configuration
- Chart types are specified on each `ChartSeries` through the `Type` property.
- All chart types are required to have at least one X and one Y value.
- Certain chart types need more than one Y value.

#### Chart Requirements Table
The following table narrates the minimum and maximum number of series and number of Y values required by each type of chart supported by Essential Chart.

---

## API Reference (if applicable)

### Class: `chartControl1`
- Methods:
  - `BeginInit()`
  - `EndUpdate()`
- Properties:
  - `ImprovePerformance` (Boolean)
  - `CalcRegions` (Boolean)
  - `EnableStyles` (Boolean)
  - `DisplayShadow` (Boolean)
  - `Indexed` (Boolean)
- Additional properties and methods for configuring chart series and chart models are available.

## Code Examples (multi-language supported)

#### C# Example for Chart Series
```csharp
using Syncfusion.Windows.Forms.Chart;

private void InitializeChart()
{
    this.chartControl1.Series.Add(new ChartSeries("Line1", ChartSeriesType.Line));
}
```

#### VB.NET Example for Chart Series
```vb
Private Sub InitializeChart()
    Me.chartControl1.Series.Add(New ChartSeries("Line1", ChartSeriesType.Line))
End Sub
```

## Cross References

- See also: "Chart Series Configuration", "Chart Data Binding", "Styling and Effects".

---

<!-- tags: [Syncfusion Winforms, Chart, Performance Optimization, Chart Types, Essential Chart, Series Configuration] keywords: [chart, performance, series, BeginUpdate, EndUpdate, chartControl, chart types, data binding, series configuration, styling, effects, multiple series, optimization] -->
```