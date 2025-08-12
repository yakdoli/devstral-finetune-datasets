```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_133.jpeg
document_name: chart
page_number: 133
page_id: chart#page_133
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:23:42Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

The penetration of a prior column's high or low, by the latest closing price, alters the colors of the lines. These colors depict either a bullish or bearish pattern. Use the `PriceUpColor` and `PriceDownColor` properties to specify the colors for these two patterns. The wider the columns, the stronger the pattern.

## Chart Details

Here is a chart displaying Kagi Series:

<rh-align:center>
![](https://via.placeholder.com/500x300?text=Stock%20Price%20Summary)
</rh-align:center>

**Figure 75: Chart displaying Kagi Series**

### Chart Details

| Details               |                  |
|-----------------------|------------------|
| Number of Y values per point | 1.            |
| Number of Series     | One.             |
| Cannot be Combined with | Pie, Bar.      |

Kagi series can be added to the chart using the following code.

```csharp
// Create chart series and add data points into it.
ChartSeries series = this.chartControl1.Model.NewSeries ("Series Name",
ChartSeriesType.Kagi);
// Arguments: X value, closing price.
```

## API Reference

```markdown
- Namespace: Syncfusion.Windows.Forms
- Class: ChartControl
- Members:
  - `Model`: Access to the chart's model.
  - `NewSeries`: Method to create a new series.
  - `PriceUpColor`: Property to specify the color for bullish patterns.
  - `PriceDownColor`: Property to specify the color for bearish patterns.
```

### Code Examples

```csharp
ChartSeries series = this.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Kagi);
```

### Cross References

- `PriceUpColor`
- `PriceDownColor`
- `ChartSeries`
- `ChartSeriesType.Kagi`

```html
<!-- tags: [chart, windows_forms, kagi_series, price_up_color, price_down_color, version: 11.4.0.26] keywords: [price_up, price_down, bearish, bullish, stock_price_summary, chart_series, kagi] -->
```