```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_091.jpeg
document_name: chart
page_number: 091
page_id: chart#page_091
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:20:46Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

PointsToolTipFormat, SmartLabels, Summary, Text, TextColor, TextFormat, TextOffset, TextOrientation, Visible

## 4.4.2.6 Tornado Chart

The Tornado chart is a bar chart which shows the variability of an output to several different inputs. Variability is displayed using relative lengths of bars across a range. It is mainly used in sensitivity analysis. It shows how different random factors can influence the prognostic outcome.

### Chart Details

| Details                     |               |
|-----------------------------|---------------|
| Number of Y values per point | 2             |
| Number of Series             | One or more   |
| Cannot be Combined with      | Pie, Bar, Polar, Radar |

The Tornado series can be added to the chart using the following code.

```csharp
// Create chart series and add data points into it.
ChartSeries series = this.chartControl1.Model.NewSeries("Series 0", 
```
```