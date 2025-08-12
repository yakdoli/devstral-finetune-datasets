```html
<!--
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_006.jpeg
document_name: chart
page_number: 006
page_id: chart#page_006
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:15:36Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Overview
- Detailed list of chart properties for Windows Forms.
- Covers various chart types, styles, and formatting options.
- Provides page references for each property description.

## Content

### Chart Properties
- **PyramidMode**: Refers to the display mode for pyramid charts.
- **Radar Type**: Defines the type of radar chart to be displayed.
- **RadarStyle**: Specifies the style for radar charts.
- **RelatedPoints**: Manages the relationship between chart data points.
- **ReversalAmount**: Controls the amount of reversal for certain chart types.
- **Rotate**: Adjusts the rotation of chart components.
- **ScatterConnectType**: Determines how scatter points are connected.
- **ScatterSplineTension**: Controls the tension of splines in scatter charts.
- **SeriesToolTipFormat**: Formats the tooltip for series data points.
- **ShadingMode**: Sets the shading mode for 3D charts.
- **ShadowInterior**: Defines the interior shadow for chart elements.
- **ShadowOffset**: Controls the offset of shadow effects.
- **ShowDataBindLabels**: Determines whether data binding labels are displayed.
- **ShowHistogramDataPoints**: Displays histogram data points.
- **ShowTicks**: Controls the visibility of chart ticks.
- **SmartLabels**: Manages intelligent label placement.
- **Spacing**: Adjusts the spacing between chart elements.
- **Spacing Between Series**: Controls the spacing between different series.
- **Spacing Between Points**: Manages spacing between individual data points.
- **Stacking Group**: Sets the stacking group for chart series.
- **Stepltem.Inverted**: Defines the inverted stacking for step charts.
- **Summary**: Displays a summary of chart data.
- **Symbol**: Manages the symbol used for data points.
- **Text (Series)**: Formats the text for series labels.
- **Text (Style)**: Formats the style of text elements.
- **TextColor**: Sets the color for text elements.
- **TextFormat**: Formats the text display style.
- **TextOffset**: Adjusts the offset for text elements.
- **TextOrientation**: Sets the orientation of text elements.
- **ToolTip**: Controls the tooltip display for chart elements.
- **ToolTipFormat**: Formats the tooltip content.
- **Visible**: Determines the visibility of chart elements.
- **VisibleAllPies**: Ensure all pie chart segments are visible.
- **XType**: Specifies the type of X-axis.
- **YType**: Specifies the type of Y-axis.

## API Reference

### Properties
- **PyramidMode**: Chart display mode for pyramids.
- **RadarType**: Type of radar chart.
- **RadarStyle**: Style for radar chart display.
- **RelatedPoints**: Inter-relatedness of data points.
- **ReversalAmount**: Amount of chart reversal.
- **Rotate**: Chart element rotation.
- **ScatterConnectType**: Connection style for scatter plots.
- **ScatterSplineTension**: Tension in scatter spline plots.
- **SeriesToolTipFormat**: Formatting for tooltips.
- **ShadingMode**: Shading in 3D charts.
- **ShadowInterior**: Interior shadow settings.
- **ShadowOffset**: Shadow offset settings.
- **ShowDataBindLabels**: Data binding label visibility.
- **ShowHistogramDataPoints**: Display histogram data points.
- **ShowTicks**: Tick visibility.
- **SmartLabels**: Intelligent label placement.
- **Spacing**: General spacing control.
- **Spacing Between Series**: Inter-series spacing.
- **Spacing Between Points**: Inter-point spacing.
- **Stacking Group**: Stacking group configuration.
- **Stepltem.Inverted**: Inverted stepping mode.
- **Summary**: Chart summary display.
- **Symbol**: Data point symbol.
- **Text (Series)**: Series text formatting.
- **Text (Style)**: Text style formatting.
- **TextColor**: Text color setting.
- **TextFormat**: Text format control.
- **TextOffset**: Text offset setting.
- **TextOrientation**: Text orientation control.
- **ToolTip**: Tooltip functionality.
- **ToolTipFormat**: Tooltip content format.
- **Visible**: Element visibility.
- **VisibleAllPies**: Display all pie chart segments.
- **XType**: X-axis type.
- **YType**: Y-axis type.

## Code Examples
```csharp
// Example of setting chart properties
chart.PyramidMode = PyramidMode.Vertical;
chart.RadarType = RadarChartType.Simple;
chart.SeriesToolTipFormat = "Value: {#Point.YValue}";
```

## Cross References
- See also: Chart Styling, Data Binding, Axis Types, Tooltip Management.

<!-- tags: [chart, windows forms, properties, styling, tooltips, axes, visibility, syncfusion, 11.4.0.26] keywords: [PyramidMode, RadarType, RadarStyle, RelatedPoints, ReversalAmount, Rotate, ScatterConnectType, ScatterSplineTension, SeriesToolTipFormat, ShadingMode, ShadowInterior, ShadowOffset, ShowDataBindLabels, ShowHistogramDataPoints, ShowTicks, SmartLabels, Spacing, Stacking Group, Stepltem.Inverted, Summary, Symbol, TextColor, TextFormat, ToolTip, ToolTipFormat, VisibleAllPies, XType, YType] -->
```