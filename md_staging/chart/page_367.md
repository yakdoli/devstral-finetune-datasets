```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_367.jpeg
document_name: chart
page_number: 367
page_id: chart#page_367
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:36:20Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

The chart series can be rearranged at run-time using ZOrder property as follows. The chart needs to be redrawn in order to reflect ZOrder property changes. we cannot call redrawing for every series ZOrder changes. In order to overcome this, we should change the order of the series in between the begin update and end update statements as follows.

## Code Examples

### C#

```csharp
this.chartControl1.BeginUpdate();
this.chartControl1.Model.Series[0].ZOrder = 2;
this.chartControl1.Model.Series[1].ZOrder = 1;
this.chartControl1.Model.Series[2].ZOrder = 0;
this.chartControl1.EndUpdate();
```

### VB.NET

```vb.NET
Me.chartControl1.BeginUpdate()
Me.chartControl1.Model.Series[0].ZOrder = 2
Me.chartControl1.Model.Series[1].ZOrder = 1
Me.chartControl1.Model.Series[2].ZOrder = 0
Me.chartControl1.EndUpdate()
```

## Visual Representation

<figure>
<img src="image_initial_order.svg" alt="Initial Order of Series" />
<figcaption>Initial Order of Series</figcaption>
</figure>

<figure>
<img src="image_rearranged_series.svg" alt="Rearranged Series" />
<figcaption>Rearranged Series</figcaption>
</figure>

**Figure 235**: Chart with Rearranged Series

## See Also

- Gantt Chart
- Histogram chart
- Tornado Chart
- Combination Chart
- Box and Whisker Chart
- Area Charts
- Polar And Radar Chart
- BarCharts
- Column Charts
- Bubble Charts
- Candle Charts
- Hilo Charts
- Hilo Open Close Chart

<!-- tags: [chart, rearrange, ZOrder, run-time, windows forms] keywords: [chart series, ZOrder property, redraw, begin update, end update, rearranged series, initial order, rearranged series, Gantt Chart, Histogram chart, Tornado Chart, Combination Chart, Box and Whisker Chart, Area Charts, Polar And Radar Chart, BarCharts, Column Charts, Bubble Charts, Candle Charts, Hilo Charts, Hilo Open Close Chart] -->
```