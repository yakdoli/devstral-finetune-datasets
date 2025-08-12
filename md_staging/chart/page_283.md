```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_283.jpeg
document_name: chart
page_number: 283
page_id: chart#page_283
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:31:36Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Explanation of the `PieType` property for pie charts.
- Description of possible values, default settings, and limitations.
- Demonstrates how to set pie chart types in C# and VB.NET.

## Content

### 4.5.1.52 PieType
**Sets pre-defined types for pie charts.**

#### Details
| Attribute           | Description                                                                                                                                                                                                                                                                     |
|---------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Possible Values** | - None - It has no specific type.<br>- OutSide - Specifies outside pie type.<br>- InSide - Specifies inside pie type.<br>- Round - Specifies Round pie type.<br>- Bevel - Specifies Bevel pie type.<br>- Custom - Specifies custom pie type. |
| **Default Value**   | None                                                                                                                                                                                                                                                                          |
| **2D / 3D Limitations** | No                                                                                                                                                                                                                                                                         |
| **Applies to Chart Element** | Any Pie Series                                                                                                                                                                                                                                                       |
| **Applies to Chart Types** | PieChart                                                                                                                                                                                                                                                                |

#### Code Examples
```csharp
[C#]
this.chartControl1.Series[0].ConfigItems.PieItem.PieType=ChartPieType.Bevel;
```
```vb.net
[VB.NET]
Me.chartControl1.Series(0).ConfigItems.PieItem.PieType = ChartPieType.Bevel
```

### Visual Representation
The following screen shots depict these types.

<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```