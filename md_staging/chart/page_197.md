```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_197.jpeg
document_name: chart
page_number: 197
page_id: chart#page_197
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:27:57Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Details

| Properties          | Description                       |
|---------------------|-----------------------------------|
| Possible Values     | Ranges from 0 to 255 bytes       |
| Default Value       | 100                               |
| 2D / 3D Limitations | No                                |
| Applies to Chart Element | All series                    |
| Applies to Chart Types | Renko Chart (Financial Charts) |

## Sample Code

### C#

```csharp
// Setting ColorsMode as DarkLight
this.chartControl1.Series[0].ConfigItems.FinancialItem.ColorsMode = ChartFinancialColorMode.DarkLight;
// Setting the power value of the darklight
this.chartControl1.Series[0].ConfigItems.FinancialItem.DarkLightPower = 200;
```

### VB.NET

```vb
' Setting ColorsMode as DarkLight
Me.chartControl1.Series(0).ConfigItems.FinancialItem.ColorsMode = ChartFinancialColorMode.DarkLight
' Setting the power value of the darklight
Me.chartControl1.Series(0).ConfigItems.FinancialItem.DarkLightPower = 200
```

<!-- tags: [product, module, control, api, version?] keywords: [chart, windows forms, renko chart, darklight, colorsmode, financialcharts] -->
``` 
