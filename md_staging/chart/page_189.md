```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_189.jpeg
document_name: chart
page_number: 189
page_id: chart#page_189
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:27:18Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Introduction to creating column charts in Windows Forms.
- Explanation of chart customization using `ColumnWidthMode`.
- Detailed example of creating a column chart with specified column widths.

## Content

### Creating a Column Chart with DefaultWidthMode

**Figure 103: Column Chart with DefaultWidthMode**

- **Description**: This figure demonstrates a column chart showing the daily performance of "Team 1". The chart displays three reviews, with each review having a different percentage value.

#### Code Example (C#)

```csharp
double Interval = this.chartControl1.PrimaryXAxis.Range.Interval;

ChartSeries series = this.chartControl1.Model.NewSeries("Team 1");
// 2nd Y value specifies the column width
series.Points.Add(1, new double[] { 24, Interval * 0.75 });
series.Points.Add(2, new double[] { 36, Interval * 0.75 });
series.Points.Add(3, new double[] { 48, Interval * 0.75 });
this.chartControl1.Series.Add(series);

this.chartControl1.ColumnWidthMode = ChartColumnWidthMode.RelativeWidthMode;
```

#### Code Example (VB.NET)

```vbnet
Dim Interval As Double = Me.chartControl1.PrimaryXAxis.Range.Interval

Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Team 1")
' 2nd Y value specifies the column width
```

## Conclusion

This section explains how to create a customized column chart in Windows Forms using the `Syncfusion` chart control. The example demonstrates setting the column width dynamically based on the interval of the X-axis.

## API Reference

- **Namespace**: `Syncfusion.Windows.Forms.Chart`
- **Class**: `ChartSeries`, `ChartColumnWidthMode`
- **Methods**: `NewSeries()`, `Add()`

## Code Examples

### C#

```csharp
double Interval = this.chartControl1.PrimaryXAxis.Range.Interval;
ChartSeries series = this.chartControl1.Model.NewSeries("Team 1");
series.Points.Add(1, new double[] { 24, Interval * 0.75 });
series.Points.Add(2, new double[] { 36, Interval * 0.75 });
series.Points.Add(3, new double[] { 48, Interval * 0.75 });
this.chartControl1.Series.Add(series);
this.chartControl1.ColumnWidthMode = ChartColumnWidthMode.RelativeWidthMode;
```

### VB.NET

```vbnet
Dim Interval As Double = Me.chartControl1.PrimaryXAxis.Range.Interval
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Team 1")
series.Points.Add(1, New Double() { 24, Interval * 0.75 })
series.Points.Add(2, New Double() { 36, Interval * 0.75 })
series.Points.Add(3, New Double() { 48, Interval * 0.75 })
Me.chartControl1.Series.Add(series)
Me.chartControl1.ColumnWidthMode = ChartColumnWidthMode.RelativeWidthMode
```

## Cross References

- See also: "Customizing Chart Appearance", "Working with Chart Series".

<!-- tags: [syncfusion, winforms, chart, column chart, width mode] keywords: [chartControl1, PrimaryXAxis, Range, Interval, ChartSeries, NewSeries, Add, ColumnWidthMode, RelativeWidthMode] -->
```