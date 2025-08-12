```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_288.jpeg
document_name: chart
page_number: 288
page_id: chart#page_288
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:33:30Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates how to set the `PointWidth` for specific data points in a Gantt Chart.
- Explains the usage of `Series.Styles[i].PointWidth` to customize the width of data points.
- Provides examples in both C# and VB.NET for setting varying `PointWidth` values for different data points.

## Content

### Specific Data Point Setting

You can also set the `PointWidth` for specific points using `Series.Styles[0].PointWidth` for the first data point, `Series.Styles[1].PointWidth` for the second data point and so on.

#### Example Code

##### C#

```csharp
ganttSeries.Styles[0].PointWidth = 0.25f;
ganttSeries.Styles[1].PointWidth = 0.5f;
```

##### VB.NET

```vb
ganttSeries.Styles(0).PointWidth = 0.25f
ganttSeries.Styles(1).PointWidth = 0.5f
```

---

### See Also

- [Gantt Chart](#)

---

### 4.5.1.56 PriceDownColor

Specifies a color for the financial item whose price is down.

---

## API Reference

### PriceDownColor
- **Namespace:** Syncfusion.Windows.Forms.Chart
- **Class:** ChartModel
- **Property:** `PriceDownColor`
- **Type:** System.Drawing.Color
- **Description:** Specifies the color for financial items with a price that is down.
- **Default:** Default color is typically determined by the chart style or theme.
- **Required:** No
- **Parameters:** None

---

### Code Examples

#### C#

```csharp
using Syncfusion.Windows.Forms.Chart;

// Setting the PriceDownColor for a financial chart
chartModel.PriceDownColor = Color.Red;
```

#### VB.NET

```vb
Imports Syncfusion.Windows.Forms.Chart

' Setting the PriceDownColor for a financial chart
chartModel.PriceDownColor = Color.Red
```

---

## Tags and Keywords
<!-- tags: esential chart, windows forms, pointwidth, gantt chart, finance chart, pricedowncolor, syncfusion winforms, customization -->
```