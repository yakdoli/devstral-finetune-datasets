```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_605.jpeg
document_name: chart
page_number: 605
page_id: chart#page_605
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:52:46Z
fidelity: lossless
-->

## Chart control events

### Overview
This section explains how to use the chart control's events to manipulate and customize chart plot area bounds using code examples in C# and VB.NET. It includes a practical example of rendering a red rectangle around the chart plot area bounds and discusses various chart control events.

### Content

#### Rendering a Rectangle Around Chart Plot Area Bounds

##### C#

```csharp
Rectangle axisBounds = this.chartControl1.ChartArea.RenderBounds;
// Render a rectangle around this bounds
e.Graphics.DrawRectangle(Pens.Red, axisBounds);
```

##### VB.NET

```vb
AddHandler Me.chartControl1.ChartAreaPaint, AddressOf chartControl1_ChartAreaPaint

Private Sub chartControl1_ChartAreaPaint(ByVal sender As Object, ByVal e As System.Windows.Forms.PaintEventArgs)
    Dim axisBounds As Rectangle = 
        Me.chartControl1.ChartArea.RenderBounds
    ' Render a rectangle around this bounds
    e.Graphics.DrawRectangle(Pens.Red, axisBounds)
End Sub
```

##### Illustration

![Illustrates Chart Plot Area Bounds in Red](Illustrates_Chart_Plot_Area_Bounds.png)

**Figure 368: Chart Plot Area Bounds in Red**

The above code snippets demonstrate how to render a rectangle around the chart plot area using the `ChartAreaPaint` event. The `RenderBounds` property of the chart area is accessed to determine the bounds, and a red rectangle is drawn around these bounds.

---

#### Chart Control Events

This section discusses events associated with the chart control. The following events are discussed in this section:
- [Event 1: Description]
- [Event 2: Description]
- [Event 3: Description]

The specific events related to the chart control are crucial for customizing its behavior and interaction. 

---

### API Reference

- **Namespace:** Syncfusion.WinForms.DataVisualization
- **Control:** Syncfusion.Windows.Forms.Chart.ChartControl
- **Events:**
  - **ChartAreaPaint:** Occurs after the chart area has been painted.

### Code Examples

The code examples in both C# and VB.NET demonstrate functionality related to the `ChartAreaPaint` event. These examples cover rendering custom graphics around the chart plot area.

---

### Cross References

- See also: 
  - Event handling in Syncfusion WinForms
  - Chart customization methods

<!-- tags: [chart, renderbounds, event_handling, chart_control, windows_forms] keywords: [chartAreaPaint, renderbounds, red_rectangle, customize_chart_appearance, event_handler] -->
```