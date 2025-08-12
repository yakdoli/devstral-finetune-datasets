```html
<!-- 
source: image
domain: syncfusion-sdk
task: pdf-ocr-to-markdown
language: en (keep original; do not translate)
source_filename: page_192.jpeg
document_name: chart
page_number: 192
page_id: chart#page_192
product: Syncfusion Winforms
version: 11.4.0.26
timestamp: 2025-08-09T03:27:59Z
fidelity: lossless
-->

## Chart Width Configuration

### Overview
- Specifies the width of each column when `ColumnWidthMode` is set to `FixedWidthMode`.
- Details include possible values, default settings, applicability to different chart elements and types, and limitations.

### Content

#### Chart Width Mode Details

| **Details**             | **Description**                                      |
|--------------------------|------------------------------------------------------|
| **Possible Values**     | An integer value                                    |
| **Default Value**       | 20                                                   |
| **2D / 3D Limitations** | None                                                |
| **Applies to Chart Element** | All Series                                       |
| **Applies to Chart Types** | Column Charts, BoxAndWhiskerChart, Candle Chart |

Here is some sample code.

#### C# Code Example

```csharp
ChartSeries series1 = new ChartSeries("Series");
series1.Points.Add(1, new double[] { 24 });
series1.Points.Add(2, new double[] { 36 });
series1.Points.Add(3, new double[] { 48 });
chartControl1.Series.Add(series1);
chartControl1.ColumnWidthMode = ChartColumnWidthMode.FixedWidthMode;
chartControl1.ColumnFixedWidth = 45;
```

#### VB.NET Code Example

```vb
Dim series1 As ChartSeries = New ChartSeries("Series")
series1.Points.Add(1, New Double() { 24 })
series1.Points.Add(2, New Double() { 36 })
series1.Points.Add(3, New Double() { 48 })
chartControl1.Series.Add(series1)
chartControl1.ColumnWidthMode = ChartColumnWidthMode.FixedWidthMode
chartControl1.ColumnFixedWidth = 45
```

#### Note: Overriding Column Width Property

> The `ColumnFixedWidth` property can be overridden by specifying a second y value in the data point. See `ColumnWidthMode` for a sample.

## API Reference

### Properties
- **ColumnWidthMode**: Specifies the mode for determining column width.
- **ColumnFixedWidth**: Specifies the fixed width for the columns when `ColumnWidthMode` is set to `FixedWidthMode`.
- **PossibleValues**: An integer value representing the possible values for column width.

### Applicability
- **Chart Elements**: All Series.
- **Chart Types**: Available in Column Charts, BoxAndWhiskerChart, and Candle Chart.

## Code Examples

The examples above demonstrate how to configure fixed column widths in column charts using Syncfusion Winforms. By setting the `ColumnWidthMode` to `FixedWidthMode` and specifying a `ColumnFixedWidth`, you can control the width of each column in your chart.

## Cross References

See also:
- Documentation on `ColumnWidthMode` for more detailed information on dynamically setting column widths based on y-values.
- Chart customization options in the Syncfusion Winforms documentation for additional styling and feature guides.

### Conclusion

This section provides a comprehensive guide to configuring column widths in column-based charts using Syncfusion Winforms, including code examples and detailed explanations of applicable properties and chart types.

## Footer

- **Copyright**: © 2013 Syncfusion. All rights reserved.
- **Page Number**: 192
- **Product**: Syncfusion Winforms
- **Version**: 11.4.0.26

<!-- tags: [syncfusion, winforms, chart, columnwidthmode, fixedwidth, columnbasedchart, userguide, codeexamples] keywords: [column width, columnmode, fixedwidth, chart settings, winforms, columnbased, chart customization] -->
```
