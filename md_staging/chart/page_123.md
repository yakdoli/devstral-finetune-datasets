```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_123.jpeg
document_name: chart
page_number: 123
page_id: chart#page_123
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:22:27Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Details

| Specifications                 | Details              |
|-------------------------------|----------------------|
| Number of Y values per point  | 1                    |
| Number of Series              | One or More.         |
| Cannot be Combined with       | Pie, Bar, Stacked Bar charts, Polar, Radar. |

## Adding Scatter Series

Scatter series can be added to the chart using the following code.

### C#

```csharp
// Create chart series and add data points into it.
ChartSeries series = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Scatter);
series.Points.Add(0, 1);
series.Points.Add(1, 3);
series.Points.Add(2, 4);

// Add the series to the chart series collection.
this.chartControl1.Series.Add(series);
```

### VB.NET

```vb
' Create chart series and add data points into it.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Scatter)
series.Points.Add(0, 1)
series.Points.Add(1, 3)
series.Points.Add(2, 4)

' Add the series to the chart series collection.
Me.chartControl1.Series.Add(series)
```

## Configuring Scatter Series Symbols

The symbols can be configured using the `ChartSeries.Styles[i].Symbol` property as in the following example.

### C#

```csharp
// Specify the symbol info required for the Scatter chart.
series.Styles[0].Symbol = new ChartSymbolInfo();
series.Styles[0].Symbol.Color = Color.Red;
series.Styles[0].Symbol.Shape = ChartSymbolShape.InvertedTriangle;

series.Styles[1].Symbol = new ChartSymbolInfo();
```

<!-- tags: [Windows Forms, Chart Control, Scatter Series, Syncfusion] keywords: [chart, scatter, series, windows forms, syncfusion, essential chart, data points, series type, styles, symbols] -->
```