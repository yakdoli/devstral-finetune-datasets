```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_236.jpeg
document_name: chart
page_number: 236
page_id: chart#page_236
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:30:40Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

```csharp
Me.chartControl1.Series(0).Style.DisplayText = True
Me.chartControl1.Series(0).Style.Font.Bold = True
Me.chartControl1.Series(0).Style.Font.Facename = "Arial"
Me.chartControl1.Series(0).Style.Text = "Series 1"
```

## Specific Data Point Setting

### C#

```csharp
//font style set for first data point
this.chartControl1.Series[0].Styles[0].Font.Bold = true;
this.chartControl1.Series[0].Styles[0].Font.Facename = "Arial";
```

### VB.NET

```vb
' font style set for first data point
Me.chartControl1.Series(0).Styles(0).Font.Bold = True
Me.chartControl1.Series(0).Styles(0).Font.Facename = "Arial"
```

## Chart Image

<figure>
<img src="Product_Comparison_Chart.png" alt="Product Comparison Chart">
<figcaption>Figure 137: Column Chart with Text</figcaption>
</figure>

## See Also

- [Product Comparison Chart]
- [Column Chart with Text]

## Page-level Navigation/TOC (if applicable)

- [Specific Data Point Setting]
- [C# Example]
- [VB.NET Example]

## Cross References

### References and Related Topics

- Product Comparison Chart
- Column Chart with Text

<!-- tags: [chart, windows forms, specific data point, csharp, vb.net, data point setting, series styling, font styling, chart control, syncfusion winforms] keywords: [chart, windows forms, specific data point, csharp, vb.net, data point setting, series styling, font styling, Chart Control, syncfusion winforms] -->
```