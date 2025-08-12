```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_416.jpeg
document_name: chart
page_number: 416
page_id: chart#page_416
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:40:16Z
fidelity: lossless
-->

## Overview
- Describes the properties of tick marks in the Essential Chart for Windows Forms.
- Provides details on `TickSize`, `TickColor`, `TickLabelGridPadding`, and `TickDrawingOperationMode`.
- Includes an example showcasing the styling of major ticks on the primary X-axis.

## Content

### Properties of Tick Marks

| Property                | Description                                                                                                              | Default               |
|-------------------------|--------------------------------------------------------------------------------------------------------------------------|-----------------------|
| TickSize                | Specifies the width and height of the tick rectangle. This is also a good way to hide the ticks. Default is \{1, 1\}.      | \{1, 1\}             |
| TickColor               | Color of the tick mark. Default is System.ControlText.                                                                | System.ControlText   |
| TickLabelGridPadding    | The padding between the tick mark in the axis and the label. Default is 5.                                          | 5                     |
| TickDrawingOperationMode | Defines the number of ticks to render while zooming.                                                                    |                       |

#### TickDrawingOperationMode Settings
- **NumberOfIntervalsFixed**: When you zoom, the number of visible intervals will be constant. So, as you zoom in, the total number of intervals will increase.
- **IntervalFixed**: The number of intervals will be constant. So, as you zoom in, fewer intervals will be visible at a time.

### Example: Styling Major Ticks

#### Figure: Primary X-Axis with Major Ticks (3x3, DarkOrange)

![Illustrates Major Ticks](image.png)

**Figure 267: Primary X-Axis with Major Ticks (3x3, DarkOrange)**

#### C# Code Example
```csharp
this.chartControl1.PrimaryXAxis.TickSize = new Size(3, 3);
this.chartControl1.PrimaryXAxis.TickColor = Color.DarkOrange;
this.chartControl1.PrimaryXAxis.TickLabelGridPadding = 8F;
```

#### VB Code Example
```vb
Me.chartControl1.PrimaryXAxis.TickSize = new Size(3, 3)
```

## Page-level Navigation/TOC (if applicable)
- The page focuses on configuring and customizing tick marks in the chart control.
- It includes property explanations and code examples to apply the settings.

## Cross References
- Refer to additional documentation on customizing other chart features or axis properties.

<!-- tags: [Syncfusion Winforms, Chart, Tick Marks, TickSize, TickColor, TickLabelGridPadding, TickDrawingOperationMode, Windows Forms, Chart Control, Styling, Properties] keywords: [major ticks, interval fixed, number of intervals fixed, zooming, axis customization, chart, chart control] -->
```