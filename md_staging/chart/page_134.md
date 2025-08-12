```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_134.jpeg
document_name: chart
page_number: 134
page_id: chart#page_134
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:23:14Z
fidelity: lossless
--> 

## Chart Control in Windows Forms

### Creating a Kagi Chart

To create and configure a Kagi chart in Windows Forms, the code examples below demonstrate how to add data points and customize the appearance of the chart.

#### C#

```csharp
series.Points.Add(0, 23);
series.Points.Add(1, 27);
series.Points.Add(2, 24.7);
series.Points.Add(3, 23);
series.Points.Add(4, 21);
series.Points.Add(5, 20);
series.Points.Add(6, 22);
series.Points.Add(7, 24);
series.Points.Add(8, 26);

series.Text = series.Name;
series.ReversalAmount = 1.0;
series.PriceUpColor = Color.Green;
series.PriceDownColor = Color.Red;

// Add the series to the chart series collection.
this.chartControl1.Series.Add (series);
```

#### VB.NET

```vb
' Create chart series and add data points into it.
Dim series As ChartSeries = Me.chartControl1.Model.NewSeries("Series Name", ChartSeriesType.Kagi)
' Arguments: X value, closing price.
series.Points.Add(0, 23)
series.Points.Add(1, 27)
series.Points.Add(2, 24.7)
series.Points.Add(3, 23)
series.Points.Add(4, 21)
series.Points.Add(5, 20)
series.Points.Add(6, 22)
series.Points.Add(7, 24)
series.Points.Add(8, 26)

series.Text = series.Name
series.ReversalAmount = 1.0
series.PriceUpColor = Color.Green
series.PriceDownColor = Color.Red

' Add the series to the chart series collection.
Me.chartControl1.Series.Add (series)
```

### Customizing the Reversal Amount

If the `ReversalAmount` is set to 0.0 instead of the default value of 1.0, the Kagi chart will appear differently. The below image (not included here) illustrates how the chart looks with the `ReversalAmount` set to 0.0.

---

## Observations and Parameters

- **ReversalAmount**: A critical parameter that determines how the Kagi chart visualizes price changes. The default value is 1.0, but setting it to 0.0 will alter the chart's appearance, as shown in the referenced image.

## Cross References

See the section on **Configuring Kagi Charts** for more advanced customization options.

## Page-level Navigation/TOC

- Essential Chart for Windows Forms
  - Creating a Kagi Chart
  - Customizing the Reversal Amount

<!-- tags: [chart, kagi chart, windows forms] keywords: [reversal amount, kagi chart customization, series, price up color, price down color, data points] -->
```