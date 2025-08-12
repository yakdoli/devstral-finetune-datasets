```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_212.jpeg
document_name: chart
page_number: 212
page_id: chart#page_212
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:29:21Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Chart Element and Types

| **Applies to Chart Element** | **Applies to Chart Types** |
|-----------------------------|-------------------------|
| All series                  | All chart types         |

### Sample Code

#### C#

```csharp
// Specified 3D View
this.chartControl1.Series3D = true;
// Setting Text Format
this.chartControl1.Series[0].Style.Font.FontStyle = 
    FontStyle.Underline;
this.chartControl1.Series[0].Style.TextColor = Color.Black;
this.chartControl1.Series[0].Style.Font.Size = 7;
this.chartControl1.Series[0].Style.Font.Fontname = "Times New Roman";
// Set SeriesNameDepth as True
this.chartControl1.Series[0].DrawSeriesNameInDepth = true;
```

#### VB.NET

```vb
' Specified 3D View
Me.chartControl1.Series3D = True
' Setting Text Format
Me.chartControl1.Series(0).Style.Font.FontStyle = FontStyle.Underline
Me.chartControl1.Series(0).Style.TextColor = Color.Black
Me.chartControl1.Series(0).Style.Font.Size = 7
Me.chartControl1.Series(0).Style.Font.Fontname = "Times New Roman"
' Set SeriesNameDepth as True
Me.chartControl1.Series(0).DrawSeriesNameInDepth = True
```

<!-- tags: [syncfusion, winforms, chart, chart control, 3D view, text format, series element, series types] keywords: [chart, windows forms, 3D series, text style, underline, font size, font name, series depth] -->
```