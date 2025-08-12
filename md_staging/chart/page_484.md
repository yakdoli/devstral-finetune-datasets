```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_484.jpeg
document_name: chart
page_number: 484
page_id: chart#page_484
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:45:05Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

**Figure 311: Interactive Cursor with Horizontal Cursor Color Red and Vertical Cursor Color Green.**

## ChartInteractiveCursor Support for Chart Area

### Overview
- Essential Chart now supports moving the interactive cursor fully over the chart area.
- It provides simple methods to display symbols at the intersection of series points and the interactive cursor.

### Use Case Scenarios
- This feature is useful for moving the interactive cursor across the entire chart area region, allowing users to get the intersection point values between the series and interactive cursor.

### Sample Link
To view a sample:
1. Open the Syncfusion Dashboard.
2. Click the Windows Forms drop-down list and select Run Locally Installed Samples.
3. Navigate to Chart samples > User Interaction > Chart Interactive Cursor.

### Properties

| Property         | Description                                                                                      | Type         | Data Type |
|-------------------|--------------------------------------------------------------------------------------------------|--------------|-----------|
| MoveToChartArea  | Specifies whether the interactive cursor is enabled for chart series or series points              | Server Side  | Boolean   |
| XInterval        | Specifies the cursor movement on the x-axis (left to right or right to left)                      | Server Side  | Double    |
| YInterval        | Specifies the cursor movement on the y-axis (top to bottom or bottom to top)                      | Server Side  | Double    |

### Methods

| Method                     | Description                                                                                        | Parameters      | Type         | Return<br>Type |
|-----------------------------|----------------------------------------------------------------------------------------------------|------------------|--------------|----------------|
| SetSeriesSymbolForCursor   | Used to customize the symbol which will be displayed at the intersection between the series point and interactive cursor. | ChartSymbolInfo | Server Side   | Void           |

## API Reference

### Properties
- `MoveToChartArea`: Boolean
- `XInterval`: Double
- `YInterval`: Double

### Methods
- `SetSeriesSymbolForCursor(ChartSymbolInfo)`: Sets the symbol to be displayed at the intersection between the series point and the interactive cursor.

## Code Examples (Placeholder)
No explicit code examples are provided in this page, but you can use the API described above to implement the interactive cursor in your Windows Forms application.

## Cross References
- Refer to the Windows Forms section and the Chart samples for practical implementations and further details.
```

<!-- tags: [essential chart, windows forms, chart interactive cursor, user interaction, series points, interactive cursor, sample link, properties, methods] keywords: [interactive cursor, chart area, series points, enable, cursor movement, symbol customization, axis movement, user interaction, sample link, data type, server side, parameters, custom symbol, x-axis, y-axis] -->