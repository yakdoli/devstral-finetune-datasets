```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_381.jpeg
document_name: chart
page_number: 381
page_id: chart#page_381
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:38:16Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview

- Explains the concept of indexing supported only on the x-axis in Essential Chart.
- Demonstrates how to enable x-axis indexing or categorizing through the `Indexed` property of the `ChartControl`.
- Provides examples in C# and VB.NET for setting the `Indexed` property.

## Content

### Load-Speed Characteristics

The figure below shows the Load-Speed Characteristics with indexed X values.

#### Figure 247: Indexed X Values

![Load-Speed Characteristics](./figure_247.png)

**Note:** Indexing is supported only on the x-axis in Essential Chart.

You can enable x-axis indexing or categorizing through the `Indexed` property of the `ChartControl` as shown below:

#### Code Examples

- **C#**

```csharp
this.chartControl1.Indexed = true;
```

- **VB.NET**

```vb
Me.chartControl1.Indexed = True
```

The above property automatically affects all the x-axes in the chart.

---

## Page-level Navigation/TOC (if applicable)
- If the body contains a local Table of Contents for this page, keep it as a bullet/numbered list with links/text as shown. Do not create links that don’t exist.

---

## Cross References
- If there are cross-references on the page, include them here as See also: bullet list with explicit links/texts present on the page. Do not fabricate.

---

## RAG Annotations
<!-- tags: [chart, windows forms, indexing, x-axis, essential chart, Syncfusion Winforms] keywords: [indexed, x-axis, load-speed characteristics, C#, VB.NET, ChartControl, property, API] -->
```