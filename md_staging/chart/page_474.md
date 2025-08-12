```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_474.jpeg
document_name: chart
page_number: 474
page_id: chart#page_474
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:46:33Z
fidelity: lossless
-->

# **Essential Chart for Windows Forms**

## Legend Context Menu

This context menu can be enabled by setting the `ShowContextMenuInLegend` property to `true`.

![Figure 305: Legend Context Menu](Illustrates chart Legend Context Menu "Figure 305: Legend Context Menu")

## 4.9.4 Interactive Features

### Interactive Cursor

This feature lets you position the mouse pointer at a specific data point in a series and hint you on its x and y values via a horizontal and vertical line passing through the data point and intersecting the x and y axis. These lines can be dragged around in order to position them at specific data points.

Interactive Cursor can be implemented by creating an instance of `ChartInteractiveCursor` with the `ChartSeries` as its input. Then add the instance to the Interactive Cursors collection as shown below.
```csharp
// Example code
ChartInteractiveCursor interactiveCursor = new ChartInteractiveCursor(chartSeries);
chart1.Inject(InteractiveCursors.Add(interactiveCursor));
```

## Code Examples (multi-language supported)
- Example of enabling the `ShowContextMenuInLegend` property:
```csharp
chart.Legend.ShowContextMenuInLegend = true;
```

## Page-level Navigation/TOC (if applicable)
- Legend Context Menu
- Interactive Features
  - Interactive Cursor

## Cross References
See also: 
- Chart properties and features
- Interactive cursors in detail

<!-- tags: [windows forms, chart, legend, context menu, interactive cursor] keywords: [legend, context menu, mouse pointer, data point, chart series, chartinteractivecursor, interactive cursors] -->
```