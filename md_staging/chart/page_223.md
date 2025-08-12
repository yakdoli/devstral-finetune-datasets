```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_223.jpeg
document_name: chart
page_number: 223
page_id: chart#page_223
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:28:18Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview

- Describes the properties and usage of the chart control in Windows Forms.
- Covers details of settings applicable to chart elements and types.
- Includes sample code in C# and VB.NET for configuring chart properties.

## Content

### Chart Element Details

| **Possible Values** | Float type values |
| **Default Value** | `20` |
| **2D / 3D Limitations** | No |
| **Applies to Chart Element** | All series |
| **Applies to Chart Types** | Pie Chart, Doughnut Chart |

### Sample Code

Here is some sample code.

#### C#

```csharp
this.chartControl1.Series[0].ExplodedAll = true;
this.chartControl1.Series[0].ExplosionOffset = 30f;
```

#### VB.NET

```vb
Me.chartControl1.Series[0].ExplodedAll = True
Me.chartControl1.Series(0).ExplosionOffset = 30f
```

### Figure 127: Exploded Pie Chart

![Project Cost Breakdown](https://example.com/ProjectCostBreakdown.png)

---

**Figure 127: Exploded Pie Chart**

## See Also

- Links to related sections or resources.

## Page-level Navigation/TOC (if applicable)

- If applicable, a local Table of Contents for this page.

## Cross References

- See also: References to related sections or resources.

## RAG Annotations

<!-- tags: [Essential Chart, Windows Forms, Chart Control, Settings, C#, VB.NET, Pie Chart, Doughnut Chart, Explosion Offset] keywords: [chart, Windows Forms, float, default, series, pie chart, doughnut chart, explosion offset] -->
```