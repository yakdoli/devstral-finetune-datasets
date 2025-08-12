```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_157.jpeg
document_name: chart
page_number: 157
page_id: chart#page_157
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:25:10Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Chart HeatMap Configuration

### Properties

| Property Name          | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| DisplayColorSwatch      | Enables the color swatch of the heat map.                                 |
| DisplayTitle           | Enables or disables the series title in the left corner of the swatch.     |
| StartText              | Sets the text for the left label in the color swatch.                     |
| EndText                | Sets the text for the right label in the color swatch.                    |
| LowestValueColor       | Sets the lowest value color of the heat map chart.                       |
| HighestValueColor      | Sets the highest value color of the heat map chart.                      |
| MiddleValueColor       | Sets the middle value color of the heat map chart.                       |
|	LabelMargin            | Sets the margin for the left and right side labels.                       |

### C# Code Example

```csharp
// Sets the Heat map style.
this.chartControl1.Series[0].ConfigItems.HeatMapItem.HeatMapStyle = ChartHeatMapLayoutStyle.Rectangular;
// Display color swatch.
this.chartControl1.Series[0].ConfigItems.HeatMapItem.DisplayColorSwatch = true;
// Sets the Series Title.
this.chartControl1.Series[0].ConfigItems.HeatMapItem.DisplayTitle = true;
// Sets the left and right label text.
this.chartControl1.Series[0].ConfigItems.HeatMapItem.StartText = "US";
this.chartControl1.Series[0].ConfigItems.HeatMapItem.EndText = "Utah";
// Sets the lowest, highest and middle value color.
this.chartControl1.Series[0].ConfigItems.HeatMapItem.LowestValueColor = Color.Red;
this.chartControl1.Series[0].ConfigItems.HeatMapItem.HighestValueColor = Color.Blue;
this.chartControl1.Series[0].ConfigItems.HeatMapItem.MiddleValueColor = Color.Yellow;
// Sets the value for label margin.
this.chartControl1.Series[0].ConfigItems.HeatMapItem.LabelMargins = 15;
```

### VB.NET Code Example

```vb.net
' Sets the Heat map style.
Me.chartControl1.Series(0).ConfigItems.HeatMapItem.HeatMapStyle = ChartHeatMapLayoutStyle.Rectangular
```

## RAG Annotations

<!-- tags: [syncfusion, winforms, chart, heatmap, colorswatch, title, label, margin, UTF, Utah] keywords: [chartHeatMapLayoutStyle, configItems, heatMapItem, startText, endText, lowestValueColor, highestValueColor, middleValueColor, labelMargins] -->
```