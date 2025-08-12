```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_324.jpeg
document_name: chart
page_number: 324
page_id: chart#page_324
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:35:31Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

Here is sample code snippet using Smart Labels in ColumnChart.

### Sample Code

#### C#
```csharp
this.chartControl1.Series[0].Style.DisplayText = true;
series.Styles[0].Text = series.Name;
this.chartControl1.Series[0].SmartLabels = true;
```

#### VB.NET
```vbnet
Me.chartControl1.Series(0).Style.DisplayText = True
series.Styles(0).Text = series.Name
Private Me.chartControl1.Series(0).SmartLabels = True
```

### Chart Illustration without SmartLabels

![Illustrates Smart Labels](https://example.com/figure204.png)

*Figure 204: Chart without enabling SmartLabels*

## API Reference

- `chartControl1.Series[0].Style.DisplayText` - Boolean property to enable or disable text display on a series.
- `series.Styles[0].Text` - Sets the text to be displayed, typically derived from the series name.
- `chartControl1.Series[0].SmartLabels` - Boolean property to enable SmartLabels functionality.

## Code Examples

Using the above properties, you can dynamically modify how labels are displayed in your ColumnChart for better readability or visual presentation.

### Additional Notes

- Ensure that the `SmartLabels` property is set to `true` to automatically adjust label positions to avoid overlaps and improve chart readability.
- Customize the `DisplayText` and `Text` properties to tailor the appearance of the labels to your specific needs.

## Page-level Navigation/TOC

- [Top](#essential-chart-for-windows-forms)
- [Sample Code](#sample-code)
- [Chart Illustration without SmartLabels](#chart-illustration-without-smartlabels)
- [API Reference](#api-reference)
- [Code Examples](#code-examples)
- [Additional Notes](#additional-notes)

<!-- tags: [syncfusion, chart, windows forms, smartlabels, columnchart, displaytext, seriesstyle, labels, essentialchart] keywords: [syncfusion winforms, smart labels, column chart, display text, series styles, smartlabels property, c#, vb.net, essential chart] -->
```