```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_336.jpeg
document_name: chart
page_number: 336
page_id: chart#page_336
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:36:04Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Explains how to display summary values using labels in a chart.
- Provides details on setting the attributes of symbols in a Windows Forms chart.

## Content

### Summary Values Displayed in Labels

![Figure 213: Summary values displayed in Labels](https://example.com/figure213.png)

**Figure 213:** Summary values displayed in Labels

**See Also**
- Chart Types
- How to find value, maximum value, and minimum value among the data points

### 4.5.1.80 Symbol

This section sets the attributes of the symbol that is to be displayed at a specific point in the chart.

#### Details
- **Possible Values**
  - **Size** - Specifies the size of the symbol.
  - **Color** - Specifies the color of the symbol.
  - **Shape** - Specifies the shape of the symbol.
  - **Offset** - Specifies the offset of the symbol.
  
- **Default Value**
  - **Size** - 10,10
  - **Color** - HighLightTextColor
  - **Shape** - None

## API Reference
- **Namespace:** Syncfusion.Windows.Forms.Chart
- **Class:** Chart

#### Properties
- **Symbol**
  - **Type:** Object
  - **Description:** Controls the attributes of the symbol displayed in the chart.
  - **Possible Values:**
    - **Size** - Specifies the size of the symbol.
    - **Color** - Specifies the color of the symbol.
    - **Shape** - Specifies the shape of the symbol.
    - **Offset** - Specifies the offset of the symbol.
  - **Default Value:**
    - **Size** - 10,10
    - **Color** - HighLightTextColor
    - **Shape** - None

## Code Examples

### C# Example
```csharp
// Example demonstrating how to set symbol attributes
chart.Series[0].Symbol.Size = new SizeF(12, 12);
chart.Series[0].Symbol.Color = Color.Red;
chart.Series[0].Symbol.Shape = ChartSymbolShape.Circle;
chart.Series[0].Symbol.Offset = new PointF(5, 5);
```

## Cross References
- Chart Types
- How to find value, maximum value, and minimum value among the data points

<!-- tags: [Essential Chart, Windows Forms, Symbol, Summary Values, Syncfusion, WinForms, version: 11.4.0.26] keywords: [chart, symbols, summary, labels, attributes, size, color, shape, offset, properties, API, reference] -->
```