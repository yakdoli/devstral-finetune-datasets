```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_423.jpeg
document_name: chart
page_number: 423
page_id: chart#page_423
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:39:38Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Content
### Customizing Gridlines in Charts

#### Chart Properties and Customization

The following sections demonstrate how to customize the gridlines in a chart using various properties.

#### Figure: Axes Gridlines Customized with Properties
![Axes Gridlines Customized with Properties](#chart_gridlines_customization)

* **GridLineType** property, **BackColor**, **DashStyle**, **ForeColor**, **PenType**, and **Width** can be specified to customize the gridlines.

#### Code Example: Gridline Customization
The following code snippet illustrates how to show the gridlines on both axes and how to customize them.

```csharp
// Customizing X-Axis Gridlines
this.chartControl1.PrimaryXAxis.DrawGrid = true;
this.chartControl1.PrimaryXAxis.GridLineType.BackColor = System.Drawing.Color.Transparent;
this.chartControl1.PrimaryXAxis.GridLineType.DashStyle = System.Drawing.Drawing2D.DashStyle.DashDotDot;
this.chartControl1.PrimaryXAxis.GridLineType.ForeColor = System.Drawing.Color.DarkBlue;
this.chartControl1.PrimaryXAxis.GridLineType.Width = 2F;

// Customizing Y-Axis Gridlines
this.chartControl1.PrimaryYAxis.DrawGrid = true;
this.chartControl1.PrimaryYAxis.GridLineType.BackColor = System.Drawing.Color.OliveDrab;
this.chartControl1.PrimaryYAxis.GridLineType.ForeColor = System.Drawing.Color.DarkOrange;
```

## API Reference
- **GridLineType**: Specifies the type of the grid line.
- **BackColor**: Sets the background color of the grid line.
- **DashStyle**: Defines the pattern of the grid line (e.g., DashDotDot).
- **ForeColor**: Specifies the foreground color of the grid line.
- **PenType**: Defines the pen type used for drawing the grid line.
- **Width**: Sets the width of the grid line.

### Cross References
See also:
- [Graphics and Layout of Chart](chart#graphics-and-layout)
- [Handling Chart Events](chart#handling-events)

<!-- tags: Syncfusion, Windows Forms, Chart, GridLines, Customization, Properties, Version: 11.4.0.26 -->
<!-- keywords: chart, winforms, gridlines, customization, backcolor, dashstyle, forecolor, pen type, width -->
```