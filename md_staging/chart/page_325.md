```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_325.jpeg
document_name: chart
page_number: 325
page_id: chart#page_325
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:35:05Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates the use of smart labels in column charts with custom borders.
- Explains how to customize the appearance of smart labels using border properties.
- Provides code examples to set the border color and width for smart labels.

## Content

### Custom borders for smart Labels

Smart labels can be made more smarter by displaying with customized borders. The color and the width of the border can be changed using the appearance properties available. **SmartLabelsBorderColor** property is used to set color for the border and **SmartLabelsBorderWidth** property is used to set the width of the border.

#### Example Code

```csharp
[C#]
this.chartControl1.Series[0].SmartLabelsBorderColor = Color.Yellow;
this.chartControl1.Series[0].SmartLabelsBorderWidth = 2;
```

```vbnet
[VB.NET]
Me.chartControl1.Series(0).SmartLabelsBorderColor = Color.Yellow
Me.chartControl1.Series(0).SmartLabelsBorderWidth = 2
```

### See Also

- [Chart Types](#chart-types)

### 4.5.1.74 Spacing

#### Spacing between data points

This section discusses the spacing between data points in the chart. However, the details are not provided in the given text.

## API Reference

- **SmartLabelsBorderColor**: The property used to set the color of the border for smart labels.
  - Type: Color
  - Default: None
  - Required: No

- **SmartLabelsBorderWidth**: The property used to set the width of the border for smart labels.
  - Type: int
  - Default: 0
  - Required: No

## Code Examples

Refer to the code examples provided in the "Content" section for setting up custom borders for smart labels.

--- 

Figure: Illustrates Smart Labels Column Chart

This figure shows a column chart with smart labels enabled. The chart demonstrates how custom borders can enhance the readability and aesthetics of the smart labels.

---

<!-- tags: [chart, smartlabels, windowsforms, customborders, charttypes] keywords: [smart labels, column chart, custom borders, appearance properties, color, border width, chart types] -->
```