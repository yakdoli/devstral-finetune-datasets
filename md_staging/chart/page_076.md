```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_076.jpeg
document_name: chart
page_number: 076
page_id: chart#page_076
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:20:25Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Code Examples

```csharp
series.Points.Add(5, 1);

// Add the series to the chart series collection.
this.chartControl1.Series.Add(series);
```

```vbnet
' Create chart series and add data points into it.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Spline)
series.Points.Add(0, 2)
series.Points.Add(1, 3)
series.Points.Add(2, 1)
series.Points.Add(3, 1.5)
series.Points.Add(4, 4)
series.Points.Add(5, 1)

' Add the series to the chart series collection.
Me.chartControl1.Series.Add(series)
```

## Customization Options

- DisplayShadow
- DisplayText
- DrawSeriesNameIndent
- ElementBorders
- HighlightInterior
- ImageIndex
- Images
- Rotate
- Spacing Between Series
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

## Rotated Spline Chart

### Overview

- Rotated Spline Chart is similar to an ordinary Spline Chart.
- The primary difference is that it is rotated.
- It plots one or several series of data, joining each series with smooth, rotated spline curves instead of straight lines.

### Description

The following image shows a sample Rotated Spline Chart.

---

#### Sample Rotated Spline Chart
<!-- Placeholder for the image -->

## API Reference

### Properties
- DisplayShadow
- DisplayText
- DrawSeriesNameIndent
- ElementBorders
- HighlightInterior
- ImageIndex
- Images
- Rotate
- Spacing Between Series
- ShadowInterior
- ShadowOffset
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

### Methods
- `Add(series)` - Adds the series to the chart series collection.

## Page-level Navigation/TOC (if applicable)
- Rotated Spline Chart
    - Overview
    - Description
    - API Reference

<!-- tags: [syncfusion winforms, chart, rotated spline chart, customization options, sample images] keywords: [rotated spline chart, display shadow, display text, draw series name indent, element borders, highlight interior, image index, images, rotate, spacing, shadow interior, shadow offset, fancy tooltip, font, interior, legend item, name, points tooltip format, smart labels, summary, text, text color, text format, text offset, text orientation, visible] -->
```
