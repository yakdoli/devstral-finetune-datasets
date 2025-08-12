```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_126.jpeg
document_name: chart
page_number: 126
page_id: chart#page_126
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:22:43Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Content

### C#

```csharp
series.Points.Add(0, 1, 7);
series.Points.Add(1, 3, 5);
series.Points.Add(2, 4, 9);

// Add the series to the chart series collection.
this.chartControl1.Series.Add(series);
```

### [VB.NET]

```vbnet
' Create chart series and add data point into it.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Bubble)
' The 2nd Y value represents the size of the shape.
series.Points.Add(0, 1, 7)
series.Points.Add(1, 3, 5)
series.Points.Add(2, 4, 9)

' Add the series to the chart series collection.
Me.chartControl1.Series.Add(series)
```

#### Customization Options
- Border, BubbleType, DisplayShadow, DisplayText, DrawSeriesNameInDepth, ElementBorders, EnablePhongStyle, HighlightInterior, ImageIndex
- Images, Spacing Between Series, FancyToolTip, Font, Interior, LegendItem, Name, PointsToolTipFormat, SmartLabels,
- Summary, Text, TextColor, TextFormat, TextOffset, TextOrientation, Visible

### See Also

- **Scatter Chart**

### 4.4.7 Financial Charts

The following charts are a staple of analytical reports in the financial world. Financial data usually has more than one y value. For example, stock price charts should include high, low, open and close prices for a day. Such data needs to be appropriately rendered in the context of "stock market data". Also, besides actual values, trends in price movement need to be depicted visually.

## Organization

### Technical Details

- **Page Footer**:
  - © 2013 Syncfusion. All rights reserved.

<!-- tags: [essential chart, windows forms, vb.net, c#, customization options, scatter chart, financial charts, financial data, stock prices, high-low-open-close, price trends, syncfusion winforms, control design, data visualization] keywords: [essential chart, windows forms, vb.net, c#, financial charts, stock prices] -->
```