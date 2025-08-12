```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_476.jpeg
document_name: chart
page_number: 476
page_id: chart#page_476
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:44:35Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

![Figure 306: Chart Interactive Cursor](./chart-interactive-cursor.png)

## Chart AutoHighlight

### Overview
- This section describes how to highlight points or series in a chart when the mouse hovers over them.
- Highlights are enabled using the `AutoHighlight` property.

### Content

#### Chart Interactive Cursor
The interactive cursor feature is demonstrated in the chart below. The cursor allows users to trace data points and view their values dynamically as they move over them.

#### Chart AutoHighlight
The points or the series of the chart can be highlighted when the mouse hovers over them. Use the `AutoHighlight` property to enable this feature.

![Figure Illustrates Series Highlighting Feature in Chart](./chart-autohighlight-feature.png)

### API Reference
#### WinForms-Specific Features
- **Interactive Cursor**: Enhances user interaction by visually linking data points.
- **AutoHighlight**: Dynamically highlights series or data points based on mouse hover events.

### Code Examples
#### C# Example
```csharp
// Enable AutoHighlight for the chart
SfChart chart = new SfChart();
LineSeries series = new LineSeries();
series.AutoHighlight = true;
chart.Series.Add(series);
```

#### VB Example
```vb
' Enable AutoHighlight for the chart
Dim chart As New SfChart()
Dim series As New LineSeries()
series.AutoHighlight = True
chart.Series.Add(series)
```

### Cross References
- Refer to the **Chart Series Highlighting** section for more details on how series highlighting works.

---

<!-- tags: [syncfusion, winforms, chart, interactive cursor, autohighlight, essential chart, SfChart, LineSeries, namespace, class] keywords: [interactive cursor, autohighlight, user interaction, data points, mouse hover, highlighting, chart, windows forms] -->
```