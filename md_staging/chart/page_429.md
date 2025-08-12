```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en
source_filename: page_429.jpeg
document_name: chart
page_number: 429
page_id: chart#page_429
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:41:19Z
fidelity: lossless
-->

## Essential Chart for Windows Forms

### Overview

This section demonstrates the configuration of chart breaks in a Windows Forms chart, using the `BreakAmount` value to control the appearance of breaks in the chart's axis.

### Content

#### Chart Breaks Example

The following figures and code demonstrate how to configure chart breaks in a bar chart to visualize data with significant gaps.

##### Figure: Chart Breaks Illustration

**Figure 276: Illustrates Chart BreakAmount Value**

- The first chart shows a bar chart with empty space where breaks are applied.
- The second chart demonstrates the effect of setting different `BreakAmount` values to control the spacing and impact of breaks on the chart's rendering.

##### C# Code Example

Here’s the code snippet to configure the chart breaks programmatically using C#:

```csharp
this.chartControl1.PrimaryYAxis.MakeBreaks = true;

this.chartControl1.PrimaryYAxis.BreakRanges.BreaksMode = ChartBreaksMode.Manual;
this.chartControl1.PrimaryYAxis.BreakRanges.Union(new DoubleRange(500, 600));
this.chartControl1.PrimaryYAxis.BreakRanges.Union(new DoubleRange(950, 3000));

this.chartControl1.PrimaryYAxis.BreakInfo.LineType = ChartBreakLineType.Wave;
this.chartControl1.PrimaryYAxis.BreakInfo.LineSpacing = 5;
```

### API References

- **MakeBreaks**: Enables or disables the breaks on the chart axis.
- **BreaksMode**: Specifies how breaks are applied (e.g., Manual, Automatic).
- **Union(DoubleRange)**: Adds a range of values where breaks should occur.
- **BreakInfo.LineType**: Controls the appearance of the break lines.
- **BreakInfo.LineSpacing**: Determines the spacing of the break lines.

### Code Examples

The provided code snippet above demonstrates how to programmatically set up chart breaks on a primary Y-axis for a bar chart control in a Windows Forms application.

### Conclusion

By utilizing chart breaks, you can effectively handle large data gaps in your visualizations, ensuring that the chart appears more understandable and less cluttered.

## Page-level Navigation/TOC (if applicable)
- Essential Chart for Windows Forms
- Chart Breaks Example
  - Figure: Chart Breaks Illustration
  - C# Code Example
- API References
- Code Examples
- Conclusion

<!-- tags: chart, windows forms, breaks, Syncfusion Windows Forms, breaksMode, union, lineType, lineSpacing keywords: chart breaks, windows forms chart, C# code, breaksMode, union, lineType, lineSpacing -->
```