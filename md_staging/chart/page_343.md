```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_343.jpeg
document_name: chart
page_number: 343
page_id: chart#page_343
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:35:04Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Code Examples

#### C#
```csharp
// labels for the individual datapoints in the series
chartControl1.Series[0].Style.DisplayText = true;
chartControl1.Series[0].Styles[0].Text = "First Point";
chartControl1.Series[0].Styles[1].Text = "Second Point";
chartControl1.Series[0].Styles[2].Text = "Third Point";
```

#### VB.NET
```vb.net
' labels for the individual datapoints in the series
chartControl1.Series(0).Style.DisplayText = True
chartControl1.Series(0).Styles(0).Text = "First Point"
chartControl1.Series(0).Styles(1).Text = "Second Point"
chartControl1.Series(0).Styles(2).Text = "Third Point"
```

### Illustration

![Figure 217: Using Series.Styles[0].Text in Column Chart](Illustrates Text)

## Page-Level Navigation/TOC (if applicable)
- **Figure 217:** Using Series.Styles[0].Text in Column Chart

## Cross References
- None provided in the image.

<!-- tags: [chart, windows forms, series, styles, labels, datapoints] keywords: [chart, windows forms, series, styles, labels, data points, column chart, point display, text display, Syncfusion Windows Forms] -->
```