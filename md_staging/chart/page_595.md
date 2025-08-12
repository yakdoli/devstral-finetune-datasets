```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_595.jpeg
document_name: chart
page_number: 595
page_id: chart#page_595
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:49:56Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Printing

Print a chart control using the PrintDocument exposed by the chart control as follows:

```csharp
this.chartControl1.PrintDocument.Print();
```

```vb.net
Me.chartControl1.PrintDocument.Print()
```

You can also specify if you want to print the chart in Color or GrayScale using this property.

| Chart control Property | Description                                                                                                                                                                                                                                                                                       |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PrintColorMode         | Indicates the color mode during printing. <br> Possible Values: <br> - Color - Always Print in Color. <br> - GrayScale - Always Print using GrayScale. <br> - CheckPrinter - If printer allows color print in color, otherwise use grayscale (default setting). |

```csharp
this.chartControl1.PrintColorMode = ChartPrintColorMode.GrayScale;
```

```vb.net
Me.chartControl1.PrintColorMode = ChartPrintColorMode.GrayScale
```

### Automatic Grayscale Handling

Setting GrayScale print mode for the chart lets you print the chart in a gray scale and when multiple series are printed in this case, chart data points are automatically rendered with a patterned brush to differentiate the different series as shown in the image below.
<!-- tags: [printing, chart control, windows forms] keywords: [printdocument, grayscale, patterned brush, color mode, syncfusion] -->
```