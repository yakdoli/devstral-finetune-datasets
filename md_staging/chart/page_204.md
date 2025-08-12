```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_204.jpeg
document_name: chart
page_number: 204
page_id: chart#page_204
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:28:52Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates setting the `DoughnutCoefficient` property in a pie chart to create a doughnut chart.
- Code examples in C# and VB.NET to configure the doughnut effect.
- Explanation of the `DrawColumnSeparatingLines` property for controlling separating lines between columns.

## Content

### Configuring Doughnut Coefficient
The `DoughnutCoefficient` property is used to create a doughnut effect in a pie chart.

#### Code Examples
- **[C#]**
  ```csharp
  this.chartControl1.Series[0].ConfigItems.PieItem.DoughnutCoeficient = 0.5f;
  ```

- **[VB.NET]**
  ```vb
  Me.chartControl1.Series(0).ConfigItems.PieItem.DoughnutCoefficient = 0.5f
  ```

#### Example Chart
![Figure 114: Pie Chart with DoughnutCoefficient Property Set](https://i.imgur.com/placeholder.png)

*Figure 114: Pie Chart with DoughnutCoefficient Property Set*

#### See Also
- [Doughnut Chart](#), [Pie Chart](#)

### 4.5.1.13 DrawColumnSeparatingLines

The drawing of separating lines between columns is controlled by this property.

#### Details
- **Possible Values**
  - `True` or `False`
- **Default Value**
  - `False`
``` 
``` 

## Page-level Navigation/TOC
- See Also
  - [Doughnut Chart](#)
  - [Pie Chart](#)
- 4.5.1.13 DrawColumnSeparatingLines

## RAG Annotations
<!-- tags: [Syncfusion, Winforms, DoughnutCoefficient, PieChart, DrawColumnSeparatingLines, 11.4.0.26] keywords: [doughnut coefficient, pie chart, separating lines, chart control, winforms, Syncfusion] -->
``` 
