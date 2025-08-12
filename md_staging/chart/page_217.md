```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_217.jpeg
document_name: chart
page_number: 217
page_id: chart#page_217
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:28:59Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- The page discusses the use of a Bubble Chart to compare products based on their range and capacity.
- It explains how to disable the PhongStyle for one series in the chart.
- The section "4.5.1.20 EnableAreaToolTip" details how to display proper tooltips for Area charts.

## Content

### Product Comparison Chart

#### Figure 122: Bubble Chart with PhongStyle disabled for One Series

![Product Comparison Chart](Bubble_Chart_Image)

This chart visually compares products based on their range (measured in miles) and capacity (measured in tones). The bubble sizes indicate the relative importance or value of each product.

#### See Also
- [Bubble Chart](https://[link])

### 4.5.1.20 EnableAreaToolTip

To display proper tooltip information for Area charts, use the `Series.EnableAreaToolTip` property. When this property is enabled, the series index and the point index are returned, which is suitable for various PointsToolTipFormats as well.

This feature splits the region between two points into two parts while hovering the mouse over the region and displays the tooltip with respect to the nearby chart point.

```csharp
this.chartControl1.Series[0].EnableAreaToolTip = true;
```

---

### Page-Level Navigation and Cross References
- **See Also:** Bubble Chart
- **Related Sections:** EnableAreaToolTip

## API Reference

- **Namespace:** Syncfusion.Windows.Forms.Chart
- **Class:** Series
- **Property:** EnableAreaToolTip
  - Type: Boolean
  - Description: Enables or disables the display of tooltips for the area of the chart.
  - Default: false

---

## Code Examples

C# Example:
```csharp
// Enable tooltips for the area of the chart
this.chartControl1.Series[0].EnableAreaToolTip = true;
```

## RAG Annotations
<!-- tags: [product, module, control, api, version?] keywords: [chart, bubble chart, product comparison, tooltip, area chart, enableAreaToolTip, see also] -->
```