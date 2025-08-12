```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_417.jpeg
document_name: chart
page_number: 417
page_id: chart#page_417
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:40:38Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Customizing the appearance of the primary X-axis using properties like `TickColor` and `TickLabelGridPadding`.
- Enabling and configuring minor ticks on the axis using `SmallTicksPerInterval` and `SmallTickSize`.

## Content

### Minor Ticks

Minor ticks are tick marks in between major ticks. These are not rendered by default. Use the properties below to enable and define the frequency of such minor tick marks.

| ChartAxis Property           | Description                                                                                          |
|------------------------------|------------------------------------------------------------------------------------------------------|
| SmallTicksPerInterval        | Specifies if and how many minor ticks, which are tick marks drawn on the axis between intervals, should be drawn. |
| SmallTickSize                | Specifies the size of the tick rectangle.                                                          |

![Illustrates Major and Minor Ticks](image.png "Illustrates Major and Minor Ticks")

**Figure 268: Primary X-Axis with Major and Minor Ticks**

### WinForms-specific implementation for minor ticks

#### C#
```csharp
this.chartControl1.PrimaryXAxis.SmallTickSize = new System.Drawing.Size(2, 2);
this.chartControl1.PrimaryXAxis.SmallTicksPerInterval = 1;
```

#### VB
```vb
this.chartControl1.PrimaryXAxis.SmallTickSize = New System.Drawing.Size(2, 2)
this.chartControl1.PrimaryXAxis.SmallTicksPerInterval = 1
```

## API Reference (if applicable)
- `PrimaryXAxis.TickColor`
- `PrimaryXAxis.TickLabelGridPadding`
- `PrimaryXAxis.SmallTicksPerInterval`
- `PrimaryXAxis.SmallTickSize`

## Code Examples (multi-language supported)
- Demonstrated in the above section for both C# and VB.

## Cross References
- Related features and properties can be explored in the Syncfusion WinForms Chart documentation.

<!-- tags: [product, module, control, api, version?] keywords: [k1, k2, ...] -->
```