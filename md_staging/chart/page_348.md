```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_348.jpeg
document_name: chart
page_number: 348
page_id: chart#page_348
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:36:47Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Example Code

```csharp
chartControl1.Series(0).Styles(0).TextFormat = "YValue : {0}"
chartControl1.Series(0).Styles(1).TextFormat = "Dollars : {0:C}"
```

### See Also

- **Chart Types**

## 4.5.1.85 TextOffset

### Overview
- **Purpose**: Sets the Offset of the text from the position of the chart point.

### Details

| Category          | Description                     |
|-------------------|---------------------------------|
| Possible Values   | Any float value                |
| Default Value     | 2.5                             |
| 2D / 3D Limitations | No                            |
| Applies to Chart Element | Any Series               |
| Applies to Chart Types | All Chart Types             |

### Sample Code Snippet
Here is a sample code snippet using `TextOffset` in Column Chart.

#### Series Wide Setting

```csharp
this.chartControl1.Series[0].Style.TextOffset = 10.0F;
```

#### [VB.NET]

```vb
Me.chartControl1.Series(0).Style.TextOffset = 10.0F
```

## Page-Level Navigation/TOC (if applicable)
- Essential Chart for Windows Forms
  - Example Code
  - See Also
  - 4.5.1.85 TextOffset
    - Overview
    - Details
    - Sample Code Snippet

### Cross References
- **Chart Types**

### RAG Annotations
```html
<!-- tags: [Syncfusion, Winforms, Chart, TextOffset, Series, Chart Styles, Chart Types] keywords: [TextOffset, Series, Chart Styles, Chart Types, Sample Code, C#, VB.NET, Offset, ChartPoint, Floating Point Value, All Chart Types] -->
```
```