```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_628.jpeg
document_name: chart
page_number: 628
page_id: chart#page_628
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:53:51Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```vb
[VB.NET]
Me.chartControl1.StyleDialogOptions.ShowBorderTab = True
Me.chartControl1.StyleDialogOptions.ShowTextTab = False
Me.chartControl1.StyleDialogOptions.ShowFancyToolTipsTab = False
Me.chartControl1.StyleDialogOptions.ShowInteriorTab = False
Me.chartControl1.StyleDialogOptions.ShowShadowTab = False
Me.chartControl1.StyleDialogOptions.ShowSymbolTab = False
```

## 5.10 How to display the Chart Area alone

This can be achieved by setting the `Legend.Visible` property of `ChartControl` to `False`, `ElementsSpacing` property of `ChartControl` to `Zero`, and `Text` property of `ChartControl` to an Empty String.

```csharp
[C#]
this.chartControl1.Text = "";
this.chartControl1.Legend.Visible = false;
this.chartControl1.ElementsSpacing = 0;
```

```vb
[VB.NET]
Me.chartControl1.Text = ""
Me.chartControl1.Legend.Visible = False
Me.chartControl1.ElementsSpacing = 0
```

## 5.11 How to get back to the gradient appearance of the Chart Series

The default appearance of the chart series is as shown in the image below.

```markdown
The default appearance of the chart series is as shown in the image below.
```

## Page-level Navigation/TOC
- 5.10 How to display the Chart Area alone
- 5.11 How to get back to the gradient appearance of the Chart Series

## Cross References
See also:
- [Previous Section: Chart Area Customization]
- [Next Section: Chart Series Appearance]

<!-- tags: [windowsforms, chart, syncfusion, gradient, legend, chartcontrol, elementspacing, chart series] keywords: [chart area, gradient appearance, chart series, legend, text property, elements spacing] -->
```