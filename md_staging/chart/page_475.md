```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_475.jpeg
document_name: chart
page_number: 475
page_id: chart#page_475
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:42:59Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates how to create and customize interactive cursors in a chart.
- Provides examples in both C# and VB.NET.
- Covers initialization of a `ChartInteractiveCursor` and its addition to the chart's interactive cursor collection.

## Content

### Creating and Customizing Interactive Cursors in a Chart

#### C#
```csharp
// Create a new instance of the ChartInteractiveCursor class and initialize chartseries into it.
ChartInteractiveCursor cursor1 = new ChartInteractiveCursor(this.chartControl1.Series[0]);

// Add the instance to the ChartInteractive Cursor collection.
this.chartControl1.ChartArea.InteractiveCursors.Add(cursor1);

// Color of the pointer
cursor1.Color = Color.Red;
```

#### VB.NET
```vb
' Create a new instance of the ChartInteractiveCursor class and initialize chartseries into it.
ChartInteractiveCursor cursor1 = New ChartInteractiveCursor(Me.chartControl1.Series(0))

' Add the instance to the ChartInteractive Cursor collection.
Me.chartControl1.ChartArea.InteractiveCursors.Add(cursor1)

' Color of the pointer
cursor1.Color = Color.Red
```

### Explanation
- **ChartInteractiveCursor**: This class represents an interactive cursor on the chart. It allows users to interact with the chart, such as hovering or clicking, to get specific data points or values.
- **Series Initialization**: The cursor is initialized with a specific `Series` object from the chart, allowing the cursor to track data points on that series.
- **Adding to Collection**: The cursor is added to the `InteractiveCursors` collection of the chart's `ChartArea` to ensure it is displayed and interactive.
- **Customization**: The `Color` property of the cursor is set to red to visually distinguish it.

### Page-level Navigation/TOC (if applicable)
- This page focuses on setting up interactive cursors for a chart in both C# and VB.NET, offering examples and explanations for customization.

### Cross References
- Refer to the documentation for `ChartInteractiveCursor` for more detailed information on available properties and methods.

<!-- tags: [chart, interactive cursor, chartcontrol, series, color, windows forms, syncfusion, 11.4.0.26] keywords: [chartinteractivecursor, c#, vb.net, interactive cursors, colors, windows forms controls] -->
```