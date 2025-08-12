```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_485.jpeg
document_name: chart
page_number: 485
page_id: chart#page_485
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:44:43Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Explains the existing features of the interactive cursor in the chart control.
- Describes how to enable dragging the cursor across the whole chart area.
- Details the axis intervals for moving the interactive cursor.
- Explains the display of symbols when the interactive cursor meets a series point.

## Content

### Existing Features
We can move the interactive cursor for series points only (i.e., the interactive cursor can be moved from one data point to another by dragging). Users cannot move the interactive cursor over the whole chart area.

### MoveToChartArea
We can enable this feature by setting the `MoveToChartArea` property of the interactive cursor to `true`. The default value is `false`.

```csharp
this.chartControl1.ChartArea.InteractiveCursors[0].MoveToChartArea = true;
```

```vb
Me.chartControl1.ChartArea.InteractiveCursors(0).MoveToChartArea = True
```

### XInterval
The cursor on the x-axis can be moved from left to right or right to left based on the value provided in this property of the interactive cursor.

### YInterval
The cursor on the y-axis can be moved from top to bottom or bottom to top based on the value provided in this property of the interactive cursor.

### Symbol
Symbols will be displayed when the interactive cursor meets the series point in the chart area by dragging.

```csharp
this.chartControl1.ChartArea.InteractiveCursors[0].XInterval = 2;
this.chartControl1.ChartArea.InteractiveCursors[0].YInterval = 50;
```

```vb
Me.chartControl1.ChartArea.InteractiveCursors(0).XInterval = 2
Me.chartControl1.ChartArea.InteractiveCursors(0).YInterval = 50
```

## API Reference

### Properties
- `MoveToChartArea`: A boolean property that specifies whether the interactive cursor can be moved across the whole chart area.
- `XInterval`: An integer property that determines the interval for the x-axis cursor movement.
- `YInterval`: An integer property that determines the interval for the y-axis cursor movement.

## Code Examples

### Enabling MoveToChartArea in C#
```csharp
this.chartControl1.ChartArea.InteractiveCursors[0].MoveToChartArea = true;
```

### Setting Axis Intervals in VB
```vb
Me.chartControl1.ChartArea.InteractiveCursors(0).XInterval = 2
Me.chartControl1.ChartArea.InteractiveCursors(0).YInterval = 50
```

## Page-level Navigation/TOC (if applicable)
- [ ] Existing Features
- [ ] MoveToChartArea
- [ ] XInterval
- [ ] YInterval
- [ ] Symbol

## Cross References
See also:
- Interactive Cursors in Chart Control
- Chart Customization Features
- Axis Interactions in WinForms

<!-- tags: [Syncfusion, WinForms, Chart, Interactive Cursors, Axis, Interval] keywords: [MoveToChartArea, XInterval, YInterval, Symbols, Cursor, Points, Dragging, Axis, Interval, Chart Control] -->
```
