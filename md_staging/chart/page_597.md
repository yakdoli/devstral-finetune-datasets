```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_597.jpeg
document_name: chart
page_number: 597
page_id: chart#page_597
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:52:12Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates how to display a toolbar in a Chart.
- Explains the use of `ShowToolBar` and `PrintToolBar` properties for controlling the visibility of the toolbar during printing.
- Discusses data manipulation features, including grouping, filtering, and computed summaries in Essential Chart.

## Content

### Displaying ToolBar while printing

The `ShowToolBar` property should be set to `true` to display a toolbar in the Chart. You can show or hide the toolbar while printing a Chart using the `PrintToolBar` property.

#### C#
```csharp
chartControl1.ShowToolbar = true;
chartControl1.PrintDocument.PrintToolBar = true;
```

#### VB.NET
```vb
chartControl1.ShowToolbar = True
chartControl1.PrintDocument.PrintToolBar = True
```

### 4.17 Data Manipulation

Essential Chart provides a series model implementation that works directly on top of grouped data. Filters, summaries, and computed expressions are all supported in Essential Chart, allowing users to easily add custom summaries and filters and have such data displayed in the chart.

#### Grouping Support

The enterprise version of Essential Chart includes Essential Grouping, which allows Essential Chart to implement a series model that works directly on top of grouped data. All the key advantages of Essential Grouping carry over into the grouping support in Essential Chart. Filters, summaries, and computed expressions are all supported in Essential Chart. With Essential Chart, you are not restricted to predefined summaries or filters. You can easily add custom summaries and filters and have such data displayed in the chart.

The following image displays stock data that is grouped by symbol to calculate the total volume. The data contains discrete transaction details with symbol information, volume, and price.

The following image displays the same data with data from transactions that occurred in the morning filtered out. Filtering is done entirely in the grouping engine, and the data changes are reflected in the chart. You will never be looking at data that is a filtered and grouped copy. Instead, you are always working with live data with the grouping layer provided by the grouping engine. Any changes made in the underlying data will be immediately reflected in the chart.

## API Reference

### Essential Grouping in Chart

- **Namespace:** Syncfusion.Windows.Forms.Chart.Chart
- **Properties:**
  - `ShowToolBar`: bool
    - Sets whether the toolbar is displayed in the Chart.
  - `PrintToolBar`: bool
    - Sets whether the toolbar is displayed during printing of the Chart.

### Code Examples

- **C#**
    ```csharp
    chartControl1.ShowToolbar = true;
    chartControl1.PrintDocument.PrintToolBar = true;
    ```
- **VB.NET**
    ```vb
    chartControl1.ShowToolbar = True
    chartControl1.PrintDocument.PrintToolBar = True
    ```

<!-- tags: [syncfusion, winforms, chart, data manipulation, grouping, toolbar, printing, version 11.4.0.26] keywords: [Essential Chart, ShowToolBar, PrintToolBar, data grouping, custom summaries, filtering, live data, grouping engine] -->
``` 
