```markdown
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_414.jpeg
document_name: chart
page_number: 414
page_id: chart#page_414
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:41:58Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Demonstrates configuring multiple chart axis titles with multiline functionality.
- Introduces the ability to display partial axis titles with ellipses and wrapping for text exceeding axis length.

## Content

### Figure 265: Chart with Multiline Axes Titles

![Figure 265: Chart with Multiline Axes Titles](#)

#### Drawing Mode of Title Text

You can now display partial axis title with an ellipse at the end of text, whose text length exceeds the axis length. There is also an option to wrap the title text, in addition to the multiline axes title feature, which is discussed above. The `Axes.TitleDrawMode` property is used to control this behavior.

#### Chart Axis Property Table

| Chart Axis Property     | Description                                                                                   |
|-------------------------|-----------------------------------------------------------------------------------------------|
| TitleDrawMode           | Sets the drawing mode of the axis title. It can be Ellipse, Wrap, or None. By default, it is set to `None`. |

### Code Examples (C#)

```csharp
// Setting drawing mode of y-axis title
this.chartControl1.PrimaryXAxis.TitleDrawMode = ChartTitleDrawMode.Ellipsis;
// Setting drawing mode of secondary y-axis title
```

## API Reference

### Properties
- `Axes.TitleDrawMode`
  - **Description**: Sets the drawing mode of the axis title.
  - **Options**: `Ellipse`, `Wrap`, or `None`.
  - **Default**: `None`.

## Cross References
- Refer to the documentation on "multiline axes titles" for more information.

<!-- tags: [chart, axis, multiline, title, titledrawmode, ellipsis, wrap, axes, drawmode] keywords: [chartControl, titleDrawMode, axes, multiline, title, ellipsis, wrap, drawing mode, text display] -->
```