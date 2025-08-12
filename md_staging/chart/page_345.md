```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_345.jpeg
document_name: chart
page_number: 345
page_id: chart#page_345
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:36:13Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Applies to Chart Types

| Applies to Chart Types | All Chart Types |
| --- | --- |

Here is sample code snippet using TextColor in Column Chart.

#### Series Wide Setting

```csharp
// Set the color of the text in the Series
this.chartControl1.Series[0].Style.TextColor = Color.Blue;
this.chartControl1.Series[1].Style.TextColor = Color.Red;
this.chartControl1.Series[2].Style.TextColor = Color.Green;
```

```vb.net
' Set the color of the text in the Series
Private Me.chartControl1.Series(0).Style.TextColor = Color.Blue
Private Me.chartControl1.Series(1).Style.TextColor = Color.Red
Private Me.chartControl1.Series(2).Style.TextColor = Color.Green
```

![](attachment:image.png)

**Figure 219: Customized Series Text Color**

<!-- tags: [chart, windows forms, text color, series, column chart, color, series wide setting, csharp, vb.net] keywords: [essential chart, windows forms, text color, series wide setting, column chart, chart control, text color customization] -->
```