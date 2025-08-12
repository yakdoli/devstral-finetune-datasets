```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_161.jpeg
document_name: chart
page_number: 161
page_id: chart#page_161
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:25:26Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Provides methods to get start and end point values from a sparkline.
- Supports three types of sparklines: Line, Column, and WinLoss.
- Demonstrates how to bind a sparkline control to a data source.

## Content

### Properties and Methods

| Property/Method | Description                    | Parameters | Default | Returns  | Notes |
|------------------|--------------------------------|------------|---------|----------|-------|
| GetStartPoint   | Gets the start point value from the sparkline. | NA      | NA      | Void  | NA    |
| GetEndPoint     | Gets the end point value from the sparkline. | NA      | NA      | Void  | NA    |

### Events
- Events: NA

### Sample Link

**To access a Sparkline sample Demo:**

1. Open the Syncfusion Dashboard.
2. Select User Interface.
3. Click the Windows Forms drop-down list and select Explore Samples.
4. Navigate to `Chart.Windows -> Samples -> 2.0 -> SparklineChart`.

### Types of Sparklines

Presently, Syncfusion SparkLine control supports three types of Sparklines, and the sparkline control must be bound to a data source. It supports a variety of datasources such as `DataTable` and any component that implements interfaces like `IEnumerable`, `ICollection`, `IList`.

- Line
- Column
- WinLoss

### Drawing Line Sparkline in an Application

The line type of sparkline represents a set of data points, connected by a line. Refer to the following code snippets to draw the line sparkline.

```csharp
// Set Sparkline points to source property
// [C#.NET]
// Code snippet to draw line sparkline
```

## Code Examples (multi-language supported)
- Code example for drawing a line sparkline is provided above.

## Page-level Navigation/TOC (if applicable)
- None specified on this page.

## Cross References
- Refer to the Syncfusion documentation for additional details on sparkline controls and its integration.

<!-- tags: [Syncfusion, Winforms, Sparkline, Chart, Sample, Data Source, SparklineControls, LineSparkline, Column, WinLoss] keywords: [access, sample, demo, dashboard, UI, Windows Forms, types, data points, line, column, winloss, drawing, code snippet] -->
```