```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_238.jpeg
document_name: chart
page_number: 238
page_id: chart#page_238
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:29:24Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Customizing Gantt Chart Appearance

The following code snippets demonstrate how to configure the appearance of a Gantt chart using the `GanttDrawMode` property to set it to `AutoSizeMode`. This ensures that the tasks and completion bars are displayed proportionally to the actual data values.

#### C# Code Example

```csharp
// Specifies GanttDrawMode as AutoSizeMode
this.chartControl1.Series[0].GanttDrawMode = ChartGanttDrawMode.AutoSizeMode;
this.chartControl1.Series[1].GanttDrawMode = ChartGanttDrawMode.AutoSizeMode;
```

#### VB.NET Code Example

```vb
' Specifies GanttDrawMode as AutoSizeMode
Me.chartControl1.Series(0).GanttDrawMode = ChartGanttDrawMode.AutoSizeMode
Me.chartControl1.Series(1).GanttDrawMode = ChartGanttDrawMode.AutoSizeMode
```

### Visualization of Gantt Chart

The figure below illustrates a Gantt chart with the `AutoSizeMode` applied, demonstrating how tasks and their completion statuses are visually represented.

![Gantt Chart with AutoSizeMode](https://via.placeholder.com/600x400?text=Figure%20138%3A%20Gantt%20Chart%20with%20AutoSizeMode)

### Key Features Highlighted

- **Task Representation**: Tasks are depicted with a brown color.
- **Completion Representation**: Completion progress is shown with a blue color.
- **Proportional Scaling**: The chart bars are scaled to reflect the actual data values accurately.

### Example Output

The Gantt chart shown in the figure effectively demonstrates the task progress and completion status using the specified `AutoSizeMode`. This mode ensures that the visual representation accurately reflects the data, providing a clear and concise view of project timelines and milestones.

## API Reference

### Properties

- **GanttDrawMode**: Configures how the Gantt chart tasks are visually rendered. Possible values include `AutoSizeMode`, `FixedWidthMode`, and `DynamicWidthMode`.

### Methods

- **SetGanttDrawMode**: Allows programmatic setting of the GanttDrawMode property.

## Code Examples

### C# Example

```csharp
using Syncfusion.Windows.Forms.Chart;

// Initialize the ChartControl
ChartControl chartControl1 = new ChartControl();

// Configure the GanttDrawMode for Series
chartControl1.Series[0].GanttDrawMode = ChartGanttDrawMode.AutoSizeMode;
chartControl1.Series[1].GanttDrawMode = ChartGanttDrawMode.AutoSizeMode;
```

### VB.NET Example

```vb
Imports Syncfusion.Windows.Forms.Chart

' Initialize the ChartControl
Dim chartControl1 As New ChartControl()

' Configure the GanttDrawMode for Series
chartControl1.Series(0).GanttDrawMode = ChartGanttDrawMode.AutoSizeMode
chartControl1.Series(1).GanttDrawMode = ChartGanttDrawMode.AutoSizeMode
```

## Page-level Navigation/TOC

- **Overview**: Brief introduction to configuring Gantt chart appearance.
- **Code Examples**: Demonstrations in C# and VB.NET.
- **Visualization**: Explanation of the figure showing the Gantt chart.

## Cross References

- Refer to the [Gantt Chart Documentation](#) for more detailed information on chart customization options.

### Additional Notes

- Ensure that the chart control is properly instantiated and configured before applying the `GanttDrawMode` settings.
- Adjust the series data to reflect actual project tasks and their respective progress.

<!-- tags: [Essential Chart, Windows Forms, Gantt Chart, AutoSizeMode] keywords: [GanttDrawMode, AutoSizeMode, C#, VB.NET, Gantt chart, task representation, completion status, proportional scaling, visualization, Windows Forms chart] -->
```