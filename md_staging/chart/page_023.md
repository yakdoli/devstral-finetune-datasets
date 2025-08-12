```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_023.jpeg
document_name: chart
page_number: 023
page_id: chart#page_023
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:16:42Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Drag a Chart control onto the form.
- Control appearance and behavior through properties such as changing the legend position.
- Add chart data programmatically using code.

## Content
### Dragging the Chart Control
2. Drag a Chart control onto the form.

### Controlling Appearance and Behavior
3. Appearance and behavior-related aspects of the Chart can be controlled by setting the appropriate properties through the properties grid. For example, change the position of the legend for the control to be top-aligned by changing the `LegendPosition` property.

#### Figure: Setting Legend Position Property
![Properties Grid](https://i.imgur.com/EXample.jpg)
*Figure 7: Setting Legend Position Property*

### Adding Data through Code
4. The data for the Chart can be added through code. Switch to code view in VS.NET and add the method shown below.

#### Code Example
[C#]

```csharp
using Syncfusion.Windows;
using Syncfusion.Windows.Forms.Chart;

// Create a new ChartSeries. The string specified is the name of the series.
ChartSeries series = this.chartControl1.Model.NewSeries("Series");

// Set the Text property of the series. This will be used by the legend to display a descriptive name.
series.Text = series.Name;
```

## API Reference

### Properties
- **LegendPosition**: Controls the position of the legend in the Chart.

### Methods
- **NewSeries(string name)**: Creates a new ChartSeries with the specified name.

## Code Examples (multi-language supported)
- C# example provided above.

## Cross References
See also: properties grid, chart data, VS.NET code view.

<!-- tags: [chart, winforms, syncfusion, essential chart, legendposition, newseries] keywords: [drag, control, appearance, behavior, data, legend, top-aligned, code, property, series, text, description] -->
``` 
