```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_191.jpeg
document_name: chart
page_number: 191
page_id: chart#page_191
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:26:34Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```vb
Dim series1 As ChartSeries = New ChartSeries("Series")
' 2nd Y value specifies the column width
series1.Points.Add(1, New Double() { 24, 25})
series1.Points.Add(2, New Double() { 36, 25})
series1.Points.Add(3, New Double() { 48, 25})
chartControl1.Series.Add(series1)
chartControl1.ColumnWidthMode = ChartColumnWidthMode.FixedWidthMode
```

> **Note:** The width of the column can also be specified by `ColumnFixedWidth` property. If both second Y value and `ColumnFixedWidth` are specified, second Y value takes higher priority.

![Figure: Column Chart with FixedWidthMode](https://i.imgur.com/unavailable.png)

**Figure 105: Column Chart with FixedWidthMode**

## See Also

- Column charts
- BoxAndWhiskerChart
- Candle Chart
- ColumnFixedWidth

### 4.5.1.6 ColumnFixedWidth

```html
© 2013 Syncfusion. All rights reserved.
191 | Page
```
```html
<!-- tags: [essential chart, winforms, chartseries, column chart, fixed width mode, column fixed width, daily performance, columnwidthmode, syncfusion winforms, task finished, daily review] keywords: [column charts, d3 charts, fixed width mode, column fixed width] -->
```