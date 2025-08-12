```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_422.jpeg
document_name: chart
page_number: 422
page_id: chart#page_422
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:42:25Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates the use of a Column Chart with 3-D Style in displaying "Bollinger Bands".
- Focuses on customizing chart grid lines using various properties.

## Content

### Chart Grid Lines

#### 4.6.12 Chart Grid Lines

The grid lines in the chart that delineate the intervals in the axes can be customized using the following properties.

**Figure 272: Column Chart with 3-D Style**

```markdown
#### Customizing Chart Grid Lines

The grid lines in the chart that delineate the intervals in the axes can be customized using the following properties:

| Chart Control Property         | Description                                                                                   |
|---------------------------------|-----------------------------------------------------------------------------------------------|
| DrawGrid                      | Specifies whether or not to draw the grid lines.                                            |
| GridLineType.ForeColor         | The forecolor of the line.                                                                   |
| GridLineType.BackColor         | The back color of the line.                                                                  |
| GridLineType.DashStyle         | The DashStyle to use for drawing the line.                                                  |
| GridLineType.PenType           | The PenType to use for drawing the line.                                                    |
| GridLineType.Width             | The thickness of the lines.                                                                  |
```

## API Reference

### Properties Used for Customizing Chart Grid Lines
- **DrawGrid**: Boolean property to specify whether to draw grid lines.
- **GridLineType.ForeColor**: Color property for the foreground color of the grid lines.
- **GridLineType.BackColor**: Color property for the background color of the grid lines.
- **GridLineType.DashStyle**: Pen.DashStyle property to define the style of the grid lines (solid, dotted, etc.).
- **GridLineType.PenType**: PenType property to control the drawing of the lines.
- **GridLineType.Width**: Single property to set the thickness of the grid lines.

## Code Examples

#### Example: Customizing Grid Lines in C#
```csharp
// Example to customize grid lines in a Syncfusion WinForms chart
using Syncfusion.Windows.Forms.Chart;

// Get the chart control
ChartControl chart = new ChartControl();

// Enable drawing of grid lines
chart.PrimaryXAxis.GridLines.DrawGrid = true;

// Set forecolor, backcolor, and other properties
chart.PrimaryXAxis.GridLines.GridLineType.ForeColor = System.Drawing.Color.Blue;
chart.PrimaryXAxis.GridLines.GridLineType.BackColor = System.Drawing.Color.LightGray;
chart.PrimaryXAxis.GridLines.GridLineType.DashStyle = System.Drawing.Drawing2D.DashStyle.Dash;
chart.PrimaryXAxis.GridLines.GridLineType.PenType = PenType.Solid;
chart.PrimaryXAxis.GridLines.GridLineType.Width = 2.0f;

// Add chart to form
this.Controls.Add(chart);
```

## Page-level Navigation/TOC (if applicable)
- 4.6.12 Chart Grid Lines
- Properties used for customization
- Code examples demonstrating chart grid line customization

## Cross References
- Refer to Section 4.x.x for further details on customizing chart styles.
- For additional information on Bollinger Bands, refer to section x.x.x.

<!-- tags: [Essential Chart, Windows Forms, chart, grid lines, 3-D style, Bollinger Bands] keywords: [customization, DrawGrid, GridLineType, DashStyle, PenType, Width, chart control, Syncfusion Winforms] -->
```