```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_286.jpeg
document_name: chart
page_number: 286
page_id: chart#page_286
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:32:33Z
fidelity: lossless
-->

# Essential Chart for Windows Forms

## Chart Properties

The following table describes the properties and their usage for configuring Pie charts:

| Possible Values | True or False |
| --- | --- |
| Default Value | False |
| 2D / 3D Limitations | No |
| Applies to Chart Element | Any Pie Series |
| Applies to Chart Types | PieChart and Doughnut chart |

### Code Examples

**[C#]**

```csharp
this.chartControl1.Series[0].ConfigItems.PieItem.PieWithSameRadius = true;
```

**[VB.NET]**

```vb
Me.chartControl1.Series(0).ConfigItems.PieItem.PieType = True
```

**Description**: Setting this property to `true` will let you display Pie Chart with the same size in the divided area.

## 4.5.1.54 PointsToolTipFormat

This section provides details about configuring the tooltip format for chart points.

- **Description**: Check the `Tooltips` topic for more information on this setting.
- **See Also**: Chart Types

## 4.5.1.55 PointWidth

- **Description**: Sets the width of this point relative to the total width available. It is very useful to render series that overlap.

## API Reference

### Chart Control Properties

- **PieWithSameRadius**: A property allowing the display of Pie charts with uniform segment sizes.
- **PieType**: Configures the type of pie segment display in charts.

### Methods

- **SetPointWidth**: Modifies the width of chart points for better rendering.

### Classes and Namespaces

- **Syncfusion.Windows.Forms.ChartBase**: Base class for chart controls.
- **Syncfusion.Windows.Forms.ChartSeries**: Defines series in the chart.

## Code Examples

### Setting Uniform Radius for Pie Charts

```csharp
// C#
this.chartControl1.Series[0].ConfigItems.PieItem.PieWithSameRadius = true;
```

```vb
' VB.NET
Me.chartControl1.Series(0).ConfigItems.PieItem.PieType = True
```

### Adjusting Point Width

```csharp
// C#
this.chartControl1.Series[0].ConfigItems.PointWidth = 0.8f;
```

```vb
' VB.NET
Me.chartControl1.Series(0).ConfigItems.PointWidth = 0.8f
```

## See Also

- Chart Types
- Tooltips

<!-- tags: [chart, pie chart, doughnut chart, point width, tool tips, syncfusion, chart control, windows forms, winforms, chart series, chart properties] keywords: [chart integration, pie chart formatting, doughnut chart customization, point width configuration, tool tips, winforms development, chart series properties, chart control, uniform radius, segment size, divided area, overlapping series, api reference, code examples] -->
```