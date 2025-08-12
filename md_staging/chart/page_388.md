```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_388.jpeg
document_name: chart
page_number: 388
page_id: chart#page_388
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:38:47Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Overview
- Demonstrates how to combine stacking and side-by-side layout in a chart.
- Explanation includes configuring multiple axes using the `ChartAxis` class and arranging them using the `ChartAxisLayout` class.
- Focuses on setting up a chart with three vertical axes and customizing their layout.

### Content

#### Example: Combining Stacking and SideBySide Layout
This section provides a code example in C# to achieve the desired chart layout as depicted in the figure below.

##### Figure: Combining Stacking and SideBySide Layout
![](image.png)

**Figure 253: Combining Stacking and SideBySide Layout**

```csharp
[C#]

// Created chart axes:
ChartAxis axis = this.chartControl1.PrimaryYAxis;
ChartAxis axis0 = new ChartAxis(ChartOrientation.Vertical);
ChartAxis axis1 = new ChartAxis(ChartOrientation.Vertical);

// Added chart axes into the chart:
chartControl1.Axes.Add(axis0);
chartControl1.Axes.Add(axis1);

// Created chart axis layout using ChartAxisLayout class: (New class)
ChartAxisLayout layout1 = new ChartAxisLayout();
```

##### Explanation
1. **Creating Chart Axes:**
   - `axis` represents the primary vertical axis of the chart.
   - `axis0` and `axis1` are additional vertical axes created using the `ChartAxis` class with a vertical orientation.

2. **Adding Axes to the Chart:**
   - The `Axes.Add` method is used to include `axis0` and `axis1` into the chart.

3. **Chart Axis Layout:**
   - A `ChartAxisLayout` object is instantiated to allow for custom axis arrangement.

### API Reference

#### ChartAxis Class
- **Namespace:** Syncfusion.Chart
- **Description:** Represents the axis of a chart.

##### Properties
- `Orientation`: Gets or sets the orientation of the axis (e.g., Vertical, Horizontal).

#### ChartAxisLayout Class
- **Namespace:** Syncfusion.Chart
- **Description:** Manages the layout of the axes within a chart.

### Code Examples

The provided C# code snippet illustrates how to configure multiple vertical axes and integrate them into a `chartControl1` instance. The `ChartAxisLayout` class is utilized to define the desired layout.

### Conclusion
This example demonstrates how to extend the functionality of a chart by adding multiple axes and customizing their layout to meet specific visualization requirements. The use of `ChartAxis` and `ChartAxisLayout` classes enables advanced chart configurations in Syncfusion Winforms.

<!-- tags: chart, windows forms, Syncfusion SDK, API, version: 11.4.0.26 -->
```