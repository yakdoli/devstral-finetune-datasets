```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_188.jpeg
document_name: chart
page_number: 188
page_id: chart#page_188
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:27:46Z
fidelity: lossless
--> 

## ColumnWidthMode for Chart Elements

### Overview
- Details about the `ColumnWidthMode` property and its functionality for chart elements.
- Explanation of how the width of chart elements is specified in `YValues[1]` but in units of the X-axis range.
- Discussion on defaults, supported chart types, and limitations.

### Details

| Parameter               | Description                                                                                                                                                  |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                       | FixedWidthMode, the width is specified in YValues[1], but in units of X-axis range.                                                                          |
| Default Value           | DefaultWidthMode                                                                                                                                            |
| 2D / 3D Limitations    | No                                                                                                                                                          |
| Applies to Chart Element| All Series                                                                                                                                                 |
| Applies to Chart Types  | Column charts, BoxAndWhiskerChart, Candle Chart                                                                                                             |

### Sample Code

#### C#

```csharp
ChartSeries series1 = new ChartSeries("Series");
series.Points.Add(1, 24);
series.Points.Add(2, 36);
series.Points.Add(3, 48);
chartControl1.Series.Add(series1);
chartControl1.ColumnWidthMode = ChartColumnWidthMode.DefaultWidthMode;
```

#### VB.NET

```vb
Dim series1 As ChartSeries = New ChartSeries("Series")
series.Points.Add(1, 24)
series.Points.Add(2, 36)
series.Points.Add(3, 48)
chartControl1.Series.Add(series1)
chartControl1.ColumnWidthMode = ChartColumnWidthMode.DefaultWidthMode
```

## Page-level Navigation/TOC (if applicable)
- This section provides a summary of the page content and any relevant cross-references or additional resources. If specific TOC items are present in the document body, they would be listed here.

## RAG Annotations
<!-- tags: [chart, chart-element, column-width, column-chart, candle-chart, box-and-whisker-chart, winforms] keywords: [columnwidthmode, series, x-axis, y-values, defaultwidthmode, chartcontrol, points] -->
``` 
